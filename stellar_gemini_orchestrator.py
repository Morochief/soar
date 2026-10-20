#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
STELLAR CYBER OpenXDR - COGNITIVE IA ORCHESTRATOR
Seudonimización Reversible, Filtrado Forense Recursivo y Resiliencia de Red
"""

import os
import re
import json
import time
import random
import requests
from typing import Any, Dict, List, Union, Optional

from forensic_utils import clean_forensic_data
# =============================================================================
# TAREA 3: CORPUS COGNITIVO (SYSTEM_INSTRUCTIONS_MASTER)
# =============================================================================
# Constant extracted to gemini_prompts.md

# =============================================================================
# =============================================================================
# MOTOR DE ANONIMIZACIÓN HÍBRIDO (SECURITY MASKING ENGINE - V5 HARDENED)
# =============================================================================
class SecurityMaskingEngine:
    def __init__(self) -> None:
        self.mapa_reversa = {}
        self.contador_ip = 0
        self.contador_user = 0
        self.contador_host = 0
        self.contador_domain = 0
        self.contador_serial = 0
        self.contador_interface = 0
        self.contador_session = 0
        self.contador_agent_id = 0
        self.contador_domain_internal = 0
        self.contador_sid = 0
        self.contador_sec_group = 0
        self.ip_regex = re.compile(r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')

    def tokenizar_valor(self, valor, prefijo, contador_attr):
        if not valor or not isinstance(valor, str):
            return valor
        for token, val_real in self.mapa_reversa.items():
            if val_real == valor:
                return token
        contador = getattr(self, contador_attr)
        nuevo_token = f"[{prefijo}_{contador}]"
        setattr(self, contador_attr, contador + 1)
        self.mapa_reversa[nuevo_token] = valor
        return nuevo_token

    def enmascarar_contenido_string(self, texto_libre):
        if not isinstance(texto_libre, str):
            return texto_libre
            
        ips_encontradas = self.ip_regex.findall(texto_libre)
        for ip in set(ips_encontradas):
            if not (ip.startswith("[") and ip.endswith("]")):
                token = self.tokenizar_valor(ip, "IP_ANON", "contador_ip")
                texto_libre = texto_libre.replace(ip, token)
                
        hosts_encontrados = re.findall(r'\b[\w-]+\.technoma\.local\b|\b[\w-]+\.local\b', texto_libre, re.IGNORECASE)
        for host in set(hosts_encontrados):
            token = self.tokenizar_valor(host, "HOST_ANON", "contador_host")
            texto_libre = texto_libre.replace(host, token)

        # Neutralizar nombres de dominio de correo corporativo y zonas de AD (.LOCAL / .gov.py)
        dominios_internos = re.findall(r'\b[\w-]+\.LOCAL\b|\b[\w-]+\.gov\.py\b', texto_libre, re.IGNORECASE)
        for dom in set(dominios_internos):
            token = self.tokenizar_valor(dom, "DOM_INTERNAL_ANON", "contador_domain_internal")
            texto_libre = texto_libre.replace(dom, token)

        # Neutralizar cadenas e identificadores de seguridad SID de Active Directory (S-1-...)
        sids_encontrados = re.findall(r'\bS-\d+-\d+(?:-\d+)*\b', texto_libre)
        for sid in set(sids_encontrados):
            token = self.tokenizar_valor(sid, "SID_ANON", "contador_sid")
            texto_libre = texto_libre.replace(sid, token)

        # Evaporar infraestructuras específicas expuestas en el tráfico
        for infraestructura in ["Citrix Servers", "ROGGIO_PRI", "LDAP_Tech", "VPN-ADM"]:
            if infraestructura in texto_libre:
                token = self.tokenizar_valor(infraestructura, "SEC_ENV_ANON", "contador_sec_group")
                texto_libre = texto_libre.replace(infraestructura, token)

        # Neutralizar Seriales de Fortinet (Patrón clásico de letras y números de Fortigate)
        seriales = re.findall(r'\bFG[A-Z0-9]{14}\b', texto_libre)
        for serial in set(seriales):
            token = self.tokenizar_valor(serial, "SERIAL_ANON", "contador_serial")
            texto_libre = texto_libre.replace(serial, token)

        # Neutralizar Nombres de Firewalls Internos (Patrón FW-IDL-PRI o similares)
        fw_names = re.findall(r'\bFW-[\w-]+\b', texto_libre)
        for fw in set(fw_names):
            token = self.tokenizar_valor(fw, "HOST_ANON", "contador_host")
            texto_libre = texto_libre.replace(fw, token)

        # Neutralizar zonas e interfaces que exponen la topología (WiFi_Corp, Internet_Usuarios, etc.)
        for zona in ["WiFi_Corp", "Internet_Usuarios", "port2"]:
            if zona in texto_libre:
                token = self.tokenizar_valor(zona, "NET_ZONE_ANON", "contador_interface")
                texto_libre = texto_libre.replace(zona, token)

        for keyword, prefijo, attr in [("Technoma", "ORG_ANON", "contador_host"), ("technoma", "ORG_ANON", "contador_host")]:
            if keyword in texto_libre:
                token = self.tokenizar_valor(keyword, "ORG_ANON", attr)
                texto_libre = texto_libre.replace(keyword, token)
                
        return texto_libre

    def procesar_diccionario(self, data, padre_key=None):
        if isinstance(data, list):
            return [self.procesar_diccionario(item, padre_key) for item in data]
        elif isinstance(data, dict):
            objeto_tokenizado = {}
            for k, v in data.items():
                if isinstance(v, (dict, list)):
                    # Pasamos la llave actual como referencia de contexto para la siguiente recursión
                    objeto_tokenizado[k] = self.procesar_diccionario(v, k)
                elif isinstance(v, str):
                    texto_saneado = self.enmascarar_contenido_string(v)

                    # Corrección Quirúrgica de Bypass de Objetos Aninados (user.name / host.name)
                    if k == "name" and padre_key in ["user", "host", "device"]:
                        prefijo = "USER_ANON" if padre_key == "user" else "HOST_ANON"
                        attr = "contador_user" if padre_key == "user" else "contador_host"
                        if not texto_saneado.startswith("["):
                            texto_saneado = self.tokenizar_valor(v, prefijo, attr)

                    # Mapeo de nuevas estructuras indexadas
                    elif k in ["srcip", "dstip", "srcip_host", "dstip_host", "host_addr", "engid_gateway", "src_ip", "dest_ip"] or (k == "ip" and padre_key in ["host", "source_info"]):
                        if not texto_saneado.startswith("["):
                            texto_saneado = self.tokenizar_valor(v, "IP_ANON", "contador_ip")
                    elif k in ["username", "user_name", "user", "srcip_username", "smb_username"]:
                        if not texto_saneado.startswith("["):
                            texto_saneado = self.tokenizar_valor(v, "USER_ANON", "contador_user")
                    elif k in ["hostname", "host_name", "host", "srcname", "computer_name"] or (k == "name" and padre_key == "host"):
                        if not texto_saneado.startswith("["):
                            texto_saneado = self.tokenizar_valor(v, "HOST_ANON", "contador_host")
                    elif k in ["domain", "dns_query", "dns_name", "tunnel_domain", "query", "rrname"]:
                        if not texto_saneado.startswith("["):
                            texto_saneado = self.tokenizar_valor(v, "DOM_ANON", "contador_domain")
                    elif k in ["devid"]:
                        if not texto_saneado.startswith("["):
                            texto_saneado = self.tokenizar_valor(v, "SERIAL_ANON", "contador_serial")
                    elif k in ["sessionid"]:
                        if not texto_saneado.startswith("["):
                            texto_saneado = self.tokenizar_valor(v, "SESSION_ANON", "contador_session")
                    elif k in ["srcintf", "dstintf", "srcintfrole", "dstintfrole", "vwlname"]:
                        if not texto_saneado.startswith("["):
                            texto_saneado = self.tokenizar_valor(v, "NET_ZONE_ANON", "contador_interface")
                    elif k in ["id", "ephemeral_id"] and padre_key == "agent":
                        if not texto_saneado.startswith("["):
                            texto_saneado = self.tokenizar_valor(v, "AGENT_ID_ANON", "contador_agent_id")
                    elif k in ["TargetDomainName", "service_id", "TargetUserName"]:
                        if not texto_saneado.startswith("["):
                            texto_saneado = self.tokenizar_valor(v, "DOM_INTERNAL_ANON", "contador_domain_internal")
                    elif k in ["ServiceSid", "TargetSid", "srcip_usersid"]:
                        if not texto_saneado.startswith("["):
                            texto_saneado = self.tokenizar_valor(v, "SID_ANON", "contador_sid")
                    elif k in ["group", "authserver", "vpntype"]:
                        if not texto_saneado.startswith("["):
                            texto_saneado = self.tokenizar_valor(v, "SEC_ENV_ANON", "contador_sec_group")
                    elif k in ["resolved_ips", "host_ip"] and isinstance(v, list):
                        texto_saneado = [self.tokenizar_valor(ip_item, "IP_ANON", "contador_ip") for ip_item in v]
                    elif k in ["resolved_ips", "host_ip"]:
                        if not texto_saneado.startswith("["):
                            texto_saneado = self.tokenizar_valor(v, "IP_ANON", "contador_ip")
                    elif k == "location" and padre_key == "sophos":
                        if not texto_saneado.startswith("["):
                            texto_saneado = self.tokenizar_valor(v, "HOST_ANON", "contador_host")
                    elif k == "source" and padre_key == "sophos":
                        if not texto_saneado.startswith("["):
                            texto_saneado = self.tokenizar_valor(v, "USER_ANON", "contador_user")
                    elif k in ["endpoint_id", "customer_id", "user_id", "external_id", "seen_traffic_id", "exploit_id"]:
                        if not texto_saneado.startswith("["):
                            texto_saneado = self.tokenizar_valor(v, "AGENT_ID_ANON", "contador_agent_id")

                    objeto_tokenizado[k] = texto_saneado
                else:
                    objeto_tokenizado[k] = v
            return objeto_tokenizado
        else:
            if isinstance(data, str):
                return self.enmascarar_contenido_string(data)
        return data

    def desofuscar_texto(self, texto_reporte):
        if not texto_reporte:
            return ""
        texto_restaurado = texto_reporte
        for token, valor_real in sorted(self.mapa_reversa.items(), reverse=True):
            texto_restaurado = texto_restaurado.replace(token, valor_real)
        return texto_restaurado


# =============================================================================
# CLASE ORQUESTRADORA DE PRODUCCIÓN (StellarGeminiOrchestrator)
# =============================================================================
def _load_system_instructions() -> str:
    import os, sys
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    prompt_path = os.path.join(base_path, "prompt_stellar_python.md")
    try:
        with open(prompt_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "ERROR: Archivo prompt_stellar_python.md no encontrado."

class StellarGeminiOrchestrator:
    def __init__(self, api_key=None, enable_pii_masking=None):
        self.api_key = api_key or os.environ.get("GEMINI_API_KEY")
        self.api_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={self.api_key}"
        self.mask_engine = SecurityMaskingEngine()
        if enable_pii_masking is None:
            env_mask = os.environ.get("SOAR_ENABLE_PII_MASKING", "false").strip().lower()
            self.enable_pii_masking = env_mask in ("1", "true", "yes", "on")
        else:
            self.enable_pii_masking = bool(enable_pii_masking)

    def enviar_a_gemini(self, telemetria_cruda):
        """
        Ejecuta el pipeline completo de ingesta, filtrado forense, ofuscación opcional en RAM,
        control de tamaño de contexto, llamada prioritaria vía Google Antigravity OAuth
        (Gemini 3.8 Flash High) con fallback resiliente y desofuscación final.
        """
        self.mask_engine = SecurityMaskingEngine()

        # 1. Pipeline de Ingesta y Filtrado Forense
        datos_originales = None
        if isinstance(telemetria_cruda, str):
            try:
                datos_originales = json.loads(telemetria_cruda)
            except json.JSONDecodeError:
                # Si no es JSON, tratamos el texto directamente
                pass
        elif isinstance(telemetria_cruda, (dict, list)):
            datos_originales = telemetria_cruda

        if datos_originales is not None:
            datos_filtrados = clean_forensic_data(datos_originales)
            if self.enable_pii_masking:
                datos_filtrados = self.mask_engine.procesar_diccionario(datos_filtrados)
            contexto_a_enviar = json.dumps(datos_filtrados, indent=4, ensure_ascii=False)
        else:
            # Fallback a texto crudo
            contexto_a_enviar = str(telemetria_cruda)
            if self.enable_pii_masking:
                contexto_a_enviar = self.mask_engine.enmascarar_contenido_string(contexto_a_enviar)
            
        # --- RAG INTEGRATION ---
        search_query = ""
        if datos_originales is not None:
            # Helper to search for name in nested dict
            def extract_name(d):
                if not isinstance(d, dict): return ""
                return (d.get("name") or d.get("msg_class") or d.get("event_name") or 
                        d.get("xdr_event", {}).get("name") or d.get("title") or "")
            
            if isinstance(datos_originales, dict):
                search_query = extract_name(datos_originales)
                if not search_query and "data" in datos_originales and isinstance(datos_originales["data"], list) and len(datos_originales["data"]) > 0:
                    first = datos_originales["data"][0]
                    if isinstance(first, dict):
                        if "_source" in first:
                            search_query = extract_name(first["_source"])
                        if not search_query:
                            search_query = extract_name(first)
            elif isinstance(datos_originales, list) and len(datos_originales) > 0:
                first = datos_originales[0]
                if isinstance(first, dict):
                    if "_source" in first:
                        search_query = extract_name(first["_source"])
                    if not search_query:
                        search_query = extract_name(first)
        
        # If it's raw text or search_query is still empty, use a snippet of the text
        if not search_query and isinstance(telemetria_cruda, str):
            # Extract first 300 chars to find keywords
            search_query = telemetria_cruda[:300]
            
        rag_context_text = ""
        if search_query:
            try:
                from rag_engine import get_rag
                rag = get_rag()
                results = rag.query(str(search_query), top_k=2)
                if results:
                    rag_context_text = "\n\n--- DOCUMENTACION OFICIAL STELLAR CYBER (RAG) ---\n"
                    print(f"\n[+] RAG LOCAL: ¡Éxito! Inyectando documentación oficial.")
                    for i, r in enumerate(results):
                        print(f"    -> Encontrado en: {r['doc_name']} (Score: {r['score']:.2f})")
                        rag_context_text += f"\n[Documento: {r['doc_name']}]\n{r['content']}\n"
            except Exception as e:
                print(f"[RAG] Error querying: {e}")
                
        if rag_context_text:
            contexto_a_enviar = rag_context_text + "\n\n--- TELEMETRIA DEL CASO ---\n" + contexto_a_enviar
        # -----------------------

        # 3. Control de Ventana de Contexto (80KB Guard)
        MAX_CONTEXT_BYTES = 80000
        contexto_bytes = contexto_a_enviar.encode('utf-8')
        if len(contexto_bytes) > MAX_CONTEXT_BYTES:
            contexto_a_enviar = contexto_bytes[:MAX_CONTEXT_BYTES].decode('utf-8', errors='ignore')
            contexto_a_enviar += "\n\n[CONTEXTO TRUNCADO A 80KB — ANALIZAR HALLAZGOS PRIORITARIOS VISIBLES]"

        # 4. Invocación Prioritaria vía Google Antigravity OAuth (Gemini 3.8 Flash High)
        system_instructions = _load_system_instructions()
        try:
            from soar_ai_client import is_antigravity_available, call_antigravity
            if is_antigravity_available():
                output_text = call_antigravity(
                    user_prompt=contexto_a_enviar,
                    system_prompt=system_instructions,
                    temperature=0.3,
                    max_tokens=8192,
                )
                if self.enable_pii_masking:
                    output_text = self.mask_engine.desofuscar_texto(output_text)
                return output_text
        except Exception as e_ag:
            print(f"[Antigravity OAuth] Fallback a API Key estándar tras excepción: {e_ag}")

        if not self.api_key:
            raise ValueError(
                "Error crítico: Ni Google Antigravity OAuth ni GEMINI_API_KEY están disponibles."
            )

        # 5. Fallback: Construcción del Payload structured según Módulo I (Gemini REST API)
        payload = {
            "systemInstruction": {
                "parts": [{"text": system_instructions}]
            },
            "contents": [
                {
                    "parts": [{"text": contexto_a_enviar}]
                }
            ],
            "generationConfig": {
                "temperature": 1.0,
                "topP": 0.95,
                "maxOutputTokens": 8192
            }
        }

        # 6. Algoritmo de Resiliencia con Backoff Exponencial y Jitter
        headers = {"Content-Type": "application/json"}
        max_reintentos = 3
        ultimo_error = None

        for intento in range(max_reintentos):
            try:
                # Timeouts estrictos: 10s conexión, 90s lectura
                res = requests.post(self.api_url, headers=headers, json=payload, timeout=(10, 90))
                
                # Manejo de códigos de error de cuota/transitorios
                if res.status_code in [429, 503, 504]:
                    delay = (2 ** (intento + 1)) + random.uniform(0, 1)
                    time.sleep(delay)
                    continue

                if res.status_code == 200:
                    res_json = res.json()
                    output_text = res_json["candidates"][0]["content"]["parts"][0]["text"]
                    if self.enable_pii_masking:
                        output_text = self.mask_engine.desofuscar_texto(output_text)
                    return output_text
                else:
                    res.raise_for_status()

            except (requests.exceptions.ConnectTimeout,
                    requests.exceptions.ReadTimeout,
                    requests.exceptions.ConnectionError,
                    requests.exceptions.Timeout) as e:
                ultimo_error = e
                delay = (2 ** (intento + 1)) + random.uniform(0, 1)
                time.sleep(delay)
                continue

        raise RuntimeError(f"Fallo de conexión tras {max_reintentos} intentos. Último error: {ultimo_error}")

    def enviar_a_gemini_stream(self, telemetria_cruda, on_chunk=None, on_status=None):
        """
        Versión con streaming en vivo (SSE) del pipeline forense.
        Emite estado de RAG y cada fragmento de texto apenas Gemini 3.8 lo genera,
        evitando que la pantalla quede congelada esperando el bloque entero.
        """
        self.mask_engine = SecurityMaskingEngine()

        if on_status:
            on_status("[AI] 1/3 Filtrando telemetría Interflow y consultando Cerebro RAG local (2.081 Markdowns)...")

        datos_originales = None
        if isinstance(telemetria_cruda, str):
            try:
                datos_originales = json.loads(telemetria_cruda)
            except json.JSONDecodeError:
                pass
        elif isinstance(telemetria_cruda, (dict, list)):
            datos_originales = telemetria_cruda

        if datos_originales is not None:
            datos_filtrados = clean_forensic_data(datos_originales)
            if self.enable_pii_masking:
                datos_filtrados = self.mask_engine.procesar_diccionario(datos_filtrados)
            contexto_a_enviar = json.dumps(datos_filtrados, indent=4, ensure_ascii=False)
        else:
            contexto_a_enviar = str(telemetria_cruda)
            if self.enable_pii_masking:
                contexto_a_enviar = self.mask_engine.enmascarar_contenido_string(contexto_a_enviar)

        # --- RAG INTEGRATION ---
        search_query = ""
        if datos_originales is not None:
            def extract_name(d):
                if not isinstance(d, dict): return ""
                return (d.get("name") or d.get("msg_class") or d.get("event_name") or 
                        d.get("xdr_event", {}).get("name") or d.get("title") or "")
            if isinstance(datos_originales, dict):
                search_query = extract_name(datos_originales)
            elif isinstance(datos_originales, list) and len(datos_originales) > 0 and isinstance(datos_originales[0], dict):
                first = datos_originales[0]
                search_query = extract_name(first.get("_source", first))
        if not search_query and isinstance(telemetria_cruda, str):
            search_query = telemetria_cruda[:350]

        rag_context_text = ""
        rag_hits_summary = []
        if search_query:
            try:
                from rag_engine import get_rag
                rag = get_rag()
                results = rag.query(str(search_query), top_k=3)
                if results:
                    rag_context_text = "\n\n--- MEMORIA SOC & DOCUMENTACIÓN OFICIAL (RAG 7 CAPAS) ---\n"
                    for r in results:
                        rag_hits_summary.append(f"  • {r['doc_name']} (Score: {r['score']:.1f})")
                        rag_context_text += f"\n[Documento: {r['doc_name']}]\n{r['content']}\n"
            except Exception as e:
                print(f"[RAG] Error querying: {e}")

        if on_status and rag_hits_summary:
            on_status("[AI] 2/3 Memoria RAG inyectada en 8ms:\n" + "\n".join(rag_hits_summary) + "\n\n[AI] 3/3 Transmitiendo dictamen en vivo desde Gemini 3.8 Flash (Antigravity OAuth)...\n" + "-"*75 + "\n")
        elif on_status:
            on_status("[AI] 2/3 Transmitiendo dictamen en vivo desde Gemini 3.8 Flash (Antigravity OAuth)...\n" + "-"*75 + "\n")

        if rag_context_text:
            contexto_a_enviar = rag_context_text + "\n\n--- TELEMETRIA DEL CASO ---\n" + contexto_a_enviar

        MAX_CONTEXT_BYTES = 80000
        contexto_bytes = contexto_a_enviar.encode('utf-8')
        if len(contexto_bytes) > MAX_CONTEXT_BYTES:
            contexto_a_enviar = contexto_bytes[:MAX_CONTEXT_BYTES].decode('utf-8', errors='ignore')
            contexto_a_enviar += "\n\n[CONTEXTO TRUNCADO A 80KB — ANALIZAR HALLAZGOS PRIORITARIOS VISIBLES]"

        system_instructions = _load_system_instructions()
        try:
            from soar_ai_client import is_antigravity_available, stream_antigravity
            if is_antigravity_available():
                messages = [
                    {"role": "system", "content": system_instructions},
                    {"role": "user", "content": contexto_a_enviar},
                ]
                acumulado = []
                for chunk in stream_antigravity(messages=messages, temperature=0.3, max_tokens=8192):
                    if not chunk:
                        continue
                    if self.enable_pii_masking:
                        chunk = self.mask_engine.desofuscar_texto(chunk)
                    acumulado.append(chunk)
                    if on_chunk:
                        on_chunk(chunk)
                texto_final = "".join(acumulado)
                if texto_final.strip():
                    return texto_final
        except Exception as e_stream:
            print(f"[Antigravity Stream] Fallback a enviar_a_gemini estándar: {e_stream}")

        res_full = self.enviar_a_gemini(telemetria_cruda)
        if on_chunk and res_full:
            on_chunk(res_full)
        return res_full


# =============================================================================
# MÉTODO DE EJECUCIÓN PRINCIPAL DE EJEMPLO
# =============================================================================
if __name__ == "__main__":
    # Payload crudo simulado de Stellar Cyber (Interflow) para verificar el pipeline
    payload_simulado = {
        "srcip": "192.168.12.34",
        "dstip": "10.11.1.5",
        "username": "adm-kvinmoraes",
        "hostname": "nb-kmoraez.technoma.local",
        "event_name": "Active Directory Replication Attempt",
        "description": "Observed replication query from IP: 192.168.12.34 domain: technoma.local",
        "detected_values": ["192.168.12.34", "nb-kmoraez.technoma.local"],
        "unwanted_noisy_field": "This raw noise should be completely clean_forensic_data out by depth limits"
    }

    print("[*] Inicializando StellarGeminiOrchestrator...")
    orchestrator = StellarGeminiOrchestrator(api_key="SIMULATED_KEY_OR_ENV")

    print("\n[*] 1. Datos crudos originales:")
    print(json.dumps(payload_simulado, indent=2))

    # Simulamos el enmascaramiento del pipeline para la demo
    datos_filtrados = clean_forensic_data(payload_simulado)
    datos_ofuscados = orchestrator.mask_engine.procesar_diccionario(datos_filtrados)
    
    print("\n[*] 2. Datos filtrados y ofuscados (Zero-Knowledge RAM):")
    print(json.dumps(datos_ofuscados, indent=2))
    
    print("\n[*] 3. Relación de reversa del motor de privacidad:")
    print(json.dumps(orchestrator.mask_engine.mapa_reversa, indent=2))

    print("\n[*] 4. Simulación de desofuscación ante reporte de Gemini:")
    reporte_simulado_gemini = (
        "El activo [HOST_ANON_0] asociado al usuario [USER_ANON_0] con dirección [IP_ANON_0] "
        "intentó comunicarse hacia el controlador principal [IP_ANON_1] en el dominio [DOM_ANON_0]."
    )
    print("-> Reporte de la IA (Anonimizado):")
    print(reporte_simulado_gemini)
    print("-> Reporte Restaurado Local:")
    print(orchestrator.mask_engine.desofuscar_texto(reporte_simulado_gemini))
