✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Azure AD B2C Information Worksheet
The following worksheet may be helpful to track certain values that you will use during
configuration. Note that case matters for all of these values.
ATTRIBUTE EXAMPLE M
Y
V
A
L
U
E
S
Stellar Cyber Server Information (obtain before you begin)
DP FQDN testdp.stellarcyber.ai

ATTRIBUTE EXAMPLE M
Y
V
A
L
U
E
S

ATTRIBUTE EXAMPLE M
Y
V
A
L
U
E
S

| ATTRIBUTE | EXAMPLE | M   |
| --------- | ------- | --- |
Y
V
A
L
U
E
S

| Tenant ID (for per tenant-SSO only) | 29443942    |     |
| ----------------------------------- | ----------- | --- |
| stellar_scope (authorization only)  | root        |     |
|                                     | super_admin |     |
stellar_privilege (authorization only)

stellar_tenant (optional) (authorization a112c31c04734b7ba5243e5e5432bfe6
only)
|     | 25320755 |     |
| --- | -------- | --- |
stellar_tenant_group (optional)
(authorization only)
Azure AD B2C Server Information (in order of occurrence)
| Domain / Primary Domain | stellarpmb2c.onmicrosoft.com |     |
| ----------------------- | ---------------------------- | --- |
Tenant ID / Tenant (Object ID) 04fcef19-20fe-4655-9498-3e5050b6dda1

Application (Client) ID for 01590824-a092-4271-99a3-f3e37b9f22cc
IdentityExperienceFramework
Application (Client) ID for 0c54849b-121f-496e-b1c3-406976bec48b
ProxyIdentityExperienceFramework
| SAML App Name | Stellar_SAML |     |
| ------------- | ------------ | --- |
identifierUris https://<Azure AD B2C tenant name>.onmicrosoft.com/<SAML
application name>
http://stellarpmb2c.onmicrosoft.com/Stellar_SAML
Application ID URI https://stellarpmb2c.b2clogin.com/stellarpmb2c.onmicrosoft.com

b2c-extensions-app: Application (Client) 0c0abe38-79ab-45d3-99fe-9378eec7b16f
ID
b2c-extensions-app: Object ID 3c34826e-3bd5-47a2-b44d-08c09034cef2
Metadata URL  https://stellarpmb2c.b2clogin.com/stellarpmb2c.onmicrosoft.com/B
2C_1A_signup_signin_saml/samlp/metadata
| Issuer URL        | http://testdp.stellarcyber.ai |     |
| ----------------- | ----------------------------- | --- |
| replyUrlsWithType | Global SSO:                   |     |
https://testdp.stellarcyber.ai/saml/login/callback

ATTRIBUTE EXAMPLE M
Y
V
A
L
U
E
S
Per-tenant SSO:
https://testdp.stellarcyber.ai/saml/login/callback/cust_id/a112c31c0
4734b7ba5243e5e5432bfe6
Azure AD B2C User IDs (email & Issuer SoCguy@stellarpmb2c.onmicrosoft.com
ID, if different)
Example of issuer assigned ID that is not the same as email:
AnalystTwo@stellarpmb2c.onmicrosoft.com,
6b744a55-9031-4b8c-ad6f-
81dac5e74055@stellarpmb2c.onmicrosoft.com
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  