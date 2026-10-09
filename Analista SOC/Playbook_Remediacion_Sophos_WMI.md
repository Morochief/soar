# Playbook: Remediación de Sophos UpdateFailure (Error 80041f00)

**Propósito:** Este documento detalla el procedimiento estándar (PB 6.4) para resolver incidentes en los cuales el motor de Inteligencia Artificial (Stellar Cyber) detecta un evento `Impair Defenses (T1562)` proveniente de un log `Event::Endpoint::UpdateFailure` de Sophos, acompañado de códigos `80041f00` repetitivos.

**Causa Raíz:** El error `80041f00` corresponde a `WBEM_E_CRITICAL_ERROR`. Esto indica que el Repositorio WMI de Windows está corrupto, lo que imposibilita la instalación y registro de los componentes de seguridad de 64 bits de Sophos (AMSI64, HitmanPro, SED64, etc.). **No es un ataque, es un riesgo operativo/salud.**

---

## Procedimiento de Remediación vía Live Response

Una vez validado que se trata de un falso positivo de ataque (pero un verdadero positivo de degradación de salud), el analista SOC o soporte técnico debe conectarse al host afectado utilizando la función **Live Response** desde Sophos Central e ingresar la siguiente justificación:

> **Session purpose:** Troubleshooting y remediación de fallo masivo de actualización de componentes Sophos (Error 80041f00). Reparación de base de datos WMI (winmgmt).

A continuación, ejecutar los comandos en este orden estricto:

### 1. Resetear la base de datos WMI a valores de fábrica
Esto borra el repositorio dañado para que Windows lo reconstruya limpio.
```cmd
winmgmt /resetrepository
```

### 2. Reiniciar el servicio WMI (Forzando dependencias)
Obliga a Windows a cargar la nueva base de datos en memoria, aceptando la detención de servicios dependientes como la Aplicación auxiliar IP.
```cmd
net stop winmgmt /y
net start winmgmt
```

### 3. Purgar la caché de actualización corrupta de Sophos
Elimina paquetes descargados a medias para asegurar un ciclo de instalación limpio.
```cmd
rd /s /q "C:\ProgramData\Sophos\AutoUpdate\Cache"
```

### 4. Reinicio Remoto Asistido (Mandatorio)
Para que el Kernel de Windows asimile la nueva estructura WMI y libere bloqueos de archivos, el reinicio es **obligatorio**. Este comando otorga 5 minutos de gracia al usuario para guardar sus documentos antes de aplicar el reinicio.
```cmd
shutdown /r /t 300 /c "Soporte IT: Reinicio de mantenimiento requerido para actualizar políticas de seguridad. Guarde su trabajo."
```

---

## Criterios de Éxito
Tras el reinicio del host:
1. El repositorio WMI estará sano.
2. El servicio interno `SophosAutoUpdateService` iniciará automáticamente.
3. Detectará su caché purgada, forzará una descarga fresca e instalará el stack faltante (`AMSI64`, `LIVETERMINAL64`, etc.).
4. El panel de Sophos Central pasará a mostrar el equipo con estado **Verde (Saludable)** en 5 a 10 minutos.
