# Resumen técnico — Diagnóstico de alertas de Brute Force (falsos positivos HealthMailbox)

## Contexto
Alertas de Stellar Cyber XDR (`internal_user_login_fail_ntlm` / `internal_user_login_fail_kerberos`, T1110 Brute Force) generadas por el motor ML sobre el host VMBASE8 / Exchange server 172.16.201.4, dominio cajaande.local.

## Comandos ejecutados y hallazgos

### 1. Verificar existencia y estado de las cuentas HealthMailbox en AD
```powershell
Get-ADUser -Filter {SamAccountName -like "HealthMailbox*"} -Properties SamAccountName,Enabled,UserPrincipalName
```
**Hallazgo:** 22 cuentas HealthMailbox existen en AD. 18 de 22 están Enabled: False, solo 4 activas. Todas tienen UserPrincipalName con sufijo `@cajaande.local`.

### 2. Identificar sufijos UPN válidos en el bosque
```powershell
Get-ADForest | Select-Object -ExpandProperty UPNSuffixes
```
**Hallazgo:** `cajaande.gov.py` es un sufijo UPN válido y registrado en el bosque (no es un error de configuración de dominio).

### 3. Revisar servicios de Exchange activos
```powershell
Get-WmiObject Win32_Service | Where-Object {$_.Name -like "*Health*" -or $_.Name -like "*MSExchange*"}
```
**Hallazgo:** MSExchangeHM (Health Manager) está Running — es el servicio responsable de los probes de Managed Availability que generan estos intentos de login.

### 4. Confirmar DNS suffix primario del servidor
```powershell
[System.Net.NetworkInformation.IPGlobalProperties]::GetIPGlobalProperties().DomainName
```
**Hallazgo:** `cajaande.local` — coincide con el UPN de las cuentas, descarta que el mismatch venga de configuración DNS local.

### 5. Revisar Accepted Domains de la organización Exchange
```powershell
Get-AcceptedDomain | Select-Object DomainName, DomainType, Default
```
**Hallazgo clave:**

| Dominio | Tipo | Default |
| :--- | :--- | :--- |
| cajaande.local | Authoritative | False |
| cajaande.gov.py | InternalRelay | True |

### 6. Revisar Email Address Policy
```powershell
Get-EmailAddressPolicy | Select-Object Name, EnabledEmailAddressTemplates, Priority
```
**Hallazgo clave:**
*   SMTP (primaria) = `@cajaande.gov.py`
*   smtp (secundaria) = `@cajaande.local`

## Causa raíz identificada

Dos problemas concurrentes generan el ruido:

1.  **Cuentas deshabilitadas siendo probadas (evento NTLM, Status 0xc0000072):** 18 de 22 cuentas HealthMailbox están deshabilitadas, pero algo (MSExchangeHM) sigue intentando autenticar contra ellas.
2.  **Mismatch de sufijo UPN (evento Kerberos, Status 0x6 / KDC_ERR_C_PRINCIPAL_UNKNOWN):** El dominio SMTP default de la organización es `cajaande.gov.py` (marcado como InternalRelay, no Authoritative), pero las cuentas HealthMailbox tienen su UserPrincipalName real en `cajaande.local`. Managed Availability arma los probes de autenticación usando el dominio primario de la Email Address Policy (gov.py), que no coincide con el UPN real de la cuenta en AD → el KDC no puede resolver el principal.

> **Nota relevante:** Que el dominio default (`gov.py`) esté configurado como InternalRelay en vez de Authoritative es una combinación atípica — sugiere una migración de dominio incompleta o una decisión de diseño que requiere contexto adicional del administrador de Exchange antes de modificar nada.

## Estado
No se ejecutó ningún comando de escritura/modificación (`Set-*`, `New-*`, `Remove-*`). Todo el diagnóstico fue con cmdlets de solo lectura (`Get-*`). La corrección de fondo (ajustar Accepted Domain/Email Address Policy o gestionar las cuentas deshabilitadas) queda pendiente de decisión del equipo de Exchange/AD, en ventana de mantenimiento planificada.

Diferencias clave
Campo	Documento 4 (Kerberos)	Documento 5 (NTLM)
event_id	4768	4776
xdr_event.subtype.name	internal_user_login_fail_kerberos	internal_user_login_fail_ntlm
task	Kerberos Authentication Service	Credential Validation
detected_fields	srcip	service_id
detected_values	172.16.201.4	VM-MARANDU
event_data.Status	0x6 (KDC_ERR_C_PRINCIPAL_UNKNOWN)	0xc0000072 (cuenta deshabilitada)
event_data.TargetUserName	HealthMailbox0ab06aa...@cajaande.**gov.py**	HealthMailbox73cb57c1...@cajaande.**local**
Cuenta HealthMailbox	0ab06aa4d6694324a4ef2ee8dfd51dc6 (confirmamos: Enabled: True)	73cb57c1bc0641e48692c639da6248bf (confirmamos: Enabled: False)
service_id	CAJAANDE.LOCAL	VM-MARANDU
Workstation/ServiceName	krbtgt/CAJAANDE.LOCAL	Workstation: VM-MARANDU
num_failed / total_failed	138 / 163	9 / 88
weighted_anomaly_score	7645	1969
fidelity	98.52	45.05
event_score	71	55
hostip_geo/srcip_geo	tiene ambos (srcip_geo porque el detector es por IP)	solo hostip_geo (no hay srcip_geo, porque el detector es por service_id, no por IP)
timestamp_utc	08:18:06	08:31:09
En términos simples

Son dos protocolos de autenticación distintos fallando por dos motivos distintos, aunque ambos involucran cuentas HealthMailbox y ambos disparan el mismo tipo de alerta genérica (T1110 Brute Force) en Stellar Cyber:

Doc 4 = Kerberos, y falla porque el UPN usado (@cajaande.gov.py) no coincide con el dominio real de la cuenta en el ticket (mismatch de sufijo que identificamos con Get-AcceptedDomain/Get-EmailAddressPolicy).
Doc 5 = NTLM, y falla porque la cuenta específica está Enabled: False en AD — directamente no puede autenticar sin importar el sufijo.

Es justo la evidencia que sostiene el diagnóstico de "dos causas raíz concurrentes" que armamos en el resumen anterior — cada evento es prueba de una de las dos.

Qué es VM-MARANDU

VM-MARANDU no es el mismo equipo que VMBASE8. Es una estación de trabajo distinta (otro host Windows del dominio cajaande.local) desde donde se originó el intento NTLM fallido. Salió del campo event_data.Workstation del evento 4776 (NTLM) — ese campo lo llena Windows con el NetBIOS name del equipo que inició la autenticación, no con su IP.

Fijate el detalle en el JSON que compartiste: en observables.host, el primer objeto tiene:

"ip": "VM-MARANDU",
"hostname": "VM-MARANDU"

Eso es un placeholder — Stellar Cyber no tenía la IP real de ese equipo disponible en el log NTLM (a diferencia del log Kerberos, que sí trae IpAddress explícito), así que usó el nombre NetBIOS también como valor del campo IP porque no tenía otro dato para llenarlo. No es un error, es una limitación del propio Windows Event Log 4776: NTLM no siempre reporta la IP de origen, solo el nombre de máquina.

En el segundo JSON pasa lo inverso: ip: 172.16.201.4 y hostname: 172.16.201.4 — ahí sí tenían la IP (evento Kerberos trae IpAddress explícito), pero no pudieron resolver el hostname (probablemente porque 172.16.201.4 no tiene un PTR record configurado en DNS reverso), así que repitieron la IP como fallback del hostname.

Por qué salen como alertas separadas

Tres motivos que se combinan:

1. Son dos protocolos de auth distintos → dos eventos de Windows distintos.

NTLM → Event ID 4776, service_id: VM-MARANDU
Kerberos → Event ID 4768, service_id: CAJAANDE.LOCAL, srcip: 172.16.201.4

Cada uno genera su propio log en el DC, y Stellar Cyber los procesa como entidades separadas desde el origen.

2. Cada detector ML agrega sobre una dimensión distinta. Mirá detected_fields:

Alerta 1 (NTLM): detected_fields: ["service_id"] → el motor agrupa por nombre de máquina/servicio (VM-MARANDU)
Alerta 2 (Kerberos): detected_fields: ["srcip"] → el motor agrupa por IP de origen (172.16.201.4)

Son detectores distintos (detector_index: 2 vs detector_index: 0) del mismo motor UEBA, cada uno mirando una faceta diferente del comportamiento anómalo (por host vs por IP). No están correlacionados entre sí — cada uno dispara su propia alerta independiente aunque el "ruido de fondo" (HealthMailbox) sea la misma causa raíz.

3. Distintas cuentas HealthMailbox involucradas. El segundo JSON que pasaste ahora ("total": 4) trae dos usuarios en observables.user — combina la cuenta 0ab06aa4...@gov.py (Kerberos, la que sí está Enabled) con 73cb57c1...@local (NTLM, la deshabilitada). Esto confirma que Stellar Cyber, al no tener un campo único y confiable de correlación entre estos eventos NTLM/Kerberos (por las limitaciones de mapeo que vimos antes), termina generando alertas fragmentadas por cada combinación de detector + dimensión agregada, en vez de una sola alerta consolidada por "ruido de HealthMailbox".

En resumen: es el mismo problema de fondo (cuentas HealthMailbox con mismatch de UPN + deshabilitadas) manifestándose como múltiples alertas fragmentadas, porque el motor ML de Stellar Cyber corre detectores independientes por IP, por host y por servicio, sin una capa de deduplicación que las una en un solo incidente.
