#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
SOPHOS CENTRAL MDR / DFIR INSPECTOR (READ-ONLY)
Technoma SOC — Módulo de Visibilidad y Telemetría Forense
=============================================================================
Objetivo:
Permitir a los analistas SOC y cazadores de amenazas (MDR casero) consultar
el estado de salud, detalles de hardware, red, usuarios, alertas de seguridad
y telemetría de eventos de Sophos Central sin ejecutar acciones intrusivas
ni de remediación/aislamiento.

Uso:
  python sophos_mdr_cli.py --summary
  python sophos_mdr_cli.py --alerts
  python sophos_mdr_cli.py --suspicious
  python sophos_mdr_cli.py --host <hostname>
  python sophos_mdr_cli.py --ip <ip_address>
  python sophos_mdr_cli.py --events [--host <hostname>] [--limit 200]
  python sophos_mdr_cli.py --json (combina con cualquiera para volcado JSON)
=============================================================================
"""

import os
import sys
import json
import argparse
import datetime
from pathlib import Path
from typing import Dict, Any, List, Optional
import urllib.parse
import urllib.request
import urllib.error

# Intentar cargar variables desde .env si python-dotenv está disponible
try:
    from dotenv import load_dotenv
    env_path = Path(__file__).resolve().parent / ".env"
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)
except ImportError:
    pass

CLIENT_ID = os.getenv("SOPHOS_CLIENT_ID", "bf10b207-b32f-4f68-8b60-e162bfb2ec15")
CLIENT_SECRET = os.getenv("SOPHOS_CLIENT_SECRET", "db35190d4a22fb63a0a2693bd5dca895282c666bc3564cf7d68074bf7fb80c598020d8c65b6df2a862126f986db36910219e")
TENANT_ID = os.getenv("SOPHOS_TENANT_ID", "37a6c0dc-b2ea-4fda-b641-456560f40ef1")
REGION_URL = os.getenv("SOPHOS_REGION_URL", "https://api-br01.central.sophos.com").rstrip("/")

OAUTH_URL = "https://id.sophos.com/api/v2/oauth2/token"


class SophosCentralClient:
    """Cliente HTTP Seguro de Solo Lectura para Sophos Central API."""

    def __init__(self, client_id: str, client_secret: str, tenant_id: str, region_url: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self.tenant_id = tenant_id
        self.region_url = region_url
        self._token: Optional[str] = None
        self._token_expiry: Optional[datetime.datetime] = None

    def _get_token(self) -> str:
        """Obtiene o renueva el token OAuth2 Bearer."""
        now = datetime.datetime.now(datetime.timezone.utc)
        if self._token and self._token_expiry and now < self._token_expiry:
            return self._token

        data = urllib.parse.urlencode({
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "scope": "token"
        }).encode("utf-8")

        req = urllib.request.Request(
            OAUTH_URL,
            data=data,
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )

        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                res_json = json.loads(resp.read().decode("utf-8"))
                self._token = res_json["access_token"]
                expires_in = res_json.get("expires_in", 3600)
                self._token_expiry = now + datetime.timedelta(seconds=expires_in - 60)
                return self._token
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Error de autenticación Sophos Central (HTTP {e.code}): {err_body}")

    def request(self, path: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Realiza peticiones GET seguras a la API de Sophos."""
        token = self._get_token()
        url = f"{self.region_url}/{path.lstrip('/')}"
        if params:
            query = urllib.parse.urlencode({k: v for k, v in params.items() if v is not None})
            if query:
                url = f"{url}?{query}"

        req = urllib.request.Request(url, headers={
            "Authorization": f"Bearer {token}",
            "X-Tenant-ID": self.tenant_id,
            "Accept": "application/json"
        })

        try:
            with urllib.request.urlopen(req, timeout=25) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as e:
            err_body = e.read().decode("utf-8", errors="replace")
            raise RuntimeError(f"Error Sophos API ({path}) HTTP {e.code}: {err_body}")

    def get_all_endpoints(self, max_pages: int = 10) -> List[Dict[str, Any]]:
        """Recupera la lista total de endpoints paginando automáticamente."""
        all_items = []
        page_from_key = None
        for _ in range(max_pages):
            params = {"view": "summary", "limit": 50}
            if page_from_key:
                params["pageFromKey"] = page_from_key

            data = self.request("/endpoint/v1/endpoints", params)
            items = data.get("items", [])
            all_items.extend(items)

            next_key = data.get("pages", {}).get("nextKey")
            if not next_key:
                break
            page_from_key = next_key

        return all_items

    def search_endpoints(self, hostname: Optional[str] = None, ip: Optional[str] = None) -> List[Dict[str, Any]]:
        """Busca endpoints específicos por nombre o IP."""
        params = {"view": "summary"}
        if hostname:
            params["hostnameContains"] = hostname
        if ip:
            params["ipAddresses"] = ip

        data = self.request("/endpoint/v1/endpoints", params)
        return data.get("items", [])

    def get_endpoint_detail(self, endpoint_id: str) -> Dict[str, Any]:
        """Obtiene la ficha técnica completa de un host."""
        return self.request(f"/endpoint/v1/endpoints/{endpoint_id}")

    def get_alerts(self, limit: int = 50) -> List[Dict[str, Any]]:
        """Obtiene las alertas activas de seguridad."""
        params = {"limit": limit}
        data = self.request("/common/v1/alerts", params)
        return data.get("items", [])

    def get_siem_events(self, limit: int = 200, exclude_types: Optional[str] = None, from_date: Optional[int] = None, cursor: Optional[str] = None) -> Dict[str, Any]:
        """Obtiene el flujo de eventos de seguridad (limit >= 200) segun OpenAPI OAS 3.0."""
        limit = max(200, min(1000, limit))
        params: Dict[str, Any] = {"limit": limit}
        if exclude_types:
            params["exclude_types"] = exclude_types
        if from_date:
            params["from_date"] = from_date
        if cursor:
            params["cursor"] = cursor
        return self.request("/siem/v1/events", params)


def print_banner():
    banner = """
=============================================================================
  SOPHOS CENTRAL MDR / DFIR INSPECTOR (READ-ONLY)
  Technoma SOC — Operaciones de Ciberseguridad & Telemetría
=============================================================================
"""
    print(banner.strip())


def cmd_summary(client: SophosCentralClient, as_json: bool):
    print("[*] Consultando inventario y telemetría general de endpoints...")
    endpoints = client.get_all_endpoints()
    alerts = client.get_alerts(limit=100)

    total = len(endpoints)
    health_counts = {"good": 0, "suspicious": 0, "bad": 0, "unknown": 0}
    os_counts = {}
    tamper_protected = 0

    for ep in endpoints:
        h = ep.get("health", {}).get("overall", "unknown").lower()
        health_counts[h] = health_counts.get(h, 0) + 1

        os_info = ep.get("os", {}).get("name", "Desconocido")
        os_counts[os_info] = os_counts.get(os_info, 0) + 1

        if ep.get("tamperProtectionEnabled"):
            tamper_protected += 1

    summary_data = {
        "tenant_id": client.tenant_id,
        "total_endpoints": total,
        "health": health_counts,
        "tamper_protection_enabled": tamper_protected,
        "active_alerts_count": len(alerts),
        "os_breakdown": os_counts
    }

    if as_json:
        print(json.dumps(summary_data, indent=2))
        return

    print("\n--- RESUMEN EJECUTIVO DE POSTURA (MDR) ---")
    print(f"Total de Dispositivos Registrados : {total}")
    print(f"  [OK] Estado Saludable (Good)    : {health_counts.get('good', 0)}")
    print(f"  [!]  Sospechosos (Suspicious)   : {health_counts.get('suspicious', 0)}")
    print(f"  [X]  Criticos / Danados (Bad)   : {health_counts.get('bad', 0)}")
    print(f"Tamper Protection Activo          : {tamper_protected}/{total}")
    print(f"Alertas de Seguridad Activas      : {len(alerts)}")

    print("\n--- DISTRIBUCION POR SISTEMA OPERATIVO ---")
    for os_name, count in sorted(os_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  * {os_name:<40}: {count} hosts")


def cmd_alerts(client: SophosCentralClient, as_json: bool):
    print("[*] Obteniendo alertas activas de Sophos Central...")
    alerts = client.get_alerts(limit=100)

    if as_json:
        print(json.dumps(alerts, indent=2))
        return

    if not alerts:
        print("[OK] No hay alertas activas pendientes en Sophos Central.")
        return

    print(f"\n[!] ALERTAS ACTIVAS DETECTADAS: {len(alerts)}")
    print("-" * 105)
    print(f"{'FECHA':<20} | {'SEVERIDAD':<10} | {'DISPOSITIVO':<20} | {'DESCRIPCION / AMENAZA'}")
    print("-" * 105)

    for al in alerts:
        dt = al.get("raisedAt", "")[:19].replace("T", " ")
        sev = al.get("severity", "unknown").upper()
        host = al.get("endpoint", {}).get("name", "N/A")
        desc = al.get("description", al.get("type", "Sin detalle"))
        print(f"{dt:<20} | {sev:<10} | {host:<20} | {desc[:50]}")
    print("-" * 105)


def cmd_suspicious(client: SophosCentralClient, as_json: bool):
    print("[*] Buscando endpoints con estado 'suspicious' o 'bad'...")
    endpoints = client.get_all_endpoints()
    flagged = [ep for ep in endpoints if ep.get("health", {}).get("overall", "").lower() in ["suspicious", "bad"]]

    if as_json:
        print(json.dumps(flagged, indent=2))
        return

    if not flagged:
        print("[OK] Todos los dispositivos presentan estado de salud 'good'. No hay hosts anomalos.")
        return

    print(f"\n[!] ENDPOINTS COMPROMETIDOS O EN RIESGO: {len(flagged)}")
    print("-" * 90)
    print(f"{'HOSTNAME':<22} | {'ESTADO':<10} | {'IPs':<20} | {'ULTIMA CONEXION':<19} | {'TAMPER'}")
    print("-" * 90)

    for ep in flagged:
        name = ep.get("hostname", "Desconocido")
        state = ep.get("health", {}).get("overall", "unknown").upper()
        ips = ",".join(ep.get("ipv4Addresses", []))[:20]
        last_seen = ep.get("lastSeenAt", "")[:19].replace("T", " ")
        tp = "SI" if ep.get("tamperProtectionEnabled") else "NO"
        print(f"{name:<22} | {state:<10} | {ips:<20} | {last_seen:<19} | {tp}")
    print("-" * 90)


def cmd_host_deepdive(client: SophosCentralClient, hostname: Optional[str], ip: Optional[str], as_json: bool):
    print(f"[*] Investigando endpoint: {hostname or ip}...")
    results = client.search_endpoints(hostname=hostname, ip=ip)

    if not results:
        print(f"[!] No se encontro ningun host que coincida con '{hostname or ip}'.")
        return

    # Si hay multiples, tomamos el primero
    ep_summary = results[0]
    ep_id = ep_summary["id"]

    full_info = client.get_endpoint_detail(ep_id)

    if as_json:
        print(json.dumps(full_info, indent=2))
        return

    health = full_info.get("health", {})
    os_info = full_info.get("os", {})
    assigned_user = full_info.get("assignedUser", {})
    services = full_info.get("health", {}).get("services", {}).get("serviceDetails", [])
    threats = full_info.get("health", {}).get("threats", {}).get("status", "N/A")

    print("\n" + "=" * 80)
    print(f"  FICHA FORENSE / MDR: {full_info.get('hostname')} ({full_info.get('type')})")
    print("=" * 80)
    print(f"Endpoint ID          : {full_info.get('id')}")
    print(f"Estado de Salud      : {health.get('overall', 'unknown').upper()}")
    print(f"Estado Amenazas      : {threats}")
    print(f"Sistema Operativo    : {os_info.get('name')} ({os_info.get('build', 'N/A')})")
    print(f"Arquitectura         : {os_info.get('platform')}")
    print(f"Ultima Conexion      : {full_info.get('lastSeenAt', '')[:19].replace('T', ' ')} UTC")
    print(f"Tamper Protection    : {'ACTIVO [OK]' if full_info.get('tamperProtectionEnabled') else 'DESACTIVADO [!] '}")
    print(f"Usuario Asignado     : {assigned_user.get('name', 'N/A')} ({assigned_user.get('email', 'N/A')})")
    print(f"IPv4 Conectadas      : {', '.join(full_info.get('ipv4Addresses', []))}")
    print(f"IPv6 Conectadas      : {', '.join(full_info.get('ipv6Addresses', []))}")
    print(f"MAC Addresses        : {', '.join(full_info.get('macAddresses', []))}")

    # Interfaces de red
    interfaces = full_info.get("networkInterfaces", [])
    if interfaces:
        print("\n--- INTERFACES DE RED ---")
        for net in interfaces:
            print(f"  * {net.get('name')}: {net.get('ipv4Addresses', [])} | MAC: {net.get('macAddress')}")

    # Servicios de proteccion Sophos
    if services:
        print("\n--- ESTADO DE SERVICIOS DE SEGURIDAD ---")
        for s in services:
            st = s.get("status", "unknown").upper()
            mark = "[OK]" if st == "RUNNING" else "[!]"
            print(f"  {mark} {s.get('name', 'Servicio'):<30}: {st}")
    print("=" * 80)


def cmd_events(client: SophosCentralClient, hostname: Optional[str], limit: int, only_threats: bool, since_hours: Optional[int], as_json: bool):
    exclude_types = None
    if only_threats:
        # Excluir eventos no amenazantes segun OpenAPI (dispositivos y updates rutinarios)
        exclude_types = "Event::Endpoint::Device::AlertedOnly,Event::Endpoint::UpdateSuccess,Event::Endpoint::UpdateRebootRequired"

    from_date = None
    if since_hours:
        since_dt = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=min(24, since_hours))
        from_date = int(since_dt.timestamp())

    print(f"[*] Obteniendo eventos SIEM (limite: {limit}, amenazas_unicamente: {only_threats})...")
    res = client.get_siem_events(limit=limit, exclude_types=exclude_types, from_date=from_date)
    events = res.get("items", [])

    if hostname:
        hostname_clean = hostname.lower()
        events = [ev for ev in events if hostname_clean in ev.get("endpoint_name", "").lower() or hostname_clean in ev.get("source_info", {}).get("ip", "") or hostname_clean in ev.get("location", "").lower()]

    if as_json:
        print(json.dumps(events, indent=2))
        return

    if not events:
        print("[OK] No se encontraron eventos de seguridad en el rango solicitado.")
        return

    print(f"\n[*] EVENTOS DE SEGURIDAD RECUPERADOS: {len(events)}")
    print("-" * 120)
    print(f"{'FECHA':<20} | {'SEVERIDAD':<10} | {'HOST / UBICACION':<20} | {'TIPO':<28} | {'DESCRIPCION / DETALLE'}")
    print("-" * 120)

    for ev in events[:50]:
        dt = ev.get("created_at", "")[:19].replace("T", " ")
        sev = ev.get("severity", "INFO").upper()
        host = ev.get("endpoint_name") or ev.get("location") or "N/A"
        etype = ev.get("type", "N/A")[:28]
        desc = ev.get("name") or ev.get("description") or "Evento"
        print(f"{dt:<20} | {sev:<10} | {host[:20]:<20} | {etype:<28} | {desc[:40]}")

        # Telemetria Forense Profunda (OpenAPI / Schema Reference)
        forensic_tags = []
        if ev.get("origin"):
            forensic_tags.append(f"Origen Motor: {ev.get('origin')}")
        if ev.get("group"):
            forensic_tags.append(f"Grupo: {ev.get('group')}")
        if ev.get("threat"):
            forensic_tags.append(f"Threat: {ev.get('threat')}")
        if ev.get("appSha256"):
            forensic_tags.append(f"SHA256: {ev.get('appSha256')}")
        if ev.get("appCerts"):
            certs = ev.get("appCerts", [])
            for c in certs:
                forensic_tags.append(f"Firma Digital: {c.get('signer')} (Thumbprint: {c.get('thumbprint')})")
        if ev.get("amsi_threat_data"):
            amsi = ev.get("amsi_threat_data", {})
            forensic_tags.append(f"AMSI Script: {amsi.get('processName')} (PID {amsi.get('processId')}, Ruta: {amsi.get('processPath')}) -> Padre: {amsi.get('parentProcessPath')}")
        if ev.get("ips_threat_data"):
            ips = ev.get("ips_threat_data", {})
            dir_str = "Inbound" if ips.get("detectionType") == 0 else "Outbound"
            forensic_tags.append(f"IPS [{dir_str}]: {ips.get('remoteIp')}:{ips.get('remotePort')} -> Local:{ips.get('localPort')} | Binario: {ips.get('executableName')} ({ips.get('executablePath')})")
        if ev.get("core_remedy_items"):
            remedy = ev.get("core_remedy_items", {})
            items = remedy.get("items", [])
            for it in items:
                forensic_tags.append(f"Remediacion EDR: {it.get('type')} '{it.get('descriptor') or it.get('processPath')}' -> Resultado: {it.get('result')}")
        if ev.get("source_info", {}).get("case_id"):
            forensic_tags.append(f"MDR Case ID: {ev['source_info']['case_id']} ({ev['source_info'].get('detection_name')})")

        if forensic_tags:
            for tag in forensic_tags:
                print(f"    --> [FORENSE] {tag}")

    if len(events) > 50:
        print(f"... y {len(events) - 50} eventos mas (utilice --json o filtre por --host / --only-threats para acotar).")
    print("-" * 120)


def main():
    parser = argparse.ArgumentParser(
        description="Sophos Central MDR / DFIR Inspector — Herramienta de Solo Lectura para el SOC."
    )
    parser.add_argument("--summary", action="store_true", help="Muestra el resumen de salud, postura y distribucion del parque.")
    parser.add_argument("--alerts", action="store_true", help="Lista las alertas activas de seguridad no resueltas.")
    parser.add_argument("--suspicious", action="store_true", help="Lista unicamente los hosts con estado de salud suspicious o bad.")
    parser.add_argument("--host", type=str, help="Inspeccion detallada (deep dive) de un equipo por Hostname.")
    parser.add_argument("--ip", type=str, help="Inspeccion detallada (deep dive) de un equipo por IP.")
    parser.add_argument("--events", action="store_true", help="Consulta eventos de seguridad via SIEM API (OpenAPI 3.0).")
    parser.add_argument("--only-threats", action="store_true", help="Filtra eventos excluyendo ruido rutinario (updates y dispositivos), dejando malware, web blocks y detecciones.")
    parser.add_argument("--since", type=int, help="Filtrar eventos ocurridos en las ultimas N horas (maximo 24 horas segun OpenAPI).")
    parser.add_argument("--limit", type=int, default=200, help="Limite de eventos a consultar (minimo 200, maximo 1000).")
    parser.add_argument("--json", action="store_true", help="Salida en formato JSON crudo para pipelines o volcados.")

    args = parser.parse_args()

    if not any([args.summary, args.alerts, args.suspicious, args.host, args.ip, args.events]):
        print_banner()
        parser.print_help()
        sys.exit(0)

    if not args.json:
        print_banner()

    client = SophosCentralClient(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        tenant_id=TENANT_ID,
        region_url=REGION_URL
    )

    try:
        if args.summary:
            cmd_summary(client, args.json)
        elif args.alerts:
            cmd_alerts(client, args.json)
        elif args.suspicious:
            cmd_suspicious(client, args.json)
        elif args.host or args.ip:
            cmd_host_deepdive(client, args.host, args.ip, args.json)
        elif args.events:
            cmd_events(client, args.host, args.limit, args.only_threats, args.since, args.json)
    except Exception as e:
        print(f"\n[!] ERROR EN EJECUCION MDR: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
