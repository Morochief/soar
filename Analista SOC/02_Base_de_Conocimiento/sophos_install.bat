Microsoft Windows [Versión 10.0.17763.7009]

(c) 2018 Microsoft Corporation. Todos los derechos reservados.



C:\Windows\system32>powershell

Windows PowerShell

Copyright (C) Microsoft Corporation. Todos los derechos reservados.



PS C:\Windows\system32> Get-Content "\\172.16.201.10\DeployServer\sophos_install.bat"

@echo off

REM --- Script de Instalacion Sophos (Grupo: Caja Ande) ---



REM 1. Verifica si ya esta instalado para no repetir

IF EXIST "C:\Program Files\Sophos\Sophos UI\Sophos UI.exe" GOTO END



REM 2. Instala Sophos y elimina Kaspersky automaticamente

REM NOTA: Cambia SERVIDOR_AD por el nombre real de tu servidor

"\\172.16.201.10\DeployServer\SophosSetupServer.exe" --quiet --products=all



:END

EXIT

PS C:\Windows\system32> 

