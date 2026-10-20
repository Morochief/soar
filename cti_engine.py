"""
=============================================================================
  STELLAR CYBER OpenXDR - CTI INTEL ENGINE (Threat Hunting Module)
  Integracion: VirusTotal v3 | AbuseIPDB v2 | URLScan.io v1 | MxToolbox v1
  Gobernanza: Technoma SOC L1/L2 - Formato DFIR de Alta Fidelidad
=============================================================================
"""

import os
import re
import json
import time
import requests
import urllib3
from concurrent.futures import ThreadPoolExecutor
from typing import Dict, Any, Optional, List, Tuple
from datetime import datetime

# Desactivar advertencias SSL en consultas CTI perimetrales
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Utilizar certificados del almacén de Windows cuando estén disponibles
try:
    import truststore
    truststore.inject_into_ssl()
except Exception:
    pass

class CtiEngine:
    """
    Motor unificado de Cyber Threat Intelligence (CTI).
    Consulta en paralelo o bajo demanda la reputacion de IOCs (IPs, Dominios, Hashes, URLs, SPF, DMARC, MX, Blacklists).
    """

    DEFAULT_TIMEOUT = 12
    VERIFY_SSL = False
    CACHE_TTL_SECONDS = 900  # 15 minutos de caché en memoria para evitar rate-limits y acelerar consultas repetidas
    _TRI_SCAN_CACHE: Dict[str, Tuple[float, Dict[str, Any]]] = {}

    @classmethod
    def get_api_keys(cls) -> Dict[str, str]:
        """Obtiene las API keys desde variables de entorno (.env) con fallback a registro Windows."""
        try:
            from dotenv import load_dotenv
            env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
            if os.path.exists(env_path):
                load_dotenv(env_path)
            else:
                load_dotenv()
        except Exception:
            pass

        keys = {
            "virustotal": os.environ.get("VIRUSTOTAL_API_KEY", "").strip(),
            "abuseipdb": os.environ.get("ABUSEIPDB_API_KEY", "").strip(),
            "urlscan": os.environ.get("URLSCAN_API_KEY", "").strip(),
            "mxtoolbox": os.environ.get("MXTOOLBOX_API_KEY", "").strip(),
            "nvd": os.environ.get("NVD_API_KEY", "").strip(),
        }

        # Fallback resiliente: Consultar el Registro de Usuario de Windows si aún no se reflejan en os.environ
        try:
            import winreg
            for k, env_name in [("virustotal", "VIRUSTOTAL_API_KEY"),
                                ("abuseipdb", "ABUSEIPDB_API_KEY"),
                                ("urlscan", "URLSCAN_API_KEY"),
                                ("mxtoolbox", "MXTOOLBOX_API_KEY"),
                                ("nvd", "NVD_API_KEY")]:
                if not keys[k]:
                    try:
                        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment") as reg_key:
                            val, _ = winreg.QueryValueEx(reg_key, env_name)
                            keys[k] = str(val).strip()
                    except Exception:
                        pass
        except Exception:
            pass

        return keys

    @classmethod
    def detect_observable_type(cls, observable: str) -> str:
        obs = observable.strip()
        if not obs:
            return "unknown"

        if re.match(r"^CVE-\d{4}-\d{4,}$", obs, re.IGNORECASE):
            return "cve"

        if obs.startswith("http://") or obs.startswith("https://"):
            return "url"

        ipv4_regex = r"^(\d{1,3}\.){3}\d{1,3}$"
        if re.match(ipv4_regex, obs):
            parts = obs.split(".")
            if all(0 <= int(p) <= 255 for p in parts):
                return "ip"

        hex_len = len(obs)
        if re.match(r"^[a-fA-F0-9]+$", obs):
            if hex_len in (32, 40, 64):
                return "hash"

        domain_regex = r"^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,}$"
        if re.match(domain_regex, obs):
            return "domain"

        return "string"

    @classmethod
    def query_abuseipdb(cls, ip: str, api_key: Optional[str] = None) -> Dict[str, Any]:
        key = api_key or cls.get_api_keys()["abuseipdb"]
        if not key:
            return {"source": "AbuseIPDB", "status": "error", "error": "API Key de AbuseIPDB no configurada en entorno (ABUSEIPDB_API_KEY)."}

        url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}&maxAgeInDays=90&verbose"
        headers = {"Key": key, "Accept": "application/json"}
        try:
            r = requests.get(url, headers=headers, timeout=cls.DEFAULT_TIMEOUT, verify=cls.VERIFY_SSL)
            if r.status_code == 200:
                d = r.json().get("data", {})
                score = d.get("abuseConfidenceScore", 0)
                reports = d.get("totalReports", 0)
                reports_list = d.get("reports", [])[:5]
                recent_comments = []
                for rep in reports_list:
                    c = rep.get("comment", "").strip()
                    if c:
                        recent_comments.append(f"[{rep.get('reportedAt', '')[:10]}] {c[:100]}")

                return {
                    "source": "AbuseIPDB",
                    "status": "success",
                    "ip": ip,
                    "score": score,
                    "is_malicious": score >= 25,
                    "verdict": "MALICIOSO" if score >= 75 else ("SOSPECHOSO" if score >= 25 else "LIMPIO / BENIGNO"),
                    "color": "#ef4444" if score >= 75 else ("#f59e0b" if score >= 25 else "#10b981"),
                    "total_reports": reports,
                    "distinct_users": d.get("numDistinctUsers", 0),
                    "isp": d.get("isp", "N/A"),
                    "country": d.get("countryCode", "N/A"),
                    "domain": d.get("domain", "N/A"),
                    "usage_type": d.get("usageType", "N/A"),
                    "is_whitelisted": d.get("isWhitelisted", False),
                    "is_tor": d.get("isTor", False),
                    "last_reported": d.get("lastReportedAt", "N/A"),
                    "recent_comments": recent_comments
                }
            elif r.status_code == 429:
                return {"source": "AbuseIPDB", "status": "rate_limited", "error": "Limite de cuota (Rate Limit) excedido en AbuseIPDB."}
            else:
                return {"source": "AbuseIPDB", "status": "error", "error": f"HTTP {r.status_code}: {r.text[:120]}"}
        except Exception as e:
            return {"source": "AbuseIPDB", "status": "exception", "error": str(e)}

    @classmethod
    def query_virustotal(cls, observable: str, api_key: Optional[str] = None) -> Dict[str, Any]:
        key = api_key or cls.get_api_keys()["virustotal"]
        if not key:
            return {"source": "VirusTotal", "status": "error", "error": "API Key de VirusTotal no configurada en entorno (VIRUSTOTAL_API_KEY)."}

        obs_type = cls.detect_observable_type(observable)
        headers = {"x-apikey": key}

        if obs_type == "ip":
            endpoint = f"https://www.virustotal.com/api/v3/ip_addresses/{observable}"
        elif obs_type == "domain":
            endpoint = f"https://www.virustotal.com/api/v3/domains/{observable}"
        elif obs_type == "hash":
            endpoint = f"https://www.virustotal.com/api/v3/files/{observable}"
        elif obs_type == "url":
            import base64
            url_id = base64.urlsafe_b64encode(observable.encode()).decode().strip("=")
            endpoint = f"https://www.virustotal.com/api/v3/urls/{url_id}"
        else:
            return {"source": "VirusTotal", "status": "unsupported", "error": f"Tipo de observable '{obs_type}' no soportado para VT directo."}

        try:
            r = requests.get(endpoint, headers=headers, timeout=cls.DEFAULT_TIMEOUT, verify=cls.VERIFY_SSL)
            if r.status_code == 200:
                data = r.json().get("data", {})
                attr = data.get("attributes", {})
                stats = attr.get("last_analysis_stats", {})
                mal = stats.get("malicious", 0)
                susp = stats.get("suspicious", 0)
                harmless = stats.get("harmless", 0)
                undetected = stats.get("undetected", 0)
                total = mal + susp + harmless + undetected

                is_mal = (mal >= 3)
                is_susp = (mal > 0 or susp >= 2)
                verdict = "MALICIOSO" if is_mal else ("SOSPECHOSO" if is_susp else "LIMPIO / BENIGNO")
                color = "#ef4444" if is_mal else ("#f59e0b" if is_susp else "#10b981")

                engines = attr.get("last_analysis_results", {})
                flagged_engines = []
                for eng_name, eng_info in engines.items():
                    category = eng_info.get("category", "")
                    if category in ("malicious", "suspicious"):
                        flagged_engines.append(f"{eng_name}: {eng_info.get('result', category)}")

                return {
                    "source": "VirusTotal",
                    "status": "success",
                    "observable": observable,
                    "type": obs_type,
                    "malicious_count": mal,
                    "suspicious_count": susp,
                    "total_engines": total,
                    "detection_ratio": f"{mal}/{total}",
                    "verdict": verdict,
                    "color": color,
                    "reputation": attr.get("reputation", 0),
                    "as_owner": attr.get("as_owner") or attr.get("network", "N/A"),
                    "asn": attr.get("asn", "N/A"),
                    "country": attr.get("country", "N/A"),
                    "tags": attr.get("tags", [])[:8],
                    "flagged_engines": flagged_engines[:10],
                    "categories": list(attr.get("categories", {}).values())[:5]
                }
            elif r.status_code == 404:
                return {"source": "VirusTotal", "status": "not_found", "verdict": "SIN REGISTRO PREVIO", "color": "#94a3b8", "observable": observable}
            elif r.status_code == 429:
                return {"source": "VirusTotal", "status": "rate_limited", "error": "Limite de cuota (Rate Limit) excedido en VirusTotal."}
            else:
                return {"source": "VirusTotal", "status": "error", "error": f"HTTP {r.status_code}: {r.text[:120]}"}
        except Exception as e:
            return {"source": "VirusTotal", "status": "exception", "error": str(e)}

    @classmethod
    def query_urlscan(cls, target: str, api_key: Optional[str] = None) -> Dict[str, Any]:
        key = api_key or cls.get_api_keys()["urlscan"]
        if not key:
            return {"source": "URLScan.io", "status": "error", "error": "API Key de URLScan.io no configurada en entorno (URLSCAN_API_KEY)."}

        obs_type = cls.detect_observable_type(target)
        if obs_type == "ip":
            q = f"ip:{target}"
        elif obs_type == "domain":
            q = f"domain:{target}"
        elif obs_type == "url":
            q = f'page.url:"{target}"'
        else:
            q = f'"{target}"'

        url = f"https://urlscan.io/api/v1/search/?q={q}&size=5"
        headers = {"API-Key": key}
        try:
            r = requests.get(url, headers=headers, timeout=cls.DEFAULT_TIMEOUT, verify=cls.VERIFY_SSL)
            if r.status_code == 200:
                results = r.json().get("results", [])
                if not results:
                    return {"source": "URLScan.io", "status": "not_found", "target": target, "verdict": "SIN ESCANEOS PREVIOS", "color": "#94a3b8", "results_count": 0}

                first = results[0]
                page = first.get("page", {}) or {}
                stats = first.get("stats", {}) or {}
                task = first.get("task", {}) or {}
                verdicts = first.get("verdicts", {}) or {}
                overall = verdicts.get("overall", {}) or {}
                is_mal = overall.get("malicious", False)
                score = overall.get("score", 0)

                engines_mal = verdicts.get("engines", {}).get("maliciousTotal", 0) if isinstance(verdicts.get("engines"), dict) else 0
                community_score = verdicts.get("community", {}).get("score", 0) if isinstance(verdicts.get("community"), dict) else 0

                verdict_str = "MALICIOSO" if (is_mal or score > 50 or engines_mal > 0) else ("SOSPECHOSO" if (score > 0 or community_score < 0) else "OBSERVADO / REGISTRADO")
                color = "#ef4444" if (is_mal or score > 50 or engines_mal > 0) else ("#f59e0b" if score > 0 else "#38bdf8")

                scans_list = []
                for res_item in results[:4]:
                    p = res_item.get("page", {}) or {}
                    t = res_item.get("task", {}) or {}
                    scans_list.append({
                        "time": t.get("time", "N/A"),
                        "url": p.get("url") or t.get("url", "N/A"),
                        "ip": p.get("ip", "N/A"),
                        "server": p.get("server", "N/A"),
                        "title": p.get("title", "N/A"),
                        "result_url": res_item.get("result", "N/A")
                    })

                return {
                    "source": "URLScan.io",
                    "status": "success",
                    "target": target,
                    "results_count": len(results),
                    "verdict": verdict_str,
                    "color": color,
                    "malicious": is_mal,
                    "score": score,
                    "page_url": page.get("url") or task.get("url", "N/A"),
                    "page_ip": page.get("ip", "N/A"),
                    "page_title": page.get("title", "N/A"),
                    "server_banner": page.get("server", "N/A"),
                    "country": page.get("country", "N/A"),
                    "asn": page.get("asn", "N/A"),
                    "asn_name": page.get("asnname", "N/A"),
                    "ptr": page.get("ptr", "N/A"),
                    "mime_type": page.get("mimeType", "N/A"),
                    "status_code": page.get("status", "N/A"),
                    "uniq_ips": stats.get("uniqIPs", 0),
                    "uniq_countries": stats.get("uniqCountries", 0),
                    "total_requests": stats.get("requests", 0),
                    "scan_time": task.get("time", "N/A"),
                    "scan_uuid": task.get("uuid", "N/A"),
                    "result_url": first.get("result", "N/A"),
                    "screenshot_url": first.get("screenshot", ""),
                    "historical_scans": scans_list
                }
            elif r.status_code == 429:
                return {"source": "URLScan.io", "status": "rate_limited", "error": "Limite de cuota excedido en URLScan.io."}
            else:
                return {"source": "URLScan.io", "status": "error", "error": f"HTTP {r.status_code}: {r.text[:120]}"}
        except Exception as e:
            return {"source": "URLScan.io", "status": "exception", "error": str(e)}

    @classmethod
    def query_mxtoolbox(cls, target: str, command: str = "dns", api_key: Optional[str] = None) -> Dict[str, Any]:
        key = api_key or cls.get_api_keys()["mxtoolbox"]
        if not key:
            return {"source": "MxToolbox", "status": "error", "error": "API Key de MxToolbox no configurada en entorno (MXTOOLBOX_API_KEY)."}

        clean_target = target.strip()
        clean_target = re.sub(r"^https?://", "", clean_target).split("/")[0].split(":")[0]

        cmd = command.lower().strip()
        url = f"https://api.mxtoolbox.com/api/v1/Lookup/{cmd}/?argument={clean_target}"
        headers = {"Authorization": key, "Accept": "application/json"}

        try:
            r = requests.get(url, headers=headers, timeout=cls.DEFAULT_TIMEOUT, verify=cls.VERIFY_SSL)
            if r.status_code == 200:
                data = r.json()
                failed = data.get("Failed") or []
                warnings = data.get("Warnings") or []
                passed = data.get("Passed") or []
                records = data.get("Records") or []
                errors = data.get("Errors") or []

                has_critical_failure = len(failed) > 0 or len(errors) > 0
                has_warnings = len(warnings) > 0

                if has_critical_failure:
                    verdict = "VULNERABLE / FALLAS DETECTADAS"
                    color = "#ef4444"
                elif has_warnings:
                    verdict = "ADVERTENCIA / CONFIGURACIÓN INCOMPLETA"
                    color = "#f59e0b"
                else:
                    verdict = "VÁLIDO / ALINEADO"
                    color = "#10b981"

                failed_details = [f"{item.get('Name')}: {item.get('Info')}" for item in failed]
                warning_details = [f"{item.get('Name')}: {item.get('Info')}" for item in warnings]
                passed_details = [f"{item.get('Name')}: {item.get('Info')}" for item in passed[:8]]

                return {
                    "source": "MxToolbox",
                    "status": "success",
                    "target": clean_target,
                    "command": cmd.upper(),
                    "verdict": verdict,
                    "color": color,
                    "failed_count": len(failed),
                    "warnings_count": len(warnings),
                    "passed_count": len(passed),
                    "failed_details": failed_details,
                    "warning_details": warning_details,
                    "passed_details": passed_details,
                    "records": records[:5],
                    "time_recorded": data.get("TimeRecorded", "N/A"),
                    "nameserver": data.get("ReportingNameServer", "N/A")
                }
            elif r.status_code == 401:
                return {"source": "MxToolbox", "status": "auth_error", "error": "API Key de MxToolbox inválida o rechazada (HTTP 401)."}
            elif r.status_code == 429:
                return {"source": "MxToolbox", "status": "rate_limited", "error": "Límite de solicitudes de MxToolbox excedido (HTTP 429)."}
            else:
                return {"source": "MxToolbox", "status": "error", "error": f"HTTP {r.status_code}: {r.text[:120]}"}
        except Exception as e:
            return {"source": "MxToolbox", "status": "exception", "error": str(e)}

    @classmethod
    def query_phishing_email_defense(cls, domain: str) -> Dict[str, Any]:
        clean_domain = domain.strip()
        clean_domain = re.sub(r"^https?://", "", clean_domain).split("/")[0].split(":")[0]

        with ThreadPoolExecutor(max_workers=3) as executor:
            f_spf = executor.submit(cls.query_mxtoolbox, clean_domain, "spf")
            f_dmarc = executor.submit(cls.query_mxtoolbox, clean_domain, "dmarc")
            f_mx = executor.submit(cls.query_mxtoolbox, clean_domain, "mx")
            spf_res = f_spf.result()
            dmarc_res = f_dmarc.result()
            mx_res = f_mx.result()

        spoofing_risk = "BAJO"
        risk_color = "#10b981"
        vuln_reasons = []

        if dmarc_res.get("status") == "success" and dmarc_res.get("failed_count", 0) > 0:
            spoofing_risk = "ALTO"
            risk_color = "#ef4444"
            vuln_reasons.append("Fallo crítico en registro o política DMARC")
        elif dmarc_res.get("status") == "success" and not dmarc_res.get("records"):
            spoofing_risk = "ALTO (SIN DMARC)"
            risk_color = "#ef4444"
            vuln_reasons.append("Dominio no tiene política DMARC publicada")

        if spf_res.get("status") == "success" and spf_res.get("failed_count", 0) > 0:
            if spoofing_risk != "ALTO":
                spoofing_risk = "MEDIO / ADVERTENCIA"
                risk_color = "#f59e0b"
            vuln_reasons.append("Inconsistencias en registro SPF")

        return {
            "domain": clean_domain,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "spoofing_risk": spoofing_risk,
            "risk_color": risk_color,
            "vuln_reasons": vuln_reasons,
            "spf": spf_res,
            "dmarc": dmarc_res,
            "mx": mx_res
        }

    @classmethod
    def query_alienvault_otx(cls, observable: str) -> Dict[str, Any]:
        """Consulta la reputación del indicador en AlienVault Open Threat Exchange (OTX)."""
        obs_type = cls.detect_observable_type(observable)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36",
            "Accept": "application/json"
        }
        type_mapping = {
            "ip": "IPv4",
            "domain": "domain",
            "hash": "file",
            "url": "url"
        }
        otx_type = type_mapping.get(obs_type)
        if not otx_type:
            return {"source": "AlienVault OTX", "status": "skipped", "reason": "Tipo de observable no soportado por OTX"}

        url = f"https://otx.alienvault.com/api/v1/indicators/{otx_type}/{observable}/general"
        try:
            r = requests.get(url, headers=headers, timeout=cls.DEFAULT_TIMEOUT, verify=cls.VERIFY_SSL)
            if r.status_code == 200:
                data = r.json()
                pulse_info = data.get("pulse_info", {})
                pulse_count = pulse_info.get("count", 0)
                pulses = pulse_info.get("pulses", [])[:5]
                pulse_names = [p.get("name", "").strip() for p in pulses if p.get("name")]
                tags = []
                for p in pulses:
                    tags.extend(p.get("tags", []))
                tags = list(set(tags))[:8]

                is_mal = (pulse_count >= 2)
                is_susp = (pulse_count == 1)
                verdict = "MALICIOSO" if is_mal else ("SOSPECHOSO" if is_susp else "LIMPIO / SIN PULSOS")
                color = "#ef4444" if is_mal else ("#f59e0b" if is_susp else "#10b981")

                return {
                    "source": "AlienVault OTX",
                    "status": "success",
                    "observable": observable,
                    "type": obs_type,
                    "pulse_count": pulse_count,
                    "pulse_names": pulse_names,
                    "tags": tags,
                    "verdict": verdict,
                    "color": color,
                    "is_malicious": is_mal
                }
            elif r.status_code == 404:
                return {
                    "source": "AlienVault OTX",
                    "status": "not_found",
                    "verdict": "LIMPIO / SIN PULSOS",
                    "pulse_count": 0,
                    "color": "#10b981",
                    "observable": observable
                }
            else:
                return {"source": "AlienVault OTX", "status": "error", "error": f"HTTP {r.status_code}"}
        except Exception as e:
            return {"source": "AlienVault OTX", "status": "exception", "error": str(e)}

    @classmethod
    def tri_scan(cls, observable: str, use_cache: bool = True) -> Dict[str, Any]:
        obs = observable.strip()
        cache_key = obs.lower()
        now = time.time()
        if use_cache and cache_key in cls._TRI_SCAN_CACHE:
            cached_ts, cached_res = cls._TRI_SCAN_CACHE[cache_key]
            if (now - cached_ts) < cls.CACHE_TTL_SECONDS:
                cached_copy = dict(cached_res)
                cached_copy["cached"] = True
                return cached_copy

        t0 = time.perf_counter()
        obs_type = cls.detect_observable_type(obs)
        res: Dict[str, Any] = {
            "observable": obs,
            "type": obs_type,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "virustotal": None,
            "abuseipdb": None,
            "urlscan": None,
            "mxtoolbox": None,
            "alienvault_otx": None,
            "cached": False,
        }

        with ThreadPoolExecutor(max_workers=5) as executor:
            f_vt = executor.submit(cls.query_virustotal, obs)
            f_otx = executor.submit(cls.query_alienvault_otx, obs)
            f_abuse = executor.submit(cls.query_abuseipdb, obs) if obs_type == "ip" else None
            f_us = executor.submit(cls.query_urlscan, obs) if obs_type in ("ip", "domain", "url") else None
            if obs_type in ("domain", "url"):
                domain_part = re.sub(r"^https?://", "", obs).split("/")[0].split(":")[0]
                f_mx = executor.submit(cls.query_phishing_email_defense, domain_part)
            else:
                f_mx = None

            res["virustotal"] = f_vt.result()
            res["alienvault_otx"] = f_otx.result()
            res["abuseipdb"] = (
                f_abuse.result()
                if f_abuse is not None
                else {"source": "AbuseIPDB", "status": "skipped", "reason": "No aplicable para observables no-IP"}
            )
            res["urlscan"] = (
                f_us.result()
                if f_us is not None
                else {"source": "URLScan.io", "status": "skipped", "reason": "No aplicable para hashes"}
            )
            if f_mx is not None:
                res["mxtoolbox"] = f_mx.result()

        # --- EVALUACIÓN HEURÍSTICA DE PLATAFORMAS CLOUD/SERVERLESS ABUSADAS ---
        cloud_abuse = cls.evaluate_cloud_abuse_heuristics(obs)
        res["cloud_abuse_heuristic"] = cloud_abuse

        is_high_risk = False
        verdict_summary = "LIMPIO / BENIGNO"
        sev_color = "#10b981"

        vt = res["virustotal"]
        abuse = res["abuseipdb"]
        us = res["urlscan"]
        mx = res["mxtoolbox"]

        if vt and vt.get("status") == "success" and vt.get("malicious_count", 0) >= 3:
            is_high_risk = True
        if abuse and abuse.get("status") == "success" and abuse.get("score", 0) >= 50:
            is_high_risk = True
        if us and us.get("status") == "success" and us.get("verdict") == "MALICIOSO":
            is_high_risk = True
        otx = res.get("alienvault_otx")
        if otx and otx.get("status") == "success" and otx.get("is_malicious"):
            is_high_risk = True

        if is_high_risk:
            verdict_summary = "CRÍTICO / MALICIOSO CONFIRMADO"
            sev_color = "#ef4444"
        elif (cloud_abuse and cloud_abuse.get("is_abused_platform")):
            verdict_summary = f"ALERTA HEURÍSTICA: {cloud_abuse.get('platform_category', 'PLATAFORMA ABUSADA')}"
            sev_color = "#f97316"  # Naranja intenso
        elif (vt and vt.get("malicious_count", 0) > 0) or (abuse and abuse.get("score", 0) >= 20) or (us and us.get("verdict") == "SOSPECHOSO") or (mx and "ALTO" in mx.get("spoofing_risk", "")):
            verdict_summary = "SOSPECHOSO / REPUTACIÓN ADVERSA"
            sev_color = "#f59e0b"

        res["consolidated_verdict"] = verdict_summary
        res["consolidated_color"] = sev_color
        res["elapsed_ms"] = round((time.perf_counter() - t0) * 1000, 1)

        cls._TRI_SCAN_CACHE[cache_key] = (time.time(), dict(res))

        return res

    @classmethod
    def evaluate_cloud_abuse_heuristics(cls, observable: str) -> Dict[str, Any]:
        """
        Evalúa si un dominio/URL pertenece a plataformas serverless, túneles o CDNs
        gratuitas que son abusadas sistemáticamente para campañas de Phishing, C2 efímero
        y evasión de sandboxes (Zero-Day Phishing bypass).
        """
        obs_clean = re.sub(r"^https?://", "", observable.strip().lower()).split("/")[0].split(":")[0]

        # Catálogo de plataformas comúnmente abusadas para phishing y bypass de reputación
        ABUSED_PATTERNS = [
            (r"\.workers\.dev$", "Cloudflare Workers (Serverless TDS / Phishing C2)", "Alto"),
            (r"\.pages\.dev$", "Cloudflare Pages (Static Web Phishing Host)", "Medio-Alto"),
            (r"\.vercel\.app$", "Vercel Serverless Edge (Phishing / Credential Harvesting)", "Medio-Alto"),
            (r"\.web\.app$|\.firebaseapp\.com$", "Google Firebase Hosting (OAuth Phishing Clone)", "Medio-Alto"),
            (r"\.appspot\.com$", "Google App Engine (Redirector TDS / Reverse Proxy)", "Medio"),
            (r"\.ngrok-free\.app$|\.ngrok\.io$", "Ngrok Tunnel (C2 / Reverse Shell / Phishing)", "Alto"),
            (r"\.trycloudflare\.com$", "Cloudflare Quick Tunnels (Túnel C2 Efímero)", "Alto"),
            (r"\.loca\.lt$", "Localtunnel (Reverse Proxy Malicioso)", "Alto"),
            (r"\.glitch\.me$", "Glitch Hosting (Micro-C2 / Phishing Host)", "Medio"),
            (r"\.blob\.core\.windows\.net$", "Azure Blob Storage (Hosting de HTML / PDF Phishing)", "Medio-Alto"),
            (r"\.s3\.amazonaws\.com$|\.s3\.[a-z0-9\-]+\.amazonaws\.com$", "AWS S3 Bucket (Payload Delivery / Phishing)", "Medio"),
            (r"\.supabase\.co$", "Supabase Edge Functions / Storage (Exfiltración)", "Medio"),
        ]

        for pattern, desc, risk_level in ABUSED_PATTERNS:
            if re.search(pattern, obs_clean):
                subdomain_part = re.sub(pattern, "", obs_clean)
                is_dga_like = bool(re.search(r"[a-z0-9]{8,}", subdomain_part) or (sum(c.isdigit() for c in subdomain_part) >= 3 and len(subdomain_part) >= 6))
                return {
                    "is_abused_platform": True,
                    "platform_category": "CLOUD SERVERLESS / TUNNEL ABUSADO",
                    "description": desc,
                    "matched_pattern": pattern,
                    "risk_level": risk_level,
                    "subdomain": subdomain_part,
                    "is_dga_like": is_dga_like,
                    "warning_message": (
                        f"⚠️ ATENCIÓN SOC: El dominio '{obs_clean}' reside en '{desc}'. "
                        "Los atacantes despliegan estas infraestructuras por 2 a 6 horas para evadir VirusTotal (falsos limpios 0/90). "
                        "Tratar con alta cautela independientemente del ratio de motores CTI."
                    )
                }

        return {"is_abused_platform": False}

    @classmethod
    def format_terminal_report_html(cls, report: Dict[str, Any]) -> str:
        obs = report.get("observable", "N/A")
        obs_type = report.get("type", "N/A").upper()
        ts = report.get("timestamp", "")
        verdict = report.get("consolidated_verdict", "N/A")
        col = report.get("consolidated_color", "#38bdf8")

        vt = report.get("virustotal") or {}
        abuse = report.get("abuseipdb") or {}
        urlscan = report.get("urlscan") or {}
        mx = report.get("mxtoolbox") or {}
        otx = report.get("alienvault_otx") or {}

        if otx.get("status") == "success":
            p_names = f" | Amenazas: {', '.join(otx.get('pulse_names')[:2])}" if otx.get("pulse_names") else ""
            otx_info = f"<span style='color: {otx.get('color')}; font-weight: bold;'>{otx.get('verdict')} ({otx.get('pulse_count')} pulsos OTX)</span>{p_names}"
        elif otx.get("status") == "not_found":
            otx_info = "<span style='color: #10b981; font-weight: bold;'>LIMPIO / SIN PULSOS REGISTRADOS</span>"
        else:
            otx_info = f"<span style='color: #94a3b8;'>{otx.get('reason', otx.get('error', 'Sin datos'))}</span>" 

        if vt.get("status") == "success":
            flagged_str = f" | Detecciones: {', '.join(vt.get('flagged_engines', [])[:4])}" if vt.get("flagged_engines") else ""
            vt_info = f"<span style='color: {vt.get('color')}; font-weight: bold;'>{vt.get('verdict')} ({vt.get('detection_ratio')} motores)</span> | AS: {vt.get('as_owner')} ({vt.get('country')}) | Reputación: {vt.get('reputation')}{flagged_str}"
        elif vt.get("status") == "not_found":
            vt_info = "<span style='color: #94a3b8;'>Sin registro previo en VT</span>"
        else:
            vt_info = f"<span style='color: #ef4444;'>{vt.get('error', 'Error en consulta')}</span>"

        if abuse.get("status") == "success":
            abuse_info = f"<span style='color: {abuse.get('color')}; font-weight: bold;'>{abuse.get('verdict')} (Score: {abuse.get('score')}%)</span> | {abuse.get('total_reports')} reportes | ISP: {abuse.get('isp')} ({abuse.get('country')}) | Whitelist: {abuse.get('is_whitelisted')}"
        elif abuse.get("status") == "skipped":
            abuse_info = "<span style='color: #64748b;'>N/A (Solo IPs)</span>"
        else:
            abuse_info = f"<span style='color: #ef4444;'>{abuse.get('error', 'Error en consulta')}</span>"

        if urlscan.get("status") == "success":
            title_part = f" | Título: '{urlscan.get('page_title')}'" if urlscan.get('page_title') != 'N/A' else ""
            server_part = f" | Web Server: {urlscan.get('server_banner')}" if urlscan.get('server_banner') != 'N/A' else ""
            urlscan_info = f"<span style='color: {urlscan.get('color')}; font-weight: bold;'>{urlscan.get('verdict')}</span> (Score: {urlscan.get('score')}) | ASN: {urlscan.get('asn_name')} ({urlscan.get('country')}){server_part}{title_part} | <a href='{urlscan.get('result_url')}' style='color: #38bdf8;'>[Auditoría URLScan]</a>"
        elif urlscan.get("status") == "not_found":
            urlscan_info = "<span style='color: #94a3b8;'>Sin escaneos web previos</span>"
        elif urlscan.get("status") == "skipped":
            urlscan_info = "<span style='color: #64748b;'>N/A (Solo dominios/URLs/IPs)</span>"
        else:
            urlscan_info = f"<span style='color: #ef4444;'>{urlscan.get('error', 'Error en consulta')}</span>"

        mx_row = ""
        if mx:
            risk = mx.get("spoofing_risk", "N/A")
            r_col = mx.get("risk_color", "#38bdf8")
            vulns = f" ({', '.join(mx.get('vuln_reasons', []))})" if mx.get("vuln_reasons") else ""
            mx_row = f"""
            <tr style="border-bottom: 1px solid #1e293b;">
                <td style="padding: 6px 8px; width: 150px; color: #38bdf8; font-weight: bold;">📬 MxToolbox Phishing:</td>
                <td style="padding: 6px 8px;">Riesgo Suplantación: <span style="color: {r_col}; font-weight: bold;">{risk}</span>{vulns}</td>
            </tr>
            """

        cloud_row = ""
        ca = report.get("cloud_abuse_heuristic") or {}
        if ca.get("is_abused_platform"):
            cloud_row = f"""
            <tr style="border-bottom: 1px solid #1e293b; background-color: #431407;">
                <td style="padding: 6px 8px; width: 150px; color: #fb923c; font-weight: bold;">☁️ Alerta Heurística Cloud:</td>
                <td style="padding: 6px 8px; color: #fdba74;">
                    <b>{ca.get('platform_category')}</b> ({ca.get('description')})<br>
                    <span style="color: #f97316; font-size: 10px;">{ca.get('warning_message')}</span>
                </td>
            </tr>
            """

        html = f"""
        <div style="background-color: #0b1120; border: 1px solid #1e293b; border-left: 4px solid {col}; border-radius: 6px; padding: 10px; margin: 8px 0; font-family: 'Consolas', monospace; font-size: 11px; color: #e2e8f0;">
            <div style="font-size: 12px; font-weight: bold; color: {col}; margin-bottom: 6px;">
                🎯 FICHA DE INTELIGENCIA CTI CONSOLIDADA: {obs} [{obs_type}]
            </div>
            <div style="margin-bottom: 8px; font-size: 11px;">
                <b>Dictamen Global:</b> <span style="color: {col}; font-weight: bold; padding: 2px 6px; background-color: #020617; border-radius: 3px;">{verdict}</span>
                &nbsp;|&nbsp; <b>Fecha:</b> <span style="color: #94a3b8;">{ts}</span>
            </div>
            <table style="width: 100%; border-collapse: collapse; font-size: 11px; background-color: #020617; border-radius: 4px;">
                {cloud_row}
                <tr style="border-bottom: 1px solid #1e293b;">
                    <td style="padding: 6px 8px; width: 150px; color: #fb923c; font-weight: bold;">🦠 VirusTotal v3:</td>
                    <td style="padding: 6px 8px;">{vt_info}</td>
                </tr>
                <tr style="border-bottom: 1px solid #1e293b;">
                    <td style="padding: 6px 8px; width: 150px; color: #34d399; font-weight: bold;">🛡️ AbuseIPDB v2:</td>
                    <td style="padding: 6px 8px;">{abuse_info}</td>
                </tr>
                <tr style="border-bottom: 1px solid #1e293b;">
                    <td style="padding: 6px 8px; width: 150px; color: #38bdf8; font-weight: bold;">🌐 URLScan.io v1:</td>
                    <td style="padding: 6px 8px;">{urlscan_info}</td>
                </tr>
                <tr style="border-bottom: 1px solid #1e293b;">
                    <td style="padding: 6px 8px; width: 150px; color: #a855f7; font-weight: bold;">👽 AlienVault OTX:</td>
                    <td style="padding: 6px 8px;">{otx_info}</td>
                </tr>
                {mx_row}
            </table>
        </div>
        """
        return html

    @classmethod
    def format_urlscan_detailed_html(cls, us: Dict[str, Any]) -> str:
        if us.get("status") == "not_found":
            target = us.get("target", "")
            return f"""
        <div style="background-color: #0b1120; border: 1px solid #1e293b; border-left: 4px solid #38bdf8; border-radius: 6px; padding: 10px; margin: 8px 0; font-family: 'Consolas', monospace; font-size: 11px; color: #e2e8f0;">
            <div style="font-size: 13px; font-weight: bold; color: #38bdf8; margin-bottom: 6px;">
                🌐 URLSCAN.IO v1 — HISTORIAL PÚBLICO: <span style="color: #f8fafc;">{target}</span>
            </div>
            <div style="color: #cbd5e1; margin-bottom: 6px;">
                ℹ️ No existen análisis web públicos registrados previamente en URLScan.io para este objetivo.
            </div>
            <div style="font-size: 10px; color: #64748b; margin-top: 4px;">
                💡 <b>Nota SOC:</b> Es habitual que IPs atacantes, bots de escaneo o servidores sin interfaces web abiertas no tengan historial en URLScan.
                &nbsp;|&nbsp; <a href="https://urlscan.io/search/#{target}" style="color: #38bdf8; text-decoration: underline;">Buscar o enviar a escanear en URLScan.io ↗</a>
            </div>
        </div>
        """

        if us.get("status") != "success":
            err = us.get("error", "Sin datos")
            return f"<span style='color: #ef4444;'><br>[🌐 URLScan.io Error]: {err}<br></span>"

        col = us.get("color", "#38bdf8")
        target = us.get("target", "")
        verdict = us.get("verdict", "N/A")
        score = us.get("score", 0)

        hist_rows = ""
        for s in us.get("historical_scans", []):
            hist_rows += f"""
            <tr style="border-bottom: 1px solid #1e293b; color: #cbd5e1;">
                <td style="padding: 4px 6px; color: #94a3b8;">{s.get('time', '')[:19]}</td>
                <td style="padding: 4px 6px; color: #38bdf8;"><a href="{s.get('result_url')}" style="color: #38bdf8;">{s.get('url')}</a></td>
                <td style="padding: 4px 6px;">{s.get('ip')}</td>
                <td style="padding: 4px 6px; color: #a855f7;">{s.get('server')}</td>
                <td style="padding: 4px 6px; color: #f59e0b;">{s.get('title')}</td>
            </tr>
            """

        html = f"""
        <div style="background-color: #0b1120; border: 1px solid #1e293b; border-left: 4px solid {col}; border-radius: 6px; padding: 10px; margin: 8px 0; font-family: 'Consolas', monospace; font-size: 11px; color: #e2e8f0;">
            <div style="font-size: 13px; font-weight: bold; color: #38bdf8; margin-bottom: 6px;">
                🌐 URLSCAN.IO v1 — INFORME TÉCNICO COMPLETO: <span style="color: #f8fafc;">{target}</span>
            </div>
            <div style="margin-bottom: 8px; font-size: 11px;">
                <b>Veredicto:</b> <span style="color: {col}; font-weight: bold; padding: 2px 6px; background-color: #020617; border-radius: 3px;">{verdict}</span>
                &nbsp;|&nbsp; <b>Score de Riesgo:</b> <span style="color: {col}; font-weight: bold;">{score}</span>
                &nbsp;|&nbsp; <b>Escaneos Encontrados:</b> <span style="color: #cbd5e1;">{us.get('results_count')}</span>
            </div>

            <table style="width: 100%; border-collapse: collapse; background-color: #020617; border-radius: 4px; margin-bottom: 8px;">
                <tr style="border-bottom: 1px solid #1e293b;">
                    <td style="padding: 5px 8px; width: 140px; color: #94a3b8; font-weight: bold;">🎯 URL Evaluada:</td>
                    <td style="padding: 5px 8px; color: #f8fafc;">{us.get('page_url')}</td>
                    <td style="padding: 5px 8px; width: 140px; color: #94a3b8; font-weight: bold;">📡 Servidor / OS:</td>
                    <td style="padding: 5px 8px; color: #f59e0b;">{us.get('server_banner')}</td>
                </tr>
                <tr style="border-bottom: 1px solid #1e293b;">
                    <td style="padding: 5px 8px; color: #94a3b8; font-weight: bold;">🏷️ Título de la Web:</td>
                    <td style="padding: 5px 8px; color: #38bdf8;">{us.get('page_title')}</td>
                    <td style="padding: 5px 8px; color: #94a3b8; font-weight: bold;">🌐 IP del Hosting:</td>
                    <td style="padding: 5px 8px; color: #10b981;">{us.get('page_ip')} (PTR: {us.get('ptr')})</td>
                </tr>
                <tr style="border-bottom: 1px solid #1e293b;">
                    <td style="padding: 5px 8px; color: #94a3b8; font-weight: bold;">🏢 ASN / Red:</td>
                    <td style="padding: 5px 8px; color: #cbd5e1;">{us.get('asn_name')} [{us.get('asn')}]</td>
                    <td style="padding: 5px 8px; color: #94a3b8; font-weight: bold;">📍 País / Código:</td>
                    <td style="padding: 5px 8px; color: #cbd5e1;">{us.get('country')}</td>
                </tr>
                <tr>
                    <td style="padding: 5px 8px; color: #94a3b8; font-weight: bold;">📊 HTTP Status / MIME:</td>
                    <td style="padding: 5px 8px; color: #cbd5e1;">HTTP {us.get('status_code')} ({us.get('mime_type')})</td>
                    <td style="padding: 5px 8px; color: #94a3b8; font-weight: bold;">🔗 Enlace de Auditoría:</td>
                    <td style="padding: 5px 8px;"><a href="{us.get('result_url')}" style="color: #38bdf8; font-weight: bold;">Abrir Auditoría en URLScan.io ↗</a></td>
                </tr>
            </table>

            <div style="font-weight: bold; color: #a855f7; margin-top: 8px; margin-bottom: 4px;">
                📜 Historial de Escaneos Públicos Recientes:
            </div>
            <table style="width: 100%; border-collapse: collapse; background-color: #020617; border-radius: 4px; font-size: 10px;">
                <thead>
                    <tr style="background-color: #0f172a; color: #94a3b8; text-align: left; border-bottom: 1px solid #1e293b;">
                        <th style="padding: 4px 6px;">Fecha / Hora</th>
                        <th style="padding: 4px 6px;">URL Escaneada</th>
                        <th style="padding: 4px 6px;">IP</th>
                        <th style="padding: 4px 6px;">Servidor</th>
                        <th style="padding: 4px 6px;">Título de Página</th>
                    </tr>
                </thead>
                <tbody>
                    {hist_rows}
                </tbody>
            </table>
        </div>
        """
        return html

    @classmethod
    def format_mxtoolbox_detailed_html(cls, report: Dict[str, Any]) -> str:
        if "spf" in report and "dmarc" in report:
            domain = report.get("domain", "")
            risk = report.get("spoofing_risk", "N/A")
            col = report.get("risk_color", "#38bdf8")
            spf = report.get("spf", {})
            dmarc = report.get("dmarc", {})
            mx = report.get("mx", {})

            spf_recs = "<br>".join([f"<code>{r}</code>" for r in spf.get("records", [])]) or "Sin registros SPF"
            dmarc_recs = "<br>".join([f"<code>{r}</code>" for r in dmarc.get("records", [])]) or "Sin registros DMARC"

            spf_status = f"<b style='color: {spf.get('color', '#10b981')};'>{spf.get('verdict', 'N/A')}</b> (Pasados: {spf.get('passed_count', 0)}, Fallos: {spf.get('failed_count', 0)})"
            dmarc_status = f"<b style='color: {dmarc.get('color', '#10b981')};'>{dmarc.get('verdict', 'N/A')}</b> (Pasados: {dmarc.get('passed_count', 0)}, Fallos: {dmarc.get('failed_count', 0)})"

            issues = []
            for item in dmarc.get("failed_details", []):
                issues.append(f"<li style='color: #ef4444;'>[DMARC CRÍTICO] {item}</li>")
            for item in dmarc.get("warning_details", []):
                issues.append(f"<li style='color: #f59e0b;'>[DMARC ADVERTENCIA] {item}</li>")
            for item in spf.get("failed_details", []):
                issues.append(f"<li style='color: #ef4444;'>[SPF CRÍTICO] {item}</li>")
            for item in spf.get("warning_details", []):
                issues.append(f"<li style='color: #f59e0b;'>[SPF ADVERTENCIA] {item}</li>")

            issues_html = "<ul>" + "".join(issues) + "</ul>" if issues else "<span style='color: #10b981;'>Ningún fallo o vulnerabilidad detectada en la configuración de correo.</span>"

            html = f"""
            <div style="background-color: #0b1120; border: 1px solid #1e293b; border-left: 4px solid {col}; border-radius: 6px; padding: 10px; margin: 8px 0; font-family: 'Consolas', monospace; font-size: 11px; color: #e2e8f0;">
                <div style="font-size: 13px; font-weight: bold; color: #38bdf8; margin-bottom: 6px;">
                    📬 MXTOOLBOX — EVALUACIÓN ANTI-PHISHING & DEFENSA DE CORREO: <span style="color: #f8fafc;">{domain}</span>
                </div>
                <div style="margin-bottom: 8px; font-size: 11px;">
                    <b>Riesgo de Suplantación / Spoofing:</b> <span style="color: {col}; font-weight: bold; padding: 2px 6px; background-color: #020617; border-radius: 3px;">{risk}</span>
                    &nbsp;|&nbsp; <b>Auditoría:</b> <span style="color: #94a3b8;">{report.get('timestamp')}</span>
                </div>

                <table style="width: 100%; border-collapse: collapse; background-color: #020617; border-radius: 4px; margin-bottom: 8px;">
                    <tr style="border-bottom: 1px solid #1e293b;">
                        <td style="padding: 5px 8px; width: 140px; color: #38bdf8; font-weight: bold;">🛡️ DMARC Policy:</td>
                        <td style="padding: 5px 8px;">{dmarc_status}<br><span style="color: #94a3b8;">Registro: {dmarc_recs}</span></td>
                    </tr>
                    <tr style="border-bottom: 1px solid #1e293b;">
                        <td style="padding: 5px 8px; width: 140px; color: #10b981; font-weight: bold;">📝 SPF Check:</td>
                        <td style="padding: 5px 8px;">{spf_status}<br><span style="color: #94a3b8;">Registro: {spf_recs}</span></td>
                    </tr>
                    <tr>
                        <td style="padding: 5px 8px; width: 140px; color: #f59e0b; font-weight: bold;">📬 Servidor MX:</td>
                        <td style="padding: 5px 8px;">NS Consultor: {mx.get('nameserver', 'N/A')} | Dictamen: {mx.get('verdict', 'OK')}</td>
                    </tr>
                </table>

                <div style="font-weight: bold; color: #ef4444; margin-top: 6px; margin-bottom: 4px;">
                    ⚠️ Hallazgos y Vulnerabilidades de Seguridad (SPF / DMARC):
                </div>
                {issues_html}
            </div>
            """
            return html
        else:
            cmd = report.get("command", "DNS")
            target = report.get("target", "")
            verdict = report.get("verdict", "N/A")
            col = report.get("color", "#38bdf8")

            issues = []
            for item in report.get("failed_details", []):
                issues.append(f"<li style='color: #ef4444;'>[FALLO] {item}</li>")
            for item in report.get("warning_details", []):
                issues.append(f"<li style='color: #f59e0b;'>[ADVERTENCIA] {item}</li>")
            issues_html = "<ul>" + "".join(issues) + "</ul>" if issues else "<span style='color: #10b981;'>Configuración conforme sin anomalías reportadas.</span>"

            html = f"""
            <div style="background-color: #0b1120; border: 1px solid #1e293b; border-left: 4px solid {col}; border-radius: 6px; padding: 10px; margin: 8px 0; font-family: 'Consolas', monospace; font-size: 11px; color: #e2e8f0;">
                <div style="font-size: 13px; font-weight: bold; color: #38bdf8; margin-bottom: 6px;">
                    📬 MXTOOLBOX [{cmd}] RESULT: <span style="color: #f8fafc;">{target}</span>
                </div>
                <div style="margin-bottom: 8px; font-size: 11px;">
                    <b>Veredicto:</b> <span style="color: {col}; font-weight: bold; padding: 2px 6px; background-color: #020617; border-radius: 3px;">{verdict}</span>
                    &nbsp;|&nbsp; Chequeos aprobados: <b style="color: #10b981;">{report.get('passed_count', 0)}</b> | Advertencias: <b style="color: #f59e0b;">{report.get('warnings_count', 0)}</b> | Fallos: <b style="color: #ef4444;">{report.get('failed_count', 0)}</b>
                </div>
                <div style="font-weight: bold; color: #ef4444; margin-top: 6px; margin-bottom: 4px;">
                    Hallazgos de la auditoría:
                </div>
                {issues_html}
            </div>
            """
            return html

    @classmethod
    def format_markdown_report(cls, report: Dict[str, Any]) -> str:
        obs = report.get("observable", "N/A")
        obs_type = report.get("type", "N/A").upper()
        verdict = report.get("consolidated_verdict", "N/A")
        ts = report.get("timestamp", "")

        lines = [
            f"### 🛡️ Reporte CTI de Reputación de Amenazas: `{obs}` ({obs_type})",
            f"**Dictamen Operativo:** **{verdict}**  ",
            f"**Timestamp Auditoría:** {ts}\n",
            f"| Fuente CTI | Veredicto / Métrica | Detalles de Atribución |",
            f"|:---|:---|:---|"
        ]

        vt = report.get("virustotal") or {}
        if vt.get("status") == "success":
            lines.append(f"| **VirusTotal v3** | {vt.get('verdict')} ({vt.get('detection_ratio')}) | AS: {vt.get('as_owner')} ({vt.get('country')}) |")
        elif vt.get("status") == "not_found":
            lines.append(f"| **VirusTotal v3** | Sin registro previo | No indexado |")

        abuse = report.get("abuseipdb") or {}
        if abuse.get("status") == "success":
            lines.append(f"| **AbuseIPDB v2** | {abuse.get('verdict')} ({abuse.get('score')}%) | {abuse.get('total_reports')} reportes (ISP: {abuse.get('isp')}) |")

        urlscan = report.get("urlscan") or {}
        if urlscan.get("status") == "success":
            lines.append(f"| **URLScan.io v1** | {urlscan.get('verdict')} | ASN: {urlscan.get('asn_name')} ([Ver Escaneo]({urlscan.get('result_url')})) |")

        otx = report.get("alienvault_otx") or {}
        if otx.get("status") == "success":
            p_str = f"Amenazas: {', '.join(otx.get('pulse_names')[:2])}" if otx.get("pulse_names") else "Sin pulsos activos"
            lines.append(f"| **AlienVault OTX** | {otx.get('verdict')} ({otx.get('pulse_count')} pulsos) | {p_str} |")
        elif otx.get("status") == "not_found":
            lines.append(f"| **AlienVault OTX** | LIMPIO / SIN PULSOS | Sin pulsos activos en OTX |")

        mx = report.get("mxtoolbox") or {}
        if mx and "spoofing_risk" in mx:
            lines.append(f"| **MxToolbox Anti-Phishing** | Riesgo: {mx.get('spoofing_risk')} | DMARC: {mx.get('dmarc', {}).get('verdict', 'N/A')} | SPF: {mx.get('spf', {}).get('verdict', 'N/A')} |")

        return "\n".join(lines)

    @classmethod
    def query_cve(cls, cve_id: str, api_key: Optional[str] = None) -> Dict[str, Any]:
        """Consulta una vulnerabilidad específica en la API 2.0 del National Vulnerability Database (NVD)."""
        key = api_key or cls.get_api_keys()["nvd"]
        cve_clean = cve_id.strip().upper()
        if not cve_clean.startswith("CVE-"):
            cve_clean = f"CVE-{cve_clean}"

        if not re.match(r"^CVE-\d{4}-\d{4,}$", cve_clean):
            return {
                "source": "NVD NIST",
                "status": "not_found",
                "cve_id": cve_clean,
                "verdict": "FORMATO INVÁLIDO",
                "color": "#94a3b8",
                "note": f"'{cve_id}' no corresponde a una sintaxis CVE válida (ej: CVE-2024-3400)."
            }

        url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?cveId={cve_clean}"
        headers = {
            "User-Agent": "StellarCyber-OpenXDR-Cockpit",
            "apiKey": key
        }
        try:
            r = requests.get(url, headers=headers, timeout=cls.DEFAULT_TIMEOUT, verify=cls.VERIFY_SSL)
            if r.status_code == 200:
                data = r.json()
                vulns = data.get("vulnerabilities", [])
                if not vulns:
                    return {
                        "source": "NVD NIST",
                        "status": "not_found",
                        "cve_id": cve_clean,
                        "verdict": "NO ENCONTRADO EN NVD",
                        "color": "#94a3b8"
                    }

                cve_obj = vulns[0].get("cve", {})
                metrics = cve_obj.get("metrics", {})
                cvss_v3x = metrics.get("cvssMetricV31", []) or metrics.get("cvssMetricV30", [])
                cvss_v2 = metrics.get("cvssMetricV2", [])

                score = 0.0
                severity = "DESCONOCIDA"
                vector = "N/A"
                if cvss_v3x:
                    cvss_data = cvss_v3x[0].get("cvssData", {})
                    score = float(cvss_data.get("baseScore", 0.0))
                    severity = cvss_data.get("baseSeverity", "DESCONOCIDA").upper()
                    vector = cvss_data.get("vectorString", "N/A")
                elif cvss_v2:
                    cvss_data = cvss_v2[0].get("cvssData", {})
                    score = float(cvss_data.get("baseScore", 0.0))
                    severity = cvss_v2[0].get("baseSeverity", "MEDIA").upper()
                    vector = cvss_data.get("vectorString", "N/A")

                color = "#ef4444" if score >= 9.0 else ("#fb923c" if score >= 7.0 else ("#f59e0b" if score >= 4.0 else "#10b981"))

                # Descripción en inglés o español
                descriptions = cve_obj.get("descriptions", [])
                desc_text = "Sin descripción disponible."
                for d in descriptions:
                    if d.get("lang") in ("es", "en"):
                        desc_text = d.get("value")
                        if d.get("lang") == "es":
                            break

                # Enlaces de referencia y parches
                refs = []
                for ref in cve_obj.get("references", [])[:6]:
                    refs.append(ref.get("url", ""))

                # Debilidades CWE
                cwes = []
                for w in cve_obj.get("weaknesses", []):
                    for desc in w.get("description", []):
                        val = desc.get("value", "")
                        if val and val != "NVD-CWE-noinfo":
                            cwes.append(val)

                return {
                    "source": "NVD NIST",
                    "status": "success",
                    "cve_id": cve_clean,
                    "score": score,
                    "severity": severity,
                    "color": color,
                    "vector": vector,
                    "published": cve_obj.get("published", "N/A"),
                    "last_modified": cve_obj.get("lastModified", "N/A"),
                    "vuln_status": cve_obj.get("vulnStatus", "N/A"),
                    "description": desc_text,
                    "cwes": cwes[:4],
                    "references": refs,
                    "nvd_url": f"https://nvd.nist.gov/vuln/detail/{cve_clean}"
                }
            elif r.status_code == 404:
                return {
                    "source": "NVD NIST",
                    "status": "not_found",
                    "cve_id": cve_clean,
                    "verdict": "NO ENCONTRADO EN NVD",
                    "color": "#94a3b8"
                }
            elif r.status_code == 403 or r.status_code == 401:
                return {"source": "NVD NIST", "status": "auth_error", "error": "API Key de NVD inválida o rechazada (HTTP 403)."}
            elif r.status_code == 429:
                return {"source": "NVD NIST", "status": "rate_limited", "error": "Límite de peticiones excedido en NVD NIST API."}
            else:
                return {"source": "NVD NIST", "status": "error", "error": f"HTTP {r.status_code}: {r.text[:120]}"}
        except Exception as e:
            return {"source": "NVD NIST", "status": "exception", "error": str(e)}

    @classmethod
    def query_cve_recent(cls, days: int = 2, severity: str = "CRITICAL", api_key: Optional[str] = None) -> Dict[str, Any]:
        """Extrae el lote de CVEs recientes de severidad Crítica o Alta publicados en los últimos días."""
        key = api_key or cls.get_api_keys()["nvd"]
        now = datetime.utcnow()
        start = now - datetime.timedelta(days=days)

        str_inicio = start.strftime("%Y-%m-%dT%H:%M:%S.000")
        str_fin = now.strftime("%Y-%m-%dT%H:%M:%S.000")
        sev_param = severity.upper().strip()

        url = f"https://services.nvd.nist.gov/rest/json/cves/2.0?pubStartDate={str_inicio}&pubEndDate={str_fin}&cvssV3Severity={sev_param}"
        headers = {
            "User-Agent": "StellarCyber-OpenXDR-Cockpit",
            "apiKey": key
        }
        try:
            r = requests.get(url, headers=headers, timeout=cls.DEFAULT_TIMEOUT + 5, verify=cls.VERIFY_SSL)
            if r.status_code == 200:
                data = r.json()
                vulns = data.get("vulnerabilities", [])
                parsed_list = []
                for v in vulns[:20]:
                    c_obj = v.get("cve", {})
                    c_id = c_obj.get("id", "N/A")
                    metrics = c_obj.get("metrics", {})
                    cvss_v3x = metrics.get("cvssMetricV31", []) or metrics.get("cvssMetricV30", [])
                    score = 0.0
                    if cvss_v3x:
                        score = float(cvss_v3x[0].get("cvssData", {}).get("baseScore", 0.0))
                    desc = "Sin descripción"
                    for d in c_obj.get("descriptions", []):
                        if d.get("lang") == "en":
                            desc = d.get("value", "")[:120]
                            break
                    parsed_list.append({
                        "id": c_id,
                        "score": score,
                        "published": c_obj.get("published", "")[:10],
                        "desc": desc
                    })

                return {
                    "source": "NVD NIST",
                    "status": "success",
                    "days": days,
                    "severity": sev_param,
                    "total_found": len(vulns),
                    "cves": parsed_list
                }
            else:
                return {"source": "NVD NIST", "status": "error", "error": f"HTTP {r.status_code}: {r.text[:120]}"}
        except Exception as e:
            return {"source": "NVD NIST", "status": "exception", "error": str(e)}

    @classmethod
    def format_cve_detailed_html(cls, res: Dict[str, Any]) -> str:
        """Genera una ficha visual completa de la vulnerabilidad CVE para la consola DFIR."""
        if res.get("status") == "not_found":
            cve_id = res.get("cve_id", "N/A")
            note = res.get("note")
            extra_msg = f"<div style='color: #cbd5e1; margin-bottom: 6px;'>{note}</div>" if note else "<div style='color: #cbd5e1; margin-bottom: 6px;'>El código de vulnerabilidad consultado no existe o no ha sido publicado aún en el catálogo oficial de NVD NIST.</div>"
            return f"""
        <div style="background-color: #0b1120; border: 1px solid #1e293b; border-left: 4px solid #94a3b8; border-radius: 6px; padding: 10px; margin: 8px 0; font-family: 'Consolas', monospace; font-size: 11px; color: #e2e8f0;">
            <div style="font-size: 13px; font-weight: bold; color: #94a3b8; margin-bottom: 4px;">
                🛡️ NVD NIST: IDENTIFICADOR NO ENCONTRADO (<span style="color: #f8fafc;">{cve_id}</span>)
            </div>
            {extra_msg}
            <div style="font-size: 10px; color: #64748b; margin-top: 4px;">
                💡 <b>Nota SOC:</b> NVD indexa vulnerabilidades por código CVE (ej: <code>CVE-2024-3400</code>). Para investigar reputación de IPs o dominios use AbuseIPDB, VirusTotal o Tri-Scan CTI.
            </div>
        </div>
        """
        if res.get("status") != "success":
            return f"<span style='color: #ef4444;'><br>[🛡️ NVD NIST Error]: {res.get('error', 'Error en consulta')}<br></span>"

        cve_id = res.get("cve_id")
        score = res.get("score", 0.0)
        sev = res.get("severity", "DESCONOCIDA")
        col = res.get("color", "#ef4444")
        vector = res.get("vector", "N/A")
        pub = res.get("published", "N/A")
        mod = res.get("last_modified", "N/A")
        status = res.get("vuln_status", "N/A")
        desc = res.get("description", "")
        cwes = ", ".join(res.get("cwes", [])) or "No especificado"
        nvd_url = res.get("nvd_url", "")

        refs_html = ""
        for r in res.get("references", []):
            refs_html += f"<li><a href='{r}' style='color: #38bdf8;'>{r[:80]}...</a></li>"
        if not refs_html:
            refs_html = "<li>Sin referencias indexadas</li>"

        html = f"""
        <div style="background-color: #0b1120; border: 1px solid #1e293b; border-left: 4px solid {col}; border-radius: 6px; padding: 10px; margin: 8px 0; font-family: 'Consolas', monospace; font-size: 11px; color: #e2e8f0;">
            <div style="font-size: 13px; font-weight: bold; color: {col}; margin-bottom: 6px;">
                🛡️ NVD NIST — INTELIGENCIA DE VULNERABILIDAD: <span style="color: #f8fafc;">{cve_id}</span>
            </div>
            <div style="margin-bottom: 8px; font-size: 11px;">
                <b>Severidad CVSS:</b> <span style="color: {col}; font-weight: bold; padding: 2px 6px; background-color: #020617; border-radius: 3px;">{sev} ({score}/10.0)</span>
                &nbsp;|&nbsp; <b>Estado NVD:</b> <span style="color: #cbd5e1;">{status}</span>
                &nbsp;|&nbsp; <b>Publicado:</b> <span style="color: #94a3b8;">{pub[:10]}</span>
                &nbsp;|&nbsp; <b>Modificado:</b> <span style="color: #94a3b8;">{mod[:10]}</span>
            </div>

            <table style="width: 100%; border-collapse: collapse; background-color: #020617; border-radius: 4px; margin-bottom: 8px;">
                <tr style="border-bottom: 1px solid #1e293b;">
                    <td style="padding: 5px 8px; width: 140px; color: #94a3b8; font-weight: bold;">Vector CVSS:</td>
                    <td style="padding: 5px 8px; color: #f8fafc;"><code>{vector}</code></td>
                </tr>
                <tr style="border-bottom: 1px solid #1e293b;">
                    <td style="padding: 5px 8px; color: #94a3b8; font-weight: bold;">Debilidad CWE:</td>
                    <td style="padding: 5px 8px; color: #f59e0b;">{cwes}</td>
                </tr>
                <tr>
                    <td style="padding: 5px 8px; color: #94a3b8; font-weight: bold;">Ficha Oficial NVD:</td>
                    <td style="padding: 5px 8px;"><a href="{nvd_url}" style="color: #38bdf8; font-weight: bold;">{nvd_url} ↗</a></td>
                </tr>
            </table>

            <div style="font-weight: bold; color: #38bdf8; margin-top: 6px; margin-bottom: 4px;">
                📝 Descripción del Fallo y Mecánica de Explotación:
            </div>
            <div style="background-color: #020617; padding: 8px; border-radius: 4px; line-height: 1.4; color: #cbd5e1; margin-bottom: 8px;">
                {desc}
            </div>

            <div style="font-weight: bold; color: #a855f7; margin-bottom: 4px;">
                🔗 Avisos de Seguridad y Parches del Fabricante:
            </div>
            <ul style="margin: 0; padding-left: 18px; color: #94a3b8;">
                {refs_html}
            </ul>
        </div>
        """
        return html
