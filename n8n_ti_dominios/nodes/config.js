// CONFIG CENTRAL DEL FLUJO
// - Recibe la entrada (webhook: body.nombres | manual: nombres).
// - Define umbrales, rutas y la REGLA EXPLÍCITA DE PONDERACIÓN del score.
// - NO contiene claves de API: todas viven en n8n Credentials (cifradas con N8N_ENCRYPTION_KEY).
const entrada = $input.first().json;
let rawNombres = (entrada.body && entrada.body.nombres) || entrada.nombres || entrada['Nombres de Empresas o Personas'] || entrada['nombres_input'] || [];

if (typeof rawNombres === 'string') {
  rawNombres = rawNombres.split(/[\r\n,;]+/).map(s => s.trim()).filter(Boolean);
} else if (!Array.isArray(rawNombres)) {
  rawNombres = [];
}
const nombres = rawNombres;

return [{
  json: {
    nombres,
    user_agent: 'SOC-TI-Dominios/1.0 (n8n; contacto: soc@example.com)',
    max_ips_por_dominio: 3,
    umbral_confianza_dominio: 0.35,
    tlds_heuristica: [
      'gov.py', 'gob.py', 'com.py', 'edu.py', 'org.py', 'py',
      'gov', 'gob', 'com', 'com.ar', 'com.uy', 'com.br', 'cl', 'co', 'net', 'org', 'io', 'tech'
    ],
    dominios_excluidos: [
      'wikipedia.org', 'wikidata.org', 'linkedin.com', 'facebook.com', 'instagram.com', 'x.com', 'twitter.com',
      'youtube.com', 'tiktok.com', 'crunchbase.com', 'bloomberg.com', 'glassdoor.com', 'indeed.com',
      'google.com', 'apple.com', 'amazon.com', 'github.com', 'medium.com', 'reddit.com', 'dnb.com',
      'zoominfo.com', 'opencorporates.com', 'mercadolibre.com.ar', 'mercadolibre.com.uy', 'blogspot.com', 'wordpress.com'
    ],
    rutas_iso: ['/', '/certificaciones', '/calidad', '/iso', '/certifications'],

    // Peso de cada técnica de coincidencia nombre -> dominio (se suman; tope 1.0)
    pesos_descubrimiento: {
      wikidata: 0.5,        // P856 "sitio web oficial" de la entidad encontrada
      crtsh: 0.3,           // certificados OV/EV con O=<nombre> en Certificate Transparency
      busqueda_top1: 0.35,  // 1er resultado orgánico del buscador
      busqueda_top5: 0.2,   // resultados 2..5
      heuristica: 0.35,     // slug(nombre) + TLD configurado (permite descubrir si resuelve por DNS)
      bonus_token: 0.15     // un token significativo del nombre aparece en el label del dominio
    },

    // ================= REGLA DE PONDERACIÓN DEL SCORE (1-100) =================
    // score = clamp( base + Σ puntos , 1 , 100 )
    // - Cada fuente tiene un TOPE de puntos positivos (max). Los negativos (señales buenas) no tienen tope.
    // - Fuentes por IP (Shodan, AbuseIPDB, IP-API, Feodo): se toma la PEOR IP del dominio.
    // - IP de infraestructura compartida (CDN/cloud o IP-API Hosting): AbuseIPDB e IP-API x cdn_factor.
    // - Fuente no disponible => 0 puntos + marca "no_disponible" (nunca se imputa un valor).
    pesos: {
      base: 10,
      min: 1,
      max: 100,
      cdn_factor: 0.5,
      abuseipdb: { max: 30, alto: { umbral: 75, pts: 30 }, medio: { umbral: 25, pts: 18 }, bajo: { umbral: 1, pts: 8 }, limpio: -3 },
      abusech:   { max: 30, feodo_c2: 30, urlhaus_online: 20, urlhaus_historico: 8, threatfox_ioc: 15, limpio: -3 },
      ipapi:     { max: 15, proxy: 15, hosting: 5, limpio: -2 },
      shodan:    { max: 20, cves_1: 8, cves_5: 12, puerto_riesgo: 3, max_puertos: 8, solo_web: -2 },
      mxtoolbox: { max: 15, blacklist: 8, sin_spf: 2, spf_permisivo: 3, sin_dmarc: 3, dmarc_none: 1, correo_ok: -3 },
      iso:       { iso27001_declarado: -1 }
    },
    puertos_riesgo: [21, 23, 25, 110, 135, 139, 143, 445, 1433, 1521, 2375, 3306, 3389, 5432, 5900, 5985, 6379, 9200, 11211, 27017],
    puertos_web: [80, 443, 8080, 8443],
    regex_infra_compartida: 'cloudflare|akamai|fastly|cloudfront|incapsula|imperva|sucuri|amazon|google|microsoft|azure'
  }
}];
