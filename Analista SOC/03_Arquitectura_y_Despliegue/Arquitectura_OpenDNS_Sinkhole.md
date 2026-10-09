# Arquitectura del Incidente: Cómo OpenDNS bloqueó al Malware

Este gráfico explica paso a paso cómo el servidor infectado intentó comunicarse con el atacante y cómo **OpenDNS (Cisco Umbrella)** actuó como un escudo, atrapando la conexión en un "Sinkhole" (Agujero Negro).

## 📊 Diagrama de Secuencia del Ataque

```mermaid
sequenceDiagram
    autonumber
    
    participant H as Servidor Infectado<br/>(172.17.10.124)
    participant FW as FortiGate Firewall
    participant DNS_Int as DNS Interno<br/>(Ignorado)
    participant OpenDNS as OpenDNS / Cisco<br/>(208.67.222.222)
    participant Sinkhole as Sinkhole Cisco<br/>(146.112.61.104)
    participant C2 as Servidor Atacante<br/>(blacksaltys.com)

    Note over H, DNS_Int: Paso 1: El malware intenta resolver el dominio
    
    H-xDNS_Int: ¿Cuál es la IP de blacksaltys.com? (Evadido)
    Note left of DNS_Int: El malware está programado<br/>para ignorar tu DNS local.
    
    H->>FW: DNS Query (UDP 53) a 208.67.222.222
    FW->>OpenDNS: Permite salida a Internet
    
    Note over OpenDNS: Paso 2: Análisis de Inteligencia
    OpenDNS-->>OpenDNS: Verifica "blacksaltys.com" en su base de datos
    OpenDNS-->>OpenDNS: ⚠️ ¡Detectado como SocGholish Malware!
    
    Note over OpenDNS, H: Paso 3: Redirección al Agujero Negro (Sinkhole)
    OpenDNS->>FW: Respuesta DNS: "La IP es 146.112.61.104"
    FW->>H: Recibe la IP falsa
    
    Note over H, C2: Paso 4: Intento de Conexión (La Trampa)
    H->>FW: HTTP GET (Puerto 80) hacia 146.112.61.104
    FW->>Sinkhole: Permite el tráfico (Policy: Serv-a-Internet)
    Sinkhole->>FW: Página HTML de "Sitio Bloqueado" (862 bytes)
    FW->>H: Entrega página de bloqueo
    
    Note over H, Sinkhole: El malware no entiende la página de bloqueo.<br/>Se queda "ciego" y repite el proceso cada 1 minuto.
    
    H-xC2: (Nunca llegó a comunicarse con el atacante real)
```

### 💡 Explicación Humana:

1. **La Evasión:** El malware está programado para ser sigiloso. En vez de usar el servidor DNS de Technoma, va directo a internet y le pregunta a **OpenDNS** (un servicio público de Cisco) cuál es la IP de `blacksaltys.com`.
2. **La Trampa:** Lo que el creador del malware no sabía es que OpenDNS tiene una lista negra mundial. Al ver que piden un dominio malicioso, OpenDNS miente a propósito. No le da la IP real del hacker.
3. **El Sinkhole:** OpenDNS le responde con la IP `146.112.61.104`. Esta IP es un **Sinkhole** (un servidor trampa de Cisco diseñado para absorber conexiones de malware).
4. **El Bucle Ciego:** El servidor infectado se conecta a ese Sinkhole creyendo que es su jefe. El Sinkhole le manda una paginita web estática (de 862 bytes). El virus, al no recibir las instrucciones que esperaba, simplemente espera un minuto y vuelve a intentar.

¡Tu red se salvó de una descarga de Ransomware gracias a que el atacante eligió usar un DNS que ya lo tenía en lista negra!
