# Reporte de CVEs Críticos Recientes

**Fecha de generación:** 2026-07-02 13:18:13 UTC
**Rango analizado:** Últimos 30 días (2026-06-02 al 2026-07-02)
**Total encontrados:** 153

---

## [CVE-2026-10611](https://nvd.nist.gov/vuln/detail/CVE-2026-10611)
* **Puntuación CVSS v3:** `10.0` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-02T14:16:44.867
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`

### Descripción
An authentication bypass vulnerability exists in MISP when LDAP mixed authentication is enabled with OTP enforcement. In deployments configured with LdapAuth.mixedAuth=true and Security.require_otp=true, users authenticated through an authentication plugin, such as LDAP, may have their authenticated session established during the application beforeFilter phase before the normal login flow enforces the OTP challenge.



As a result, an attacker with valid primary authentication credentials could bypass the required OTP step by authenticating through the plugin-backed login flow and then directly accessing another application URL instead of completing the OTP verification page. This allows access to the application as the affected user without providing a valid TOTP, HOTP, or email OTP code.



The issue affects configurations where plugin-based authentication is enabled and OTP is expected to be mandatory. The fix ensures that OTP requirements are checked immediately after plugin authentication and before the user session is established, redirecting users to the appropriate OTP challenge when required.

---

## [CVE-2026-42074](https://nvd.nist.gov/vuln/detail/CVE-2026-42074)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-02T17:16:32.073
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
OpenClaude is an open-source coding-agent command line interface for cloud and local model providers. Prior to version 0.5.1, the dangerouslyDisableSandbox parameter is exposed as part of the BashTool input schema, meaning the LLM (an untrusted principal per the project's own threat model) can set it to true in any tool_use response. Combined with the default allowUnsandboxedCommands: true setting, a prompt-injected model can escape the sandbox for any arbitrary command, achieving full host-level code execution. This issue has been patched in version 0.5.1.

---

## [CVE-2026-5241](https://nvd.nist.gov/vuln/detail/CVE-2026-5241)
* **Puntuación CVSS v3:** `9.6` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-03T14:16:46.337
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H`

### Descripción
A vulnerability in the LightGlue model loading path of huggingface/transformers version 5.2.0 allows an attacker-controlled model repository to execute arbitrary code during model initialization. The issue arises because the `trust_remote_code` parameter, intended to prevent remote code execution, is overridden by untrusted serialized configuration data in a nested code path. Specifically, when loading a LightGlue model using `AutoModel.from_pretrained()` with `trust_remote_code=False`, the `LightGlueConfig` reads the `trust_remote_code` value from the untrusted `config.json` file and propagates it into nested `AutoConfig.from_pretrained()` calls. This results in the execution of attacker-provided Python modules, even when the victim explicitly disables remote code execution. The vulnerability poses a high risk for environments such as API inference servers, research notebooks, CI/CD pipelines, and model evaluation workers, potentially leading to credential theft, lateral movement, or persistence/backdoor deployment.

---

## [CVE-2026-49185](https://nvd.nist.gov/vuln/detail/CVE-2026-49185)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-04T04:17:15.387
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
The FieldX MDM adb messaging topic passes unverified payloads directly into Runtime.exec(), allowing command/instruction injection.

---

## [CVE-2026-49186](https://nvd.nist.gov/vuln/detail/CVE-2026-49186)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-04T04:17:15.550
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
The local MQTT broker does not enforce topic-level Access Control Lists (ACLs). This allows any client to subscribe using wildcard characters (# or +) to enumerate hidden network devices or publish rogue control commands.

---

## [CVE-2026-49188](https://nvd.nist.gov/vuln/detail/CVE-2026-49188)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-04T06:16:24.583
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
The ai_cmd utility executes with full root permissions. It pipes socket inputs directly to popen(), paving the way for unauthenticated users to execute arbitrary root commands.

---

## [CVE-2026-49191](https://nvd.nist.gov/vuln/detail/CVE-2026-49191)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-04T07:16:27.013
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
The production build of the M3WebServer hard-codes its backend API keys, which can be easily intercepted through verbose error handling pages.

---

## [CVE-2026-50208](https://nvd.nist.gov/vuln/detail/CVE-2026-50208)
* **Puntuación CVSS v3:** `9.4` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-04T09:16:29.277
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:L`

### Descripción
High-risk TrustAllCerts routines disable standard TLS certificate validation. Combined with hard-coded DES symmetric encryption keys, a Man-in-the-Middle (MITM) actor could decrypt network traffic.

---

## [CVE-2026-50211](https://nvd.nist.gov/vuln/detail/CVE-2026-50211)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-04T09:16:29.700
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Leftover engineering diagnostics and factory-level diagnostic software remain exposed on retail builds, giving malicious apps write privileges to internal NVRAM registers.

---

## [CVE-2026-50214](https://nvd.nist.gov/vuln/detail/CVE-2026-50214)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-04T10:16:39.850
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
The /v1/Plan service relies entirely on a shared global API token for full administrative management, allowing arbitrary creation of zero-cost network access plans.

---

## [CVE-2026-50225](https://nvd.nist.gov/vuln/detail/CVE-2026-50225)
* **Puntuación CVSS v3:** `9.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-04T10:16:40.123
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:H`

### Descripción
The registration path /v1/account/register provides no bot mitigation mechanisms, allowing malicious automated systems to flood the database.

---

## [CVE-2026-48040](https://nvd.nist.gov/vuln/detail/CVE-2026-48040)
* **Puntuación CVSS v3:** `9.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-04T18:16:31.220
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`

### Descripción
The netty incubator codec.bhttp is a java language binary http parser. The library implements Oblivious HTTP (RFC 9458) using BoringSSL's HPKE C library via JNI. When deriving native memory addresses for cryptographic operations versions prior to 0.0.22.Final provide a fallback path for direct ByteBufs that do not expose their memory address through `hasMemoryAddress()`. This fallback occurs when `sun.misc.Unsafe` is unavailable to Netty — for example, when the JVM is started with `-Dio.netty.noUnsafe=true`, when a SecurityManager restricts Unsafe access, or when running on non-HotSpot JVMs. In these configurations, Netty's default `PooledByteBufAllocator` returns `PooledDirectByteBuf` instances for which `hasMemoryAddress()` returns false.  Under the enabling JVM configuration, an unauthenticated network attacker can cause the OHTTP gateway to corrupt memory belonging to other concurrent connections and disclose the contents of adjacent pooled direct buffers by triggering cryptographic operations with crafted OHTTP requests. The corruption occurs regardless of whether the AEAD tag verification succeeds, as BoringSSL zeroizes the output buffer on failure. The information disclosure path provides the attacker with the encryption key needed to extract the leaked data. This violates the confidentiality and integrity of all connections sharing the same Netty buffer arena. Version 0.0.22.Final fixes the issue.

---

## [CVE-2026-50292](https://nvd.nist.gov/vuln/detail/CVE-2026-50292)
* **Puntuación CVSS v3:** `7.4` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-04T18:16:32.530
* **Vector de Ataque:** `CVSS:3.1/AV:L/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
In libinput before 1.30.4 and 1.31.x before 1.31.3, libinput-device-group unescaped phys output can inject udev properties leading to arbitrary root code execution

---

## [CVE-2026-10931](https://nvd.nist.gov/vuln/detail/CVE-2026-10931)
* **Puntuación CVSS v3:** `9.6` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-04T23:16:55.550
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H`

### Descripción
Use after free in FileSystem in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: High)

---

## [CVE-2026-10966](https://nvd.nist.gov/vuln/detail/CVE-2026-10966)
* **Puntuación CVSS v3:** `9.6` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-04T23:16:59.723
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H`

### Descripción
Inappropriate implementation in Codecs in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to potentially perform a sandbox escape via a crafted video file. (Chromium security severity: High)

---

## [CVE-2026-10971](https://nvd.nist.gov/vuln/detail/CVE-2026-10971)
* **Puntuación CVSS v3:** `9.6` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-04T23:17:00.290
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H`

### Descripción
Insufficient validation of untrusted input in Printing in Google Chrome on Windows prior to 149.0.7827.53 allowed a remote attacker who had compromised the renderer process to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: High)

---

## [CVE-2026-10972](https://nvd.nist.gov/vuln/detail/CVE-2026-10972)
* **Puntuación CVSS v3:** `9.6` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-04T23:17:00.400
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H`

### Descripción
Use after free in Ozone in Google Chrome on Linux prior to 149.0.7827.53 allowed a remote attacker to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: High)

---

## [CVE-2026-10974](https://nvd.nist.gov/vuln/detail/CVE-2026-10974)
* **Puntuación CVSS v3:** `9.6` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-04T23:17:00.623
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H`

### Descripción
Insufficient validation of untrusted input in ANGLE in Google Chrome prior to 149.0.7827.53 allowed a remote attacker to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: High)

---

## [CVE-2026-10990](https://nvd.nist.gov/vuln/detail/CVE-2026-10990)
* **Puntuación CVSS v3:** `9.6` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-04T23:17:02.427
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H`

### Descripción
Use after free in Glic in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who had compromised the renderer process to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: Medium)

---

## [CVE-2026-11002](https://nvd.nist.gov/vuln/detail/CVE-2026-11002)
* **Puntuación CVSS v3:** `9.6` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-04T23:17:03.943
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H`

### Descripción
Use after free in Autofill in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who had compromised the renderer process to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: Medium)

---

## [CVE-2026-11029](https://nvd.nist.gov/vuln/detail/CVE-2026-11029)
* **Puntuación CVSS v3:** `9.6` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-04T23:17:06.923
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H`

### Descripción
Insufficient validation of untrusted input in Drag and Drop in Google Chrome on Android prior to 149.0.7827.53 allowed a remote attacker who had compromised the renderer process to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: Medium)

---

## [CVE-2026-11113](https://nvd.nist.gov/vuln/detail/CVE-2026-11113)
* **Puntuación CVSS v3:** `9.6` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-04T23:17:16.950
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H`

### Descripción
Insufficient validation of untrusted input in ANGLE in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who had compromised the renderer process to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: Medium)

---

## [CVE-2026-11120](https://nvd.nist.gov/vuln/detail/CVE-2026-11120)
* **Puntuación CVSS v3:** `9.6` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-04T23:17:17.790
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H`

### Descripción
Insufficient validation of untrusted input in Enterprise Reporting in Google Chrome prior to 149.0.7827.53 allowed a remote attacker who had compromised the renderer process to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: Medium)

---

## [CVE-2026-48567](https://nvd.nist.gov/vuln/detail/CVE-2026-48567)
* **Puntuación CVSS v3:** `10.0` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-04T23:17:32.677
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:N/I:H/A:H`

### Descripción
Authentication bypass by spoofing in Azure HorizonDB allows an unauthorized attacker to elevate privileges over a network.

---

## [CVE-2026-48907](https://nvd.nist.gov/vuln/detail/CVE-2026-48907)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-05T08:16:30.797
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
A vulnerability in the JCE editor extension for Joomla allows the creation of new editor profiles for unauthenticated users, ultimately resulting in PHP code upload and execution.

---

## [CVE-2026-46389](https://nvd.nist.gov/vuln/detail/CVE-2026-46389)
* **Puntuación CVSS v3:** `10.0` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-05T19:16:32.703
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`

### Descripción
UDS Identity Config builds the Keycloak configuration image (realm, plugins, theme, truststore, JARs) consumed by UDS Core's Identity deployment. In versions 0.11.0 through 0.26.0, a logic error in the `client-kubernetes-secret` Keycloak client authenticator (shipped by `uds-identity-config` and consumed by UDS Core) causes the submitted `client_secret` to be overwritten with the mounted Kubernetes secret before comparison. An attacker who can reach the Keycloak token endpoint and knows a `client_id` using this authenticator can authenticate as that client with any `client_secret` value and obtain OAuth2 tokens scoped to the client's service account. In the case of the `uds-operator` client this token can be used to registry/modify other clients. Version 0.26.1 patches the issue.

---

## [CVE-2026-11414](https://nvd.nist.gov/vuln/detail/CVE-2026-11414)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-05T20:17:29.033
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
A hard-coded cryptographic key is used by Altium Enterprise Server to sign file download URLs in the Vault service. Because the key is identical across all installations, an unauthenticated network attacker who can reach the server can forge valid download signatures and retrieve files from the Vault storage area without any authentication, session, or credentials.


A separate path traversal vulnerability in the same download endpoint allows the configured storage root to be escaped, enabling reads of arbitrary files on the server filesystem. Combined, these issues allow an unauthenticated attacker to obtain sensitive server configuration and key material, which can lead to full server compromise. The vulnerability can be chained with CVE-2026-9152 to enumerate and bulk-download stored content. Altium 365 cloud deployments are not impacted in practice, as file storage uses object storage rather than the local filesystem.

---

## [CVE-2026-11420](https://nvd.nist.gov/vuln/detail/CVE-2026-11420)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-05T20:17:29.350
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Two path traversal vulnerabilities in the Network Installation Service (NIS) of Altium Enterprise Server allow an unauthenticated network attacker to write arbitrary files to any writable location on the server filesystem and to read package archive files from the server. No authentication, session, or credentials are required.




Because content-controlled files can be written to web-accessible directories, or used to overwrite application binaries or configuration files, exploitation can be escalated to remote code execution in the context of the service account, and can disclose deployment package contents. Altium 365 cloud deployments are not affected, as the Network Installation Service is not part of the cloud offering.

---

## [CVE-2026-45777](https://nvd.nist.gov/vuln/detail/CVE-2026-45777)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-05T20:17:32.687
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
OpenXDMoD is an open framework for collecting and analyzing HPC metrics. Starting in version 9.5.0 and prior to version 11.0.3, an attacker can remotely execute arbitrary system commands on the web server hosting Open XDMoD with the privileges of the web server process. This could allow an attacker to read or modify application data, alter system configuration, or disrupt service availability. All deployments of Open XDMoD versions 9.5.0 through 11.0.2 (inclusive) are impacted. This issue was reported privately on 2026-04-06, and at this time there is no evidence that this vulnerability has been exploited in the wild. The vulnerability was patched in Open XDMoD 11.0.3 on 2026-05-12. As a workaround, apply the patch manually.

---

## [CVE-2026-45779](https://nvd.nist.gov/vuln/detail/CVE-2026-45779)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-05T20:17:33.023
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
OpenXDMoD is an open framework for collecting and analyzing HPC metrics. An SQL injection vulnerability exists in Open XDMoD versions prior to 10.0.3 that allows an unauthenticated remote attacker to execute arbitrary SQL statements. Exploitation requires no authentication or user interaction and can result in complete compromise of the underlying database. All deployments of Open XDMoD prior to 10.0.3 are impacted. This issue was discovered on 2023-08-03 and patched on 2023-08-04. At this time there is no evidence that this vulnerability has been exploited in the wild. The vulnerability was patched in Open XDMoD 10.0.3 on 2023-08-04. As a workaround, apply the patch manually.

---

## [CVE-2026-42861](https://nvd.nist.gov/vuln/detail/CVE-2026-42861)
* **Puntuación CVSS v3:** `9.6` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-08T16:16:39.503
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:N`

### Descripción
Flowise is a drag & drop user interface to build a customized large language model flow. Prior to version 3.1.2, a mass assignment vulnerability exists in the variable update endpoint of FlowiseAI. The endpoint allows authenticated users to modify server-controlled properties such as workspaceId, createdDate, and updatedDate when updating a variable resource. Due to missing server-side validation and authorization checks, an attacker can manipulate the workspaceId field and reassign variables to arbitrary workspaces. This behavior may break tenant isolation in multi-workspace environments. This issue has been patched in version 3.1.2.

---

## [CVE-2026-46440](https://nvd.nist.gov/vuln/detail/CVE-2026-46440)
* **Puntuación CVSS v3:** `9.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-08T16:16:41.043
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`

### Descripción
Flowise is a drag & drop user interface to build a customized large language model flow. Prior to version 3.1.2, the checkBasicAuth endpoint validates credentials in plaintext without rate limiting and with direct comparison. This issue has been patched in version 3.1.2.

---

## [CVE-2026-46441](https://nvd.nist.gov/vuln/detail/CVE-2026-46441)
* **Puntuación CVSS v3:** `9.6` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-08T16:16:41.190
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:N`

### Descripción
Flowise is a drag & drop user interface to build a customized large language model flow. Prior to version 3.1.2, a mass assignment vulnerability exists in the assistant update endpoint of FlowiseAI. The endpoint allows authenticated users to modify server-controlled properties such as workspaceId, createdDate, and updatedDate when updating an assistant resource. Due to missing server-side validation and authorization checks, an attacker can manipulate the workspaceId field and reassign assistants to arbitrary workspaces. This breaks tenant isolation in multi-workspace environments. This issue has been patched in version 3.1.2.

---

## [CVE-2026-46442](https://nvd.nist.gov/vuln/detail/CVE-2026-46442)
* **Puntuación CVSS v3:** `9.9` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-08T16:16:41.347
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H`

### Descripción
Flowise is a drag & drop user interface to build a customized large language model flow. Prior to version 3.1.2, POST /api/v1/node-custom-function lacks route-level authorization, allowing any authenticated user or API key to submit arbitrary JavaScript to the Custom JS Function node. When E2B_APIKEY is not configured — the common deployment case — Flowise executes this code inside a NodeVM sandbox. This sandbox can be escaped, allowing an attacker to reach the host process object and execute system commands via child_process. The result is authenticated remote code execution on the Flowise server host. This issue has been patched in version 3.1.2.

---

## [CVE-2026-41855](https://nvd.nist.gov/vuln/detail/CVE-2026-41855)
* **Puntuación CVSS v3:** `8.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-09T05:16:37.770
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
In an untrusted JMS environment, org.springframework.jms.support.converter.MappingJackson2MessageConverter and org.springframework.jms.support.converter.JacksonJsonMessageConverter allow arbitrary class instantiation, which can lead to unauthorized actions via gadget class deserialization.

Affected versions:
Spring Framework 7.0.0 through 7.0.7; 6.2.0 through 6.2.18; 6.1.0 through 6.1.27; 5.3.0 through 5.3.48.

---

## [CVE-2026-44083](https://nvd.nist.gov/vuln/detail/CVE-2026-44083)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-09T08:16:28.940
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
An authorization bypass through user-controlled key vulnerability has been reported to affect QuMagie. The remote attackers can then exploit the vulnerability to gain unintended privileges.

We have already fixed the vulnerability in the following version:
QuMagie 2.9.1 and later

---

## [CVE-2026-9698](https://nvd.nist.gov/vuln/detail/CVE-2026-9698)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-09T08:16:29.190
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
DBI versions before 1.648 for Perl saved errors in a limited-sized buffer.

Error messages that were returned when RaiseError, PrintError or HandleError were set were written to a 200-byte buffer without a length limit.

Attackers that can influence the error text in an application can trigger a buffer overflow.

---

## [CVE-2026-46749](https://nvd.nist.gov/vuln/detail/CVE-2026-46749)
* **Puntuación CVSS v3:** `7.5` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-09T10:16:44.410
* **Vector de Ataque:** `CVSS:3.1/AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H`

### Descripción
A vulnerability has been identified in SINEC INS (All versions < V1.0 SP2 Update 6). The affected application uses a password hashing implementation with a static, hardcoded salt shared across all users and installations, and is configured with an insufficient number of iterations. This could allow an attacker to efficiently recover user passwords using brute-force or precomputed attacks, potentially resulting in unauthorized access.

---

## [CVE-2026-10523](https://nvd.nist.gov/vuln/detail/CVE-2026-10523)
* **Puntuación CVSS v3:** `9.9` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-09T16:16:35.837
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H`

### Descripción
An Authentication Bypass vulnerability (CWE-288) in Ivanti Sentry before the R10.5.2, R10.6.2 and R10.7.1 versions allows a remote unauthenticated attacker to create arbitrary administrative accounts and obtain full administrative access

---

## [CVE-2026-47928](https://nvd.nist.gov/vuln/detail/CVE-2026-47928)
* **Puntuación CVSS v3:** `9.6` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-09T21:17:22.700
* **Vector de Ataque:** `CVSS:3.1/AV:A/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`

### Descripción
ColdFusion versions 2023.19, 2025.8 and earlier are affected by an Improper Input Validation vulnerability that could result in arbitrary code execution in the context of the current user. Exploitation of this issue does not require user interaction. Scope is changed.

---

## [CVE-2026-47929](https://nvd.nist.gov/vuln/detail/CVE-2026-47929)
* **Puntuación CVSS v3:** `8.4` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-09T21:17:22.813
* **Vector de Ataque:** `CVSS:3.1/AV:A/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H`

### Descripción
ColdFusion versions 2023.19, 2025.8 and earlier are affected by an Incorrect Authorization vulnerability that could result in arbitrary code execution in the context of the current user. A high-privileged attacker could exploit this vulnerability to gain elevated access or control over the victim's account or session. Exploitation of this issue does not require user interaction. Scope is changed.

---

## [CVE-2026-47931](https://nvd.nist.gov/vuln/detail/CVE-2026-47931)
* **Puntuación CVSS v3:** `8.4` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-09T21:17:23.050
* **Vector de Ataque:** `CVSS:3.1/AV:A/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H`

### Descripción
ColdFusion versions 2023.19, 2025.8 and earlier are affected by an Improper Input Validation vulnerability that could result in arbitrary code execution in the context of the current user. An attacker with high privileges could exploit this vulnerability to execute arbitrary code. Exploitation of this issue does not require user interaction. Scope is changed.

---

## [CVE-2026-47932](https://nvd.nist.gov/vuln/detail/CVE-2026-47932)
* **Puntuación CVSS v3:** `8.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-09T21:17:23.170
* **Vector de Ataque:** `CVSS:3.1/AV:A/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H`

### Descripción
ColdFusion versions 2023.19, 2025.8 and earlier are affected by an Improper Limitation of a Pathname to a Restricted Directory ('Path Traversal') vulnerability that could result in a Security feature bypass. An attacker could leverage this vulnerability to access unauthorized files or directories outside the intended restrictions. Exploitation of this issue requires user interaction in that a victim must open a malicious file. Scope is changed.

---

## [CVE-2025-66276](https://nvd.nist.gov/vuln/detail/CVE-2025-66276)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-10T03:16:24.730
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
QuTS hero is not affected.

We have already fixed the vulnerability in the following version:
QTS 5.2.7.3256 build 20250913 and later

---

## [CVE-2026-26240](https://nvd.nist.gov/vuln/detail/CVE-2026-26240)
* **Puntuación CVSS v3:** `9.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-10T05:16:38.987
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:H`

### Descripción
A buffer overflow vulnerability has been reported to affect File Station 5. The remote attackers can then exploit the vulnerability to modify memory or crash processes.

We have already fixed the vulnerability in the following version:
File Station 5 5.5.6.5243 and later

---

## [CVE-2026-26241](https://nvd.nist.gov/vuln/detail/CVE-2026-26241)
* **Puntuación CVSS v3:** `9.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-10T05:16:39.103
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:H`

### Descripción
A buffer overflow vulnerability has been reported to affect File Station 5. The remote attackers can then exploit the vulnerability to modify memory or crash processes.

We have already fixed the vulnerability in the following version:
File Station 5 5.5.6.5243 and later

---

## [CVE-2026-41699](https://nvd.nist.gov/vuln/detail/CVE-2026-41699)
* **Puntuación CVSS v3:** `8.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-11T07:16:28.280
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Spring for GraphQL applications are vulnerable to Unsafe Deserialization when processing paginated GraphQL queries. An attacker can craft a malicious GraphQL request that can lead to Remote Code Execution when the application exposes a paginated (Connection) field and the classpath contains specific classes that can be leveraged during deserialization.

Affected versions:
Spring for GraphQL 2.0.0 through 2.0.3; 1.4.0 through 1.4.5; 1.3.0 through 1.3.8.

---

## [CVE-2026-49261](https://nvd.nist.gov/vuln/detail/CVE-2026-49261)
* **Puntuación CVSS v3:** `10.0` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-11T18:16:26.553
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`

### Descripción
MariaDB server is a community developed fork of MySQL server. Versions 10.6.1 through 10.6.26, 10.11.1 through 10.11.17, 11.4.1 through 11.4.11, 11.8.1 through 11.8.7, and 12.3.1 with  `wsrep_notify_cmd` enabled would execute shell commands embedded in the name of the joiner node. This is fixed in 10.6.27, 10.11.18, 11.4.12, 11.8.8, and 12.3.2. As a workaround, anyone who cannot upgrade now should disable `wsrep_notify_cmd`.

---

## [CVE-2026-45177](https://nvd.nist.gov/vuln/detail/CVE-2026-45177)
* **Puntuación CVSS v3:** `9.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-11T19:16:41.903
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`

### Descripción
Idira Secrets Manager SaaS Edge versions prior to 1.8 exhibit improper access control within its internal authentication components. A remote, unauthenticated attacker could exploit this by submitting a specially crafted request. Under specific circumstances, this could allow the attacker to manipulate internal validation mechanisms, potentially leading to a bypass of identity verification and the unauthorized acquisition of an access token. CyberArk Security Bulletin: CA26-20

---

## [CVE-2026-49875](https://nvd.nist.gov/vuln/detail/CVE-2026-49875)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-12T10:16:22.340
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Apache CXF's EndpointReferenceUtils and W3CMultiSchemaFactory classes construct a SAXParserFactory without the necessary JAXP hardening configurations, enabling out-of-band (OOB) 
external entity resolution. Users are recommended to upgrade to versions 4.2.2 or 4.1.7, which fix this issue.

---

## [CVE-2026-50627](https://nvd.nist.gov/vuln/detail/CVE-2026-50627)
* **Puntuación CVSS v3:** `9.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-12T10:16:22.587
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H`

### Descripción
The JwtAccessTokenValidator class in Apache CXF fails to validate the 'aud' (Audience) claims of incoming JWT access tokens. This allows a JWT issued for one Resource Server to be successfully replayed against a completely different Resource Server, leading to Token Confusion/Routing attacks. Users are recommended to upgrade to versions 4.2.2 or 4.1.7, which fixes this issue.

---

## [CVE-2026-50628](https://nvd.nist.gov/vuln/detail/CVE-2026-50628)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-12T10:16:22.710
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
A logic error in OAuthRequestFilter rejects legitimate requests originating from the bound IP address, while blindly allowing requests from any other IP address. Enabling this

security feature inadvertently creates an inverse security check. Users are recommended to upgrade to versions 4.2.2 or 4.1.7, which fixes this issue.

---

## [CVE-2026-45674](https://nvd.nist.gov/vuln/detail/CVE-2026-45674)
* **Puntuación CVSS v3:** `8.7` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-12T15:16:27.550
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:N`

### Descripción
Netty is a network application framework for development of protocol servers and clients. Prior to versions 4.1.135.Final and 4.2.15.Final, Netty's DnsResolveContext fails to validate the origin (bailiwick) of CNAME records in DNS responses. Versions 4.1.135.Final and 4.2.15.Final patch the issue.

---

## [CVE-2026-47691](https://nvd.nist.gov/vuln/detail/CVE-2026-47691)
* **Puntuación CVSS v3:** `8.7` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-12T16:16:30.310
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:N`

### Descripción
Netty is a network application framework for development of protocol servers and clients. Prior to versions 4.1.135.Final and 4.2.15.Final, Netty's `DnsResolveContext` insufficiently validates the bailiwick of NS records, enabling DNS Cache Poisoning. An attacker controlling an authoritative name server for a subdomain can poison the cache for parent domains (like `.co.uk`). In `io.netty.resolver.dns.DnsResolveContext.AuthoritativeNameServerList#add` method accepts any NS record from the AUTHORITY section as long as the record's name is a suffix of the questionName. Subsequently, the `handleWithAdditional` method caches the associated A records from the ADDITIONAL section directly into the `authoritativeDnsServerCache` under the parent domain's key. This bypasses standard bailiwick rules, where a server authoritative for a subdomain should not be trusted to provide authoritative records for its parent. The poisoned cache is then used for all future resolutions under the parent domain's key. Versions 4.1.135.Final and 4.2.15.Final patch the issue.

---

## [CVE-2026-44170](https://nvd.nist.gov/vuln/detail/CVE-2026-44170)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-12T18:16:33.853
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
MariaDB server is a community developed fork of MySQL server. From versions 10.6.1 to before 10.6.26, 10.11.1 to before 10.11.17, 11.4.1 to before 11.4.11, 11.8.1 to before 11.8.7, and 12.3.1, MariaDB on WIndows with installed CONNECT engine and enabled REST support interpolated table HTTP attribute into the curl command line without proper sanitizing. This allows the user to execute shell commands on the server. This issue has been patched in versions 10.6.26, 10.11.17, 11.4.11, 11.8.7, and 12.3.2.

---

## [CVE-2026-44172](https://nvd.nist.gov/vuln/detail/CVE-2026-44172)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-12T18:16:34.123
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
MariaDB server is a community developed fork of MySQL server. In versions 3.3.18 and 3.4.8, an application that was taking non-validated user input, escaping it with mysql_real_escape_string() and sending it to the database using text protocol and big5 character set was vulnerable to SQL injections, even though mysql_real_escape_string() was supposed to prevent them. This issue has been patched in versions 3.3.19 and 3.4.9.

---

## [CVE-2026-53407](https://nvd.nist.gov/vuln/detail/CVE-2026-53407)
* **Puntuación CVSS v3:** `8.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-12T19:16:29.973
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N`

### Descripción
Improper Authorization in Handler for Custom URL Scheme in Zoom Workplace before version 7.0.4 for Android and before 7.0.3 for iOS may allow an unauthenticated user to conduct an escalation of privilege via network access.

---

## [CVE-2026-9258](https://nvd.nist.gov/vuln/detail/CVE-2026-9258)
* **Puntuación CVSS v3:** `6.5` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-16T00:16:35.460
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N`

### Descripción
Improper validation of SSH host keys in Canon EOS Network Setting Tool Version 1.5.0 or earlier

---

## [CVE-2026-9259](https://nvd.nist.gov/vuln/detail/CVE-2026-9259)
* **Puntuación CVSS v3:** `6.5` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-16T00:16:35.623
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:N/A:N`

### Descripción
Improper validation of server certificates in Canon EOS Network Setting Tool Version 1.5.0 or earlier

---

## [CVE-2026-9260](https://nvd.nist.gov/vuln/detail/CVE-2026-9260)
* **Puntuación CVSS v3:** `6.2` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-16T00:16:35.757
* **Vector de Ataque:** `CVSS:3.1/AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N`

### Descripción
Use of hard-coded cryptographic keys in Canon EOS Network Setting Tool Version 1.5.0 or earlier

---

## [CVE-2026-9261](https://nvd.nist.gov/vuln/detail/CVE-2026-9261)
* **Puntuación CVSS v3:** `6.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-16T00:16:35.887
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:U/C:H/I:H/A:N`

### Descripción
Use of weak SSH cryptographic algorithms in Canon EOS Network Setting Tool Version 1.5.0 or earlier

---

## [CVE-2026-12293](https://nvd.nist.gov/vuln/detail/CVE-2026-12293)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-16T13:16:29.553
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Use-after-free in the Graphics: WebGPU component. This vulnerability was fixed in Firefox 152 and Thunderbird 152.

---

## [CVE-2026-53861](https://nvd.nist.gov/vuln/detail/CVE-2026-53861)
* **Puntuación CVSS v3:** `6.6` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-16T19:17:04.027
* **Vector de Ataque:** `CVSS:3.1/AV:L/AC:L/PR:L/UI:R/S:U/C:H/I:H/A:N`

### Descripción
OpenClaw before 2026.5.6 contains an allowlist bypass vulnerability in the macOS Swift exec feature that misses combined POSIX inline-command flags. Attackers can execute shell content outside the intended allowlist check by using combined flag forms, potentially allowing unauthorized command execution depending on operator configuration.

---

## [CVE-2026-0126](https://nvd.nist.gov/vuln/detail/CVE-2026-0126)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-16T20:16:23.547
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
In WC-Radio, there is a possible out of bounds write due to a missing bounds check. This could lead to remote code execution with no additional execution privileges needed. User interaction is not needed for exploitation.

---

## [CVE-2026-48776](https://nvd.nist.gov/vuln/detail/CVE-2026-48776)
* **Puntuación CVSS v3:** `4.2` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-17T10:55:15.113
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:U/C:L/I:L/A:N`

### Descripción
LangGraph Python SDK is used to connect to running LangGraph API servers, manage assistants, threads and stream runs from Python applications. Versions 0.3.14 and prior have unsafe URL path construction through unsanitized caller-supplied identifier values used in HTTP request paths for resource operations. Without sanitization of those values, identifiers that contain characters with special meaning in URL paths could cause the resulting request to address a different resource (and potentially a different resource type) than the SDK method's call site indicates. In deployments where the SDK receives identifier values that originate from untrusted sources, this could result in unintended access, modification, or deletion of resources beyond the calling user's authorization scope. This issue is most consequential in deployments that forward end-user-supplied values directly into SDK identifier parameters without first validating them against an expected format (such as a UUID), and rely on URL-prefix-based authorization at an upstream layer (reverse proxy, edge gateway, WAF), where the authorization decision is made on the SDK call's intended path rather than on the final delivered request path. The issue has been fixed in version 0.3.15.

---

## [CVE-2025-59872](https://nvd.nist.gov/vuln/detail/CVE-2025-59872)
* **Puntuación CVSS v3:** `4.3` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-17T13:19:15.180
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:U/C:L/I:N/A:N`

### Descripción
HCL ZIE for Web is affetced by an Unrestricted File Upload vulnerability, If the server is configured to execute code, then it may be possible to obtain command execution on the server by uploading a file known as a web shell, which allows you to execute arbitrary code or operating system commands. For this attack to be successful, the file needs to be uploaded inside the Webroot, and the server must be configured to execute the code

---

## [CVE-2026-32966](https://nvd.nist.gov/vuln/detail/CVE-2026-32966)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-17T13:20:16.097
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
DataSource API Missing Authorization Check Leads to Arbitrary Data Source Metadata Disclosure in Apache DolphinScheduler.

This issue affects Apache DolphinScheduler: before 3.4.2.

Users are recommended to upgrade to version 3.4.2, which fixes the issue.

---

## [CVE-2026-32967](https://nvd.nist.gov/vuln/detail/CVE-2026-32967)
* **Puntuación CVSS v3:** `9.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-17T13:20:16.233
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`

### Descripción
Incorrect Authorization vulnerability of `/v2` experimental interface in Apache DolphinScheduler.

This issue affects Apache DolphinScheduler: before 3.4.2.

Users are recommended to upgrade to version 3.4.2, which fixes the issue.

---

## [CVE-2026-49268](https://nvd.nist.gov/vuln/detail/CVE-2026-49268)
* **Puntuación CVSS v3:** `9.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-17T14:17:56.903
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`

### Descripción
A remote attacker can inject LDAP special characters into the Distinguished Name (DN) construction in DefaultLdapRealm class. User-supplied username input is directly concatenated into the LDAP DN template without any escaping of RFC 2253 special characters. This allows an attacker to manipulate the DN structure used for LDAP bind authentication, potentially bypassing authentication or impersonating other users.

This issue affects all Apache Shiro versions through 2.2.0, and 3.0.0-alpha-1 when using DefaultLdapRealm
Upgrade to Apache Shiro 2.2.1 or 3.0.0-alpha-2 or later, which fixes the issue.

---

## [CVE-2026-12569](https://nvd.nist.gov/vuln/detail/CVE-2026-12569)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-18T01:18:12.040
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
A critical remote code execution (RCE) vulnerability has been reported in PTC Windchill PDMlink and PTC FlexPLM. The vulnerability may be exploited through the deserialization of untrusted data.   *  This advisory also applies to all CPS versions
  *  The identified vulnerability also impacts Windchill and FlexPLM releases prior to 11.0 M030

---

## [CVE-2026-8024](https://nvd.nist.gov/vuln/detail/CVE-2026-8024)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-18T14:17:35.190
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
A remote, unauthenticated attacker may exploit a deserialization of untrusted data vulnerability in ibaPDA or ibaDatCoordinator to gain full access to the affected systems.

---

## [CVE-2026-55203](https://nvd.nist.gov/vuln/detail/CVE-2026-55203)
* **Puntuación CVSS v3:** `7.5` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-18T17:16:34.373
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:C/C:L/I:H/A:N`

### Descripción
HAProxy through 3.4.0, fixed in commit 5985276, contains an integer overflow vulnerability in the fcgi_conn structure's drl field that allows buffer misparse as new FCGI record headers. When contentLength is 65535 and paddingLength is 1 or more, the drl field wraps to 0, causing incorrect record consumption and allowing malicious FastCGI backends to desynchronize the FCGI framing parser, potentially causing request routing errors, response smuggling, or memory safety issues.

---

## [CVE-2026-43994](https://nvd.nist.gov/vuln/detail/CVE-2026-43994)
* **Puntuación CVSS v3:** `8.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-18T21:16:28.630
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Coturn is a free open source implementation of TURN and STUN Server. Versions prior to 4.10.0 contain a stack buffer overflow in decode_oauth_token_gcm(). A uint16_t nonce_len field read from an attacker-supplied OAuth access token (0-65535) is passed directly to memcpy() as the copy length into a 256-byte stack buffer (oauth_encrypted_block.nonce[256]) without bounds checking. The overflow occurs before AES-GCM authentication is verified, the attacker does not need to know the OAuth key or produce a valid AES-GCM token. Up to 735 bytes of attacker-controlled data are written past the buffer, may corrupt adjacent stack data, including control-flow data depending on compiler, ABI, and mitigations. Requires --oauth mode (non-default). This may provide a plausible RCE primitive depending on exploit mitigations; because coturn is widely deployed for WebRTC TURN/STUN and --oauth is commonly recommended, impact can be broad. This issue has been fixed in version 4.10.0.

---

## [CVE-2026-50242](https://nvd.nist.gov/vuln/detail/CVE-2026-50242)
* **Puntuación CVSS v3:** `10.0` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-19T13:16:36.987
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`

### Descripción
In JetBrains Hub before 2026.1.13757,
2025.3.148033,
2025.2.148048,
2025.1.148120,
2024.3.148430,
2024.2.148429 authentication bypass via direct database access leading to administrative access was possible

---

## [CVE-2026-39999](https://nvd.nist.gov/vuln/detail/CVE-2026-39999)
* **Puntuación CVSS v3:** `9.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-19T14:16:21.950
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`

### Descripción
Authentication Bypass by Spoofing vulnerability in Apache APISIX.

The attacker can completely bypass authentication capitalising on certain configurations of jwt-auth plugin.
This issue affects Apache APISIX: from v2.2 through v3.16.0.

Users are recommended to upgrade to version v3.17.0, which fixes the issue.

---

## [CVE-2026-44087](https://nvd.nist.gov/vuln/detail/CVE-2026-44087)
* **Puntuación CVSS v3:** `9.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-19T14:16:22.200
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`

### Descripción
Insufficient Verification of Data Authenticity vulnerability in Apache APISIX.

The openid-connect plugin under default configuration has an attack surface that allows the attacker to spoof identity headers allowing the attacker to get unauthorized access the protected resources.
This issue affects Apache APISIX: from 2.3 through 3.16.0.

Users are recommended to upgrade to version 3.17.0, which fixes the issue.

---

## [CVE-2026-48137](https://nvd.nist.gov/vuln/detail/CVE-2026-48137)
* **Puntuación CVSS v3:** `9.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-19T14:16:22.680
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`

### Descripción
There is an untrusted pointer dereference vulnerability in the NI grpc-device sideband streaming API that may allow an attacker to cause an arbitrary memory dereference, potentially resulting in remote code execution.  Successful exploitation requires an attacker  to supply a specially crafted Moniker protobuf message.  This affects NI grpc-device 2.17.0 and prior versions.

---

## [CVE-2026-49230](https://nvd.nist.gov/vuln/detail/CVE-2026-49230)
* **Puntuación CVSS v3:** `9.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-19T14:16:23.427
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`

### Descripción
Improper Validation of Integrity Check Value vulnerability in Apache APISIX.

The jwe-decrypt plugin under default configuration is vulnerable to authentication bypass. 
This issue affects Apache APISIX: from 3.8.0 through 3.16.0.

Users are recommended to upgrade to version 3.17.0, which fixes the issue.

---

## [CVE-2026-49871](https://nvd.nist.gov/vuln/detail/CVE-2026-49871)
* **Puntuación CVSS v3:** `9.3` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-19T14:16:23.800
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:N`

### Descripción
Cross-Site Request Forgery (CSRF) vulnerability in the cas-auth plugin under default configurations.

This defect allows a remote attacker that manages to send a victim to a webpage controlled by them can cause the victim's browser to become authenticated as a different identity.

Actions the victim takes upstream are then attributed to attackers identity.


This issue affects Apache APISIX: from 3.0.0 through 3.16.0.

Users are recommended to upgrade to version 3.17.0, which fixes the issue.

---

## [CVE-2026-48908](https://nvd.nist.gov/vuln/detail/CVE-2026-48908)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-20T13:16:42.080
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
A vulnerability in SP Page Builder for Joomla allows unauthenticated users to upload arbitrary files, ultimately resulting in the upload and execution of PHP code.

---

## [CVE-2026-48939](https://nvd.nist.gov/vuln/detail/CVE-2026-48939)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-20T13:16:42.433
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
A vulnerability in the iCagenda extension for Joomla allows the upload of arbitrary files in the file attachment feature, ultimately resulting in PHP code upload and execution.

---

## [CVE-2026-12773](https://nvd.nist.gov/vuln/detail/CVE-2026-12773)
* **Puntuación CVSS v3:** `7.3` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-21T04:16:28.230
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L`

### Descripción
A weakness has been identified in BerriAI litellm up to 1.59.8. Affected is the function UserAPIKeyAuth of the file litellm/proxy/_experimental/mcp_server/auth/user_api_key_auth_mcp.py of the component MCP Proxy. Executing a manipulation can lead to improper authentication. The attack may be launched remotely. The exploit has been made available to the public and could be used for attacks. The vendor was contacted early about this disclosure.

---

## [CVE-2026-56367](https://nvd.nist.gov/vuln/detail/CVE-2026-56367)
* **Puntuación CVSS v3:** `3.7` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-21T14:16:25.360
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:L/I:N/A:N`

### Descripción
ImageMagick before 7.1.2-15 and 6.9.x before 6.9.13-40 contains an integer overflow in the PSB (PSD v2) RLE decoding path (ReadPSDChannelRLE in coders/psd.c) that causes a heap out-of-bounds read on 32-bit builds. Processing a crafted PSB file can lead to information disclosure or a crash.

---

## [CVE-2026-8646](https://nvd.nist.gov/vuln/detail/CVE-2026-8646)
* **Puntuación CVSS v3:** `7.4` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-22T16:16:42.360
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N`

### Descripción
IBM WebSphere Application Server 9.0 and 8.5 and IBM WebSphere Application Server - Liberty 17.0.0.3 through 26.0.0.6 are vulnerable to HTTP request smuggling. A remote attacker could smuggle a specially crafted request to the application server thereby allowing the attacker to bypass security controls, spoof identity, escalate privilege, and expose sensitive information.

---

## [CVE-2026-9006](https://nvd.nist.gov/vuln/detail/CVE-2026-9006)
* **Puntuación CVSS v3:** `7.4` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-22T16:16:43.233
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N`

### Descripción
IBM WebSphere Application Server 9.0, and 8.5 is vulnerable to server-side request forgery (SSRF) with the Ajax Proxy configured. This may allow an attacker to send unauthorized requests from the system, resulting in a security bypass or information disclosure.

---

## [CVE-2026-9072](https://nvd.nist.gov/vuln/detail/CVE-2026-9072)
* **Puntuación CVSS v3:** `8.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-22T16:16:43.500
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
IBM WebSphere Application Server and IBM WebSphere Application Server Liberty - when using Intelligent Management with the WebSphere WebServer Plug-in component - are vulnerable to remote code execution and denial of service. This vulnerability can be exploited when an attacker impersonates backend servers and sends crafted responses to the plug-in.

---

## [CVE-2026-49468](https://nvd.nist.gov/vuln/detail/CVE-2026-49468)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-22T21:16:25.190
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
LiteLLM is a proxy server (AI Gateway) to call LLM APIs in OpenAI (or native) format. Prior to 1.84.0,  This vulnerability is fixed in 1.84.0.

---

## [CVE-2026-48509](https://nvd.nist.gov/vuln/detail/CVE-2026-48509)
* **Puntuación CVSS v3:** `9.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-22T22:16:47.573
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:H`

### Descripción
MessagePack for C# is a MessagePack serializer for C#. Prior to 2.5.301 and 3.1.7, the parameterless MessagePackInputFormatter() constructor uses default serializer options, which resolve to MessagePackSerializerOptions.Standard with MessagePackSecurity.TrustedData. The formatter is designed for ASP.NET Core MVC request bodies, which commonly cross an HTTP trust boundary. This insecure default can expose applications to denial-of-service attacks that MessagePackSecurity.UntrustedData is intended to mitigate, such as hash-collision attacks against dictionary-like model properties. This vulnerability is fixed in 2.5.301 and 3.1.7.

---

## [CVE-2026-56348](https://nvd.nist.gov/vuln/detail/CVE-2026-56348)
* **Puntuación CVSS v3:** `9.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-22T22:16:52.353
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:L/A:L`

### Descripción
n8n before 2.20.0 contains a credential exfiltration vulnerability in the POST /rest/dynamic-node-parameters/options endpoint that allows authenticated users to bypass Allowed HTTP Request Domains restrictions. Attackers with credential access can cause the n8n server to issue HTTP requests with credentials to unauthorized hosts, exfiltrating sensitive authentication data.

---

## [CVE-2026-54309](https://nvd.nist.gov/vuln/detail/CVE-2026-54309)
* **Puntuación CVSS v3:** `10.0` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-23T16:17:01.860
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:L`

### Descripción
n8n is an open source workflow automation platform. Prior to 2.25.7 and 2.26.2, when @n8n/mcp-browser is run in HTTP transport mode, the MCP endpoint accepts session initialization and tool invocation requests without any authentication. Any network-reachable client, or any website visited by the user, can establish an MCP session and invoke browser-control tools. Where the n8n AI Browser Bridge extension is installed and a browser connection is active, an unauthenticated caller can access browser-control capabilities including navigation, JavaScript evaluation, and cookie and storage access against the user's real browser profile. This issue only affects instances where @n8n/mcp-browser is run with the HTTP transport (--transport http). This vulnerability is fixed in 2.25.7 and 2.26.2.

---

## [CVE-2026-54310](https://nvd.nist.gov/vuln/detail/CVE-2026-54310)
* **Puntuación CVSS v3:** `9.9` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-23T16:17:01.990
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H`

### Descripción
n8n is an open source workflow automation platform. Prior to 2.25.7 and 2.26.2, an authenticated user with permission to create or modify workflows could supply a crafted parameters to the TimescaleDB and/or legacy Postgres v1 node's allowing arbitrary SQL to be injected and executed against the connected database within the privileges of the configured database account. This vulnerability is fixed in 2.25.7 and 2.26.2.

---

## [CVE-2026-44789](https://nvd.nist.gov/vuln/detail/CVE-2026-44789)
* **Puntuación CVSS v3:** `9.9` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-23T17:16:59.290
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H`

### Descripción
n8n is an open source workflow automation platform. Prior to 1.123.43, 2.22.1, and 2.20.7, an authenticated user with permission to create or modify workflows could achieve global prototype pollution via an unvalidated pagination parameter in the HTTP Request node. Combined with other techniques this could lead to RCE on the instance. This vulnerability is fixed in 1.123.43, 2.22.1, and 2.20.7.

---

## [CVE-2026-44791](https://nvd.nist.gov/vuln/detail/CVE-2026-44791)
* **Puntuación CVSS v3:** `9.9` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-23T17:16:59.547
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H`

### Descripción
n8n is an open source workflow automation platform. Prior to 1.123.43, 2.22.1, and 2.20.7, an authenticated user with permission to create or modify workflows could bypass the patch for CVE-2026-42232 in the XML node. When combined with other nodes, this could lead to RCE on the n8n host. This vulnerability is fixed in 1.123.43, 2.22.1, and 2.20.7.

---

## [CVE-2026-44792](https://nvd.nist.gov/vuln/detail/CVE-2026-44792)
* **Puntuación CVSS v3:** `9.0` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-23T17:16:59.670
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:H`

### Descripción
n8n is an open source workflow automation platform. Prior to 1.123.43, 2.22.1, and 2.20.7, an attacker with write access to the git repository connected to an n8n Source Control configuration could commit a malicious Data Table JSON file containing a crafted column name. When an administrator performed a Source Control Pull, n8n imported the file and could lead to SQL injection on the internal PostgreSQL instance. Exploitation requires the n8n instance uses PostgreSQL as its database backend, the Source Control feature is enabled and connected to a repository the attacker can write to, and an administrator triggers a Source Control Pull. This vulnerability is fixed in 1.123.43, 2.22.1, and 2.20.7.

---

## [CVE-2026-50023](https://nvd.nist.gov/vuln/detail/CVE-2026-50023)
* **Puntuación CVSS v3:** `8.3` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-23T17:17:03.000
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:H`

### Descripción
yt-dlp is a command-line audio/video downloader. Prior to 2026.06.09, a vulnerability exists in yt-dlp that allows a remote attacker to write arbitrary OS-shortcut files (such as .desktop, .url, .webloc) to the user's filesystem, bypassing the remediation for CVE-2024-38519. The allowlist explicitly included the unsafe extensions .desktop, .url, and .webloc so that the functionality of the --write-link option (and its variants) could be preserved. These allowlist inclusions can be exploited by an attacker to write malicious OS-shortcut files in the context of a media or subtitles download. This vulnerability is fixed in 2026.06.09.

---

## [CVE-2026-50574](https://nvd.nist.gov/vuln/detail/CVE-2026-50574)
* **Puntuación CVSS v3:** `8.3` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-23T17:17:03.340
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:H`

### Descripción
yt-dlp is a command-line audio/video downloader. Prior to 2026.06.09, if aria2c is used as an external downloader for a fragmented manifest format (such as an HLS/DASH stream), yt-dlp passes insufficiently sanitized input to aria2c that allows an attacker to perform an arbitrary file write. On Windows platforms, this can lead to immediate arbitrary code execution. On non-Windows platforms, this can lead to arbitrary code execution upon the next invocation of yt-dlp. This vulnerability is fixed in 2026.06.09.

---

## [CVE-2026-54305](https://nvd.nist.gov/vuln/detail/CVE-2026-54305)
* **Puntuación CVSS v3:** `9.9` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-23T17:17:06.743
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:L`

### Descripción
n8n is an open source workflow automation platform. Prior to 1.123.55, 2.25.7, and 2.26.2, three EE endpoints used by the Dynamic Credentials feature accepted any authenticated n8n session without performing per-resource ownership or scope checks on the target workflow or credential. An authenticated user with no project membership or credential sharing relationship could enumerate credential identifiers, names, and types referenced by any private workflow in the instance, initiate an OAuth authorization flow against another user's credential to overwrite its stored tokens with tokens bound to an account they control, or revoke another user's stored credential tokens entirely. Workflows relying on a hijacked credential would subsequently execute under the attacker's OAuth identity, enabling data exfiltration to attacker-controlled external services and persistent takeover of integrations. Token revocation would break affected workflows. This vulnerability is fixed in 1.123.55, 2.25.7, and 2.26.2.

---

## [CVE-2026-54307](https://nvd.nist.gov/vuln/detail/CVE-2026-54307)
* **Puntuación CVSS v3:** `9.6` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-23T17:17:07.010
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:N`

### Descripción
n8n is an open source workflow automation platform. Prior to 1.123.55, 2.25.7, and 2.26.2, a member-level user with editor access to a shared workflow could reference credentials they do not own via specific public API endpoints. Credential ownership checks were only enforced partially leading to cross-user credential access. This issue affects instances where workflow sharing is enabled and at least one workflow has been shared with a member-level user as an Editor. This vulnerability is fixed in 1.123.55, 2.25.7, and 2.26.2.

---

## [CVE-2026-44726](https://nvd.nist.gov/vuln/detail/CVE-2026-44726)
* **Puntuación CVSS v3:** `7.4` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-23T18:17:48.623
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:N`

### Descripción
Deno is a JavaScript, TypeScript, and WebAssembly runtime. From 2.0.0 until 2.7.8, a flaw in Deno's Node.js tls compatibility layer could cause a TLS client to transmit application data in plaintext after a connection retry. When `autoSelectFamily was enabled and the first address-family attempt failed, the socket reinitialization path reused a stale TLS upgrade hook that was bound to the original, failed handle. As a result, the replacement TCP connection was never upgraded to TLS, and any data the application wrote before the secureConnect event travelled over the network unencrypted. A network attacker positioned to cause the initial connection attempt to fail (for example, by dropping IPv6 traffic on a dual-stack host) could deterministically trigger the fallback path and observe or tamper with traffic that the application believed was TLS-protected. This vulnerability is fixed in 2.7.8.

---

## [CVE-2026-54316](https://nvd.nist.gov/vuln/detail/CVE-2026-54316)
* **Puntuación CVSS v3:** `9.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-23T18:18:08.623
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`

### Descripción
Claude Code is an agentic coding tool.  From 0.2.54 until 2.1.163, because the hostname huggingface.co was pre-approved as a bare hostname for the WebFetch tool, any path on that domain—including attacker-controlled model repositories—was auto-approved without a permission prompt or being subject to --allowedTools restrictions. An attacker able to inject untrusted content into a Claude Code context could direct it to issue WebFetch requests against attacker-controlled repository files (e.g. /resolve/main/config.json), which HuggingFace counts as downloads server-side, creating a covert out-of-band channel for encoding and exfiltrating data Claude can access such as files, environment variables, or command output. Reliably exploiting this required the ability to add untrusted content into a Claude Code context window. This vulnerability is fixed in 2.1.163.

---

## [CVE-2026-53753](https://nvd.nist.gov/vuln/detail/CVE-2026-53753)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-23T19:17:07.107
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Crawl4AI is an open-source LLM friendly web crawler & scraper. Prior to 0.8.7, the _safe_eval_expression() function in the computed fields feature uses an AST validator that only blocks attributes starting with underscore. Python generator and frame object attributes (gi_frame, f_back, f_builtins) do NOT start with underscore, enabling a complete sandbox escape to achieve arbitrary code execution. The attack requires no authentication (JWT disabled by default) and is triggered via POST /crawl with a crafted extraction schema. This vulnerability is fixed in 0.8.7.

---

## [CVE-2026-48020](https://nvd.nist.gov/vuln/detail/CVE-2026-48020)
* **Puntuación CVSS v3:** `10.0` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-23T20:16:47.993
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N`

### Descripción
Traefik is an HTTP reverse proxy and load balancer. Prior to 2.11.48, 3.6.19, and 3.7.3, there is a high severity vulnerability in Traefik's StripPrefix middleware that allows an unauthenticated attacker to bypass route-level authentication and authorization. When a public router matches on a PathPrefix rule and applies the StripPrefix middleware, a request path containing .. or its percent-encoded form %2e%2e can match the public route at routing time and then, after the prefix is stripped and the path is normalized, resolve to a path served by a separate, authenticated router. As a result, an attacker can reach protected backend paths — such as admin or internal configuration endpoints — without satisfying the authentication middleware attached to the protected router. This vulnerability is fixed in 2.11.48, 3.6.19, and 3.7.3.

---

## [CVE-2026-48491](https://nvd.nist.gov/vuln/detail/CVE-2026-48491)
* **Puntuación CVSS v3:** `10.0` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-23T20:16:48.123
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N`

### Descripción
Traefik is an HTTP reverse proxy and load balancer. From 3.7.0 until 3.7.3, there is a high severity vulnerability in Traefik's domain-fronting protection (SNICheck) that allows an unauthenticated client to bypass mutual TLS enforced through wildcard router TLSOptions. When a router uses a wildcard host rule such as Host(*.example.com) with stricter TLS options (for example RequireAndVerifyClientCert), SNICheck resolves the TLS options for the HTTP Host header using exact map lookups only and never applies wildcard matching. If another permissive SNI is served on the same entrypoint, an attacker can complete the TLS handshake under the permissive options and then send an HTTP Host header targeting the wildcard-protected backend, reaching it without presenting a client certificate. This affects the regular HTTPS / HTTP-2 path and does not require HTTP/3. This vulnerability is fixed in 3.7.3.

---

## [CVE-2026-53622](https://nvd.nist.gov/vuln/detail/CVE-2026-53622)
* **Puntuación CVSS v3:** `10.0` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-23T20:16:48.777
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N`

### Descripción
Traefik is an HTTP reverse proxy and load balancer. Prior to 3.7.3, there is a critical vulnerability in Traefik's HTTP/3 (QUIC) TLS configuration selection that allows unauthenticated clients to bypass router-specific mTLS enforcement. When HTTP/3 is enabled on an entrypoint, the TLS handshake selects the applicable TLS configuration through an exact, case-sensitive lookup on the SNI value, which fails to match wildcard host patterns (e.g., *.example.com) or case variants of the configured hostname. Because the handshake falls back to the default TLS configuration — which may not require client certificates — a client can complete the QUIC handshake without presenting a certificate, while the subsequent HTTP routing layer still dispatches the request to a backend protected by a router-specific mTLS policy. The issue affects deployments where HTTP/3 is enabled, a router uses a wildcard Host rule or case-insensitive hostname matching, a router-specific TLSOptions enforces client certificate authentication, and UDP access to the entrypoint is reachable by an attacker. This vulnerability is fixed in 3.7.3.

---

## [CVE-2026-56351](https://nvd.nist.gov/vuln/detail/CVE-2026-56351)
* **Puntuación CVSS v3:** `8.2` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-24T13:16:36.473
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:N`

### Descripción
n8n before version 2.4.0 contains a sql injection vulnerability in MySQL, PostgreSQL, and Microsoft SQL nodes that allows authenticated users to inject arbitrary SQL through unescaped identifier values in node configuration parameters. Attackers with workflow creation permissions can supply specially crafted table or column names to execute unauthorized database commands and compromise data integrity.

---

## [CVE-2026-56121](https://nvd.nist.gov/vuln/detail/CVE-2026-56121)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-24T16:16:33.193
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Feast before 0.63.0 contains an unsafe deserialization vulnerability that allows unauthenticated or unauthorized attackers to achieve remote code execution by sending a crafted gRPC request to the registry server. The user_defined_function.body field of an OnDemandFeatureView spec is decoded from base64 and passed to dill.loads() before any authorization check is performed, enabling attackers to embed a malicious serialized Python object with an arbitrary __reduce__ method to execute OS commands as the feast service account.

---

## [CVE-2026-54906](https://nvd.nist.gov/vuln/detail/CVE-2026-54906)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-24T17:17:29.550
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
concurrent-ruby is a modern concurrency tools for Ruby. Prior to 1.3.7, Concurrent::ReadWriteLock#release_write_lock does not verify that the calling thread acquired the write lock. Any thread with access to the lock object can release an active write lock held by another thread. A second writer can then enter its critical section while the first writer is still running. Concurrent::ReadWriteLock#release_read_lock also decrements the shared counter even when no read lock is held. Calling it on a fresh lock changes the counter from 0 to -1, after which normal read acquisition raises Concurrent::ResourceLimitError. This is a synchronization correctness issue in the public Concurrent::ReadWriteLock API. This vulnerability is fixed in 1.3.7.

---

## [CVE-2026-55455](https://nvd.nist.gov/vuln/detail/CVE-2026-55455)
* **Puntuación CVSS v3:** `9.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-24T22:16:49.137
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`

### Descripción
Appsmith is a platform to build admin panels, internal tools, and dashboards. Prior to 2.1, the outbound HTTP host filter applied by WebClientUtils (used by the REST API and GraphQL datasource plugins) validates hosts against an exact-match string denylist. The comprehensive address-class check (loopback, any-local, link-local, fc00::/7) exists only on a separate code path used by SMTP, not by the HTTP plugin path. As a result, an authenticated user can craft outbound requests that reach loopback-bound services inside the container. This vulnerability is fixed in 2.1.

---

## [CVE-2026-39948](https://nvd.nist.gov/vuln/detail/CVE-2026-39948)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-24T23:16:40.830
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Cacti is an open source performance and fault management framework. In versions 1.2.30 and prior, the rfilter request parameter is retrieved via the raw accessor grv() (rather than gfrv() with FILTER_VALIDATE_IS_REGEX validation) and concatenated directly into RLIKE SQL clauses in lib/html_graph.php and lib/html_tree.php, which are reachable pre-authentication through graph_view.php on installations with guest graph viewing enabled. Because the unbalanced-quote payload bypasses the regex validation that would otherwise reject it, an unauthenticated attacker can inject arbitrary SQL to compromise the confidentiality, integrity, and availability of the database. This advisory is similar to GHSA-69gg-mjfm-jjpc. This issue has been fixed in version 1.2.31.

---

## [CVE-2026-40079](https://nvd.nist.gov/vuln/detail/CVE-2026-40079)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-25T00:17:47.570
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Cacti is an open source performance and fault management framework. Versions 1.2.30 and prior are vulnerable to Command Injection due to lack of sanitization in the escape_command() function. The escape_command() function at lib/rrd.php is a no-op: it returns $command unchanged. The command line built by rrdtool_function_graph() is passed through this function and then to shell_exec($full_commandline). The risk is in __rrd_execute() where text_format values from graph templates (which may contain host variable substitutions) reach shell_exec without adequate escaping. This issue has been addressed in version 1.2.31.

---

## [CVE-2026-8592](https://nvd.nist.gov/vuln/detail/CVE-2026-8592)
* **Puntuación CVSS v3:** `7.7` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-25T02:16:34.990
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:L`

### Descripción
OS Command Injection vulnerability in the process_string action of Rapid7 InsightConnect AWK Plugin on Linux allows remote attackers to execute arbitrary OS commands via the text or expression parameters due to unsafe shell command construction in the processing pipeline.

---

## [CVE-2026-8660](https://nvd.nist.gov/vuln/detail/CVE-2026-8660)
* **Puntuación CVSS v3:** `7.7` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-25T02:16:35.110
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:L`

### Descripción
OS Command Injection vulnerability in the ping action of Rapid7 InsightConnect Ping Plugin on Linux allows remote attackers to execute arbitrary OS commands via the host parameter due to insufficient input validation when constructing shell commands.

---

## [CVE-2026-8665](https://nvd.nist.gov/vuln/detail/CVE-2026-8665)
* **Puntuación CVSS v3:** `7.7` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-25T02:16:35.340
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:L`

### Descripción
OS Command Injection vulnerability in the TR action of Rapid7 InsightConnect Translate Plugin on Linux allows remote attackers to execute arbitrary OS commands via the text or expression parameters due to insufficient input sanitization in shell command construction.

---

## [CVE-2026-8666](https://nvd.nist.gov/vuln/detail/CVE-2026-8666)
* **Puntuación CVSS v3:** `7.7` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-25T02:16:35.567
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:L`

### Descripción
OS Command Injection vulnerability in the traceroute action of Rapid7 InsightConnect Traceroute Plugin on Linux allows remote attackers to execute arbitrary OS commands via the host, port, max_ttl, count, or time_out request parameters due to insufficient input validation when constructing shell commands.

---

## [CVE-2026-54030](https://nvd.nist.gov/vuln/detail/CVE-2026-54030)
* **Puntuación CVSS v3:** `8.0` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-25T17:16:40.660
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:N/UI:R/S:C/C:H/I:H/A:N`

### Descripción
LibreChat is an enhanced ChatGPT clone that supports multiple AI providers. Prior to 0.8.5, LibreChat's MCP OAuth implementation does not validate that the resource parameter from OAuth Protected Resource metadata (RFC 9728) matches the configured MCP server URL, allowing a malicious MCP server to steal access tokens intended for a legitimate server. This vulnerability is fixed in 0.8.5.

---

## [CVE-2026-56123](https://nvd.nist.gov/vuln/detail/CVE-2026-56123)
* **Puntuación CVSS v3:** `8.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-25T17:17:01.967
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
socat versions 1.8.0.0 through 1.8.1.1 contain a heap-based buffer overflow vulnerability that allows a malicious SOCKS5 proxy server to overwrite adjacent heap memory by exploiting a sign-extension flaw in the DOMAINNAME reply parser. During connection setup, the domain name length byte is read through a signed char field causing a negative bytes_to_read value that is implicitly converted to size_t, resulting in an unbounded heap write into the 262-byte reply buffer with attacker-controlled size and content.

---

## [CVE-2026-6094](https://nvd.nist.gov/vuln/detail/CVE-2026-6094)
* **Puntuación CVSS v3:** `9.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-25T18:16:41.567
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:H`

### Descripción
Heap buffer overread in wc_PKCS7_DecodeEnvelopedData when parsing crafted PKCS7 EnvelopedData. This could theoretically be triggered by attacker-supplied data delivered via S/MIME or CMS.

---

## [CVE-2026-50548](https://nvd.nist.gov/vuln/detail/CVE-2026-50548)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-25T19:16:39.660
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Cursor is a code editor built for programming with AI. Prior to 3.0, Cursor runs agent terminal commands in a sandbox by default, and the sandbox grants write access to the command's working directory. A flaw was identified in how the agent could modify the working_directory parameter, which could cause the sandbox to include writable paths outside the intended workspace. A malicious agent could set working_directory to a sensitive location and write arbitrary files outside the workspace under the user's privileges. This enables non-sandboxed Remote Code Execution — for example by overwriting the cursorsandbox helper so later commands run unsandboxed — with no user interaction beyond a benign prompt. This vulnerability is fixed in 3.0.

---

## [CVE-2026-50549](https://nvd.nist.gov/vuln/detail/CVE-2026-50549)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-25T19:16:39.793
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Cursor is a code editor built for programming with AI. Prior to 3.0, Cursor runs agent terminal commands in a sandbox by default. Before a Write, the agent canonicalizes the target path to confirm it stays inside the workspace, but when canonicalization fails it falls back to the original path and writes without approval. A malicious agent can create an in-workspace symlink that points outside the workspace and force canonicalization to fail — either because the target does not exist or because read permission is removed from the path — so the agent writes through the symlink to an arbitrary location without approval. A malicious agent could write arbitrary files outside the workspace under the user's privileges. This enables non-sandboxed Remote Code Execution — for example by overwriting the cursorsandbox helper so later commands run unsandboxed — with no user interaction beyond a benign prompt. This vulnerability is fixed in 3.0.

---

## [CVE-2026-54917](https://nvd.nist.gov/vuln/detail/CVE-2026-54917)
* **Puntuación CVSS v3:** `10.0` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-25T19:16:42.230
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N`

### Descripción
SeaweedFS is a distributed storage system for object storage (S3), file systems, and Iceberg tables. Prior to 4.30, the S3 API gateway and the Iceberg REST catalog gateway construct their routers with mux.NewRouter().SkipClean(true). With path cleaning disabled, a .. segment inside the URL survives routing, so a request such as `GET /bucket-A/../evil-bucket/key`, is matched as bucket=bucket-A, object=../evil-bucket/key. The captured object key is then joined into a filer path with util.JoinPath (S3) / path.Join (Iceberg), which collapse the .. server-side, so the actual read or write lands in evil-bucket. This vulnerability is fixed in 4.30.

---

## [CVE-2026-56786](https://nvd.nist.gov/vuln/detail/CVE-2026-56786)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-25T19:16:44.997
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
RTKLIB through 2.4.3 contains an out-of-bounds write vulnerability in decode_type1033 function that fails to clamp length counters to destination buffer size, allowing up to 191-byte overflow into fixed 64-byte descriptor fields. An attacker controlling an NTRIP or serial RTCM3 correction stream can craft a valid CRC-bearing type-1033 message to corrupt adjacent rtcm_t object members, potentially achieving arbitrary code execution or denial of service.

---

## [CVE-2026-7531](https://nvd.nist.gov/vuln/detail/CVE-2026-7531)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-25T20:17:17.763
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Use-after-free in PQC hybrid key-share handling. This is an incomplete-fix follow-up to CVE-2026-5460 (released in 5.9.1): a malicious TLS 1.3 server sending a truncated PQC hybrid KeyShare can still trigger the error cleanup path to operate on freed memory.

---

## [CVE-2025-71333](https://nvd.nist.gov/vuln/detail/CVE-2025-71333)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-25T22:16:59.010
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Flowise through 2.2.4 contains an unauthenticated arbitrary file upload vulnerability in the /api/v1/attachments endpoint when storageType is set to local. Attackers can exploit path traversal in the chatId and chatflowId parameters to upload malicious files to arbitrary directories, potentially enabling remote code execution and server compromise.

---

## [CVE-2025-71338](https://nvd.nist.gov/vuln/detail/CVE-2025-71338)
* **Puntuación CVSS v3:** `10.0` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-25T22:16:59.520
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`

### Descripción
Flowise contains a path traversal vulnerability in the /api/v1/document-store/loader/process endpoint that allows unauthenticated attackers to write arbitrary files to the filesystem. Attackers can exploit unsanitized fileName parameters with ../ sequences to overwrite critical files like package.json and achieve remote code execution when the application restarts.

---

## [CVE-2026-48930](https://nvd.nist.gov/vuln/detail/CVE-2026-48930)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-26T02:16:52.723
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
A flaw in Node.js TLS hostname handling can cause Embedded-nul hostnames can lead to silent authority rebinding due to c-string truncation in resolver bindings.

This vulnerability affects all supported release lines: **Node.js 22**, **Node.js 24**, and **Node.js 26**.

---

## [CVE-2026-2053](https://nvd.nist.gov/vuln/detail/CVE-2026-2053)
* **Puntuación CVSS v3:** `8.3` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-26T08:16:21.603
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:L/A:L`

### Descripción
The WSO2 API Manager's message flow component, when processing WS-Addressing headers, does not sufficiently validate or restrict user-controlled input within these headers. This omission allows an attacker to manipulate WS-Addressing headers to specify arbitrary destinations for server-initiated requests.

Successful exploitation allows an unauthenticated attacker to control the destination of server-initiated requests originating from the WSO2 API Manager. This direct control can enable unauthorized access to internal network resources or services that would typically be inaccessible from external networks.

---

## [CVE-2026-53914](https://nvd.nist.gov/vuln/detail/CVE-2026-53914)
* **Puntuación CVSS v3:** `6.7` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-26T14:17:05.157
* **Vector de Ataque:** `CVSS:3.1/AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:L/A:L`

### Descripción
In JetBrains Kotlin before 2.4.20 code execution was possible via unsafe deserialization in the build cache metadata

---

## [CVE-2026-57926](https://nvd.nist.gov/vuln/detail/CVE-2026-57926)
* **Puntuación CVSS v3:** `2.6` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-26T14:17:07.780
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:L/UI:R/S:U/C:N/I:L/A:N`

### Descripción
In JetBrains YouTrack before 2026.2.16593 the websandbox bridge was vulnerable to a prototype pollution attack

---

## [CVE-2026-54636](https://nvd.nist.gov/vuln/detail/CVE-2026-54636)
* **Puntuación CVSS v3:** `9.0` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-26T17:16:34.083
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:L/UI:R/S:C/C:H/I:H/A:H`

### Descripción
Dokku is a docker-powered PaaS. Prior to 0.38.7, the cron plugin utilizes commands in the app.json file to manage system cron running as the Dokku user. An app.json cron command utilizing special shell characters - including, but not limited to, > or ; - can break out of the Docker container and execute commands on the host as the Dokku user. This vulnerability is fixed in 0.38.7.

---

## [CVE-2026-50137](https://nvd.nist.gov/vuln/detail/CVE-2026-50137)
* **Puntuación CVSS v3:** `9.4` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-26T21:16:34.673
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:L`

### Descripción
Budibase is an open-source low-code platform. Prior to 3.39.0, an anonymous attacker who knows or can enumerate a workspace id (app_...) and an S3-source datasource id (ds_...) can call this endpoint with no auth and obtain a 15-minute pre-signed PUT URL minted on the victim's IAM identity. The endpoint also returns the publicUrl so the attacker knows exactly where their PUT lands. Because bucket is attacker-controlled, the attacker can write to any bucket those IAM credentials can write to, not only the bucket the datasource was configured for. The Budibase server route POST /api/attachments/:datasourceId/url (packages/server/src/api/routes/static.ts) is registered with only the recaptcha middleware. There is no authorized(...) middleware in the chain. The controller (packages/server/src/api/controllers/static/index.ts::getSignedUploadURL) looks the requested datasource up, instantiates an AWS S3 client with the datasource's stored accessKeyId / secretAccessKey, and returns an AWS Signature V4 pre-signed PutObjectCommand URL for the caller-supplied bucket and key. The bucket is not pinned to the datasource's configured bucket. The workspace context required by sdk.datasources.get is sourced by getWorkspaceIdFromCtx (packages/backend-core/src/utils/utils.ts) from any of: the x-budibase-app-id header, the JSON body appId, a path segment that begins with the workspace prefix, or ?appId=. auth.buildAuthMiddleware([], { publicAllowed: true }) runs before any of this and explicitly allows anonymous requests. The currentWorkspace middleware's "deny access to dev preview" branch only triggers under isBrowser(ctx) && !isApiKey(ctx); isBrowser checks the parsed User-Agent for a recognised browser, so any non-browser client (curl, the supplied PoC, any tool not setting a browser UA) is neither and reaches dev workspaces too. This vulnerability is fixed in 3.39.0.

---

## [CVE-2026-54350](https://nvd.nist.gov/vuln/detail/CVE-2026-54350)
* **Puntuación CVSS v3:** `10.0` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-26T21:16:35.040
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:N`

### Descripción
Budibase is an open-source low-code platform. Prior to 3.39.12,  an unauthenticated visitor of any published Budibase app reads every document of the backing MongoDB, CouchDB, Elasticsearch, DynamoDB-PartiQL, or REST-with-JSON-body collection and, where the builder has published a PUBLIC write query, modifies every document of that collection with one HTTP request. enrichContext at packages/server/src/sdk/workspace/queries/queries.ts:121-138 substitutes parameter values into the raw JSON body of a query, then JSON.parses the result. The validator validateQueryInputs at packages/server/src/api/controllers/query/index.ts:61-71 rejects only Handlebars markers ({{, }}) in user input and does not escape JSON metacharacters (", \, }). A parameter value containing a closing quote and additional keys lifts attacker-controlled fields into the parsed filter object. For Mongo find, the parsed filter passes directly to collection.find() (packages/server/src/integrations/mongodb.ts:506-510). Duplicate-key JSON parsing overrides the builder's {name: "..."} with {name: {$exists: true}} and returns every document. The same primitive against an updateMany query (mongodb.ts:577-585) widens the filter scope to the full collection while the builder-controlled $set body runs against every matched document. The authorized middleware at packages/server/src/middleware/authorized.ts:141-148 short-circuits when the query's role is PUBLIC. CSRF is not enforced on this path. POST /api/v2/queries/:queryId (packages/server/src/api/routes/query.ts:63) accepts the call with no session, only an x-budibase-app-id header that is public from the published-app URL. This vulnerability is fixed in 3.39.12.

---

## [CVE-2026-54351](https://nvd.nist.gov/vuln/detail/CVE-2026-54351)
* **Puntuación CVSS v3:** `8.2` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-26T21:16:35.170
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:N`

### Descripción
Budibase is an open-source low-code platform. Prior to 3.39.9, the webhook trigger endpoint in Budibase is publicly accessible and passes the full HTTP request body into automation execution parameters. A mass assignment vulnerability in externalTrigger() allows an attacker to overwrite the internal appId property by including it in the webhook POST body. When the automation is processed asynchronously (the default path for webhooks without a collect step), the worker executes the attacker-defined automation in the context of the victim's workspace, granting full read/write access to the victim's database. This vulnerability is fixed in 3.39.9.

---

## [CVE-2026-13751](https://nvd.nist.gov/vuln/detail/CVE-2026-13751)
* **Puntuación CVSS v3:** `4.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-29T17:16:30.050
* **Vector de Ataque:** `CVSS:3.1/AV:L/AC:H/PR:N/UI:R/S:C/C:L/I:L/A:N`

### Descripción
Improper handling of untrusted remote references in Snowflake CLI versions prior to 3.19 allowed server-side request forgery. The SQL statement reader's !source/!load directives could reference remote URLs that were retrieved at runtime without sufficient restriction on the request destination. By supplying crafted SQL content processed through a vulnerable command path, an attacker could cause the victim's environment to issue unintended outbound requests to internal or otherwise non-public network locations, and could cause remote SQL content to be retrieved and executed in the context of the victim user's session. Successful exploitation requires the victim to process attacker-controlled content through a vulnerable command path and is limited by the privileges available to that session and environment. The fix is available in Snowflake CLI version 3.19, which adds an option to disable remote URL retrieval.

---

## [CVE-2026-11720](https://nvd.nist.gov/vuln/detail/CVE-2026-11720)
* **Puntuación CVSS v3:** `9.1` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-29T18:16:36.173
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:N`

### Descripción
A path traversal vulnerability exists in the HTTP tool URL builder of googleapis/mcp-toolbox.

When constructing downstream API requests, the URL builder substitutes user-controlled pathParams into the configured tool path and parses the resulting string as a relative URL. While it checks that the input does not alter the scheme, host, or user info, it relies on ResolveReference for the final URL resolution. Because dot segments (../) are normalized during this resolution step, an attacker can supply path parameters containing directory traversal sequences to escape the operator-configured path scope. This allows the client to coerce the toolbox into making requests to unintended endpoints on the same target host while forwarding the toolbox's configured credentials (e.g., bypassing a restricted path like /api/v1/users/{{.id}} to reach /admin/secrets).

---

## [CVE-2026-58016](https://nvd.nist.gov/vuln/detail/CVE-2026-58016)
* **Puntuación CVSS v3:** `7.5` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-30T13:19:17.840
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:N/I:N/A:H`

### Descripción
A flaw was found in GLib. A state confusion issue exists in g_dbus_node_info_new_for_xml() in the gio/gdbusintrospection.c file when processing malformed D-Bus introspection XML, specifically with a <node> element nested within other elements like <method>, <signal>, <property> or <arg>. This issue can cause an unsigned integer overflow and lead to an out-of-bounds read, resulting in a denial of service.

---

## [CVE-2026-8452](https://nvd.nist.gov/vuln/detail/CVE-2026-8452)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-30T13:19:33.450
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Memory overflow vulnerability NetScaler ADC and NetScaler Gateway leading to unpredictable or erroneous behavior and Denial of Service if the appliance is configured as a Gateway (SSL VPN, ICA Proxy, CVPN, RDP Proxy) or AAA virtual server

---

## [CVE-2026-8655](https://nvd.nist.gov/vuln/detail/CVE-2026-8655)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-30T13:19:34.083
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Multiple Memory overflow vulnerabilities in NetScaler ADC and NetScaler Gateway leading to unpredictable or erroneous behavior and Denial of Service if NetScaler ADC is configured as an LB of type Oracle OR NetScaler ADC is configured as a DNS Proxy OR NetScaler ADC is configured as a DNS recursive resolver deployment

---

## [CVE-2026-14241](https://nvd.nist.gov/vuln/detail/CVE-2026-14241)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-30T14:16:26.087
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Memory safety bugs present in Firefox 152.0.3. Some of these bugs showed evidence of memory corruption and we presume that with enough effort some of these could have been exploited to run arbitrary code. This vulnerability was fixed in Firefox 152.0.4.

---

## [CVE-2026-13775](https://nvd.nist.gov/vuln/detail/CVE-2026-13775)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-30T23:16:52.397
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Use after free in GPU in Google Chrome prior to 150.0.7871.47 allowed a remote attacker who had compromised the renderer process to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: Critical)

---

## [CVE-2026-13776](https://nvd.nist.gov/vuln/detail/CVE-2026-13776)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-30T23:16:52.490
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Type Confusion in Dawn in Google Chrome prior to 150.0.7871.47 allowed a remote attacker who had compromised the renderer process to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: Critical)

---

## [CVE-2026-13780](https://nvd.nist.gov/vuln/detail/CVE-2026-13780)
* **Puntuación CVSS v3:** `9.6` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-30T23:16:52.873
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H`

### Descripción
Insufficient validation of untrusted input in ANGLE in Google Chrome prior to 150.0.7871.47 allowed a remote attacker who had compromised the renderer process to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: Critical)

---

## [CVE-2026-13781](https://nvd.nist.gov/vuln/detail/CVE-2026-13781)
* **Puntuación CVSS v3:** `9.6` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-30T23:16:52.967
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H`

### Descripción
Insufficient validation of untrusted input in Skia in Google Chrome prior to 150.0.7871.47 allowed a remote attacker who had compromised the renderer process to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: Critical)

---

## [CVE-2026-13782](https://nvd.nist.gov/vuln/detail/CVE-2026-13782)
* **Puntuación CVSS v3:** `10.0` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-30T23:16:53.063
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`

### Descripción
Use after free in Browser in Google Chrome prior to 150.0.7871.47 allowed a remote attacker who had compromised the renderer process to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: Critical)

---

## [CVE-2026-13785](https://nvd.nist.gov/vuln/detail/CVE-2026-13785)
* **Puntuación CVSS v3:** `9.6` (CRÍTICA)
* **Fecha de Publicación:** 2026-06-30T23:16:53.347
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H`

### Descripción
Use after free in Bluetooth in Google Chrome on Mac prior to 150.0.7871.47 allowed a remote attacker who convinced a user to engage in specific UI gestures to potentially perform a sandbox escape via a crafted HTML page. (Chromium security severity: Critical)

---

## [CVE-2026-34099](https://nvd.nist.gov/vuln/detail/CVE-2026-34099)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-07-01T17:16:32.820
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Guardian language-system passes the id GET parameter directly into an unsanitized SQL query in job_info.php (line 16): SELECT * FROM jobs where id = '\".$_GET['id'].\"'. No authentication is required. An unauthenticated attacker can perform error-based SQL injection to extract the database version, current user, schema names, and table contents.

---

## [CVE-2026-34100](https://nvd.nist.gov/vuln/detail/CVE-2026-34100)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-07-01T17:16:32.940
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Guardian language-system passes the id GET parameter directly into an unsanitized SQL query in media.php (line 17): SELECT id, filename, extension, type, duration, owner, private FROM files where id = '\".$_GET['id'].\"'. An authenticated attacker can perform error-based SQL injection to extract database contents.

---

## [CVE-2026-34105](https://nvd.nist.gov/vuln/detail/CVE-2026-34105)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-07-01T17:16:33.537
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Guardian language-system passes the id GET parameter directly into an unsanitized SQL query in translate_text.php (line 15): SELECT id, filename, extension, type FROM files where id = '\".$_GET['id'].\"'. An authenticated attacker can perform error-based SQL injection to extract database contents.

---

## [CVE-2026-34106](https://nvd.nist.gov/vuln/detail/CVE-2026-34106)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-07-01T17:16:33.657
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Guardian language-system passes the id GET parameter directly into a PHP exec() call in subtitles.php (line 19) without sanitization: exec(\"php jobs/subtitle_rendering.php \".$login_session.\" \".$_GET['id'].\" ...\"). No authentication is required. An unauthenticated remote attacker can append shell metacharacters to the id parameter to execute arbitrary OS commands on the server.

---

## [CVE-2026-34108](https://nvd.nist.gov/vuln/detail/CVE-2026-34108)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-07-01T17:16:33.970
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Guardian language-system passes the id GET parameter directly into a PHP exec() call in text.php (line 15) without sanitization: exec(\"php jobs/text.php \".$login_session.\" \".$_GET['id'].\" ...\"). No authentication is required. An unauthenticated remote attacker can append shell metacharacters to execute arbitrary OS commands on the server.

---

## [CVE-2026-34114](https://nvd.nist.gov/vuln/detail/CVE-2026-34114)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-07-01T17:16:34.780
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Guardian language-system passes the id GET parameter directly into a PHP exec() call in translate_text.php (line 18) without sanitization: exec(\"php jobs/translate_text.php \".$login_session.\" \".$_GET['id'].\" ...\"). No authentication is required. An unauthenticated remote attacker can append shell metacharacters to execute arbitrary OS commands on the server.

---

## [CVE-2026-58453](https://nvd.nist.gov/vuln/detail/CVE-2026-58453)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-07-01T17:16:40.517
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
JAIOTlink C492A-W6 Wi-Fi IP cameras running firmware 4.8.30.57701411 contain a hard-coded credentials vulnerability that allows network-adjacent attackers to gain unauthorized access by using the default admin username with an empty password accepted by the anyka_ipc HTTP service on port 80. Attackers can authenticate with these hardcoded credentials to access camera snapshots, video streams, network configuration, and factory-level API endpoints including the SetMAC command injection surface.

---

## [CVE-2026-58457](https://nvd.nist.gov/vuln/detail/CVE-2026-58457)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-07-01T20:17:11.427
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
Shenzhen Aitemi M300 Wi-Fi Repeater (hardware model MT02) contains an unauthenticated OS command injection vulnerability that allows network-adjacent attackers to execute arbitrary shell commands by injecting unsanitized input through the smacfilter_conf handler in the commuos web backend. Attackers can append semicolon-delimited payloads to the name, enable, or mac GET parameters, which are passed without sanitization into sprintf() to build uci shell commands executed via doSystemCmdComlib(), granting full root-level control of the device.

---

## [CVE-2026-5524](https://nvd.nist.gov/vuln/detail/CVE-2026-5524)
* **Puntuación CVSS v3:** `9.8` (CRÍTICA)
* **Fecha de Publicación:** 2026-07-02T13:17:00.587
* **Vector de Ataque:** `CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H`

### Descripción
The Divi Form Builder plugin for WordPress is vulnerable to Arbitrary File Upload leading to Remote Code Execution in all versions up to and including 5.1.8. This is due to insufficient file extension validation in the do_image_upload() function where user-supplied input from the acceptFileTypes POST parameter is directly interpolated into a regular expression used to validate uploaded files. Attackers can specify PHP-executable extensions such as .phtml, .phar, .php5, or .php7 to bypass the plugin's .htaccess protection which only blocks .php files specifically. Additionally, on Nginx-based servers, the .htaccess protection is completely ineffective as Nginx does not process .htaccess files. This makes it possible for unauthenticated attackers (who can obtain a nonce from any public page containing a form) to upload executable PHP files to the publicly accessible /wp-content/uploads/de_fb_uploads/ directory and achieve Remote Code Execution by accessing the uploaded file via HTTP. The vulnerability was partially patched in version 5.1.3.

---

