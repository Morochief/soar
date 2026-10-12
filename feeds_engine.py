#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
  TECHNOMA SOC - FEEDS INTEL ENGINE (CTI & RSS/ATOM INGESTION CORE)
=============================================================================
Motor concurrente de ingesta, normalización y deduplicación de fuentes de
inteligencia de amenazas (CTI) para el OpenXDR Master Cockpit SOAR.
"""

import os
import re
import html
import sqlite3
import hashlib
from typing import Dict, Any, List, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime
import xml.etree.ElementTree as ET
import requests
import urllib3

# Desactivar advertencias SSL en consultas CTI perimetrales
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# =============================================================================
# TIERS Y CLASIFICACION OFICIAL DE CTI (TECHNOMA SOC)
# =============================================================================
TIER_TACTICAL = "CTI Técnico / Avisos"
TIER_RESEARCH = "Investigación DFIR"
TIER_NEWS = "Noticias / Brechas"

CTI_TIERS = [TIER_TACTICAL, TIER_RESEARCH, TIER_NEWS]

FEED_TIER_MAPPING: Dict[str, str] = {
    # 1. CTI Técnico y Avisos Críticos (Actionable / KEV / Telemetry / 0-Days / Live IoCs)
    "cisa_advisories": TIER_TACTICAL,
    "cisa_kev": TIER_TACTICAL,
    "forti_psirt": TIER_TACTICAL,
    "sans_isc": TIER_TACTICAL,
    "0dayfans": TIER_TACTICAL,
    "tweetfeed": TIER_TACTICAL,
    "threatfox": TIER_TACTICAL,
    "urlhaus": TIER_TACTICAL,
    "feodotracker": TIER_TACTICAL,
    "openphish": TIER_TACTICAL,
    "malwarebazaar": TIER_TACTICAL,

    # 2. Investigación Forense y Análisis de Malware (Threat Research & DFIR)
    "unit42": TIER_RESEARCH,
    "securelist": TIER_RESEARCH,
    "sophos_threat_research": TIER_RESEARCH,
    "sophos_secops": TIER_RESEARCH,
    "welivesecurity": TIER_RESEARCH,

    # 3. Inteligencia Estratégica, Brechas y Actualidad (News & Cybercrime)
    "seguinfo": TIER_NEWS,
    "the_cyber_security_hub": TIER_NEWS,
    "elhacker_net": TIER_NEWS,
    "daily_dark_web": TIER_NEWS,
    "dark_web_informer": TIER_NEWS,
    "bleeping_computer": TIER_NEWS,
    "the_hacker_news": TIER_NEWS,
    "security_week": TIER_NEWS,
    "krebs_on_security": TIER_NEWS,
    "troy_hunt": TIER_NEWS,
    "graham_cluley": TIER_NEWS,
    "schneier_on_security": TIER_NEWS,
    "darknet_diaries": TIER_NEWS,
}

# Configuración Oficial de Feeds CTI de Technoma SOC
FEEDS_CONFIG: List[Dict[str, str]] = [
    {
        "id": "threatfox",
        "name": "ThreatFox IoCs (abuse.ch)",
        "url": "https://threatfox.abuse.ch/export/json/recent/",
        "category": "Malware & C2 IoCs",
        "tier": "CTI Técnico / Avisos",
        "format": "json_threatfox"
    },
    {
        "id": "urlhaus",
        "name": "URLhaus Malware URLs (abuse.ch)",
        "url": "https://urlhaus.abuse.ch/downloads/json_recent/",
        "category": "Malware Distribution URLs",
        "tier": "CTI Técnico / Avisos",
        "format": "json_urlhaus"
    },
    {
        "id": "openphish",
        "name": "OpenPhish Live Phishing URLs",
        "url": "https://raw.githubusercontent.com/openphish/public_feed/refs/heads/main/feed.txt",
        "category": "Live Phishing Feeds",
        "tier": "CTI Técnico / Avisos",
        "format": "text_openphish"
    },
    {
        "id": "feodotracker",
        "name": "Feodo Tracker C2 Blocklist (abuse.ch)",
        "url": "https://feodotracker.abuse.ch/downloads/ipblocklist.json",
        "category": "Botnet C2 IP Blocklist",
        "tier": "CTI Técnico / Avisos",
        "format": "json_feodo"
    },
    {
        "id": "malwarebazaar",
        "name": "MalwareBazaar Hashes (abuse.ch)",
        "url": "https://bazaar.abuse.ch/export/csv/recent/",
        "category": "Malware Hashes (SHA256)",
        "tier": "CTI Técnico / Avisos",
        "format": "csv_malwarebazaar"
    },
    {
        "id": "tweetfeed",
        "name": "TweetFeed (Live Twitter IOCs)",
        "url": "https://api.tweetfeed.live/v1/today",
        "category": "IOCs / Threat Intel",
        "tier": "CTI Técnico / Avisos",
        "format": "json_tweetfeed"
    },
    {
        "id": "darknet_diaries",
        "name": "Darknet Diaries",
        "url": "https://podcast.darknetdiaries.com/",
        "category": "Podcast / Case Studies",
        "tier": "Noticias / Brechas"
    },
    {
        "id": "graham_cluley",
        "name": "Graham Cluley",
        "url": "https://grahamcluley.com/feed/",
        "category": "Advisories & Breaches",
        "tier": "Noticias / Brechas"
    },
    {
        "id": "krebs_on_security",
        "name": "Krebs on Security",
        "url": "https://krebsonsecurity.com/feed/",
        "category": "Cybercrime & Investigation",
        "tier": "Noticias / Brechas"
    },
    {
        "id": "sans_isc",
        "name": "SANS Internet Storm Center",
        "url": "https://isc.sans.edu/rssfeed_full.xml",
        "category": "Telemetry & Attacks",
        "tier": "CTI Técnico / Avisos"
    },
    {
        "id": "schneier_on_security",
        "name": "Schneier on Security",
        "url": "https://www.schneier.com/feed/atom/",
        "category": "Crypto & Policy",
        "tier": "Noticias / Brechas"
    },
    {
        "id": "securelist",
        "name": "Securelist (Kaspersky)",
        "url": "https://securelist.com/feed/",
        "category": "APT & Malware",
        "tier": "Investigación DFIR"
    },
    {
        "id": "sophos_secops",
        "name": "Sophos Security Operations",
        "url": "https://news.sophos.com/en-us/category/security-operations/feed/",
        "category": "SOC Ops & Response",
        "tier": "Investigación DFIR"
    },
    {
        "id": "the_hacker_news",
        "name": "The Hacker News",
        "url": "https://feeds.feedburner.com/TheHackersNews?format=xml",
        "category": "Breaking News",
        "tier": "Noticias / Brechas"
    },
    {
        "id": "sophos_threat_research",
        "name": "Sophos Threat Research",
        "url": "https://news.sophos.com/en-us/category/threat-research/feed/",
        "category": "Reverse Eng & Research",
        "tier": "Investigación DFIR"
    },
    {
        "id": "troy_hunt",
        "name": "Troy Hunt",
        "url": "https://www.troyhunt.com/rss/",
        "category": "Breaches & Web Security",
        "tier": "Noticias / Brechas"
    },
    {
        "id": "bleeping_computer",
        "name": "BleepingComputer",
        "url": "https://www.bleepingcomputer.com/feed/",
        "category": "Ransomware & Breaches",
        "tier": "Noticias / Brechas"
    },
    {
        "id": "cisa_advisories",
        "name": "CISA Cybersecurity Alerts",
        "url": "https://www.cisa.gov/cybersecurity-advisories/all.xml",
        "category": "Gov Critical Advisories",
        "tier": "CTI Técnico / Avisos"
    },
    {
        "id": "security_week",
        "name": "SecurityWeek",
        "url": "https://www.securityweek.com/feed/",
        "category": "Enterprise Security",
        "tier": "Noticias / Brechas"
    },
    {
        "id": "welivesecurity",
        "name": "WeLiveSecurity (ESET)",
        "url": "https://feeds.feedburner.com/eset/blog",
        "category": "Malware & Phishing",
        "tier": "Investigación DFIR"
    },
    {
        "id": "unit42",
        "name": "Unit 42 (Palo Alto)",
        "url": "https://unit42.paloaltonetworks.com/feed/",
        "category": "APT & Threat Research",
        "tier": "Investigación DFIR"
    },
    {
        "id": "forti_psirt",
        "name": "Fortinet PSIRT Advisories",
        "url": "https://www.fortiguard.com/rss/ir.xml",
        "category": "Fortinet PSIRT & 0-Days",
        "tier": "CTI Técnico / Avisos"
    },
    {
        "id": "cisa_kev",
        "name": "CISA Known Exploited Vulns",
        "url": "https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json",
        "category": "Exploited Vulns (KEV)",
        "tier": "CTI Técnico / Avisos",
        "format": "json_cisa_kev"
    },
    {
        "id": "seguinfo",
        "name": "Segu-Info (Cristian Borghello)",
        "url": "https://blog.segu-info.com.ar/feeds/posts/default",
        "category": "Cono Sur & Ciberdelito",
        "tier": "Noticias / Brechas"
    },
    {
        "id": "the_cyber_security_hub",
        "name": "The Cyber Security Hub",
        "url": "https://www.cshub.com/rss/news",
        "category": "Enterprise Security Trends",
        "tier": "Noticias / Brechas"
    },
    {
        "id": "elhacker_net",
        "name": "elhacker.net",
        "url": "https://blog.elhacker.net/feeds/posts/default",
        "category": "Hacking & Exploits",
        "tier": "Noticias / Brechas"
    },
    {
        "id": "daily_dark_web",
        "name": "Daily Dark Web",
        "url": "https://dailydarkweb.net/feed/",
        "category": "Dark Web & Ransomware Leaks",
        "tier": "Noticias / Brechas"
    },
    {
        "id": "dark_web_informer",
        "name": "Dark Web Informer",
        "url": "https://darkwebinformer.com/feed/",
        "category": "Dark Web Threat Intel",
        "tier": "Noticias / Brechas"
    },
    {
        "id": "0dayfans",
        "name": "0dayfans",
        "url": "https://0dayfans.com/feed.rss",
        "category": "Exploits & 0-Days",
        "tier": "CTI Técnico / Avisos"
    }
]


@dataclass(frozen=True)
class FeedItem:
    """Entidad inmutable que representa un artículo o alerta de un feed."""
    feed_id: str
    feed_name: str
    title: str
    link: str
    summary: str
    content_hash: str
    published_date: str
    ingested_at: str
    category: str
    status: str = "NUEVO"
    severity: str = "PENDIENTE"
    ai_report: str = ""
    ticket_id: str = ""
    tier: str = ""
    id: Optional[int] = None


def sanitize_html(raw_html: str) -> str:
    """Elimina etiquetas HTML y entidades codificadas para texto forense legible."""
    if not raw_html:
        return ""
    # Quitar scripts y estilos
    clean = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', raw_html, flags=re.DOTALL | re.IGNORECASE)
    # Quitar etiquetas HTML
    clean = re.sub(r'<[^>]+>', ' ', clean)
    # Decodificar entidades HTML
    clean = html.unescape(clean)
    # Normalizar espacios en blanco
    clean = re.sub(r'\s+', ' ', clean).strip()
    return clean


def compute_content_hash(feed_id: str, title: str, link: str) -> str:
    """Genera un hash SHA-256 único e inmutable para deduplicación estricta."""
    canonical_str = f"{feed_id.strip()}|{title.strip().lower()}|{link.strip().lower()}"
    return hashlib.sha256(canonical_str.encode("utf-8")).hexdigest()


from contextlib import contextmanager

class FeedsDatabase:
    """Gestor de persistencia SQLite para almacenamiento y deduplicación de feeds."""

    DEFAULT_DB_NAME = "feeds_intel.db"

    def __init__(self, db_path: Optional[str] = None):
        if db_path is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            self.db_path = os.path.join(base_dir, self.DEFAULT_DB_NAME)
        else:
            self.db_path = db_path
        self._init_db()

    @contextmanager
    def _connection(self):
        """Context manager que asegura el cierre de la conexión SQLite en Windows."""
        conn = sqlite3.connect(self.db_path, timeout=15)
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()

    def _init_db(self) -> None:
        """Inicializa el esquema de base de datos con índices de alta velocidad."""
        with self._connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS feed_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    feed_id TEXT NOT NULL,
                    feed_name TEXT NOT NULL,
                    title TEXT NOT NULL,
                    link TEXT NOT NULL,
                    summary TEXT,
                    content_hash TEXT UNIQUE NOT NULL,
                    published_date TEXT,
                    ingested_at TEXT NOT NULL,
                    category TEXT,
                    status TEXT DEFAULT 'NUEVO',
                    severity TEXT DEFAULT 'PENDIENTE',
                    ai_report TEXT DEFAULT '',
                    ticket_id TEXT DEFAULT '',
                    full_content TEXT DEFAULT ''
                );
            """)
            cursor.execute("PRAGMA table_info(feed_items);")
            existing_cols = [row[1] for row in cursor.fetchall()]
            if "full_content" not in existing_cols:
                cursor.execute("ALTER TABLE feed_items ADD COLUMN full_content TEXT DEFAULT '';")
            if "tier" not in existing_cols:
                cursor.execute("ALTER TABLE feed_items ADD COLUMN tier TEXT DEFAULT '';")

            for feed_id, tier_name in FEED_TIER_MAPPING.items():
                cursor.execute("UPDATE feed_items SET tier = ? WHERE feed_id = ? AND (tier IS NULL OR tier = '')", (tier_name, feed_id))

            cursor.execute("CREATE INDEX IF NOT EXISTS idx_feed_hash ON feed_items(content_hash);")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_feed_tier ON feed_items(tier);")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_feed_status ON feed_items(status);")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_feed_source ON feed_items(feed_name);")
            cursor.execute("CREATE INDEX IF NOT EXISTS idx_feed_ingested ON feed_items(ingested_at DESC);")
            conn.commit()

    def insert_item(self, item: FeedItem) -> bool:
        """
        Inserta un artículo si no existe (idempotente). Retorna True si es nuevo, False si ya existía.
        """
        with self._connection() as conn:
            cursor = conn.cursor()
            try:
                cursor.execute("""
                    INSERT INTO feed_items (
                        feed_id, feed_name, title, link, summary, content_hash,
                        published_date, ingested_at, category, status, severity, ai_report, ticket_id, tier
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    item.feed_id, item.feed_name, item.title, item.link, item.summary, item.content_hash,
                    item.published_date, item.ingested_at, item.category, item.status, item.severity,
                    item.ai_report, item.ticket_id, (item.tier or FEED_TIER_MAPPING.get(item.feed_id, TIER_NEWS))
                ))
                conn.commit()
                return True
            except sqlite3.IntegrityError:
                # Ya existe por hash
                return False

    def get_items(self, 
                  limit: int = 50, 
                  offset: int = 0,
                  feed_name: Optional[str] = None, 
                  status: Optional[str] = None, 
                  search: Optional[str] = None,
                  days: Optional[int] = None,
                  tier: Optional[str] = None,
                  order_by: str = "id DESC") -> List[Dict[str, Any]]:
        """Recupera los artículos filtrados por fuente, nivel CTI, estado, fecha y búsqueda con paginación."""
        query = "SELECT * FROM feed_items WHERE 1=1"
        params: List[Any] = []

        if tier and tier not in ("Todos", "Todos los Niveles", "Todas las Categorías", "Todas"):
            query += " AND tier = ?"
            params.append(tier)

        if feed_name and feed_name != "Todas" and feed_name != "Todas las Fuentes":
            query += " AND feed_name = ?"
            params.append(feed_name)

        if status and status != "Todos":
            query += " AND status = ?"
            params.append(status)

        if search:
            query += " AND (title LIKE ? OR summary LIKE ? OR ai_report LIKE ?)"
            term = f"%{search.strip()}%"
            params.extend([term, term, term])

        if days and days > 0:
            query += f" AND (ingested_at >= datetime('now', '-{int(days)} days'))"

        # Validar columnas permitidas para evitar inyecciones en ORDER BY
        valid_orders = ["id DESC", "id ASC", "published_date DESC", "published_date ASC", "severity DESC", "status ASC"]
        safe_order = order_by if order_by in valid_orders else "id DESC"

        query += f" ORDER BY {safe_order} LIMIT ? OFFSET ?"
        params.extend([limit, offset])

        with self._connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, tuple(params))
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    def get_items_count(self,
                        feed_name: Optional[str] = None,
                        status: Optional[str] = None,
                        search: Optional[str] = None,
                        days: Optional[int] = None,
                        tier: Optional[str] = None) -> int:
        """Retorna el número total de artículos que coinciden con los filtros para paginación."""
        query = "SELECT COUNT(*) FROM feed_items WHERE 1=1"
        params: List[Any] = []

        if tier and tier not in ("Todos", "Todos los Niveles", "Todas las Categorías", "Todas"):
            query += " AND tier = ?"
            params.append(tier)

        if feed_name and feed_name != "Todas" and feed_name != "Todas las Fuentes":
            query += " AND feed_name = ?"
            params.append(feed_name)

        if status and status != "Todos":
            query += " AND status = ?"
            params.append(status)

        if search:
            query += " AND (title LIKE ? OR summary LIKE ? OR ai_report LIKE ?)"
            term = f"%{search.strip()}%"
            params.extend([term, term, term])

        if days and days > 0:
            query += f" AND (ingested_at >= datetime('now', '-{int(days)} days'))"

        with self._connection() as conn:
            cursor = conn.cursor()
            cursor.execute(query, tuple(params))
            return cursor.fetchone()[0]

    def get_item_by_id(self, item_id: int) -> Optional[Dict[str, Any]]:
        """Recupera un artículo específico por su ID primario."""
        with self._connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM feed_items WHERE id = ?", (item_id,))
            row = cursor.fetchone()
            return dict(row) if row else None

    def update_ai_report(self, item_id: int, ai_report: str, severity: str, status: str = "ANALIZADO") -> bool:
        """Actualiza el reporte generado por la IA y la severidad calculada."""
        with self._connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE feed_items 
                SET ai_report = ?, severity = ?, status = ?
                WHERE id = ?
            """, (ai_report, severity, status, item_id))
            conn.commit()
            return cursor.rowcount > 0

    def update_ticket(self, item_id: int, ticket_id: str, status: str = "ESCALADO") -> bool:
        """Asocia un ticket generado (ej. THN-SOC-XXXX) al artículo del feed."""
        with self._connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE feed_items 
                SET ticket_id = ?, status = ?
                WHERE id = ?
            """, (ticket_id, status, item_id))
            conn.commit()
            return cursor.rowcount > 0

    def update_full_content(self, item_id: int, full_content: str) -> bool:
        """Guarda el contenido web completo extraído del artículo para visualización in-app."""
        with self._connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE feed_items SET full_content = ? WHERE id = ?", (full_content, item_id))
            conn.commit()
            return cursor.rowcount > 0

    def mark_status(self, item_id: int, status: str) -> bool:
        """Actualiza el estado de un artículo (NUEVO, ANALIZADO, IGNORADO, ESCALADO)."""
        with self._connection() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE feed_items SET status = ? WHERE id = ?", (status, item_id))
            conn.commit()
            return cursor.rowcount > 0

    def get_statistics(self) -> Dict[str, int]:
        """Calcula el conteo por estado de los feeds."""
        with self._connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT 
                    COUNT(*) as total,
                    SUM(CASE WHEN status = 'NUEVO' THEN 1 ELSE 0 END) as nuevos,
                    SUM(CASE WHEN status = 'ANALIZADO' THEN 1 ELSE 0 END) as analizados,
                    SUM(CASE WHEN status = 'ESCALADO' THEN 1 ELSE 0 END) as escalados,
                    SUM(CASE WHEN status = 'IGNORADO' THEN 1 ELSE 0 END) as ignorados
                FROM feed_items
            """)
            row = cursor.fetchone()
            if row:
                return {
                    "total": row["total"] or 0,
                    "nuevos": row["nuevos"] or 0,
                    "analizados": row["analizados"] or 0,
                    "escalados": row["escalados"] or 0,
                    "ignorados": row["ignorados"] or 0
                }
            return {"total": 0, "nuevos": 0, "analizados": 0, "escalados": 0, "ignorados": 0}


class RSSFeedParser:
    """Parser multi-formato resiliente capaz de procesar RSS 2.0 y Atom 1.0."""

    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"

    @classmethod
    def _find_child_by_tag(cls, element: ET.Element, tag_name: str) -> Optional[ET.Element]:
        """Busca un hijo directo o descendiente ignorando namespaces XML."""
        for child in element:
            local_name = child.tag.split("}")[-1] if "}" in child.tag else child.tag
            if local_name.lower() == tag_name.lower():
                return child
        return None

    @classmethod
    def _find_all_by_tag(cls, element: ET.Element, tag_name: str) -> List[ET.Element]:
        """Encuentra todos los elementos que coincidan con tag_name ignorando namespaces."""
        matched = []
        for elem in element.iter():
            local_name = elem.tag.split("}")[-1] if "}" in elem.tag else elem.tag
            if local_name.lower() == tag_name.lower():
                matched.append(elem)
        return matched

    @classmethod
    def fetch_and_parse(cls, feed_config: Dict[str, str], timeout_sec: int = 10) -> List[FeedItem]:
        """Descarga y parsea el feed devolviendo una lista de FeedItem inmutables."""
        url = feed_config["url"]
        headers = {
            "User-Agent": cls.USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,application/json,*/*;q=0.8",
            "Accept-Language": "es-ES,es;q=0.9,en;q=0.8"
        }
        
        response = requests.get(url, headers=headers, timeout=timeout_sec, verify=False)
        response.raise_for_status()

        fmt = feed_config.get("format", "")
        if fmt == "json_cisa_kev" or "known_exploited_vulnerabilities.json" in url:
            return cls.parse_cisa_kev_json(response.content, feed_config)
        elif fmt == "json_tweetfeed" or "tweetfeed.live" in url:
            return cls.parse_tweetfeed_json(response.content, feed_config)
        elif fmt == "json_threatfox" or "threatfox.abuse.ch" in url:
            return cls.parse_threatfox_json(response.content, feed_config)
        elif fmt == "json_urlhaus" or "urlhaus.abuse.ch" in url:
            return cls.parse_urlhaus_json(response.content, feed_config)
        elif fmt == "json_feodo" or "feodotracker.abuse.ch" in url:
            return cls.parse_feodo_json(response.content, feed_config)
        elif fmt == "text_openphish" or "openphish" in url:
            return cls.parse_openphish_text(response.text, feed_config)
        elif fmt == "csv_malwarebazaar" or "bazaar.abuse.ch" in url:
            return cls.parse_malwarebazaar_csv(response.text, feed_config)

        xml_bytes = response.content
        return cls.parse_xml_bytes(xml_bytes, feed_config)

    @classmethod
    def parse_threatfox_json(cls, json_bytes: bytes, feed_config: Dict[str, str]) -> List[FeedItem]:
        """Parsea los IoCs recientes de ThreatFox (abuse.ch)."""
        import json
        feed_id = feed_config["id"]
        feed_name = feed_config["name"]
        category = feed_config.get("category", "Malware & C2 IoCs")
        tier = feed_config.get("tier", TIER_TACTICAL)
        ingested_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        items: List[FeedItem] = []
        try:
            payload = json.loads(json_bytes.decode("utf-8", errors="ignore"))
            # El JSON tiene claves con IDs de IoC mapeados a arrays o diccionarios
            entries = []
            for k, v in payload.items():
                if isinstance(v, list):
                    entries.extend(v)
                elif isinstance(v, dict):
                    entries.append(v)

            # Tomar los 60 más recientes
            for entry in entries[:60]:
                val = str(entry.get("ioc_value", "")).strip()
                if not val:
                    continue
                ioc_type = str(entry.get("ioc_type", "ioc")).strip().upper()
                threat_type = str(entry.get("threat_type", "c2")).strip().upper()
                malware = str(entry.get("malware_printable") or entry.get("malware") or "Unknown").strip()
                confidence = entry.get("confidence_level", 100)
                date_val = str(entry.get("first_seen_utc", ingested_at)).strip()
                tags = str(entry.get("tags") or "")
                
                title = f"[{malware}] {ioc_type}: {val} ({threat_type})"
                link = f"https://threatfox.abuse.ch/browse/"
                summary = (
                    f"IoC de Alta Fidelidad - ThreatFox (abuse.ch)\n"
                    f"Malware / Amenaza: {malware}\n"
                    f"Observable: {val} ({ioc_type})\n"
                    f"Tipo de Amenaza: {threat_type}\n"
                    f"Nivel de Confianza: {confidence}%\n"
                    f"Etiquetas: {tags}\n"
                    f"Primera Detección: {date_val}"
                )
                c_hash = compute_content_hash(feed_id, title, val + "|" + malware)
                items.append(FeedItem(
                    feed_id=feed_id,
                    feed_name=feed_name,
                    title=title,
                    link=link,
                    summary=summary,
                    content_hash=c_hash,
                    published_date=date_val,
                    ingested_at=ingested_at,
                    category=category,
                    tier=tier,
                    status="NUEVO",
                    severity="ALTA" if confidence >= 80 else "MEDIA"
                ))
        except Exception as e:
            print(f"[RSSFeedParser] Error parseando ThreatFox JSON: {e}")
        return items

    @classmethod
    def parse_urlhaus_json(cls, json_bytes: bytes, feed_config: Dict[str, str]) -> List[FeedItem]:
        """Parsea las URLs de distribución de malware recientes de URLhaus (abuse.ch)."""
        import json
        feed_id = feed_config["id"]
        feed_name = feed_config["name"]
        category = feed_config.get("category", "Malware Distribution URLs")
        tier = feed_config.get("tier", TIER_TACTICAL)
        ingested_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        items: List[FeedItem] = []
        try:
            payload = json.loads(json_bytes.decode("utf-8", errors="ignore"))
            entries = []
            for k, v in payload.items():
                if isinstance(v, list):
                    entries.extend(v)
                elif isinstance(v, dict):
                    entries.append(v)

            # Tomar los 60 más recientes
            for entry in entries[:60]:
                raw_url = str(entry.get("url", "")).strip()
                if not raw_url:
                    continue
                threat = str(entry.get("threat", "malware")).strip()
                status = str(entry.get("url_status", "online")).strip().upper()
                tags = entry.get("tags") or []
                tags_str = ", ".join(tags) if isinstance(tags, list) else str(tags)
                link = str(entry.get("urlhaus_link", "https://urlhaus.abuse.ch/"))
                date_val = str(entry.get("dateadded", ingested_at)).strip()

                title = f"[{threat.upper()}] URL Maliciosa: {raw_url[:65]}..."
                summary = (
                    f"Alerta de Distribución de Malware - URLhaus (abuse.ch)\n"
                    f"URL Maliciosa: {raw_url}\n"
                    f"Estado de la URL: {status}\n"
                    f"Tipo de Amenaza: {threat}\n"
                    f"Tags / Malware: {tags_str}\n"
                    f"Fecha de Detección: {date_val}\n"
                    f"Enlace de Análisis: {link}"
                )
                c_hash = compute_content_hash(feed_id, title, raw_url)
                items.append(FeedItem(
                    feed_id=feed_id,
                    feed_name=feed_name,
                    title=title,
                    link=link,
                    summary=summary,
                    content_hash=c_hash,
                    published_date=date_val,
                    ingested_at=ingested_at,
                    category=category,
                    tier=tier,
                    status="NUEVO",
                    severity="CRÍTICA" if status == "ONLINE" else "ALTA"
                ))
        except Exception as e:
            print(f"[RSSFeedParser] Error parseando URLhaus JSON: {e}")
        return items

    @classmethod
    def parse_feodo_json(cls, json_bytes: bytes, feed_config: Dict[str, str]) -> List[FeedItem]:
        """Parsea la lista negra de IPs de Botnets y C2 de Feodo Tracker (abuse.ch)."""
        import json
        feed_id = feed_config["id"]
        feed_name = feed_config["name"]
        category = feed_config.get("category", "Botnet C2 IP Blocklist")
        tier = feed_config.get("tier", TIER_TACTICAL)
        ingested_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        items: List[FeedItem] = []
        try:
            payload = json.loads(json_bytes.decode("utf-8", errors="ignore"))
            entries = payload if isinstance(payload, list) else []
            for entry in entries[:60]:
                ip = str(entry.get("ip_address", "")).strip()
                if not ip:
                    continue
                port = entry.get("port", "")
                malware = str(entry.get("malware", "Botnet C2")).strip()
                status = str(entry.get("status", "online")).strip().upper()
                first_seen = str(entry.get("first_seen", ingested_at)).strip()
                asn = str(entry.get("as_name", "Desconocido"))

                endpoint = f"{ip}:{port}" if port else ip
                title = f"[{malware}] C2 Botnet IP: {endpoint} ({status})"
                link = f"https://feodotracker.abuse.ch/browse/"
                summary = (
                    f"Servidor de Comando y Control (C2) - Feodo Tracker (abuse.ch)\n"
                    f"IP / Puerto C2: {endpoint}\n"
                    f"Familia Malware: {malware}\n"
                    f"Estado del Servidor: {status}\n"
                    f"ISP / ASN: {asn}\n"
                    f"Fecha Primera Vista: {first_seen}"
                )
                c_hash = compute_content_hash(feed_id, title, endpoint + "|" + malware)
                items.append(FeedItem(
                    feed_id=feed_id,
                    feed_name=feed_name,
                    title=title,
                    link=link,
                    summary=summary,
                    content_hash=c_hash,
                    published_date=first_seen,
                    ingested_at=ingested_at,
                    category=category,
                    tier=tier,
                    status="NUEVO",
                    severity="CRÍTICA" if status == "ONLINE" else "ALTA"
                ))
        except Exception as e:
            print(f"[RSSFeedParser] Error parseando Feodo JSON: {e}")
        return items

    @classmethod
    def parse_openphish_text(cls, text_content: str, feed_config: Dict[str, str]) -> List[FeedItem]:
        """Parsea el feed de URLs de Phishing en vivo de OpenPhish."""
        feed_id = feed_config["id"]
        feed_name = feed_config["name"]
        category = feed_config.get("category", "Live Phishing Feeds")
        tier = feed_config.get("tier", TIER_TACTICAL)
        ingested_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        items: List[FeedItem] = []
        lines = [line.strip() for line in text_content.splitlines() if line.strip() and line.startswith("http")]
        for u in lines[:60]:
            import urllib.parse
            parsed = urllib.parse.urlparse(u)
            dom = parsed.netloc or u
            title = f"[PHISHING] URL Activa: {dom} ({u[:45]}...)"
            summary = (
                f"Campaña de Phishing Activa Detectada - OpenPhish Feed\n"
                f"URL Trampa: {u}\n"
                f"Dominio Suplantador: {dom}\n"
                f"Fecha de Detección: {ingested_at}\n"
                f"Recomendación: Bloquear dominio en Gateway Web y Firewall."
            )
            c_hash = compute_content_hash(feed_id, title, u)
            items.append(FeedItem(
                feed_id=feed_id,
                feed_name=feed_name,
                title=title,
                link=u,
                summary=summary,
                content_hash=c_hash,
                published_date=ingested_at,
                ingested_at=ingested_at,
                category=category,
                tier=tier,
                status="NUEVO",
                severity="ALTA"
            ))
        return items

    @classmethod
    def parse_malwarebazaar_csv(cls, csv_text: str, feed_config: Dict[str, str]) -> List[FeedItem]:
        """Parsea las muestras y hashes de malware recientes de MalwareBazaar (abuse.ch)."""
        import csv
        import io
        feed_id = feed_config["id"]
        feed_name = feed_config["name"]
        category = feed_config.get("category", "Malware Hashes (SHA256)")
        tier = feed_config.get("tier", TIER_TACTICAL)
        ingested_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        items: List[FeedItem] = []
        try:
            valid_lines = [l for l in csv_text.splitlines() if not l.startswith("#") and l.strip()]
            reader = csv.reader(io.StringIO("\n".join(valid_lines)), skipinitialspace=True)
            for row in list(reader)[:60]:
                if len(row) < 9:
                    continue
                first_seen = row[0].strip()
                sha256 = row[1].strip()
                file_name = row[5].strip() or "sample.bin"
                file_type = row[6].strip().upper()
                signature = row[8].strip() or "Malware Desconocido"
                link = f"https://bazaar.abuse.ch/sample/{sha256}/"

                title = f"[{signature}] SHA256: {sha256[:16]}... ({file_name})"
                summary = (
                    f"Muestra de Malware Reciente - MalwareBazaar (abuse.ch)\n"
                    f"Firma / Familia: {signature}\n"
                    f"Archivo: {file_name} ({file_type})\n"
                    f"Hash SHA-256: {sha256}\n"
                    f"Primera Detección: {first_seen}\n"
                    f"Enlace de Muestra: {link}"
                )
                c_hash = compute_content_hash(feed_id, title, sha256)
                items.append(FeedItem(
                    feed_id=feed_id,
                    feed_name=feed_name,
                    title=title,
                    link=link,
                    summary=summary,
                    content_hash=c_hash,
                    published_date=first_seen,
                    ingested_at=ingested_at,
                    category=category,
                    tier=tier,
                    status="NUEVO",
                    severity="ALTA"
                ))
        except Exception as e:
            print(f"[RSSFeedParser] Error parseando MalwareBazaar CSV: {e}")
        return items

    @classmethod
    def parse_tweetfeed_json(cls, json_bytes: bytes, feed_config: Dict[str, str]) -> List[FeedItem]:
        """Parsea el feed en vivo de IOCs de TweetFeed (JSON) en FeedItems inmutables."""
        import json
        feed_id = feed_config["id"]
        feed_name = feed_config["name"]
        category = feed_config.get("category", "IOCs / Threat Intel")
        tier = feed_config.get("tier", TIER_TACTICAL)
        ingested_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        items: List[FeedItem] = []
        try:
            payload = json.loads(json_bytes.decode("utf-8", errors="ignore"))
            if not isinstance(payload, list):
                return items

            for entry in payload:
                val = str(entry.get("value", "")).strip()
                if not val:
                    continue
                ioc_type = str(entry.get("type", "ioc")).strip().upper()
                user = str(entry.get("user", "ThreatIntel")).strip()
                date_val = str(entry.get("date", ingested_at)).strip()
                tweet_url = str(entry.get("tweet", "https://tweetfeed.live")).strip()
                tags = entry.get("tags", [])
                tags_str = " ".join(tags) if isinstance(tags, list) else str(tags)

                title = f"[{ioc_type}] {val} (@{user})"
                summary = (
                    f"Indicador de Compromiso (IOC) en Vivo desde Twitter/X\n"
                    f"Valor IOC: {val}\n"
                    f"Tipo: {ioc_type}\n"
                    f"Etiquetas / Malware: {tags_str}\n"
                    f"Investigador / Fuente: @{user}\n"
                    f"Fecha de Publicación: {date_val}\n"
                    f"Enlace Tweet: {tweet_url}"
                )
                c_hash = compute_content_hash(feed_id, title, tweet_url + "|" + val)

                lower_tags = tags_str.lower()
                if any(k in lower_tags for k in ["c2", "cobaltstrike", "ransomware", "rat", "stealer", "apt"]):
                    sev = "ALTA"
                elif any(k in lower_tags for k in ["phish", "scam", "malspam"]):
                    sev = "MEDIA"
                else:
                    sev = "MEDIA"

                items.append(FeedItem(
                    feed_id=feed_id,
                    feed_name=feed_name,
                    title=title,
                    link=tweet_url,
                    summary=summary,
                    content_hash=c_hash,
                    published_date=date_val,
                    ingested_at=ingested_at,
                    category=category,
                    tier=tier,
                    status="NUEVO",
                    severity=sev
                ))
        except Exception as e:
            print(f"[RSSFeedParser] Error parseando TweetFeed JSON: {e}")
        return items

    @classmethod
    def parse_cisa_kev_json(cls, json_bytes: bytes, feed_config: Dict[str, str]) -> List[FeedItem]:
        """Parsea el catálogo oficial de CISA KEV (JSON) en FeedItems."""
        import json
        feed_id = feed_config["id"]
        feed_name = feed_config["name"]
        category = feed_config.get("category", "Exploited Vulns (KEV)")
        tier = feed_config.get("tier", TIER_TACTICAL)
        ingested_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        items: List[FeedItem] = []
        try:
            payload = json.loads(json_bytes.decode("utf-8", errors="ignore"))
            vulns = payload.get("vulnerabilities", [])
            recent_vulns = sorted(vulns, key=lambda x: x.get("dateAdded", ""), reverse=True)[:40]
            for v in recent_vulns:
                cve = v.get("cveID", "CVE-Desconocido")
                vendor = v.get("vendorProject", "Desconocido")
                product = v.get("product", "")
                v_name = v.get("vulnerabilityName", "")
                date_added = v.get("dateAdded", ingested_at)
                desc = v.get("shortDescription", "")
                action = v.get("requiredAction", "Aplicar mitigaciones o parches del fabricante")
                due = v.get("dueDate", "N/A")

                title = f"[{cve}] {vendor} {product} - {v_name}".strip()
                link = f"https://nvd.nist.gov/vuln/detail/{cve}"
                summary = desc + chr(10) + chr(10) + "Acción requerida: " + action + " | Vencimiento: " + due

                chash = compute_content_hash(feed_id, title, link)
                items.append(FeedItem(
                    feed_id=feed_id,
                    feed_name=feed_name,
                    title=title,
                    link=link,
                    summary=summary,
                    content_hash=chash,
                    published_date=date_added,
                    ingested_at=ingested_at,
                    category=category,
                    tier=tier
                ))
        except Exception as e:
            pass
        return items

    @classmethod
    def parse_xml_bytes(cls, xml_bytes: bytes, feed_config: Dict[str, str]) -> List[FeedItem]:
        """Parsea bytes XML en FeedItems soportando tanto RSS 2.0 como Atom."""
        feed_id = feed_config["id"]
        feed_name = feed_config["name"]
        category = feed_config.get("category", "General")
        ingested_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        items: List[FeedItem] = []
        try:
            root = ET.fromstring(xml_bytes)
        except ET.ParseError:
            # Reintento limpiando caracteres nulos o entidades inválidas
            cleaned_text = xml_bytes.decode('utf-8', errors='ignore')
            cleaned_text = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F]', '', cleaned_text)
            root = ET.fromstring(cleaned_text.encode('utf-8'))

        # 1. Detección de RSS Estándar (<item>)
        rss_items = cls._find_all_by_tag(root, "item")
        if rss_items:
            for node in rss_items:
                title_node = cls._find_child_by_tag(node, "title")
                title = sanitize_html(title_node.text) if title_node is not None and title_node.text else "Sin Título"

                link_node = cls._find_child_by_tag(node, "link")
                link = ""
                if link_node is not None:
                    link = (link_node.text or link_node.get("href") or "").strip()

                desc_node = cls._find_child_by_tag(node, "description")
                if desc_node is None:
                    desc_node = cls._find_child_by_tag(node, "summary")
                desc = sanitize_html(desc_node.text) if desc_node is not None and desc_node.text else ""

                pub_node = cls._find_child_by_tag(node, "pubdate")
                if pub_node is None:
                    pub_node = cls._find_child_by_tag(node, "date")
                pub_date = pub_node.text.strip() if pub_node is not None and pub_node.text else ingested_at

                if not link and not title:
                    continue

                chash = compute_content_hash(feed_id, title, link)
                items.append(FeedItem(
                    feed_id=feed_id,
                    feed_name=feed_name,
                    title=title,
                    link=link,
                    summary=desc,
                    content_hash=chash,
                    published_date=pub_date,
                    ingested_at=ingested_at,
                    category=category,
                    tier=(feed_config.get("tier") or FEED_TIER_MAPPING.get(feed_id, TIER_NEWS))
                ))
            return items

        # 2. Detección de formato Atom (<entry>)
        atom_entries = cls._find_all_by_tag(root, "entry")
        for node in atom_entries:
            title_node = cls._find_child_by_tag(node, "title")
            title = sanitize_html(title_node.text) if title_node is not None and title_node.text else "Sin Título"

            link = ""
            for lk in cls._find_all_by_tag(node, "link"):
                rel = lk.get("rel", "")
                href = (lk.get("href") or "").strip()
                if rel == "alternate" and href:
                    link = href
                    break
                if not link and href and "comments" not in href:
                    link = href
            if not link:
                link_node = cls._find_child_by_tag(node, "link")
                if link_node is not None:
                    link = (link_node.get("href") or link_node.text or "").strip()

            summary_node = cls._find_child_by_tag(node, "summary")
            if summary_node is None:
                summary_node = cls._find_child_by_tag(node, "content")
            summary = sanitize_html(summary_node.text) if summary_node is not None and summary_node.text else ""

            date_node = cls._find_child_by_tag(node, "updated")
            if date_node is None:
                date_node = cls._find_child_by_tag(node, "published")
            pub_date = date_node.text.strip() if date_node is not None and date_node.text else ingested_at

            if not link and not title:
                continue

            chash = compute_content_hash(feed_id, title, link)
            items.append(FeedItem(
                feed_id=feed_id,
                feed_name=feed_name,
                title=title,
                link=link,
                summary=summary,
                content_hash=chash,
                published_date=pub_date,
                ingested_at=ingested_at,
                category=category,
                tier=(feed_config.get("tier") or FEED_TIER_MAPPING.get(feed_id, TIER_NEWS))
            ))

        return items


# =============================================================================
# INTEGRACIÓN ASÍNCRONA PYSIDE6 (QRunnable / QThreadPool)
# =============================================================================
try:
    from PySide6.QtCore import QRunnable, QObject, Signal

    class RSSWorkerSignals(QObject):
        """Señales para reportar el progreso de descarga de feeds a la UI."""
        feed_completed = Signal(str, int, int) # feed_name, new_items_count, total_fetched
        feed_error = Signal(str, str)          # feed_name, error_message

    class RSSFetchTask(QRunnable):
        """Tarea asíncrona ejecutable en QThreadPool para procesar un feed sin bloquear la GUI."""

        def __init__(self, feed_config: Dict[str, str], db: FeedsDatabase):
            super().__init__()
            self.feed_config = feed_config
            self.db = db
            self.signals = RSSWorkerSignals()

        def run(self) -> None:
            feed_name = self.feed_config["name"]
            try:
                items = RSSFeedParser.fetch_and_parse(self.feed_config, timeout_sec=8)
                new_count = 0
                for it in items:
                    if self.db.insert_item(it):
                        new_count += 1
                self.signals.feed_completed.emit(feed_name, new_count, len(items))
            except Exception as e:
                self.signals.feed_error.emit(feed_name, str(e))

except ImportError:
    # Soporte para entornos headless o sin PySide6 instalado en el path de prueba
    RSSWorkerSignals = None
    RSSFetchTask = None


def sync_all_feeds_headless(db_path: Optional[str] = None, feed_ids: Optional[List[str]] = None) -> Dict[str, Any]:
    """
    Ejecuta la sincronización masiva o selectiva de feeds CTI en modo headless (apto para SOAR y tareas cron/diarias).
    Retorna métricas de sincronización: total de feeds, nuevos ítems insertados y errores.
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed

    db = FeedsDatabase(db_path)
    target_feeds = FEEDS_CONFIG
    if feed_ids:
        target_feeds = [f for f in FEEDS_CONFIG if f["id"] in feed_ids]

    results = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "feeds_processed": 0,
        "total_items_fetched": 0,
        "new_items_inserted": 0,
        "errors": []
    }

    def _fetch_single(feed_cfg):
        try:
            items = RSSFeedParser.fetch_and_parse(feed_cfg, timeout_sec=12)
            inserted = 0
            for item in items:
                if db.insert_item(item):
                    inserted += 1
            return (feed_cfg["name"], len(items), inserted, None)
        except Exception as e:
            return (feed_cfg["name"], 0, 0, str(e))

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(_fetch_single, f): f for f in target_feeds}
        for future in as_completed(futures):
            feed_name, fetched, inserted, err = future.result()
            results["feeds_processed"] += 1
            results["total_items_fetched"] += fetched
            results["new_items_inserted"] += inserted
            if err:
                results["errors"].append({"feed": feed_name, "error": err})

    return results
