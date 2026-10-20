#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
🛡️ TECHNOMA SOC — MOTOR DE GOBERNANZA SLA / SLO, MTTD, MTTR Y TRIAJE POE L1
=============================================================================
Módulo independiente extraído de command_center.py para evaluación en RAM
de acuerdos de nivel de servicio (SLA/SLO) sin requerir interfaz gráfica Qt.
Operador responsable L1: kevinmoraes@technoma.com.py
=============================================================================
"""

import time
from collections import Counter
from typing import Any, Dict, List, Optional, Tuple


class SlaGovernanceEngine:
    """
    Motor en memoria para evaluación de acuerdos de nivel de servicio (SLA/SLO).
    Cálculo 100% en memoria RAM (Zero Network Overhead).
    Operador responsable L1: kevinmoraes@technoma.com.py
    """
    # Umbrales contractuales en milisegundos
    # P1 (Crítica): MTTD 20m, MTTR 1h, Triage POE 15m
    P1_MTTD_MS = 20 * 60 * 1000       # 1,200,000 ms (20 min)
    P1_MTTR_MS = 60 * 60 * 1000       # 3,600,000 ms (1 hora)
    P1_TRIAGE_MS = 15 * 60 * 1000     # 900,000 ms (15 min)

    # P2 (Alta): MTTD 2h, MTTR 4h, Triage POE 15m
    P2_MTTD_MS = 2 * 60 * 60 * 1000   # 7,200,000 ms (2 horas)
    P2_MTTR_MS = 4 * 60 * 60 * 1000   # 14,400,000 ms (4 horas)
    P2_TRIAGE_MS = 15 * 60 * 1000     # 900,000 ms (15 min)

    # P3 (Media): MTTD 8h, MTTR 24h, Triage POE 30m
    P3_MTTD_MS = 8 * 60 * 60 * 1000   # 28,800,000 ms (8 horas)
    P3_MTTR_MS = 24 * 60 * 60 * 1000  # 86,400,000 ms (24 horas)
    P3_TRIAGE_MS = 30 * 60 * 1000     # 1,800,000 ms (30 min)

    # P4 (Baja / Info): MTTD 168h (semanal / mejor esfuerzo), MTTR 168h, Triage POE 60m (PARAMETROS.html)
    P4_MTTD_MS = 168 * 60 * 60 * 1000  # 604,800,000 ms (7 días / semanal)
    P4_MTTR_MS = 168 * 60 * 60 * 1000  # 604,800,000 ms (7 días / semanal)
    P4_TRIAGE_MS = 60 * 60 * 1000      # 3,600,000 ms (dentro del turno)

    # Matriz contractual de Priorización (Impacto x Urgencia) - Sección 1 PARAMETROS.html
    PRIORITY_MATRIX = {
        ("ALTO", "ALTA"): "P1",
        ("ALTO", "MEDIA"): "P2",
        ("ALTO", "BAJA"): "P3",
        ("MEDIO", "ALTA"): "P2",
        ("MEDIO", "MEDIA"): "P3",
        ("MEDIO", "BAJA"): "P4",
        ("BAJO", "ALTA"): "P3",
        ("BAJO", "MEDIA"): "P4",
        ("BAJO", "BAJA"): "P4"
    }

    @classmethod
    def calculate_priority_matrix(cls, impact: str, urgency: str) -> str:
        """Calcula prioridad P1-P4 usando la matriz 3x3 de PARAMETROS.html."""
        imp = (impact or "").strip().upper()
        urg = (urgency or "").strip().upper()
        return cls.PRIORITY_MATRIX.get((imp, urg), "P3")

    @classmethod
    def normalize_score(cls, raw_score: Any) -> float:
        if raw_score is None:
            return 0.0
        try:
            val = float(raw_score)
            if 0.0 < val <= 10.0:
                val = val * 10.0
            return round(val, 1)
        except (ValueError, TypeError):
            return 0.0

    @classmethod
    def get_priority(cls, case: dict) -> Tuple[str, str]:
        """
        Retorna (Código Prioridad, Severidad Normalizada).
        Alineado estrictamente con PARAMETROS.html (TB-THN-POS-01 Rev. 01):
        - P1: Crítica (score 90 - 100 o severity Critical)
        - P2: Alta / Mayor (score 75 - 89 o severity High)
        - P3: Media / Menor (score 41 - 74 o severity Medium)
        - P4: Baja / Informativa (score < 40 o Low/Informational)
        """
        raw_imp = case.get("impact") or case.get("impacto")
        raw_urg = case.get("urgency") or case.get("urgencia")
        if raw_imp and raw_urg:
            p_matrix = cls.calculate_priority_matrix(str(raw_imp), str(raw_urg))
            labels = {"P1": "CRÍTICA", "P2": "ALTA", "P3": "MEDIA", "P4": "BAJA"}
            return p_matrix, labels.get(p_matrix, "MEDIA")

        score = cls.normalize_score(case.get("score"))
        raw_sev = str(case.get("severity", "")).strip().lower()

        if score > 0.0:
            if score >= 90.0:
                return "P1", "CRÍTICA"
            elif score >= 75.0:
                return "P2", "ALTA"
            elif score >= 41.0:
                return "P3", "MEDIA"
            else:
                return "P4", "BAJA"

        if raw_sev in ["critical", "critico", "crítica"]:
            return "P1", "CRÍTICA"
        elif raw_sev in ["high", "alto", "alta"]:
            return "P2", "ALTA"
        elif raw_sev in ["medium", "medio", "media"]:
            return "P3", "MEDIA"
        else:
            return "P4", "BAJA"

    @classmethod
    def get_sla_limits(cls, priority: str) -> Tuple[int, int, int]:
        """Retorna (mttd_limit_ms, mttr_limit_ms, triage_limit_ms) según prioridad."""
        if priority == "P1":
            return cls.P1_MTTD_MS, cls.P1_MTTR_MS, cls.P1_TRIAGE_MS
        elif priority == "P2":
            return cls.P2_MTTD_MS, cls.P2_MTTR_MS, cls.P2_TRIAGE_MS
        elif priority == "P3":
            return cls.P3_MTTD_MS, cls.P3_MTTR_MS, cls.P3_TRIAGE_MS
        else:
            return cls.P4_MTTD_MS, cls.P4_MTTR_MS, cls.P4_TRIAGE_MS

    @classmethod
    def format_duration(cls, ms: int) -> str:
        """Formatea milisegundos en formato legible compacto."""
        if ms < 0:
            ms = abs(ms)
            prefix = "-"
        else:
            prefix = ""
        total_seconds = int(ms // 1000)
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        if hours > 0:
            return f"{prefix}{hours}h {minutes:02d}m"
        elif minutes > 0:
            return f"{prefix}{minutes}m {seconds:02d}s"
        else:
            return f"{prefix}{seconds}s"

    @classmethod
    def evaluate_mttd(cls, case: dict, timestamp_now_ms: Optional[int] = None) -> dict:
        """Evalúa el estado del SLO de MTTD (Tiempo de Acuse / Asignación)."""
        now = timestamp_now_ms if timestamp_now_ms else int(time.time() * 1000)
        created_at = case.get("created_at") or now
        priority, sev_label = cls.get_priority(case)
        mttd_limit, mttr_limit, triage_limit = cls.get_sla_limits(priority)

        status = str(case.get("status", "")).strip().lower()
        is_acknowledged = status in ["in progress", "resolved", "cancelled", "closed"]
        raw_assignee = case.get("assignee_name") or case.get("assignee")
        if raw_assignee and str(raw_assignee).strip().lower() not in ["unassigned", "none", "libre", ""]:
            is_acknowledged = True

        raw_ack = case.get("acknowledged")
        if raw_ack and isinstance(raw_ack, (int, float)) and raw_ack > 0:
            ack_time = int(raw_ack)
            is_acknowledged = True
        else:
            ack_time = case.get("modified_at") or now if is_acknowledged else now

        elapsed_mttd = max(0, ack_time - created_at)
        remaining_mttd = mttd_limit - elapsed_mttd

        breached = elapsed_mttd > mttd_limit
        warning = (not breached) and (remaining_mttd < (mttd_limit * 0.25) or remaining_mttd < 5 * 60 * 1000)

        return {
            "priority": priority,
            "severity_label": sev_label,
            "elapsed_ms": elapsed_mttd,
            "limit_ms": mttd_limit,
            "remaining_ms": remaining_mttd,
            "breached": breached,
            "warning": warning,
            "is_acknowledged": is_acknowledged,
            "elapsed_str": cls.format_duration(elapsed_mttd),
            "remaining_str": cls.format_duration(remaining_mttd) if not breached else f"+{cls.format_duration(abs(remaining_mttd))}",
            "limit_str": cls.format_duration(mttd_limit)
        }

    @classmethod
    def evaluate_mttr(cls, case: dict, timestamp_now_ms: Optional[int] = None) -> dict:
        """Evalúa el estado del SLA de MTTR (Resolución / Cierre / Notificación RFA)."""
        now = timestamp_now_ms if timestamp_now_ms else int(time.time() * 1000)
        created_at = case.get("created_at") or now
        priority, sev_label = cls.get_priority(case)
        mttd_limit, mttr_limit, triage_limit = cls.get_sla_limits(priority)

        status = str(case.get("status", "")).strip().lower()
        is_resolved = status in ["resolved", "cancelled", "closed"]

        raw_closed = case.get("closed")
        if raw_closed and isinstance(raw_closed, (int, float)) and raw_closed > 0:
            resolution_time = int(raw_closed)
            is_resolved = True
        else:
            resolution_time = case.get("modified_at") or now if is_resolved else now

        elapsed_mttr = max(0, resolution_time - created_at)
        remaining_mttr = mttr_limit - elapsed_mttr

        breached = elapsed_mttr > mttr_limit
        warning = (not breached) and (remaining_mttr < (mttr_limit * 0.20) or remaining_mttr < 15 * 60 * 1000)

        return {
            "priority": priority,
            "severity_label": sev_label,
            "elapsed_ms": elapsed_mttr,
            "limit_ms": mttr_limit,
            "remaining_ms": remaining_mttr,
            "breached": breached,
            "warning": warning,
            "is_resolved": is_resolved,
            "elapsed_str": cls.format_duration(elapsed_mttr),
            "remaining_str": cls.format_duration(remaining_mttr) if not breached else f"+{cls.format_duration(abs(remaining_mttr))}",
            "limit_str": cls.format_duration(mttr_limit)
        }

    @classmethod
    def calculate_deep_metrics(cls, cases: List[dict], target_analyst: str = "kevinmoraes@technoma.com.py",
                               time_from_ms: Optional[int] = None, time_to_ms: Optional[int] = None,
                               priority_filter: str = "TODAS") -> dict:
        """
        Cálculo analítico profundo de métricas ejecutivas en memoria RAM.
        Evalúa MTTD, MTTR, Triaje L1 POE, SLA Compliance %, precisión FP/TP y desglose multi-tenant.
        """
        filtered_cases = []
        target_norm = (target_analyst or "").strip().lower()
        is_consolidated = target_norm in ["todos", "todos / equipo completo soc", "equipo completo", "consolidado", "all", ""]
        target_user = target_norm.split("@")[0] if "@" in target_norm else target_norm

        p_filt = (priority_filter or "TODAS").strip().upper()

        for c in cases:
            c_time = c.get("created_at") or 0
            if time_from_ms is not None and c_time < time_from_ms:
                continue
            if time_to_ms is not None and c_time > time_to_ms:
                continue

            if not is_consolidated:
                a_email = str(c.get("assignee") or "").strip().lower()
                a_name = str(c.get("assignee_name") or "").strip().lower()
                a_combined = f"{a_email} {a_name} {a_name.replace(' ', '')}"
                if (target_norm not in a_combined) and (target_user not in a_combined):
                    continue

            p_code, _ = cls.get_priority(c)
            if p_filt not in ["TODAS", "ALL", ""] and (p_code not in p_filt):
                continue

            filtered_cases.append(c)

        total_cases = len(filtered_cases)
        status_counts = {"new": 0, "in_progress": 0, "resolved": 0, "other": 0}
        verdict_counts = {"False Positive": 0, "True Positive": 0, "Benign": 0, "Sin Veredicto": 0, "Otros": 0}
        priority_matrix = {
            "P1": {"total": 0, "compliant": 0, "breached": 0, "mttd_sum": 0, "mttd_cnt": 0, "mttr_sum": 0, "mttr_cnt": 0},
            "P2": {"total": 0, "compliant": 0, "breached": 0, "mttd_sum": 0, "mttd_cnt": 0, "mttr_sum": 0, "mttr_cnt": 0},
            "P3": {"total": 0, "compliant": 0, "breached": 0, "mttd_sum": 0, "mttd_cnt": 0, "mttr_sum": 0, "mttr_cnt": 0},
            "P4": {"total": 0, "compliant": 0, "breached": 0, "mttd_sum": 0, "mttd_cnt": 0, "mttr_sum": 0, "mttr_cnt": 0},
        }
        tenant_counter: Counter = Counter()
        threat_counter: Counter = Counter()
        total_alerts_mitigated = 0
        all_mttd = []
        all_mttr = []
        all_triage = []
        sla_compliant_total = 0
        sla_breached_total = 0

        for c in filtered_cases:
            st = str(c.get("status", "")).strip().lower()
            p_code, _ = cls.get_priority(c)
            sz = c.get("size", 1)
            sz = int(sz) if isinstance(sz, int) else 1

            tenant = str(c.get("tenant_name", "Global")).strip()
            tenant_counter[tenant] += 1

            threat_name = str(c.get("name", "Incidente Desconocido")).strip()
            if " and " in threat_name:
                threat_name = threat_name.split(" and ")[0]
            threat_counter[threat_name] += 1

            mttd_res = cls.evaluate_mttd(c)
            mttr_res = cls.evaluate_mttr(c)

            priority_matrix[p_code]["total"] += 1

            if mttd_res["is_acknowledged"]:
                all_mttd.append(mttd_res["elapsed_ms"])
                priority_matrix[p_code]["mttd_sum"] += mttd_res["elapsed_ms"]
                priority_matrix[p_code]["mttd_cnt"] += 1

            if st in ["resolved", "cancelled", "closed"]:
                status_counts["resolved"] += 1
                total_alerts_mitigated += sz
                all_mttr.append(mttr_res["elapsed_ms"])
                priority_matrix[p_code]["mttr_sum"] += mttr_res["elapsed_ms"]
                priority_matrix[p_code]["mttr_cnt"] += 1

                raw_ack = c.get("acknowledged") or 0
                raw_clo = c.get("closed") or 0
                if raw_clo > 0 and raw_ack > 0 and raw_clo >= raw_ack:
                    triage_dur = raw_clo - raw_ack
                else:
                    triage_dur = min(mttr_res["elapsed_ms"], 15 * 60 * 1000)
                all_triage.append(triage_dur)

                res_val = str(c.get("resolution") or "").strip().lower()
                if "false positive" in res_val or "falso" in res_val:
                    verdict_counts["False Positive"] += 1
                elif "true positive" in res_val or "verdadero" in res_val:
                    verdict_counts["True Positive"] += 1
                elif "benign" in res_val or "benigno" in res_val:
                    verdict_counts["Benign"] += 1
                elif res_val:
                    verdict_counts["Otros"] += 1
                else:
                    verdict_counts["Sin Veredicto"] += 1

                if not mttr_res["breached"]:
                    sla_compliant_total += 1
                    priority_matrix[p_code]["compliant"] += 1
                else:
                    sla_breached_total += 1
                    priority_matrix[p_code]["breached"] += 1

            elif st == "in progress":
                status_counts["in_progress"] += 1
                if not mttr_res["breached"]:
                    sla_compliant_total += 1
                    priority_matrix[p_code]["compliant"] += 1
                else:
                    sla_breached_total += 1
                    priority_matrix[p_code]["breached"] += 1
            elif st == "new":
                status_counts["new"] += 1
                if not mttd_res["breached"]:
                    sla_compliant_total += 1
                    priority_matrix[p_code]["compliant"] += 1
                else:
                    sla_breached_total += 1
                    priority_matrix[p_code]["breached"] += 1
            else:
                status_counts["other"] += 1

        avg_mttd_ms = int(sum(all_mttd) / len(all_mttd)) if all_mttd else 0
        avg_mttr_ms = int(sum(all_mttr) / len(all_mttr)) if all_mttr else 0
        avg_triage_ms = int(sum(all_triage) / len(all_triage)) if all_triage else 0

        sla_eval_total = sla_compliant_total + sla_breached_total
        sla_pct = round((sla_compliant_total / max(1, sla_eval_total)) * 100.0, 1) if sla_eval_total > 0 else 100.0

        resolved_tot = status_counts["resolved"]
        fp_cnt = verdict_counts["False Positive"]
        tp_cnt = verdict_counts["True Positive"]
        benign_cnt = verdict_counts["Benign"]
        fp_pct = round((fp_cnt / max(1, resolved_tot)) * 100.0, 1) if resolved_tot > 0 else 0.0
        tp_pct = round((tp_cnt / max(1, resolved_tot)) * 100.0, 1) if resolved_tot > 0 else 0.0
        benign_pct = round((benign_cnt / max(1, resolved_tot)) * 100.0, 1) if resolved_tot > 0 else 0.0

        if time_from_ms is not None and time_to_ms is not None and time_to_ms > time_from_ms:
            span_hours = max(0.5, (time_to_ms - time_from_ms) / (1000.0 * 3600.0))
        elif filtered_cases:
            ts_list = [c.get("created_at", 0) for c in filtered_cases if c.get("created_at")]
            if ts_list and max(ts_list) > min(ts_list):
                span_hours = max(0.5, (max(ts_list) - min(ts_list)) / (1000.0 * 3600.0))
            else:
                span_hours = 8.0
        else:
            span_hours = 8.0
        velocity = round(total_cases / span_hours, 2)

        for p_k in ["P1", "P2", "P3", "P4"]:
            item = priority_matrix[p_k]
            m_cnt = item["mttd_cnt"]
            r_cnt = item["mttr_cnt"]
            item["avg_mttd_str"] = cls.format_duration(int(item["mttd_sum"] / m_cnt)) if m_cnt > 0 else "N/A"
            item["avg_mttr_str"] = cls.format_duration(int(item["mttr_sum"] / r_cnt)) if r_cnt > 0 else "N/A"
            comp_eval = item["compliant"] + item["breached"]
            item["compliance_pct"] = round((item["compliant"] / max(1, comp_eval)) * 100.0, 1) if comp_eval > 0 else 100.0

        return {
            "total_cases": total_cases,
            "status_counts": status_counts,
            "verdict_counts": verdict_counts,
            "priority_matrix": priority_matrix,
            "tenant_counter": tenant_counter,
            "threat_counter": threat_counter,
            "total_alerts_mitigated": total_alerts_mitigated,
            "avg_mttd_ms": avg_mttd_ms,
            "avg_mttd_str": cls.format_duration(avg_mttd_ms),
            "avg_mttr_ms": avg_mttr_ms,
            "avg_mttr_str": cls.format_duration(avg_mttr_ms),
            "avg_triage_ms": avg_triage_ms,
            "avg_triage_str": cls.format_duration(avg_triage_ms),
            "sla_compliance_pct": sla_pct,
            "sla_compliant_total": sla_compliant_total,
            "sla_breached_total": sla_breached_total,
            "fp_count": fp_cnt,
            "tp_count": tp_cnt,
            "benign_count": benign_cnt,
            "fp_pct": fp_pct,
            "tp_pct": tp_pct,
            "benign_pct": benign_pct,
            "velocity": velocity,
            "target_analyst": target_analyst,
            "span_hours": round(span_hours, 1)
        }
