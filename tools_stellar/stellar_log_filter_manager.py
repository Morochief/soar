#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Módulo Gestor de Log Filters para Stellar Cyber (Command Center SOC)
Permite listar, inspeccionar, crear y actualizar Log Filters directamente vía API.
Puede ser importado en command_center.py o ejecutado de forma independiente.
"""

import os
import requests
import json
import base64
import urllib3
from typing import Dict, List, Optional, Any

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class StellarLogFilterManager:
    def __init__(self, host: Optional[str] = None, email: Optional[str] = None, token: Optional[str] = None, cust_id: Optional[str] = None):
        self.host = host or os.environ.get("STELLAR_HOST", "technoma.stellarcyber.cloud")
        self.email = email or os.environ.get("STELLAR_EMAIL", "kevinmoraes@technoma.com.py")
        self.token = token or os.environ.get("STELLAR_TOKEN", "")
        self.cust_id = cust_id or "e511c3fc54cd4d668bb67612c2ef4b04"
        self._jwt = None

    def _get_headers(self) -> Dict[str, str]:
        if not self._jwt:
            auth_str = f"{self.email}:{self.token}"
            auth_b64 = base64.b64encode(auth_str.encode('utf-8')).decode('utf-8')
            headers_auth = {"Authorization": f"Basic {auth_b64}", "Content-Type": "application/x-www-form-urlencoded"}
            r = requests.post(f"https://{self.host}/connect/api/v1/access_token", headers=headers_auth, json={}, timeout=15, verify=False)
            if r.status_code == 200:
                self._jwt = r.json().get("access_token")
            else:
                raise Exception(f"Error de autenticación Stellar Cyber: {r.status_code} {r.text}")
        return {"Authorization": f"Bearer {self._jwt}", "Content-Type": "application/json"}

    def list_filters(self, filter_keyword: Optional[str] = None) -> List[Dict[str, Any]]:
        """Obtiene la lista completa de Log Filters registrados."""
        url = f"https://{self.host}/connect/api/v1/log_filters"
        r = requests.get(url, headers=self._get_headers(), timeout=15, verify=False)
        if r.status_code != 200:
            raise Exception(f"Error al listar filtros: {r.status_code} {r.text}")
        
        all_filters = r.json().get("data", [])
        if filter_keyword:
            kw = filter_keyword.lower()
            return [f for f in all_filters if kw in f.get("name", "").lower()]
        return all_filters

    def get_filter(self, filter_id: str) -> Dict[str, Any]:
        """Obtiene el detalle completo de un filtro por ID."""
        url = f"https://{self.host}/connect/api/v1/log_filters/{filter_id}"
        r = requests.get(url, headers=self._get_headers(), timeout=15, verify=False)
        if r.status_code != 200:
            raise Exception(f"Error al obtener filtro {filter_id}: {r.status_code} {r.text}")
        return r.json().get("data", {})

    def create_filter(self, name: str, rules_dict: Dict[str, Any], dev_type: str = "fw_fortigate", dev_type_label: str = "Fortinet FortiGate") -> Dict[str, Any]:
        """
        Crea un nuevo Log Filter en Stellar Cyber.
        
        Ejemplo de rules_dict:
        {
            "action": {"type": "string", "op": "==", "value": ["passthrough"]},
            "dstip": {"type": "ip", "op": "matches", "value": ["1.2.3.4", "10.0.0.0/8"]}
        }
        """
        url = f"https://{self.host}/connect/api/v1/log_filters"
        rule_content = {
            "dev_type": dev_type,
            "dev_type_label": dev_type_label,
            "rules": rules_dict
        }
        payload = {
            "name": name,
            "cust_id": self.cust_id,
            "content": json.dumps(rule_content)
        }
        r = requests.post(url, headers=self._get_headers(), json=payload, timeout=15, verify=False)
        if r.status_code not in (200, 201):
            raise Exception(f"Error creando filtro {name}: {r.status_code} {r.text}")
        return r.json().get("data", {})

    def add_ips_to_filter(self, filter_id: str, new_ips_or_cidrs: List[str]) -> Dict[str, Any]:
        """Suma nuevas IPs o subredes al campo dstip de un filtro existente."""
        filtro = self.get_filter(filter_id)
        content = json.loads(filtro.get("content", "{}"))
        
        rules = content.setdefault("rules", {})
        dstip_rule = rules.setdefault("dstip", {"type": "ip", "op": "matches", "value": []})
        current_ips = dstip_rule.get("value", [])
        
        updated_ips = list(dict.fromkeys(current_ips + new_ips_or_cidrs))
        dstip_rule["value"] = updated_ips
        
        url = f"https://{self.host}/connect/api/v1/log_filters/{filter_id}"
        payload_put = {
            "name": filtro["name"],
            "cust_id": filtro["cust_id"],
            "content": json.dumps(content)
        }
        r = requests.put(url, headers=self._get_headers(), json=payload_put, timeout=15, verify=False)
        if r.status_code != 200:
            raise Exception(f"Error actualizando filtro {filter_id}: {r.status_code} {r.text}")
        return {"id": filter_id, "name": filtro["name"], "total_ips": len(updated_ips), "ips": updated_ips}

if __name__ == "__main__":
    mgr = StellarLogFilterManager()
    print("[*] Conectando a Stellar Cyber Log Filter Manager...")
    filtros = mgr.list_filters("drop")
    print(f"[+] Total filtros de tipo DROP encontrados: {len(filtros)}")
    for f in filtros:
        print(f"  - [{f.get('_id')}] {f.get('name')}")
