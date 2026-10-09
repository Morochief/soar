#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pruebas unitarias para el motor de feeds CTI (feeds_engine.py).
Valida:
1. Creación e inicialización del esquema SQLite en memoria.
2. Inserción idempotente y deduplicación por SHA-256.
3. Sanitización de HTML.
4. Parsing de fuentes RSS 2.0 y Atom 1.0.
5. Filtros de búsqueda y estadísticas.
"""

import unittest
import os
import tempfile
from feeds_engine import (
    FeedsDatabase, FeedItem, sanitize_html, compute_content_hash, RSSFeedParser
)


class TestFeedsEngine(unittest.TestCase):

    def setUp(self):
        # Base de datos temporal para pruebas aisladas
        self.temp_dir = tempfile.TemporaryDirectory()
        self.db_path = os.path.join(self.temp_dir.name, "test_feeds.db")
        self.db = FeedsDatabase(self.db_path)

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_sanitize_html(self):
        raw = "<p>Alerta de <b>vulnerabilidad</b> en <script>alert(1)</script> Apache &amp; Nginx.</p>"
        cleaned = sanitize_html(raw)
        self.assertEqual(cleaned, "Alerta de vulnerabilidad en Apache & Nginx.")

    def test_content_hash_deterministic(self):
        h1 = compute_content_hash("thn", "Nueva Falla en Linux", "https://thehackernews.com/falla1")
        h2 = compute_content_hash("thn", "Nueva Falla en Linux", "https://thehackernews.com/falla1")
        h3 = compute_content_hash("thn", "Falla distinta", "https://thehackernews.com/falla1")
        self.assertEqual(h1, h2)
        self.assertNotEqual(h1, h3)

    def test_insert_and_deduplication(self):
        item1 = FeedItem(
            feed_id="test_feed",
            feed_name="Test Source",
            title="CVE-2026-9999 RCE detectado",
            link="https://example.com/cve-2026-9999",
            summary="Vulnerabilidad crítica en software de borde",
            content_hash=compute_content_hash("test_feed", "CVE-2026-9999 RCE detectado", "https://example.com/cve-2026-9999"),
            published_date="2026-09-25 06:00:00",
            ingested_at="2026-09-25 06:10:00",
            category="0-Days"
        )

        # Primera inserción: Debe ser exitosa
        self.assertTrue(self.db.insert_item(item1))

        # Segunda inserción con mismo hash: Debe retornar False (Deduplicado)
        self.assertFalse(self.db.insert_item(item1))

        # Verificar total
        stats = self.db.get_statistics()
        self.assertEqual(stats["total"], 1)
        self.assertEqual(stats["nuevos"], 1)

    def test_rss_xml_parsing(self):
        sample_rss = """<?xml version="1.0" encoding="UTF-8"?>
        <rss version="2.0">
            <channel>
                <title>Security Feed</title>
                <item>
                    <title><![CDATA[Falla Crítica en FortiOS]]></title>
                    <link>https://fortiguard.com/psirt/FG-IR-26-001</link>
                    <description><![CDATA[Un desbordamiento de búfer permite RCE no autenticado.]]></description>
                    <pubDate>Thu, 24 Sep 2026 12:00:00 GMT</pubDate>
                </item>
            </channel>
        </rss>""".encode('utf-8')

        config = {"id": "forti", "name": "FortiGuard", "category": "Advisories"}
        items = RSSFeedParser.parse_xml_bytes(sample_rss, config)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].title, "Falla Crítica en FortiOS")
        self.assertEqual(items[0].link, "https://fortiguard.com/psirt/FG-IR-26-001")
        self.assertIn("desbordamiento de búfer", items[0].summary)

    def test_atom_xml_parsing(self):
        sample_atom = b"""<?xml version="1.0" encoding="utf-8"?>
        <feed xmlns="http://www.w3.org/2005/Atom">
            <title>Schneier on Security</title>
            <entry>
                <title>New AI Security Standard</title>
                <link href="https://schneier.com/blog/archives/2026/09/ai_standard.html" />
                <summary>Bruce Schneier analyzes the new security framework.</summary>
                <published>2026-09-24T18:00:00Z</published>
            </entry>
        </feed>"""

        config = {"id": "schneier", "name": "Schneier on Security", "category": "Crypto"}
        items = RSSFeedParser.parse_xml_bytes(sample_atom, config)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].title, "New AI Security Standard")
        self.assertEqual(items[0].link, "https://schneier.com/blog/archives/2026/09/ai_standard.html")

    def test_tweetfeed_json_parsing(self):
        sample_json = b"""[
            {
                "date": "2026-09-30 12:00:00",
                "user": "threat_hunter",
                "type": "ip",
                "value": "198.51.100.25",
                "tags": ["#c2", "#cobaltstrike"],
                "tweet": "https://x.com/threat_hunter/status/123456789"
            }
        ]"""
        config = {
            "id": "tweetfeed",
            "name": "TweetFeed (Live Twitter IOCs)",
            "category": "IOCs / Threat Intel",
            "format": "json_tweetfeed"
        }
        items = RSSFeedParser.parse_tweetfeed_json(sample_json, config)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0].severity, "ALTA")
        self.assertIn("198.51.100.25", items[0].title)
        self.assertIn("cobaltstrike", items[0].summary.lower())

    def test_update_ai_report_and_ticket(self):
        item = FeedItem(
            feed_id="krebs",
            feed_name="Krebs on Security",
            title="DDoS Botnet Takedown",
            link="https://krebsonsecurity.com/takedown",
            summary="Law enforcement dismantles infrastructure.",
            content_hash=compute_content_hash("krebs", "DDoS Botnet Takedown", "https://krebsonsecurity.com/takedown"),
            published_date="2026-09-25",
            ingested_at="2026-09-25",
            category="Cybercrime"
        )
        self.db.insert_item(item)
        items = self.db.get_items(search="Botnet")
        self.assertEqual(len(items), 1)
        item_id = items[0]["id"]

        # Actualizar reporte de IA
        self.db.update_ai_report(item_id, "### Reporte Ejecutivo: Botnet...", "Alta 🔴")
        updated = self.db.get_item_by_id(item_id)
        self.assertEqual(updated["status"], "ANALIZADO")
        self.assertEqual(updated["severity"], "Alta 🔴")
        self.assertIn("Reporte Ejecutivo", updated["ai_report"])

        # Actualizar ticket
        self.db.update_ticket(item_id, "THN-SOC-4450")
        escalated = self.db.get_item_by_id(item_id)
        self.assertEqual(escalated["status"], "ESCALADO")
        self.assertEqual(escalated["ticket_id"], "THN-SOC-4450")


if __name__ == "__main__":
    unittest.main()
