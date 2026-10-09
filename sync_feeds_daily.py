#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
  TECHNOMA SOC / SOAR - SINCRONIZADOR DIARIO AUTOMÁTICO DE FEEDS CTI & IOCs
=============================================================================
Consume y normaliza diariamente los feeds de CTI, incluyendo los IOCs en vivo
de Twitter/X (TweetFeed), CISA KEV, SANS ISC y fuentes líderes de DFIR.
Diseñado para ejecución desatendida (Headless / Cron / Windows Task Scheduler)
y llamado nativo desde el OpenXDR Central Command Cockpit SOAR.
"""

import os
import sys
import argparse
from datetime import datetime

# Asegurar path de importación al directorio base de soc-env
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from feeds_engine import (
    FEEDS_CONFIG, FeedsDatabase, RSSFeedParser, sync_all_feeds_headless
)


def run_daily_sync(feed_filter=None, verbose=True):
    print("=" * 75)
    print(f"  TECHNOMA SOC / SOAR - SINCRONIZACIÓN DIARIA DE FEEDS CTI & IOCs")
    print(f"  Inicio: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 75)

    db = FeedsDatabase()
    initial_stats = db.get_statistics()
    if verbose:
        print(f"[*] Estado inicial de Base de Datos:")
        print(f"    - Total ítems históricos: {initial_stats.get('total', 0)}")
        print(f"    - Nuevos pendientes:      {initial_stats.get('nuevos', 0)}")
        print(f"    - Analizados / CTI:       {initial_stats.get('analizados', 0)}")
        print("-" * 75)

    print(f"[*] Iniciando ingesta concurrente de {len(FEEDS_CONFIG)} fuentes CTI...")
    results = sync_all_feeds_headless(db_path=db.db_path, feed_ids=feed_filter)

    final_stats = db.get_statistics()
    print("-" * 75)
    print(f"[+] Sincronización completada con éxito:")
    print(f"    - Fuentes procesadas:     {results['feeds_processed']} de {len(FEEDS_CONFIG)}")
    print(f"    - Ítems descargados:      {results['total_items_fetched']}")
    print(f"    - Nuevos IOCs / Alertas:  {results['new_items_inserted']}")
    print(f"    - Total en BD acumulado:  {final_stats.get('total', 0)}")
    
    if results["errors"]:
        print(f"[!] Advertencias o errores en {len(results['errors'])} fuentes:")
        for err in results["errors"]:
            print(f"    - {err['feed']}: {err['error']}")
    else:
        print("[+] 100% de fuentes CTI sincronizadas sin errores.")

    # Muestra especial de los últimos IOCs de TweetFeed
    tweetfeed_items = db.get_items(feed_name="TweetFeed (Live Twitter IOCs)", limit=5)
    if tweetfeed_items:
        print("-" * 75)
        print("[*] Últimos IOCs ingeridos desde Twitter/X (TweetFeed Live):")
        for item in tweetfeed_items:
            print(f"    [{item['severity']}] {item['title']}")
            print(f"         Link: {item['link']}")

    print("=" * 75)
    print(f"  Fin de tarea SOAR: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 75)
    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sincronizador diario de Feeds CTI para el SOAR")
    parser.add_argument("--only", nargs="+", help="IDs de feeds específicos a sincronizar (ej. --only tweetfeed cisa_kev)")
    parser.add_argument("--quiet", action="store_true", help="Modo silencioso para ejecución en cron/scheduler")
    args = parser.parse_args()

    run_daily_sync(feed_filter=args.only, verbose=not args.quiet)
