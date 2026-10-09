@echo off
title TECHNOMA SOAR - Sincronizador Diario de Feeds CTI
cd /d "%~dp0"
echo ============================================================================
echo   TECHNOMA SOC / SOAR - Sincronizador Diario de Feeds CTI & TweetFeed IOCs
echo ============================================================================
echo.
python sync_feeds_daily.py %*
echo.
pause
