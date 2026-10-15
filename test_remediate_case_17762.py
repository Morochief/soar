import os
import sys
import json
import base64
import requests
import urllib3

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_credentials():
    host = os.environ.get("STELLAR_HOST")
    email = os.environ.get("STELLAR_EMAIL")
    token = os.environ.get("STELLAR_TOKEN")
    if not (host and email and token):
        try:
            import winreg
            for hive in (winreg.HKEY_LOCAL_MACHINE, winreg.HKEY_CURRENT_USER):
                subkey = r"SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
                try:
                    with winreg.OpenKey(hive, subkey) as reg_key:
                        if not host:
                            try: host = str(winreg.QueryValueEx(reg_key, "STELLAR_HOST")[0]).strip()
                            except Exception: pass
                        if not email:
                            try: email = str(winreg.QueryValueEx(reg_key, "STELLAR_EMAIL")[0]).strip()
                            except Exception: pass
                        if not token:
                            try: token = str(winreg.QueryValueEx(reg_key, "STELLAR_TOKEN")[0]).strip()
                            except Exception: pass
                except Exception:
                    pass
        except Exception:
            pass
    return host, email, token

def get_jwt(host, email, token):
    url = f"https://{host}/connect/api/v1/access_token"
    pair = f"{email}:{token}"
    b64 = base64.b64encode(pair.encode('utf-8')).decode('utf-8')
    headers = {"Authorization": f"Basic {b64}", "Content-Type": "application/json"}
    res = requests.post(url, headers=headers, json={}, verify=False, timeout=10)
    res.raise_for_status()
    return res.json().get("access_token")

def audit_case_dpapi(case_id, ticket_id):
    host, email, token = get_credentials()
    jwt = get_jwt(host, email, token)
    headers = {"Authorization": f"Bearer {jwt}", "Content-Type": "application/json"}
    session = requests.Session()

    url_alerts = f"https://{host}/connect/api/v1/cases/{case_id}/alerts"
    r_alerts = session.get(url_alerts, headers=headers, params={"limit": "100", "skip": "0"}, verify=False, timeout=15)
    r_alerts.raise_for_status()
    alerts_data = r_alerts.json()
    docs = []
    if isinstance(alerts_data, dict):
        data_inner = alerts_data.get("data", alerts_data)
        if isinstance(data_inner, dict):
            docs = data_inner.get("docs", [])
        elif isinstance(data_inner, list):
            docs = data_inner
    elif isinstance(alerts_data, list):
        docs = alerts_data

    print(f"[*] Auditando Caso #{ticket_id} ({case_id}) - Total Alertas: {len(docs)}")

    detected_users = set()
    detected_hosts = set()
    detected_src_ips = set()
    detected_dst_ips = set()
    non_dpapi_events = []
    valid_dpapi_count = 0

    for doc in docs:
        src = doc.get("_source", {}) if isinstance(doc, dict) else {}
        event_data = src.get("event_data", {})
        xdr_event = src.get("xdr_event", {})

        user = (
            event_data.get("SubjectUserName") or 
            src.get("srcip_username") or 
            src.get("username")
        )
        if user and str(user).strip() and str(user).strip() != "-":
            domain = event_data.get("SubjectDomainName")
            u_str = f"{domain}\\{user}" if domain else str(user)
            detected_users.add(u_str)

        comp = src.get("computer_name") or src.get("host", {}).get("name") or src.get("engid_name")
        if comp and str(comp).strip():
            detected_hosts.add(str(comp).strip())

        src_ip = src.get("srcip") or event_data.get("IpAddress")
        if src_ip and str(src_ip).strip() and str(src_ip).strip() != "-":
            detected_src_ips.add(str(src_ip).strip())

        dst_ip = src.get("hostip") or src.get("host", {}).get("ip")
        if dst_ip and str(dst_ip).strip():
            detected_dst_ips.add(str(dst_ip).strip())

        event_id = src.get("event_id")
        target_name = str(event_data.get("RelativeTargetName") or "").lower()
        share_name = str(event_data.get("ShareName") or "").lower()
        comp_upper = str(comp or "").upper()
        subtype_name = str(xdr_event.get("subtype", {}).get("name") or "").lower()
        desc = str(xdr_event.get("description", "")).lower()

        is_5145 = (event_id == 5145) or ("5145" in str(src.get("stellar", {}).get("task", "")))
        is_protected_storage = "protected_storage" in target_name or "protected_storage" in subtype_name or "protected_storage" in desc
        is_ipc = "ipc$" in share_name or "ipc$" in desc
        is_vmbase8 = ("VMBASE8" in comp_upper) or ("172.16.201.8" in detected_dst_ips) or ("172.16.201.8" in str(dst_ip))

        if is_5145 and is_protected_storage and is_ipc and is_vmbase8:
            valid_dpapi_count += 1
        else:
            reason = f"Evento fuera de patron DPAPI: ID={event_id}, Share={share_name}, Target={target_name}, Host={comp}"
            non_dpapi_events.append(reason)

    print(f"  Valid DPAPI Events: {valid_dpapi_count}/{len(docs)}")
    print(f"  Non-DPAPI Events: {len(non_dpapi_events)}")
    print(f"  Detected Users: {detected_users}")
    print(f"  Detected Hosts: {detected_hosts}")
    print(f"  Detected Src IPs: {detected_src_ips}")
    if non_dpapi_events:
        print(f"  [!] Fallos de validacion: {non_dpapi_events}")
    else:
        print("  [+] AUDITORIA 100% SUPERADA: Caso completamente seguro para auto-cierre.")

if __name__ == "__main__":
    audit_case_dpapi("6ad0bf15a9a3e2ee2766c08a", "17762")
