"""
19_actualizar_log_filters_en_caliente.py
----------------------------------------
Herramienta oficial del SOC para actualizar en caliente (Hot-Reload) cualquier Log Filter
existente en Stellar Cyber vía `PUT /connect/api/v1/log_filters/{id}` preservando su
asociación activa al Sensor Profile (`in_use.sensor_profile`).

Por qué existe esta herramienta:
- El endpoint `/connect/api/v1/data_sensors/sensor_profiles` solo expone `GET` en la API pública.
- Crear un filtro nuevo con `POST` deja `in_use: {}` hasta vincularlo manualmente en la GUI.
- En cambio, modificar un filtro YA vinculado al perfil (`PUT /connect/api/v1/log_filters/{id}`)
  aplica los cambios en caliente en el Modular Sensor sin intervención manual en la consola web.

Incluye las configuraciones quirúrgicas de referencia desplegadas el 18/10/2026:
  1. `69ba96e97ce7a80ccca17cc4` (`filter - 165.1.125.196`) -> Canal TLS 8889 de Sensores (`192.168.15.70`, `192.168.9.5`)
  2. `6ac785e01b7191d76a1b1d02` (`Drop_FW_Denial_Internal_WUDO_7680`) -> Incluye VLAN Servidores `192.168.15.0/24`
  3. `6ad394ab3a5c745b75a319be` (`Drop_FW_Close_TCP_7001_and_8010_Internal_Services`) -> Cierres TCP 7001 y 8010
  4. `691ccf38fd93619a950d179c` (`Filter NOC deny TCP 7002 8000`) -> Restringido a `deny`/`close` (preserva `accept`)
  5. `691dfc77fd93619a950d1813` (`technoma NOC deny BGP`) -> Restringido a `deny`/`close` (preserva `accept`)

Uso:
  python auditoria_cuota_stellar/19_actualizar_log_filters_en_caliente.py --status
  python auditoria_cuota_stellar/19_actualizar_log_filters_en_caliente.py --apply-baseline
"""

import os
import sys
import json
import base64
import argparse
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

HOST = os.environ.get("STELLAR_HOST", "technoma.stellarcyber.cloud")
EMAIL = os.environ.get("STELLAR_EMAIL", "kevinmoraes@technoma.com.py")
TOKEN = os.environ.get("STELLAR_TOKEN", "rOnKd624_hTAvi5TyDDsPmfbiEOf3NThpGMkUL8sR6IrmkBEovOn41EvFdLtdWkTO6XuFSH6d16x0B1J3lJSBQ")

BASELINE_FILTERS = {
    "69ba96e97ce7a80ccca17cc4": {
        "name": "filter - 165.1.125.196",
        "cust_id": "all-tenants",
        "content": {
            "dev_type": "",
            "dev_type_label": "",
            "rules": {
                "srcip": {"type": "ip", "op": "matches", "value": ["192.168.15.70", "192.168.9.5"]},
                "dstip": {"type": "ip", "op": "matches", "value": ["165.1.125.196"]}
            }
        }
    },
    "6ac785e01b7191d76a1b1d02": {
        "name": "Drop_FW_Denial_Internal_WUDO_7680",
        "cust_id": "e511c3fc54cd4d668bb67612c2ef4b04",
        "content": {
            "dev_type": "fw_fortigate",
            "dev_type_label": "Fortinet FortiGate",
            "rules": {
                "action": {"type": "string", "op": "==", "value": ["deny"]},
                "dstport": {"type": "number", "op": "==", "value": [7680]},
                "srcip": {"type": "ip", "op": "matches", "value": ["192.168.169.0/24", "192.168.100.0/24", "192.168.15.0/24"]},
                "dstip": {"type": "ip", "op": "matches", "value": ["192.168.169.0/24", "192.168.100.0/24", "192.168.15.0/24"]},
                "proto": {"type": "number", "op": "==", "value": [6]}
            }
        }
    },
    "6ad394ab3a5c745b75a319be": {
        "name": "Drop_FW_Close_TCP_7001_and_8010_Internal_Services",
        "cust_id": "e511c3fc54cd4d668bb67612c2ef4b04",
        "content": {
            "dev_type": "fw_fortigate",
            "dev_type_label": "Fortinet FortiGate",
            "rules": {
                "action": {"type": "string", "op": "==", "value": ["close"]},
                "dstport": {"type": "number", "op": "==", "value": [7001, 8010]},
                "dstip": {"type": "ip", "op": "matches", "value": ["192.168.15.60/32", "10.11.5.4/32"]}
            }
        }
    },
    "691ccf38fd93619a950d179c": {
        "name": "Filter NOC deny TCP 7002 8000",
        "cust_id": "e511c3fc54cd4d668bb67612c2ef4b04",
        "content": {
            "dev_type": "fw_fortigate",
            "dev_type_label": "Fortinet FortiGate",
            "rules": {
                "dstport": {"type": "number", "op": "==", "value": [7002, 8000, 38881]},
                "action": {"type": "string", "op": "==", "value": ["deny", "close", "timeout", "client-rst", "server-rst"]}
            }
        }
    },
    "691dfc77fd93619a950d1813": {
        "name": "technoma NOC deny BGP",
        "cust_id": "e511c3fc54cd4d668bb67612c2ef4b04",
        "content": {
            "dev_type": "fw_fortigate",
            "dev_type_label": "Fortinet FortiGate",
            "rules": {
                "appid_name": {"type": "string", "op": "==", "value": ["BGP"]},
                "action": {"type": "string", "op": "==", "value": ["deny", "close", "timeout", "client-rst", "server-rst"]}
            }
        }
    }
}


def get_jwt():
    auth_str = f"{EMAIL}:{TOKEN}"
    auth_b64 = base64.b64encode(auth_str.encode("utf-8")).decode("utf-8")
    headers = {"Authorization": f"Basic {auth_b64}", "Content-Type": "application/x-www-form-urlencoded"}
    r = requests.post(f"https://{HOST}/connect/api/v1/access_token", headers=headers, json={}, timeout=15, verify=False)
    r.raise_for_status()
    return r.json().get("access_token")


def main():
    parser = argparse.ArgumentParser(description="Actualizador en caliente de Log Filters vía API PUT")
    parser.add_argument("--status", action="store_true", help="Muestra el estado actual de los 5 filtros quirúrgicos de referencia")
    parser.add_argument("--apply-baseline", action="store_true", help="Re-aplica en caliente (PUT) el baseline de los 5 filtros quirúrgicos")
    args = parser.parse_args()

    jwt = get_jwt()
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}

    r = requests.get(f"https://{HOST}/connect/api/v1/log_filters", headers=headers, timeout=20, verify=False)
    r.raise_for_status()
    all_filters = {f.get("_id"): f for f in r.json().get("data", [])}

    if args.apply_baseline:
        print("⚡ Aplicando Baseline Quirúrgico en Caliente (PUT /connect/api/v1/log_filters/{id})...")
        for fid, cfg in BASELINE_FILTERS.items():
            payload = {
                "name": cfg["name"],
                "cust_id": cfg["cust_id"],
                "content": json.dumps(cfg["content"], separators=(",", ":"))
            }
            resp = requests.put(
                f"https://{HOST}/connect/api/v1/log_filters/{fid}",
                headers=headers,
                json=payload,
                timeout=15,
                verify=False
            )
            print(f"  -> [{fid}] {cfg['name']}: HTTP {resp.status_code}")

        r = requests.get(f"https://{HOST}/connect/api/v1/log_filters", headers=headers, timeout=20, verify=False)
        all_filters = {f.get("_id"): f for f in r.json().get("data", [])}

    print("\n=====================================================================================")
    print("📋 ESTADO EN VIVO DE LOS 5 LOG FILTERS QUIRÚRGICOS EN EL MODULAR SENSOR")
    print("=====================================================================================")
    for fid in BASELINE_FILTERS:
        f = all_filters.get(fid, {})
        in_use = f.get("in_use", {}).get("sensor_profile", [])
        print(f"ID: {fid} | Nombre: {f.get('name')}")
        print(f"  Perfiles Asociados: {in_use}")
        print(f"  Content: {f.get('content')}")
        print("-" * 85)


if __name__ == "__main__":
    main()
