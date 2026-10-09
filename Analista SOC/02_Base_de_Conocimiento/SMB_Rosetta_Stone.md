# 🪨 Piedra de Rosetta: Diccionario Maestro de Comandos SMB (v1, v2 y v3)

Esta guía estructura los comandos de la especificación `[MS-CIFS]` y SMBv2/v3 para traducir identificadores encontrados en logs de red (Stellar Cyber, Wireshark, etc.).

---

## PARTE 1: PROTOCOLO SMBv1 (Legacy)

### 1. Identificadores Críticos (Sección 2.2.1.6)
* **UID (User ID):** Identificador del usuario.
* **TID (Tree ID):** Identificador de la conexión a una carpeta compartida.
* **FID (File ID):** Identificador de un archivo abierto en memoria.
* **PID (Process ID):** Identificador del proceso cliente.
* **MID (Multiplex ID):** Empareja Request con Response.

### 2. Batched Messages ("AndX")
Comandos con terminación `_ANDX` (ej. `SMB_COM_SESSION_SETUP_ANDX`) agrupan un comando principal y el siguiente a ejecutar en un solo paquete para ahorrar tráfico.

### 3. Comandos Principales SMBv1 (Decimales para Logs)

**Conexión y Sesión (Los más vistos)**
| Hex | Dec | Comando Oficial | Significado |
| :--- | :--- | :--- | :--- |
| `0x72` | **114** | `SMB_COM_NEGOTIATE` | Saludo Inicial e Intercambio de Dialectos. |
| `0x73` | **115** | `SMB_COM_SESSION_SETUP_ANDX` | Autenticación y creación de sesión. |
| `0x75` | **117** | `SMB_COM_TREE_CONNECT_ANDX` | Conexión a Carpeta o recurso. |
| `0x71` | **113** | `SMB_COM_TREE_DISCONNECT` | Desconexión voluntaria. |
| `0x74` | **116** | `SMB_COM_LOGOFF_ANDX` | Cierre de sesión. |

**Operaciones Básicas**
| Hex | Dec | Comando Oficial | Significado |
| :--- | :--- | :--- | :--- |
| `0x00` | **0** | `SMB_COM_CREATE_DIRECTORY` | Crear carpeta. |
| `0x02` | **2** | `SMB_COM_OPEN` | Abrir archivo. |
| `0x03` | **3** | `SMB_COM_CREATE` | Crear/Sobrescribir archivo. |
| `0x04` | **4** | `SMB_COM_CLOSE` | Cerrar acceso al archivo. |
| `0x08` | **8** | `SMB_COM_QUERY_INFORMATION` | Pedir atributos. |
| `0x0A` | **10** | `SMB_COM_READ` | Leer datos. |
| `0x0B` | **11** | `SMB_COM_WRITE` | Escribir datos. |

**Subcomandos TRANS (Interprocesos / Pipes)**
| Hex | Dec | Comando Oficial | Significado |
| :--- | :--- | :--- | :--- |
| `0x0026` | **38** | `TRANS_TRANSACT_NMPIPE` | Lectura/Escritura en tubería en un paso. |
| `0x0054` | **84** | `TRANS_CALL_NMPIPE` | Abrir, escribir, leer y cerrar tubería. |

---

## PARTE 2: PROTOCOLO SMBv2 / SMBv3 (Moderno)

### 1. Códigos de Contexto de Negociación (Comando 0 - `SMB2 NEGOTIATE`)
| Hex | Dec | Nombre Oficial del Contexto | ¿Qué registra en tu Log? |
| :--- | :--- | :--- | :--- |
| `0x0001` | **1** | `SMB2_PREAUTH_INTEGRITY` | Parámetros de preautenticación para evitar ataques maliciosos. |
| `0x0002` | **2** | `SMB2_ENCRYPTION_CAPABILITIES` | El tipo de algoritmo de cifrado que van a usar (ej. AES-128 o AES-256). |
| `0x0003` | **3** | `SMB2_COMPRESSION_CAPABILITIES` | Si van a comprimir los archivos en la red para ir más rápido. |
| `0x0005` | **5** | `SMB2_NETNAME_NEGOTIATE_CONTEXT_ID` | El nombre del servidor o dominio al que se está apuntando. |
| `0x0006` | **6** | `SMB2_TRANSPORT_CAPABILITIES` | Características de la velocidad y tipo de conexión de red. |
| `0x0007` | **7** | `SMB2_RDMA_TRANSFORM_CAPABILITIES` | Optimización para tarjetas de red de alta velocidad (RDMA). |
| `0x0008` | **8** | `SMB2_SIGNING_CAPABILITIES` | El tipo de firma digital que usarán para que nadie altere los paquetes. |

### 2. Códigos de Contexto de Creación (Comando 5 - `SMB2 CREATE`)
| Tag | Hex | Dec | Nombre Oficial | Significado |
| :--- | :--- | :--- | :--- | :--- |
| **ExtA** | `0x45787441` | **1165522001** | `SMB2_CREATE_EA_BUFFER` | Solicitud de atributos extendidos del archivo. |
| **SecD** | `0x53656344` | **1399153476** | `SMB2_CREATE_SD_BUFFER` | Descriptor de seguridad (permisos ACL de Windows). |
| **DHnQ** | `0x44486E51` | **1145597521** | `SMB2_CREATE_DURABLE_HANDLE_REQUEST` | Pide un acceso "duradero" por si la red se desconecta temporalmente. |
| **DHnC** | `0x44486E43` | **1145597507** | `SMB2_CREATE_DURABLE_HANDLE_RECONNECT` | Intento de reconexión usando el acceso duradero anterior. |
| **MxAc** | `0x4D784163` | **1299726691** | `SMB2_CREATE_QUERY_MAXIMAL_ACCESS` | Pregunta: *"¿Cuál es el máximo permiso que tengo aquí?"* |
| **AlSi** | `0x416C5369` | **1097618281** | `SMB2_CREATE_ALLOCATION_SIZE` | Asigna un tamaño de espacio fijo en disco para el archivo. |
| **TWrp** | `0x54577270` | **1415017072** | `SMB2_CREATE_TIMEWARP_TOKEN` | Intento de abrir una **versión vieja del archivo** (Shadow Copies). |
| **RqLs** | `0x52714C73` | **1383152755** | `SMB2_CREATE_REQUEST_LEASE` | Solicitud de concesión de caché (Lease) versión 1. |
| **QFid** | `0x51466964` | **1363536228** | `SMB2_CREATE_QUERY_ON_DISK_ID` | Pide el ID interno que tiene el archivo dentro del disco duro. |
| **RqLs** | `0x52714C73` | **1383152755** | `SMB2_CREATE_REQUEST_LEASE_V2` | Solicitud de concesión de caché (Lease) versión 2 (v3.x). |
| **DH2Q** | `0x44483251` | **1145582161** | `SMB2_CREATE_DURABLE_HANDLE_REQUEST_V2` | Pide acceso duradero mejorado (v2). |
| **DH2C** | `0x44483243` | **1145582147** | `SMB2_CREATE_DURABLE_HANDLE_RECONNECT_V2` | Reconexión de acceso duradero mejorado (v2). |
| **AppI** | `0x41707049` | **1097887817** | `SMB2_CREATE_APP_INSTANCE_ID` | ID único de la aplicación que está abriendo el archivo. |
| **SVHD** | `0x53564844` | **1398167620** | `SVHDX_OPEN_DEVICE_CONTEXT` | Apertura de un disco virtual compartido (usado en Hyper-V). |
| **AIVs** | `0x41495673` | **1095325300** | `SMB2_CREATE_APP_INSTANCE_VERSION` | Versión de la aplicación que abrió el archivo. |

### 3. Códigos de Operación IOCTL / FSCTL (Comando 11 - `SMB2 IOCTL`)
| Hex | Dec | Nombre Técnico de la Operación | Significado en el Log |
| :--- | :--- | :--- | :--- |
| `0x001440F2` | **1327346** | `FSCTL_SRV_COPYCHUNK` | Copiar un pedazo de archivo directamente de un lado a otro del servidor. |
| `0x001440F6` | **1327350** | `FSCTL_SRV_COPYCHUNK_WRITE` | Escribir los pedazos copiados internamente en el servidor. |
| `0x001441BB` | **1327547** | `FSCTL_SRV_READ_HASH` | Pide el hash (huella digital) de un archivo para verificar si cambió. |
| `0x001401D4` | **1311188** | `FSCTL_LMR_REQUEST_RESILIENCY` | Solicita que la conexión sea resistente a microcortes de red. |
| `0x00140204` | **1311236** | `FSCTL_VALIDATE_NEGOTIATE_INFO` | Comando de seguridad obligatorio para verificar que nadie alteró el "saludo". |
| `0x00140078` | **1310840** | `FSCTL_SRV_REQUEST_RESUME_KEY` | Solicita una clave para reanudar una copia de archivos que se pausó. |
| `0x001401FC` | **1311228** | `FSCTL_QUERY_NETWORK_INTERFACE_INFO` | Le pide al servidor la lista de sus IPs y tarjetas de red activas. |

### 4. Códigos de Niveles de Información (Comandos 16 y 17 - `QUERY_INFO / SET_INFO`)
| Código Dec | Nombre del Nivel | ¿Qué datos se están moviendo en la red? |
| :--- | :--- | :--- |
| **1** | `SMB2_0_INFO_FILE` | Metadatos del archivo (fechas de creación, nombre, tamaño). |
| **2** | `SMB2_0_INFO_FILESYSTEM` | Información del disco (espacio total, espacio libre, formato NTFS). |
| **3** | `SMB2_0_INFO_SECURITY` | **Seguridad:** Permisos de usuarios, dueños del archivo y SIDs. |
| **4** | `SMB2_0_INFO_QUOTA` | Las cuotas de disco asignadas a los usuarios de la red. |
