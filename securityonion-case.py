# -*- coding: utf-8 -*-
"""
SecurityOnionCaseAlerter (Custom ElastAlert Alerter v2)
Crea y escala automáticamente un CASO oficial en Security Onion (índice so-case)
y asocia la entrada en so-casehistory cuando una regla de correlación ElastAlert hace match.

Características v2:
- Assignee desacoplado: Por defecto queda sin asignar ("") o se define por regla (case_assignee: "soc-tier1").
- Títulos inteligentes dinámicos basados en la regla y observables detectados.
"""

import json
import uuid
from time import gmtime, strftime
from datetime import datetime, timezone
import requests
import urllib3
from elastalert.alerts import Alerter

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class SecurityOnionCaseAlerter(Alerter):
    """
    Alertador personalizado para crear casos automáticos en so-case.
    """

    required_options = set(['detection_title'])

    def alert(self, matches):
        headers = {"Content-Type": "application/json"}
        creds = None
        if 'es_username' in self.rule and 'es_password' in self.rule:
            creds = (self.rule['es_username'], self.rule['es_password'])

        es_host = self.rule.get('es_host', 'soc-onion')
        es_port = self.rule.get('es_port', 9200)

        for match in matches:
            now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")
            case_id = str(uuid.uuid4())
            
            rule_title = self.rule['detection_title']
            severity = self.rule.get('case_severity', self.rule.get('sigma_level', 'high')).lower()
            category = self.rule.get('case_category', 'Correlated Threat')
            tags = self.rule.get('case_tags', ['elastalert-automated', 'soar'])
            
            # Asignación: Por defecto SIN ASIGNAR ("") para que la guardia lo tome, salvo que la regla indique lo contrario
            assignee = self.rule.get('case_assignee', '')

            # Extraer observables del match.
            # Los eventos crudos traen los campos en la raiz (source.ip), pero las alertas de
            # logs-detections.alerts-so los traen anidados bajo event_data (event_data.source.ip).
            ed = match.get('event_data') if isinstance(match.get('event_data'), dict) else {}

            def _nested(doc, key, sub):
                val = doc.get(key)
                return val.get(sub) if isinstance(val, dict) else None

            src_ip = (_nested(match, 'source', 'ip') or match.get('src_ip')
                      or _nested(ed, 'source', 'ip') or ed.get('src_ip') or '')
            dst_ip = (_nested(match, 'destination', 'ip') or match.get('dst_ip')
                      or _nested(ed, 'destination', 'ip') or ed.get('dst_ip') or '')
            user_name = (_nested(match, 'user', 'name') or (match.get('user') if isinstance(match.get('user'), str) else None)
                         or _nested(ed, 'user', 'name') or '')
            user_name = str(user_name).strip()
            dst_port = (_nested(match, 'destination', 'port') or match.get('dst_port')
                        or _nested(ed, 'destination', 'port') or '')

            # Generar Título Profesional Dinámico
            # Prioridad 1: Si la regla define un formato específico (case_title_format)
            # Prioridad 2: Título estándar estructurado: "[AUTO] <Nombre Regla> | <Detalle Observable>"
            if 'case_title' in self.rule:
                base_title = self.rule['case_title']
            else:
                base_title = rule_title

            observables_summary = []
            if src_ip and dst_ip:
                if dst_port:
                    observables_summary.append(f"{src_ip} -> {dst_ip}:{dst_port}")
                else:
                    observables_summary.append(f"{src_ip} -> {dst_ip}")
            elif src_ip:
                observables_summary.append(f"Origen: {src_ip}")
            elif dst_ip:
                observables_summary.append(f"Destino: {dst_ip}")

            if user_name and user_name != 'N/A':
                observables_summary.append(f"Usuario: {user_name}")

            if observables_summary:
                final_title = f"[AUTO] {base_title} ({' | '.join(observables_summary)})"
            else:
                final_title = f"[AUTO] {base_title}"

            description = (
                f"Caso creado automáticamente por el motor de correlación ElastAlert.\n"
                f"Regla Activada: {rule_title}\n"
                f"Severidad: {severity.upper()}\n"
                f"Observables: {', '.join(observables_summary) if observables_summary else 'N/A'}\n\n"
                f"--- Evidencia Forense Cruda ---\n"
                f"{json.dumps(match, indent=2, default=str)[:1200]}"
            )

            case_doc = {
                "@timestamp": now_iso,
                "so_kind": "case",
                "so_case": {
                    "title": final_title,
                    "description": description,
                    "severity": severity,
                    "status": "open",
                    "priority": 1,
                    "category": category,
                    "createTime": now_iso,
                    "startTime": now_iso,
                    "completeTime": "0001-01-01T00:00:00Z",
                    "userId": "elastalert-automation",
                    "assigneeId": assignee,
                    "template": "Standard",
                    "tlp": "amber",
                    "pap": "amber",
                    "tags": tags
                }
            }

            history_doc = {
                "@timestamp": now_iso,
                "so_kind": "casehistory",
                "so_casehistory": {
                    "caseId": case_id,
                    "action": "create",
                    "description": f"Caso generado automáticamente por correlación ElastAlert: {rule_title}. Asignado a: {assignee if assignee else 'Bandeja General (Sin asignar)'}.",
                    "userId": "elastalert-automation",
                    "time": now_iso
                }
            }

            # 1. Crear Caso en so-case
            case_url = f"https://{es_host}:{es_port}/so-case/_doc/{case_id}?refresh=true"
            requests.post(case_url, data=json.dumps(case_doc), headers=headers, verify=False, auth=creds)

            # 2. Registrar en so-casehistory
            hist_url = f"https://{es_host}:{es_port}/so-casehistory/_doc?refresh=true"
            requests.post(hist_url, data=json.dumps(history_doc), headers=headers, verify=False, auth=creds)

            # 3. También registrar la alerta estándar en logs-detections.alerts-so
            es_alert_url = f"https://{es_host}:{es_port}/logs-detections.alerts-so/_doc/"
            alert_payload = {
                "tags": ["alert", "automated-case"],
                "rule": {
                    "name": self.rule['detection_title'],
                    "uuid": self.rule.get('detection_public_id', case_id),
                    "case_id": case_id
                },
                "event": {
                    "severity": self.rule.get('event.severity', 3),
                    "module": "elastalert",
                    "dataset": "elastalert.case",
                    "severity_label": severity
                },
                "event_data": match,
                "@timestamp": now_iso
            }
            requests.post(es_alert_url, data=json.dumps(alert_payload), headers=headers, verify=False, auth=creds)

    def get_info(self):
        return {'type': 'SecurityOnionCaseAlerter'}
