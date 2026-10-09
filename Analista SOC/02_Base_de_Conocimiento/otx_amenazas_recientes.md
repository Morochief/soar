# 👽 Inteligencia de Amenazas Activas (AlienVault OTX)

**Generado el:** 2026-07-02 10:51:15 UTC
> **Nota del Analista:** Este reporte muestra las campañas maliciosas en curso. Los 'IoCs' (Indicadores de Compromiso) son las armas que usan los atacantes (IPs, Dominios, Hashes de virus). Debes bloquearlos en el Firewall.

---

## 🛑 Campaña: A single RedLine C2 pivots into a maritime spear-phishing cluster and attacker-owned infrastructure.
* **Descripción:** An investigation beginning with a single RedLine Stealer C2 server from VMRay UniqueSignal evolved into uncovering a targeted Business Email Compromise campaign against South Korean maritime infrastructure. The analysis started with IP 194.156.79.122 on port 55615, leveraging fingerprinting techniques through FOFA and VirusTotal to identify additional C2 infrastructure. Pivoting through communicating files revealed spear-phishing emails targeting Kangrim Heavy Industries, a major South Korean marine boiler manufacturer. The campaign delivered Formbook malware through impersonated maritime supply chain companies. Further infrastructure analysis identified seven fraudulent domains hosted on TheHost LLC infrastructure, utilizing similar naming patterns and TLS certificates. The attack demonstrates sophisticated BEC tactics combining malware delivery with social engineering, mimicking legitimate business correspondence within the maritime shipping sector.
* **Tags / Palabras clave:** `spear-phishing, south korean victims, business email compromise, infrastructure pivoting, maritime sector targeting, formbook, metamorfo, redline stealer, domain impersonation, casbaneiro, xloader`
* **Total de Armas detectadas (IoCs):** 27

### Muestra de Indicadores Críticos a bloquear (Top 5):
- **IPV4**: `194.156.79.122`
- **URL**: `http://194.156.79.122:55615`
- **IPV4**: `85.17.40.98`
- **URL**: `http://85.17.40.98:55615`
- **IPV4**: `185.252.24.52`

---

## 🛑 Campaña: RustDuck: An In-Depth Analysis of a Two-Stage Botnet
* **Descripción:** Since February 2026, a new malware family utilizing a Loader plus Core two-stage architecture has been detected, primarily conducting large-scale DDoS attacks with strong cross-platform capabilities. The family is transitioning from C to Rust programming language, demonstrating rapid evolution in anti-defense and traffic encryption techniques. Propagation methods include weak password brute-forcing via Telnet and SSH, exploitation of IoT device vulnerabilities affecting Android ADB, TVT API, Ruijie, TP-Link, and ZTE devices, plus web component vulnerabilities in ThinkPHP, Jenkins, and YARN. The botnet employs sophisticated anti-debugging mechanisms including environment checks, honeypot detection, and timing verification. Communication protocols leverage Curve25519 key exchange, ChaCha20-Poly1305 and AES-GCM encryption, implementing strict handshake verification processes. Over 20 IPs have been observed spreading the botnet, with multiple variants showing increasingly complex encryption and obfuscation techn
* **Tags / Palabras clave:** `two-stage loader, ddos botnet, cve-2025-29635, iot compromise, cve-2018-8007, weak password attacks, encrypted c2, cross-platform, cve-2017-17215, cve-2024-1781, anti-debugging, rustduck`
* **Total de Armas detectadas (IoCs):** 23

### Muestra de Indicadores Críticos a bloquear (Top 5):
- **CVE**: `CVE-2017-17215`
- **CVE**: `CVE-2024-1781`
- **CVE**: `CVE-2018-8007`
- **DOMAIN**: `disciplinenahidwin.st`
- **CVE**: `CVE-2025-29635`

---

## 🛑 Campaña: Blacksite: New AiTM Phishing Kit Evades URL Scanners via Cloaked.gg
* **Descripción:** Blacksite is a newly identified adversary-in-the-middle phishing-as-a-service offering sold alongside Cloaked.gg, a cloaking platform that conceals phishing infrastructure from automated security analysis. The kit operates as a reverse-proxy that intercepts authentication tokens, session cookies, and 2FA codes in real time, enabling full account takeover even against MFA-protected accounts. Cloaked.gg blocks traffic from AWS, Google Cloud, and Azure networks while serving AI-generated decoy pages to suspected scanners, making malicious URLs appear benign during automated analysis. Priced between $600-$1,000 monthly, the service commercializes sophisticated AiTM techniques, lowering technical barriers for attackers. The pairing of credential theft capabilities with anti-detection infrastructure creates a split-view environment where security tools see harmless content while intended victims are routed to live phishing pages targeting consumer, financial, and enterprise identity systems.
* **Tags / Palabras clave:** `credential-theft, url-evasion, aitm, mfa-bypass, blacksite, session-hijacking, cloaking, reverse-proxy, tycoon 2fa, phishing-as-a-service`
* **Total de Armas detectadas (IoCs):** 8

### Muestra de Indicadores Críticos a bloquear (Top 5):
- **DOMAIN**: `allegro-pl.site`
- **DOMAIN**: `allegro-pl.top`
- **DOMAIN**: `charliesdemons.com`
- **DOMAIN**: `cloaked-demo.com`
- **DOMAIN**: `cloaked.gg`

---

## 🛑 Campaña: Inside an affiliate panel targeting Microsoft 365
* **Descripción:** Cisco Talos discovered ARToken, a sophisticated phishing-as-a-service panel sharing infrastructure and operational patterns with the EvilTokens platform. The panel exposes over 80 API endpoints enabling device code phishing, Primary Refresh Token persistence, email access, business email compromise operations, and SharePoint exfiltration through a React-based dashboard. The platform deploys a seven-layer anti-analysis system combining client-side behavioral verification with XOR-encrypted payloads. ARToken abuses Microsoft's OAuth 2.0 Device Authorization Grant to bypass multi-factor authentication entirely. Analysis reveals post-compromise capabilities including token management across password resets, automated BEC operations, inbox rule manipulation for evidence suppression, cross-account keyword monitoring, and SharePoint file operations. The platform operates as multi-tenant infrastructure with subscription-based affiliate access, representing a complete operations environment rather than simple phish...
* **Tags / Palabras clave:** `oauth abuse, phishing-as-a-service, eviltokens, business email compromise, microsoft 365, artoken, device code phishing, primary refresh token`
* **Total de Armas detectadas (IoCs):** 5

### Muestra de Indicadores Críticos a bloquear (Top 5):
- **CVE**: `CVE-2025-20333`
- **CVE**: `CVE-2025-20362`
- **CVE**: `CVE-2026-20182`
- **HOSTNAME**: `dashboard-bl.pamconj.com`
- **HOSTNAME**: `spx.pamconj.com`

---

## 🛑 Campaña: Browser-Only Ransomware: From LLM Hallucinations to a Practical Attack Technique
* **Descripción:** Check Point Research discovered a novel browser-native ransomware technique that emerged from AI-generated code attributed to DeepSeek. The attack leverages the File System Access API in Chromium browsers to encrypt files without requiring native payloads, exploits, or app installations. A malicious sample disguised as an AI image upscaler was analyzed, revealing how LLMs can connect theoretical platform risks to practical attack workflows. The technique is particularly concerning on Android, where Chrome allows web pages to access photo directories after user approval through legitimate permission prompts. By using social engineering with a fake AI enhancement tool, attackers can persuade victims to grant folder-level access, enabling file exfiltration and encryption entirely within the browser. This demonstrates how frontier AI models can autonomously design novel attack chains by reasoning across existing knowledge.
* **Tags / Palabras clave:** `infernograbber, llm-generated malware, android chrome exploitation, social engineering, deepseek, voidlink, ai-assisted attacks, phishing lures, file system access api, browser-native ransomware`
* **Total de Armas detectadas (IoCs):** 1

### Muestra de Indicadores Críticos a bloquear (Top 5):
- **FILEHASH-SHA256**: `07c39f79ab92fb21557b82283472dce1c112f577d796111fb752c3c6d84c86b5`

---

## 🛑 Campaña: How a single ScreenConnect incident exposed a massive campaign
* **Descripción:** A massive campaign distributes malicious installer archives hosted on spoofed websites masquerading as popular software like OBS Studio, DNS Jumper, DS4Windows, and Bandicam. Over 90 domain names localized across 10 languages were discovered. The malicious archives bundle a legitimate Microsoft-signed install.exe binary with a rogue install.res.1033.dll library deployed via DLL sideloading. This installs the ScreenConnect remote access service, which then deploys AsyncRAT payloads through PowerShell and VBS scripts. The threat actors leverage SEO techniques to position fraudulent sites at the top of search engine results, targeting both individual users and corporate networks. The infrastructure spans three IP addresses with domains registered between October 2025 and March 2026, creating a global footprint with multi-language support.
* **Tags / Palabras clave:** `remote access trojan, fake software, c2 infrastructure, process hollowing, screenconnect, powershell loader, typosquatting, seo poisoning, dll sideloading, asyncrat`
* **Total de Armas detectadas (IoCs):** 134

### Muestra de Indicadores Críticos a bloquear (Top 5):
- **DOMAIN**: `corel-draw.net`
- **IPV4**: `185.254.97.249`
- **DOMAIN**: `vlc-player.net`
- **DOMAIN**: `processhacker.net`
- **DOMAIN**: `km-player.com`

---

## 🛑 Campaña: Iran-Nexus Disseminates MarkiRAT Surveillance Tool
* **Descripción:** TAG-182, an Iran-nexus threat cluster, is conducting surveillance operations targeting Iranian citizens both domestically and abroad using MarkiRAT malware. The group distributes fake Android applications masquerading as VPN services and media players through social media platforms, particularly Instagram. Following Iran's partial internet restoration in May 2026 after an 88-day shutdown, these surveillance activities have intensified as Iranian security apparatus seeks to monitor perceived dissidents and anti-government activists. MarkiRAT samples demonstrate tradecraft overlaps with previously documented Ferocious Kitten operations, including use of Background Intelligent Transfer Service (BITS). The group operates infrastructure across multiple autonomous systems, utilizing domains with naming conventions mimicking legitimate services like Microsoft, Google, and Facebook.
* **Tags / Palabras clave:** `ferocious kitten, irgc, furball, surveillance, iran, fake vpn, bouldspy, markirat, tag-182, dchspy, farsi-speaking targets`
* **Total de Armas detectadas (IoCs):** 85

### Muestra de Indicadores Críticos a bloquear (Top 5):
- **IPV4**: `46.30.191.123`
- **FILEHASH-SHA256**: `400eb6a94810323a1fc5f8ab31c682fe765aaec2cc61b37c31d719c7e45c9a6c`
- **DOMAIN**: `yemplayer.site`
- **HOSTNAME**: `min.comi-site.website`
- **HOSTNAME**: `microsoft.comi-site.website`

---

## 🛑 Campaña: Analysis of Ongoing Ousaban Attacks Targeting the Iberian Peninsula
* **Descripción:** In May 2026, an attack campaign targeting banking users in Spain and Portugal was identified involving the Ousaban banking Trojan. The malware, previously active in Brazil, spreads through phishing PDFs that redirect victims to malicious webpages performing environment checks to ensure targets are located in Spain or Portugal. The attack chain involves VBS scripts downloading steganographic images containing the payload, which is then dropped and executed on victims' systems. Ousaban establishes persistence, monitors banking activity across multiple financial institutions, and uses daily-changing DDNS domains to resolve C2 server addresses. The malware employs screenshot capture, keylogging, clipboard injection, and remote control capabilities to steal banking credentials. It utilizes custom encryption algorithms and geofencing techniques to evade detection and limit exposure to intended targets.
* **Tags / Palabras clave:** `credential theft, phishing, portugal, iberian peninsula, ousaban, geofencing, casbaneiro, spain, banking trojan`
* **Total de Armas detectadas (IoCs):** 36

### Muestra de Indicadores Críticos a bloquear (Top 5):
- **IPV4**: `162.33.179.46`
- **IPV4**: `91.92.240.140`
- **IPV4**: `78.40.209.32`
- **FILEHASH-SHA256**: `d4eb4ff02df659fdeec17d36b77084627469623bb3c7d16383d257404b52d1c3`
- **FILEHASH-MD5**: `18205d398e5df7d38705dbdc700ccb46`

---

## 🛑 Campaña: A New Threat Actor Using ClickFix and Fake Update Drive-By Attacks in Thousands of Compromised Sites
* **Descripción:** A sophisticated threat actor named DriveSurge operates as an Initial Access Broker using a Pay-Per-Install model to deliver malware at scale. The actor compromises thousands of legitimate websites and uses zTDS (Traffic Distribution System) to silently redirect visitors to malicious content. Victims encounter either FakeUpdates campaigns that impersonate browser update prompts for 11 different browsers, or ClickFix attacks that trick users into executing malicious commands through fake error messages. DriveSurge's infrastructure utilizes bulletproof hosting services, primarily NiceNIC registrar, and has been operating since at least 2015. The campaigns target both Windows and macOS systems, employing sophisticated obfuscation techniques and clipboard hijacking to achieve infection. Eight technical fingerprints have been identified to track this actor's infrastructure and activities.
* **Tags / Palabras clave:** `initial access broker, fakeupdates, ztds, browser impersonation, clickfix, bulletproof hosting`
* **Total de Armas detectadas (IoCs):** 30

### Muestra de Indicadores Críticos a bloquear (Top 5):
- **DOMAIN**: `ztds.info`
- **DOMAIN**: `cptoptious.com`
- **DOMAIN**: `captioto.com`
- **DOMAIN**: `newtdsone.shop`
- **DOMAIN**: `maxintora.com`

---

## 🛑 Campaña: FSB’s matryoshka #1/3 – Gamaredon’s gifts that keeps unpacking – GammaPhish and GammaWorm
* **Descripción:** Gamaredon, a cyberespionage group operated by Russia's FSB, conducts long-term intrusion operations targeting Ukrainian government, military, and critical infrastructure. This analysis documents their 2026 infection chain, which uses HTML smuggling with weaponized xHTML files delivering RAR archives that exploit CVE-2025-8088 to extract HTA files into Windows Startup directories. The chain deploys GammaPhish for initial access, GammaLoad for staging, GammaWorm for propagation via USB and network drives, and GammaSteal for exfiltration. The architecture is nearly fileless, leveraging NTFS Alternate Data Streams to conceal modules and using Dead Drop Resolvers on legitimate platforms like Telegram and Cloudflare for C2 infrastructure. Every stage functions as an independent backdoor capable of executing arbitrary VBScript, representing a shift from their historical Pteranodon framework to a modular ecosystem designed for persistent espionage.
* **Tags / Palabras clave:** `gammaworm, gammaload, pteranodon, gamaredon, gammasteal, gammaphish, fsb`
* **Total de Armas detectadas (IoCs):** 11

### Muestra de Indicadores Críticos a bloquear (Top 5):
- **CVE**: `CVE-2018-20250`
- **CVE**: `CVE-2025-8088`
- **HOSTNAME**: `iiwdsxwamylbwwsoyrmj.supabase.co`
- **DOMAIN**: `quitethepastry.ru`
- **FILEHASH-MD5**: `1794369214b7f62e70a0485e61335c61`

---

## 🛑 Campaña: The Gentlemen are knocking: сustom backdoors and evolving tactics
* **Descripción:** The Gentlemen ransomware-as-a-service group emerged as a top-10 threat actor in the first half of 2026. The group exploits vulnerabilities in internet-facing devices like VPNs and firewalls, potentially collaborating with initial access brokers. They employ comprehensive reconnaissance using tools like SharpADWS, NetScan, and Advanced IP Scanner, capturing network traffic with netsh. The attackers disable security products through BYOVD techniques using vulnerable drivers, and deploy custom Go-based backdoors and ransomware variants. They spread laterally via GPO deployment and PsExec, encrypt files using Curve25519 and XChaCha20, and recently developed a C-based ransomware variant using AES256-GCM and RSA. The group targets multiple industries worldwide, particularly in Brazil, China, Indonesia, Taiwan, and Thailand, with attacks focusing on manufacturing, IT services, healthcare, and financial sectors.
* **Tags / Palabras clave:** `vulnerable drivers, sharkloader, zichatbot, coolclient, gpo deployment, ransomware-as-a-service, powercloud, appleseed, mgbot, encryption tactics, byovd, reversesocks, cobalt strike, network reconnaissance, custom backdoor, lateral movement`
* **Total de Armas detectadas (IoCs):** 48

### Muestra de Indicadores Críticos a bloquear (Top 5):
- **HOSTNAME**: `rsat.activedirectory.ds-lds.tools`
- **FILEHASH-MD5**: `9321a61a25c7961d9f36852ecaa86f55`
- **FILEHASH-SHA1**: `6afc6b04cf73dd461e4a4956365f25c1f1162387`
- **FILEHASH-SHA256**: `f8965fdce668692c3785afa3559159f9a18287bc0d53abb21902895a8ecf221b`
- **FILEHASH-SHA256**: `5af1dae21425dda8311a2044209c308525135e1733eeff5dd20649946c6e054c`

---

## 🛑 Campaña: Not very gentlemanly: Analyzing a zero-day exploit used to disable targets' EDRs
* **Descripción:** The Gentlemen ransomware group, which emerged in July 2025, employed a zero-day vulnerability in a bring-your-own-vulnerable-driver (BYOVD) attack to disable endpoint detection and response systems. During an incident investigated in early April, the group leveraged an obscure third-party driver named ktapi.sys from Kontron to bypass security protections. The sophisticated exploit chains multiple advanced techniques to navigate Windows exploit mitigations, including bypassing Supervisor Mode Access Prevention and Supervisor Mode Execution Prevention. The toolkit enables the attackers to call privileged kernel mode functions from user mode processes, ultimately terminating EDR processes including Windows Defender, ESET, Palo Alto Cortex XDR, and SentinelOne. The vulnerability had no prior public documentation and was previously absent from vulnerable driver blocklists.
* **Tags / Palabras clave:** `the gentlemen, edr killer, byovd, ransomware, kontron driver, zero-day, endpoint protection bypass, ktapi.sys, kernel exploit`
* **Total de Armas detectadas (IoCs):** 3

### Muestra de Indicadores Críticos a bloquear (Top 5):
- **FILEHASH-SHA256**: `7ee17efef04bb7c9de90d5210263ed6993f867e5a11f86e65e3bb1362c7de237`
- **FILEHASH-SHA256**: `9ca9432b0d29204cb5420a1a6b01533d4552130c2a8a5ecd7837efadefb4a046`
- **FILEHASH-SHA256**: `c277ae5a4dd62f51de5278790796cd2700de7f77ea17762e97729f27872d076b`

---

## 🛑 Campaña: An Analysis of ValleyRAT Infection Campaigns from Fake Installers, Japanese Malicious Emails
* **Descripción:** LevelBlue has identified two distinct ValleyRAT attack vectors: campaigns using fake installers and malicious email-based campaigns. Detection volume increased significantly from May 2025, nearly doubling in 2026. The fake installer attacks primarily target Chinese-speaking users and employ advanced techniques including Pool Party Variant 7 process injection and BYOVD methods. The malicious email campaigns target both Chinese and Japanese-speaking users, delivering ZIP archives containing EXE and DLL files that leverage DLL sideloading. The malware employs multiple evasion techniques including junk code insertion, memory size checks, sleeping duration checks, process count validation, and fileless execution using Donut-generated shellcode. ValleyRAT establishes persistence through registry modification and enables remote access capabilities for threat actors.
* **Tags / Palabras clave:** `phishing emails, process injection, fake installers, donut shellcode, japanese targets, dll sideloading, chinese targets, valleyrat`
* **Total de Armas detectadas (IoCs):** 6

### Muestra de Indicadores Críticos a bloquear (Top 5):
- **IPV4**: `154.92.16.22`
- **HOSTNAME**: `frehf.oss-cn-hongkong.aliyuncs.com`
- **FILEHASH-SHA1**: `e8be03f19ada1f5cec74b143e21d4939e781671d`
- **FILEHASH-SHA1**: `65168c8dd93b16d3b77092fb70c0fa6fba4dffcc`
- **URL**: `http://154.92.16.22/xz.bin`

---

## 🛑 Campaña: A stealthy RAT burrowing deep into Android devices
* **Descripción:** BTMOB is an Android remote access trojan that evolved from SpySolr malware and poses significant threats beyond traditional banking trojans. The malware combines phishing-led delivery with an APK builder interface that enables rapid payload generation without coding skills. Distributed through fake app stores impersonating streaming services, cryptocurrency platforms, and government agencies, BTMOB abuses Android Accessibility Services to gain elevated permissions. Marketed as malware-as-a-service with a reported $5,000 lifetime license, it provides adversaries with capabilities to exfiltrate sensitive data, capture screenshots, record device activity, and establish remote control. The tool's customizable phishing lures have been adapted for specific regions, including campaigns impersonating Argentine tax authorities, making it a rapidly evolving threat with global reach.
* **Tags / Palabras clave:** `android rat, latin america, phishing campaigns, spysolr evolution, apk builder, remote access, brazil, accessibility abuse, malware-as-a-service, spysolr, btmob`
* **Total de Armas detectadas (IoCs):** 99

### Muestra de Indicadores Críticos a bloquear (Top 5):
- **FILEHASH-MD5**: `25e3c200de4868d754a3b4f4f09ec2bf`
- **FILEHASH-SHA256**: `0a542751724a432a8448324613e0ce10393e41739a1800cbb7d5a2c648fcdc35`
- **DOMAIN**: `arbsniper.com`
- **FILEHASH-SHA256**: `aa56f350882ce63429c6626567487b041f06168bb60f4fc371a262eabadfa660`
- **FILEHASH-SHA256**: `0628ad6d1fd836b13b22e75fa169502d8ce78b7ad20f0261eb5151da98437bca`

---

## 🛑 Campaña: India's government and energy sectors targeted with ZOHOMURK and MINIRECON
* **Descripción:** Mustang Panda orchestrated two concurrent espionage campaigns targeting Indian government entities and hydropower infrastructure between May and June 2026. The campaigns leveraged DLL sideloading via legitimate executables to deploy newly identified malware including SHARDLOADER, MINIRECON, and ZOHOMURK. MINIRECON represents an evolution of Toneshell with WebSocket-based command-and-control capabilities, while ZOHOMURK abuses Zoho WorkDrive cloud services for C2 communications and data exfiltration. Distribution occurred through spear-phishing with lures themed around India-Taiwan cooperation agreements and hydropower projects. The activity demonstrates code overlaps with previous tooling, infrastructure proximity to known operations, and targeting patterns aligned with Chinese strategic intelligence collection priorities. Multiple compromised government systems were identified, with coordination conducted through CERT-In for victim notification and remediation.
* **Tags / Palabras clave:** `india, government targeting, websocket, minirecon, zohomurk, shadowpad, cloud c2, hydropower, espionage, pubload, shardloader, toneshell, zoho workdrive, dll sideloading`
* **Total de Armas detectadas (IoCs):** 17

### Muestra de Indicadores Críticos a bloquear (Top 5):
- **FILEHASH-MD5**: `c04c947efdfdd9ce24617903b6746a83`
- **FILEHASH-SHA1**: `43d646eda4166261eb1433c7599bf5cc9129a4f1`
- **FILEHASH-SHA256**: `fcf4efa82d477c924d42cc6b71aa672ab2381ca256769925ae34dabe2e77e025`
- **FILEHASH-SHA256**: `390148f5157c0f6b337ff19d162c3c2ee3e6d782fdfbe11fb1e411c0684fd33b`
- **FILEHASH-SHA256**: `f53fd0626404a129dcddb8ee7589387dd7bda7999814e0df46c670af6b3da5f5`

---

