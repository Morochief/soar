#!/usr/bin/env python3
# =============================================================================
#      SECURITY ONION ENTERPRISE CONNECTOR ENGINE (so_engine.py)
#      OpenXDR Cockpit Integration - Fault-Tolerant, Circuit Breaker & Async
# =============================================================================

import os
import time
import socket
import logging
import urllib3
import requests
import json
from typing import Dict, Any, List, Optional, Tuple

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

_logger = logging.getLogger("so_engine")


class SecurityOnionEngine:
    """
    Motor conector resiliente de nivel empresarial para Security Onion.
    Implementa:
      1. Patron Circuit Breaker: Timeout de 1.0s. Si esta fuera de red (Home Office),
         pasa a modo OFFLINE silencioso sin bloquear la GUI.
      2. Consultas forenses de IOCs bajo demanda (Zeek, Suricata, Syslog).
      3. Monitor pasivo de salud de cluster y nodos distribuidos (Grid Pulse).
    """

    DEFAULT_URL = "https://172.17.10.25:9200"
    DEFAULT_API_KEY = "SlcyYkk1OEJaZEtFR0l3ZTNNMGc6MktWaGRzV2VQTU9iZmNkRVZkT2E1dw=="

    def __init__(
        self,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        connect_timeout: float = 1.0,
        read_timeout: float = 5.0,
    ):
        self.base_url = (
            base_url
            or os.environ.get("SO_ELASTIC_URL")
            or self.DEFAULT_URL
        ).rstrip("/")
        self.api_key = (
            api_key
            or os.environ.get("SO_ELASTIC_API_KEY")
            or self.DEFAULT_API_KEY
        )
        self.connect_timeout = float(
            os.environ.get("SO_CONNECT_TIMEOUT", connect_timeout)
        )
        self.read_timeout = read_timeout

        # Estado del Circuit Breaker
        self._is_online: bool = False
        self._last_check_ts: float = 0.0
        self._check_interval: float = 45.0  # segundos entre verificaciones pasivas
        self._last_error: str = ""

        # Sesion HTTP reutilizable con pool de conexiones
        self._session = requests.Session()
        self._session.headers.update({
            "Authorization": f"ApiKey {self.api_key}",
            "Content-Type": "application/json",
            "User-Agent": "OpenXDR-Cockpit-SOEngine/1.0",
        })

    def is_online(self, force: bool = False) -> bool:
        """
        Comprobacion no bloqueante con patron Circuit Breaker.
        Verifica conectividad en <= 1.0s. Respeta cache para no ralentizar.
        """
        now = time.time()
        if not force and (now - self._last_check_ts < self._check_interval):
            return self._is_online

        self._last_check_ts = now
        try:
            # Peticion ultraligera al endpoint raiz de Elasticsearch con timeout estricto
            resp = self._session.get(
                self.base_url,
                verify=False,
                timeout=(self.connect_timeout, 2.0),
            )
            if resp.status_code == 200:
                self._is_online = True
                self._last_error = ""
                return True
            else:
                self._is_online = False
                self._last_error = f"HTTP {resp.status_code}"
                return False
        except (requests.exceptions.ConnectTimeout, requests.exceptions.ConnectionError, socket.timeout) as exc:
            self._is_online = False
            self._last_error = "Fuera de red corporativa (Home Office / No alcanzable)"
            return False
        except Exception as exc:
            self._is_online = False
            self._last_error = str(exc)
            return False

    def get_grid_health(self) -> Dict[str, Any]:
        """
        Obtiene el pulso de salud del cluster y nodos de Security Onion.
        Si esta offline, retorna inmediatamente sin congelar la GUI.
        """
        if not self.is_online():
            return {
                "status": "offline",
                "message": self._last_error or "Desconectado (Modo Remoto)",
                "cluster_health": "unknown",
                "nodes_count": 0,
                "nodes": [],
                "shards_active": 0,
                "unassigned_shards": 0,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            }

        try:
            # 1. Consultar estado del cluster
            health_resp = self._session.get(
                f"{self.base_url}/_cluster/health",
                verify=False,
                timeout=(self.connect_timeout, self.read_timeout),
            )
            health_data = health_resp.json() if health_resp.status_code == 200 else {}

            # 2. Consultar nodos activos
            nodes_resp = self._session.get(
                f"{self.base_url}/_cat/nodes?format=json&h=ip,name,heap.percent,ram.percent,cpu,load_1m,node.role,master",
                verify=False,
                timeout=(self.connect_timeout, self.read_timeout),
            )
            nodes_data = nodes_resp.json() if nodes_resp.status_code == 200 else []

            cluster_status = health_data.get("status", "unknown").lower()
            return {
                "status": "online",
                "cluster_name": health_data.get("cluster_name", "securityonion"),
                "cluster_health": cluster_status,
                "nodes_count": health_data.get("number_of_nodes", len(nodes_data)),
                "data_nodes": health_data.get("number_of_data_nodes", 0),
                "shards_active": health_data.get("active_shards", 0),
                "primary_shards": health_data.get("active_primary_shards", 0),
                "unassigned_shards": health_data.get("unassigned_shards", 0),
                "relocating_shards": health_data.get("relocating_shards", 0),
                "nodes": nodes_data,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            }
        except Exception as exc:
            self._is_online = False
            return {
                "status": "error",
                "message": f"Fallo al consultar Grid: {exc}",
                "cluster_health": "error",
                "nodes_count": 0,
                "nodes": [],
                "shards_active": 0,
                "unassigned_shards": 0,
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            }

    def hunt_ioc(self, ioc: str, days: int = 7) -> Dict[str, Any]:
        """
        Caza cruzada de IOCs bajo demanda en Security Onion (Zeek + Suricata + Syslog).
        No genera ruido en la bandeja.
        """
        ioc = (ioc or "").strip()
        if not ioc:
            return {"status": "error", "message": "IOC vacio"}

        if not self.is_online():
            return {
                "status": "offline",
                "ioc": ioc,
                "message": "Security Onion no disponible (Fuera de Red Corporativa)",
                "zeek_hits": 0,
                "suricata_hits": 0,
                "syslog_hits": 0,
                "alerts": [],
                "connections": [],
                "syslog_events": [],
                "syslog_samples": [],
            }

        ioc_type = self._detect_ioc_type(ioc)
        time_range = f"now-{days}d/d"

        results = {
            "status": "online",
            "ioc": ioc,
            "ioc_type": ioc_type,
            "query_window_days": days,
            "zeek_hits": 0,
            "suricata_hits": 0,
            "syslog_hits": 0,
            "alerts": [],
            "connections": [],
            "syslog_events": [],
            "syslog_samples": [],
            "internal_hosts": set(),
            "first_seen": None,
            "last_seen": None,
        }

        try:
            # 1. Busqueda en Suricata Alerts (.ds-logs-suricata.alerts-*)
            suricata_query = self._build_suricata_query(ioc, ioc_type, time_range)
            s_resp = self._session.post(
                f"{self.base_url}/.ds-logs-suricata.alerts-*/_search",
                json=suricata_query,
                verify=False,
                timeout=(self.connect_timeout, self.read_timeout),
            )
            if s_resp.status_code == 200:
                s_data = s_resp.json()
                results["suricata_hits"] = s_data.get("hits", {}).get("total", {}).get("value", 0)
                for hit in s_data.get("hits", {}).get("hits", [])[:10]:
                    src = hit.get("_source", {})
                    rule = src.get("rule", {}).get("name") or src.get("message") or "Suricata Detection"
                    sev = src.get("event", {}).get("severity", 3)
                    results["alerts"].append({
                        "timestamp": src.get("@timestamp"),
                        "signature": rule,
                        "severity": sev,
                        "src_ip": src.get("source", {}).get("ip"),
                        "dest_ip": src.get("destination", {}).get("ip"),
                        "dest_port": src.get("destination", {}).get("port"),
                    })

            # 2. Busqueda en Zeek Network Logs (.ds-logs-zeek-*)
            zeek_query = self._build_zeek_query(ioc, ioc_type, time_range)
            z_resp = self._session.post(
                f"{self.base_url}/.ds-logs-zeek-*/_search",
                json=zeek_query,
                verify=False,
                timeout=(self.connect_timeout, self.read_timeout),
            )
            if z_resp.status_code == 200:
                z_data = z_resp.json()
                results["zeek_hits"] = z_data.get("hits", {}).get("total", {}).get("value", 0)
                for hit in z_data.get("hits", {}).get("hits", [])[:15]:
                    src = hit.get("_source", {})
                    ts = src.get("@timestamp")
                    proto = src.get("network", {}).get("protocol") or src.get("data_stream", {}).get("dataset", "")
                    src_ip = src.get("source", {}).get("ip")
                    if src_ip and (src_ip.startswith("10.") or src_ip.startswith("192.168.") or src_ip.startswith("172.")):
                        results["internal_hosts"].add(src_ip)

                    results["connections"].append({
                        "timestamp": ts,
                        "protocol": proto,
                        "src_ip": src_ip,
                        "dest_ip": src.get("destination", {}).get("ip"),
                        "dest_port": src.get("destination", {}).get("port"),
                        "bytes": src.get("network", {}).get("bytes", 0),
                    })
                    if not results["last_seen"] or ts > results["last_seen"]:
                        results["last_seen"] = ts
                    if not results["first_seen"] or ts < results["first_seen"]:
                        results["first_seen"] = ts

            # 3. Busqueda en Syslog y FortiGate (.ds-logs-*syslog*,.ds-logs-fortinet_fortigate.log-*)
            results["syslog_events"] = []
            results["syslog_samples"] = []
            sys_resp = self._session.get(
                f"{self.base_url}/.ds-logs-*syslog*,.ds-logs-fortinet_fortigate.log-*/_count?q=*{ioc}*",
                verify=False,
                timeout=(self.connect_timeout, self.read_timeout),
            )
            if sys_resp.status_code == 200:
                results["syslog_hits"] = sys_resp.json().get("count", 0)

            # Extraer eventos estructurados (hasta 100) para mostrar en tabla dedicada
            if results["syslog_hits"] > 0:
                try:
                    s_body = {
                        "size": 100,
                        "sort": [{"@timestamp": {"order": "desc"}}],
                        "query": {"query_string": {"query": f"*{ioc}*"}}
                    }
                    s_r = self._session.post(
                        f"{self.base_url}/.ds-logs-*syslog*,.ds-logs-fortinet_fortigate.log-*/_search",
                        json=s_body,
                        verify=False,
                        timeout=(self.connect_timeout, self.read_timeout)
                    )
                    if s_r.status_code == 200:
                        for h in s_r.json().get("hits", {}).get("hits", []):
                            src = h.get("_source", {})
                            msg = src.get("message", "")
                            # Si es un log estructurado de FortiGate sin mensaje largo, construir detalle descriptivo
                            if not msg or msg in ["Connection Failed", "none"]:
                                action = src.get("event", {}).get("action", "traffic")
                                s_ip = src.get("source", {}).get("ip", "")
                                d_ip = src.get("destination", {}).get("ip", "")
                                d_port = src.get("destination", {}).get("port", "")
                                proto = src.get("network", {}).get("transport", "") or src.get("network", {}).get("protocol", "")
                                pol = src.get("rule", {}).get("name", "")
                                if s_ip:
                                    msg = f"[{action.upper()}] {s_ip} -> {d_ip}:{d_port} ({proto}) Policy: {pol}"
                                else:
                                    msg = msg or "FortiGate Traffic Event"

                            ts = src.get("@timestamp", "")
                            host_name = src.get("observer", {}).get("name") or src.get("host", {}).get("name", "")
                            ds = src.get("data_stream", {}).get("dataset", "") or src.get("process", {}).get("name", "syslog")
                            
                            results["syslog_events"].append({
                                "timestamp": ts,
                                "host": host_name,
                                "dataset": ds,
                                "message": msg,
                            })
                            if len(results["syslog_samples"]) < 3 and msg:
                                results["syslog_samples"].append(msg[:180])
                            
                            if not results["last_seen"] or (ts and ts > results["last_seen"]):
                                results["last_seen"] = ts
                            if not results["first_seen"] or (ts and ts < results["first_seen"]):
                                results["first_seen"] = ts
                except Exception:
                    pass

            results["internal_hosts"] = sorted(list(results["internal_hosts"]))

            # Calcular veredicto forense
            if results["suricata_hits"] > 0:
                results["verdict"] = "ALERT_CONFIRMED"
                results["verdict_color"] = "#ff4444"
                results["verdict_label"] = "ALERTA CONFIRMADA EN RED (Suricata IDS)"
            elif results["zeek_hits"] > 0:
                results["verdict"] = "TRAFFIC_DETECTED"
                results["verdict_color"] = "#ffbb33"
                results["verdict_label"] = "TRAFICO DETECTADO (Zeek Network Logs)"
            elif results["syslog_hits"] > 0:
                results["verdict"] = "SYSLOG_ACTIVITY"
                results["verdict_color"] = "#38bdf8"
                results["verdict_label"] = f"ACTIVIDAD EN SYSLOG / FIREWALL ({results['syslog_hits']} eventos)"
            else:
                results["verdict"] = "NOT_SEEN_IN_NETWORK"
                results["verdict_color"] = "#00C851"
                results["verdict_label"] = "LIMPIO (Sin actividad en Security Onion)"

            return results

        except Exception as exc:
            results["status"] = "error"
            results["message"] = f"Fallo al cazar IOC en SO: {exc}"
            results["internal_hosts"] = list(results["internal_hosts"])
            return results

    def get_node_telemetry_summary(self, host_name: str = "secops-vascol", limit: int = 15) -> Dict[str, Any]:
        """
        Obtiene los eventos recientes de auditoria y comandos ejecutados en un nodo remoto.
        """
        if not self.is_online():
            return {"status": "offline", "events": [], "count": 0}

        try:
            query = {
                "size": limit,
                "sort": [{"@timestamp": {"order": "desc"}}],
                "query": {
                    "bool": {
                        "must": [
                            {"term": {"host.name": host_name}}
                        ]
                    }
                }
            }
            resp = self._session.post(
                f"{self.base_url}/.ds-logs-system.syslog-*/_search",
                json=query,
                verify=False,
                timeout=(self.connect_timeout, self.read_timeout),
            )
            if resp.status_code == 200:
                data = resp.json()
                total = data.get("hits", {}).get("total", {}).get("value", 0)
                events = []
                for h in data.get("hits", {}).get("hits", []):
                    src = h.get("_source", {})
                    events.append({
                        "timestamp": src.get("@timestamp"),
                        "process": src.get("process", {}).get("name", "syslog"),
                        "message": src.get("message", ""),
                        "host_ip": src.get("host", {}).get("ip", []),
                    })
                return {"status": "online", "host": host_name, "count": total, "events": events}
            return {"status": "error", "events": [], "count": 0, "code": resp.status_code}
        except Exception as exc:
            return {"status": "error", "message": str(exc), "events": [], "count": 0}

    def _detect_ioc_type(self, ioc: str) -> str:
        import re
        if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ioc):
            return "ip"
        if len(ioc) in (32, 40, 64) and re.match(r"^[a-fA-F0-9]+$", ioc):
            return "hash"
        return "domain"

    def _build_suricata_query(self, ioc: str, ioc_type: str, time_range: str) -> Dict[str, Any]:
        match_clause = (
            [{"multi_match": {"query": ioc, "fields": ["source.ip", "destination.ip"]}}]
            if ioc_type == "ip"
            else [{"query_string": {"query": f"*{ioc}*"}}]
        )
        return {
            "size": 10,
            "sort": [{"@timestamp": {"order": "desc"}}],
            "query": {
                "bool": {
                    "must": match_clause,
                    "filter": [{"range": {"@timestamp": {"gte": time_range}}}],
                }
            },
        }

    def _build_zeek_query(self, ioc: str, ioc_type: str, time_range: str) -> Dict[str, Any]:
        if ioc_type == "ip":
            match_clause = [{"multi_match": {"query": ioc, "fields": ["source.ip", "destination.ip"]}}]
        elif ioc_type == "domain":
            match_clause = [{
                "multi_match": {
                    "query": ioc,
                    "fields": ["dns.question.name", "tls.client.server_name", "http.request.host"]
                }
            }]
        else:
            match_clause = [{"multi_match": {"query": ioc, "fields": ["file.hash.sha256", "hash.sha256", "hash.md5"]}}]

        return {
            "size": 15,
            "sort": [{"@timestamp": {"order": "desc"}}],
            "query": {
                "bool": {
                    "must": match_clause,
                    "filter": [{"range": {"@timestamp": {"gte": time_range}}}],
                }
            },
        }
