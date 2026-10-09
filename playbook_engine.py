# =============================================================================
# TECHNOMA SOC - ADAPTIVE PLAYBOOK & HITL INVESTIGATION ENGINE
# Operational Standard Operating Procedures (SOPs) based on NIST SP 800-61 Rev.3 & MITRE ATT&CK
# =============================================================================

import os
import json
import re
from typing import Dict, List, Any, Optional

CATALOG_JSON_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), '00_Playbooks', 'playbooks_catalog.json')

class PlaybookEngine:
    _catalog: List[Dict[str, Any]] = []
    _loaded: bool = False

    @classmethod
    def load_catalog(cls) -> List[Dict[str, Any]]:
        if cls._loaded and cls._catalog:
            return cls._catalog
        
        if os.path.exists(CATALOG_JSON_PATH):
            try:
                with open(CATALOG_JSON_PATH, 'r', encoding='utf-8') as f:
                    cls._catalog = json.load(f)
                    cls._loaded = True
                    return cls._catalog
            except Exception as e:
                print(f'[PlaybookEngine] Error al cargar catalogo: {e}')
        return []

    @classmethod
    def recommend_playbook(cls, case_obj: Dict[str, Any], telemetry_text: str = '') -> Optional[Dict[str, Any]]:
        catalog = cls.load_catalog()
        if not catalog:
            return None

        case_name = str(case_obj.get('name', '')).lower()
        tags = [str(t).lower() for t in case_obj.get('tags', [])]
        description = str(case_obj.get('description', '')).lower()
        telemetry_sample = str(telemetry_text)[:5000].lower()
        tag_str = ' '.join(tags)

        search_corpus = f'{case_name} {tag_str} {description} {telemetry_sample}'

        scored = []
        for pb in catalog:
            score = 0
            for kw in pb.get('keywords', []):
                if kw in search_corpus:
                    score += 12
            
            clean_title = pb.get('title', '').lower()
            for w in clean_title.split():
                if len(w) > 4 and w in search_corpus:
                    score += 6
            
            mitre = pb.get('mitre', '').lower()
            for m in re.findall(r't\d{4}(?:\.\d{3})?', mitre):
                if m in search_corpus:
                    score += 20

            if score > 0:
                scored.append((score, pb))

        scored.sort(key=lambda x: x[0], reverse=True)
        if scored:
            return scored[0][1]
        
        return catalog[1] if len(catalog) > 1 else (catalog[0] if catalog else None)

    @classmethod
    def get_playbook_by_id(cls, pb_id: str) -> Optional[Dict[str, Any]]:
        catalog = cls.load_catalog()
        for pb in catalog:
            if pb.get('id') == pb_id or pb.get('title') == pb_id:
                return pb
        return None

    @classmethod
    def format_playbook_html(cls, pb: Dict[str, Any], case_obj: Optional[Dict[str, Any]] = None) -> str:
        if not pb:
            return "<div style='color: #64748b;'>No hay playbook seleccionado.</div>"

        prio = pb.get('priority', 'P2')
        prio_color = '#ef4444' if prio == 'P1' else ('#f59e0b' if prio == 'P2' else '#38bdf8')
        title = pb.get('title', 'Playbook')
        mitre = pb.get('mitre', 'N/A')
        obj = pb.get('objective', 'N/A')
        analyst = pb.get('analyst', 'N1 / N2')
        nature = pb.get('operational_nature', 'Reactivo (Respuesta & Contención)')
        nature_color = '#10b981' if 'Proactivo' in nature else '#f43f5e'
        framework = pb.get('origin_framework', 'Technoma SOC (NIST / CSF 2.0)')
        fw_color = '#8b5cf6' if 'CERT-PY' in framework else '#0284c7'

        html = f'''
        <div style="font-family: 'Segoe UI', Tahoma, sans-serif; color: #f8fafc;">
            <div style="background-color: #0f172a; border-left: 4px solid {prio_color}; padding: 10px 14px; border-radius: 4px; margin-bottom: 12px;">
                <div style="font-size: 15px; font-weight: bold; color: #38bdf8;">📘 {title}</div>
                <div style="font-size: 12px; margin-top: 5px; color: #94a3b8;">
                    <span style="background-color: {fw_color}; color: #ffffff; font-weight: bold; padding: 2px 6px; border-radius: 3px;">{framework}</span>
                    &nbsp;|&nbsp; <span style="background-color: {prio_color}; color: #000000; font-weight: bold; padding: 2px 6px; border-radius: 3px;">PRIORIDAD {prio}</span>
                    &nbsp;|&nbsp; <span style="background-color: {nature_color}; color: #ffffff; font-weight: bold; padding: 2px 6px; border-radius: 3px;">{nature.upper()}</span>
                    &nbsp;|&nbsp; <b>MITRE:</b> <span style="color: #cbd5e1;">{mitre}</span>
                    &nbsp;|&nbsp; <b>Rol:</b> <span style="color: #cbd5e1;">{analyst}</span>
                </div>
            </div>

            <div style="background-color: #020617; border: 1px solid #1e293b; padding: 10px 14px; border-radius: 4px; margin-bottom: 12px;">
                <div style="color: #38bdf8; font-weight: bold; font-size: 12px; margin-bottom: 4px;">🎯 OBJETIVO DEL PROCEDIMIENTO:</div>
                <div style="font-size: 12px; color: #e2e8f0; line-height: 1.4;">{obj}</div>
            </div>

            <div style="background-color: #020617; border: 1px solid #1e293b; padding: 10px 14px; border-radius: 4px;">
                <div style="color: #10b981; font-weight: bold; font-size: 12px; margin-bottom: 8px;">📋 GUÍA DE ACCIÓN Y VALIDACIÓN SOC (PASO A PASO):</div>
        '''

        paras = pb.get('paragraphs', [])
        step_html = ''
        for p in paras:
            p_clean = p.strip()
            if not p_clean or p_clean.startswith('[DATOS') or p_clean.startswith('[ALINEAMIENTO') or 'Taxonom' in p_clean:
                continue
            if p_clean.startswith('Fase '):
                step_html += f"<div style='margin-top: 10px; margin-bottom: 4px; font-weight: bold; color: #f59e0b; font-size: 12px;'>▶ {p_clean}</div>"
            elif p_clean.startswith('Paso ') or p_clean.startswith('Acción') or p_clean.startswith('Acci'):
                step_html += f"<div style='margin-top: 6px; font-weight: bold; color: #38bdf8; font-size: 11px;'>• {p_clean}</div>"
            else:
                step_html += f"<div style='margin-left: 14px; margin-bottom: 4px; color: #cbd5e1; font-size: 11px; line-height: 1.3;'>{p_clean}</div>"

        html += step_html + '''
            </div>
        </div>
        '''
        return html
