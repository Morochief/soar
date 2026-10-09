Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Azure AD B2C SSO: Configure & Upload
Policies / Keys

The steps in this section are critical to perform after you have completed steps in the previous
section. Here you manage the keys and policies to support the overall configuration.

 If you stop and return to any of the procedures in this configuration process, ensure that you
switch to the correct directory before you continue so that you are working on the correct
Azure AD B2C Tenant container.

Upload the Stellar Cyber DP Server Certificate
Configure Custom Policies to support SAML

Download & Rename Sample Template Files
Make Global Edits to the Files
Edit TrustFrameworkBase.xml
Edit TrustFrameworkLocalization.xml
Edit TrustFrameworkExtensions.xml
Edit SignUpOrSignin.xml
Edit ProfileEdit.xml
Edit PasswordReset.xml
Edit SignUporSigninSAML.xml

Upload Custom Policies

 The order in which you perform certain steps matters. Perform the steps in exactly the order

shown.

Upload the Stellar Cyber DP Server Certificate
Steps

1. Locate the Stellar Cyber DP server .pfx you obtained before you started the steps in this

topic. If you created a password for it, have that value noted.

 Self-signed server certificates are NOT supported by Azure AD B2C for this

purpose.

2. Access All services from the top-left corner of the Azure portal, and then search for

and select Azure AD B2C.

3. From the Overview page, select Identity Experience Framework.

4. Select Policy Keys and then select Add.

5. For Options, choose Upload.

6. Enter a Name for the policy key for the Stellar Cyber pfx file. For example, enter

SamlIdpCert. The prefix B2C_1A_is added automatically to the name of your key.



The name you enter here MUST be the same as the values for the following fields
in the file ending with TrustFrameworkBase.xml:

<Key Id="MetadataSigning"
StorageReferenceId="B2C_1A_SamlIdpCert" />

<Key Id="SamlMessageSigning"
StorageReferenceId="B2C_1A_SamlIdpCert" />

<Key Id="SamlAssertionSigning"
StorageReferenceId="B2C_1A_SamlIdpCert" />

7. Browse to and select the public .pfx certificate file with the private key that you obtained
for the Stellar Cyber DP. (Password is not required unless you created the pfx with a
password)

8. Click Create.

9. The pane refreshes to display the key and the associated container file that is

automatically created: B2C_1A_AdminClientEncryptionKeyContainer.

Configure Custom Policies to support SAML

 If you stop and return to any of the procedures in this configuration process, ensure that you
switch to the correct directory before you continue so that you are working on the correct
Azure AD B2C Tenant container.

Download & Rename Sample Template Files

Steps

The following instructions are based on sample templates that you can download below. The
template files are set up to support configuration of both Authentication and Authorization, but
can also be used to configure just Authentication.



As you edit these files, pay attention to the following:

Note that some attributes appear multiple times. You MUST ensure they are all
consistent.

The values are case sensitive.

The policy names within each template file (PolicyId attribute) must match the
naming of the corresponding file. In the templates, the syntax for the filenames is
<upload order number> _<tenant name-domain>—<filename>.xml.

1. Download the sample policy templates.

If you are configuring standard logins, use: authentication_authorization.zip

If want to configure multi-factor authentication that will use Microsoft
Authenticator (Azure Native) use: authentication_authorization_MFA.zip

Ensure you Enabled security defaults as mentioned in the previous topic.

2. Unzip the package and either use the samples as a guide to customize your own policy

files or customize these for upload.

3. Rename all the files to use the Azure AD B2C Primary Domain you copied to your
worksheet, replacing stellarpmb2c.onmicrosoft.com with your primary domain.

Make Global Edits to the Files

Steps

Make the following global edits in every file.

1. Use the Azure AD B2C Primary Domain you copied to your worksheet and replace the

TenantId value and the domain portion of the
PublicPolicyUri="http://<domain>/<filename> value.

2. Use the Azure AD B2C Tenant ID you copied to your worksheet) and replace the

TenantObjectId value.

Edit TrustFrameworkBase.xml

Steps

1. Some of the edits for this file were completed with the Global edits you made above.

Edit the file ending with TrustFrameworkBase.xml and ensure the highlighted values
were made.

<TrustFrameworkPolicy
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns="http://schemas.microsoft.com/online/cpim/schemas/2013/06"
PolicySchemaVersion="0.3.0.0"
TenantId="stellarpmb2c.onmicrosoft.com"
PolicyId="B2C_1A_TrustFrameworkBase"
PublicPolicyUri="http://stellarpmb2c.onmicrosoft.com/B2C_1A_Trus
tFrameworkBase" TenantObjectId="04fcef19-20fe-4655-9498-
3e5050b6dda1">

2. Make the additional changes, as needed, to ensure the highlighted values below are

consistent with the values you recorded on your worksheet.

<Item
Key="IssuerUri">https://stellarpmb2c.b2clogin.com/stellarpmb2c.o
nmicrosoft.com/B2C_1A_signup_signin_SAML</Item>

<Key Id="MetadataSigning"
StorageReferenceId="B2C_1A_SamlIdpCert" />

<Key Id="SamlMessageSigning"
StorageReferenceId="B2C_1A_SamlIdpCert" />

<Key Id="SamlAssertionSigning"
StorageReferenceId="B2C_1A_SamlIdpCert" />

<Key Id="issuer_secret"
StorageReferenceId="B2C_1A_TokenSigningKeyContainer" />

<Key Id="issuer_refresh_token_key"
StorageReferenceId="B2C_1A_TokenEncryptionKeyContainer" />

Your standard authentication file will look similar to the following:

 Azure AD or Azure Active Directory refers to Microsoft Entra ID.

TrustFrameworkBase.xml

1
2

<TrustFrameworkPolicy xmlns:xsi="http://www.w3.org/2001/XMLSchema-
instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"

3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89

xmlns="http://schemas.microsoft.com/online/cpim/schemas/2013/06"
PolicySchemaVersion="0.3.0.0" TenantId="stellarpmb2c.onmicrosoft.com"
PolicyId="B2C_1A_TrustFrameworkBase"
PublicPolicyUri="http://stellarpmb2c.onmicrosoft.com/B2C_1A_TrustFrame
workBase" TenantObjectId="04fcef19-20fe-4655-9498-3e5050b6dda1">
  <BuildingBlocks>
    <ClaimsSchema>
      <!-- The ClaimsSchema is divided into three sections:
           1. Section I lists the minimum claims that are required for
the user journeys to work properly.
           2. Section II lists the claims required for query string
parameters and other special parameters
              to be passed to other claims providers, esp.
login.microsoftonline.com for authentication.
              Please do not modify these claims.
           3. Section III lists any additional (optional) claims that
can be collected from the user, stored
              in the directory and sent in tokens during sign in. Add
new claims to be collected from the user
              and/or sent in the token in Section III. -->
      <!-- NOTE: The claims schema contains restrictions on certain
claims such as passwords and usernames.
           The trust framework policy treats Azure AD as any other
claims provider and all its restrictions
           are modelled in the policy. A policy could be modified to
add more restrictions, or use another
           claims provider for credential storage which will have its
own restrictions. -->
      <!-- SECTION I: Claims required for user journeys to work
properly -->
      <ClaimType Id="socialIdpUserId">
        <DisplayName>Username</DisplayName>
        <DataType>string</DataType>
        <UserHelpText />
        <UserInputType>TextBox</UserInputType>
        <Restriction>
          <Pattern RegularExpression="^[a-zA-Z0-9]+[a-zA-Z0-9_-]*$"
HelpText="The username you provided is not valid. It must begin with
an alphabet or number and can contain alphabets, numbers and the
following symbols: _ -" />
        </Restriction>
      </ClaimType>
      <ClaimType Id="tenantId">
        <DisplayName>User's Object's Tenant ID</DisplayName>
        <DataType>string</DataType>
        <DefaultPartnerClaimTypes>
          <Protocol Name="OAuth2" PartnerClaimType="tid" />
          <Protocol Name="OpenIdConnect" PartnerClaimType="tid" />
          <Protocol Name="SAML2"
PartnerClaimType="http://schemas.microsoft.com/identity/claims/tenanti
d" />
        </DefaultPartnerClaimTypes>
        <UserHelpText>Tenant identifier (ID) of the user object in
Azure AD.</UserHelpText>
      </ClaimType>
      <ClaimType Id="objectId">
        <DisplayName>User's Object ID</DisplayName>
        <DataType>string</DataType>
        <DefaultPartnerClaimTypes>
          <Protocol Name="OAuth2" PartnerClaimType="oid" />
          <Protocol Name="OpenIdConnect" PartnerClaimType="oid" />
          <Protocol Name="SAML2"
PartnerClaimType="http://schemas.microsoft.com/identity/claims/objecti
dentifier" />
        </DefaultPartnerClaimTypes>
        <UserHelpText>Object identifier (ID) of the user object in
Azure AD.</UserHelpText>
      </ClaimType>
      <!-- Claims needed for local accounts. -->
      <ClaimType Id="signInName">
        <DisplayName>Sign in name</DisplayName>
        <DataType>string</DataType>
        <UserHelpText />
        <UserInputType>TextBox</UserInputType>
      </ClaimType>
      <ClaimType Id="signInNames.emailAddress">
        <DisplayName>Email Address</DisplayName>
        <DataType>string</DataType>
        <UserHelpText>Email address to use for signing in.
</UserHelpText>
        <UserInputType>TextBox</UserInputType>
      </ClaimType>
      <ClaimType Id="accountEnabled">
        <DisplayName>Account Enabled</DisplayName>
        <DataType>boolean</DataType>
        <AdminHelpText>Specifies whether the user's account is
enabled.</AdminHelpText>

90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176

        <UserHelpText>Specifies whether your account is enabled.
If you are configuring Azure native multi-factor authentication, your file will look
</UserHelpText>
      </ClaimType>
      <ClaimType Id="password">
        <DisplayName>Password</DisplayName>
        <DataType>string</DataType>
        <UserHelpText>Enter password</UserHelpText>
        <UserInputType>Password</UserInputType>
      </ClaimType>
      <!-- The claim types newPassword and reenterPassword are
considered special, please do not change the names.
           The UI validates that the user correctly re-entered their
password during account creation based on these
           claim types.      -->
      <ClaimType Id="newPassword">
        <DisplayName>New Password</DisplayName>
        <DataType>string</DataType>
        <UserHelpText>Enter new password</UserHelpText>
        <UserInputType>Password</UserInputType>
        <Restriction>
          <Pattern RegularExpression="^((?=.*[a-z])(?=.*[A-Z])(?
=.*\d)|(?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9])|(?=.*[a-z])(?=.*\d)(?
=.*[^A-Za-z0-9])|(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]))([A-Za-
z\d@#$%^&amp;*\-_+=[\]{}|\\:',?/`~&quot;();!]|\.(?!@)){8,16}$"
HelpText="8-16 characters, containing 3 out of 4 of the following:
Lowercase characters, uppercase characters, digits (0-9), and one or
more of the following symbols: @ # $ % ^ &amp; * - _ + = [ ] { } | \ :
' , ? / ` ~ &quot; ( ) ; ." />
        </Restriction>
      </ClaimType>
      <!-- The password regular expression above is constructed for
AAD passwords based on restrictions at https://msdn.microsoft.com/en-
us/library/azure/jj943764.aspx

        ^( # one of the following four combinations must appear in the
password
         (?=.*[a-z])(?=.*[A-Z])(?=.*\d) |            # matches lower
case, upper case or digit
         (?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9]) |  # matches lower
case, upper case or special character (i.e. non-alpha or digit)
         (?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]) |     # matches lower
case, digit, or special character
         (?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9])       # matches upper
case, digit, or special character
        )
        ( # The password must match the following restrictions
         [A-Za-z\d@#$%^&*\-_+=[\]{}|\\:',?/`~"();!] |   # The list of
all acceptable characters (without .)
         \.(?!@)                                        # or . can
appear as long as not followed by @
        ) {8,16}$                                       # the length
must be between 8 and 16 chars inclusive

      -->
      <ClaimType Id="reenterPassword">
        <DisplayName>Confirm New Password</DisplayName>
        <DataType>string</DataType>
        <UserHelpText>Confirm new password</UserHelpText>
        <UserInputType>Password</UserInputType>
        <Restriction>
          <Pattern RegularExpression="^((?=.*[a-z])(?=.*[A-Z])(?
=.*\d)|(?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9])|(?=.*[a-z])(?=.*\d)(?
=.*[^A-Za-z0-9])|(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]))([A-Za-
z\d@#$%^&amp;*\-_+=[\]{}|\\:',?/`~&quot;();!]|\.(?!@)){8,16}$"
HelpText=" " />
        </Restriction>
      </ClaimType>
      <ClaimType Id="passwordPolicies">
        <DisplayName>Password Policies</DisplayName>
        <DataType>string</DataType>
        <UserHelpText>Password policies used by Azure AD to determine
password strength, expiry etc.</UserHelpText>
      </ClaimType>
      <ClaimType Id="client_id">
        <DisplayName>client_id</DisplayName>
        <DataType>string</DataType>
        <AdminHelpText>Special parameter passed to EvoSTS.
</AdminHelpText>
        <UserHelpText>Special parameter passed to EvoSTS.
</UserHelpText>
      </ClaimType>
      <ClaimType Id="resource_id">
        <DisplayName>resource_id</DisplayName>
        <DataType>string</DataType>
        <AdminHelpText>Special parameter passed to EvoSTS.
</AdminHelpText>
        <UserHelpText>Special parameter passed to EvoSTS.

177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260
261
262
263

</UserHelpText>
similar to this:
      </ClaimType>
      <ClaimType Id="sub">
        <DisplayName>Subject</DisplayName>
TrustFrameworkBase (MFA)
        <DataType>string</DataType>
        <DefaultPartnerClaimTypes>
          <Protocol Name="OpenIdConnect" PartnerClaimType="sub" />
        </DefaultPartnerClaimTypes>
        <UserHelpText />
      </ClaimType>
      <ClaimType Id="identityProvider">
        <DisplayName>Identity Provider</DisplayName>
        <DataType>string</DataType>
        <DefaultPartnerClaimTypes>
          <Protocol Name="OAuth2" PartnerClaimType="idp" />
          <Protocol Name="OpenIdConnect" PartnerClaimType="idp" />
          <Protocol Name="SAML2"
PartnerClaimType="http://schemas.microsoft.com/identity/claims/identit
yprovider" />
        </DefaultPartnerClaimTypes>
        <UserHelpText />
      </ClaimType>
      <ClaimType Id="displayName">
        <DisplayName>Display Name</DisplayName>
        <DataType>string</DataType>
        <DefaultPartnerClaimTypes>
          <Protocol Name="OAuth2" PartnerClaimType="unique_name" />
          <Protocol Name="OpenIdConnect" PartnerClaimType="name" />
          <Protocol Name="SAML2"
PartnerClaimType="http://schemas.xmlsoap.org/ws/2005/05/identity/claim
s/name" />
        </DefaultPartnerClaimTypes>
        <UserHelpText>Your display name.</UserHelpText>
        <UserInputType>TextBox</UserInputType>
      </ClaimType>
      <ClaimType Id="email">
        <DisplayName>Email Address</DisplayName>
        <DataType>string</DataType>
        <DefaultPartnerClaimTypes>
          <Protocol Name="OpenIdConnect" PartnerClaimType="email" />
        </DefaultPartnerClaimTypes>
        <UserHelpText>Email address that can be used to contact you.
</UserHelpText>
        <UserInputType>TextBox</UserInputType>
        <Restriction>
          <Pattern RegularExpression="^[a-zA-Z0-
9.!#$%&amp;'^_`{}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
HelpText="Please enter a valid email address." />
        </Restriction>
      </ClaimType>
      <ClaimType Id="otherMails">
        <DisplayName>Alternate Email Addresses</DisplayName>
        <DataType>stringCollection</DataType>
        <UserHelpText>Email addresses that can be used to contact the
user.</UserHelpText>
      </ClaimType>
      <ClaimType Id="userPrincipalName">
        <DisplayName>UserPrincipalName</DisplayName>
        <DataType>string</DataType>
        <DefaultPartnerClaimTypes>
          <Protocol Name="OAuth2" PartnerClaimType="upn" />
          <Protocol Name="OpenIdConnect" PartnerClaimType="upn" />
          <Protocol Name="SAML2"
PartnerClaimType="http://schemas.microsoft.com/identity/claims/userpri
ncipalname" />
        </DefaultPartnerClaimTypes>
        <UserHelpText>Your user name as stored in the Azure Active
Directory.</UserHelpText>
      </ClaimType>
      <ClaimType Id="upnUserName">
        <DisplayName>UPN User Name</DisplayName>
Edit TrustFrameworkLocalization.xml
        <DataType>string</DataType>
        <UserHelpText>The user name for creating user principal name.
</UserHelpText>
Steps
      </ClaimType>
      <ClaimType Id="newUser">
The edits for this file should have been completed with the Global edits, above.
        <DisplayName>User is new</DisplayName>
        <DataType>boolean</DataType>
 Edit the file ending with TrustFrameworkLocalization.xml and ensure the
        <UserHelpText />
      </ClaimType>
highlighted values are consistent with the values you recorded on your
      <ClaimType Id="executed-SelfAsserted-Input">
        <DisplayName>Executed-SelfAsserted-Input</DisplayName>
worksheet.
        <DataType>string</DataType>
        <UserHelpText>A claim that specifies whether attributes were
collected from the user.</UserHelpText>
      </ClaimType>
      <ClaimType Id="authenticationSource">

264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350

        <DisplayName>AuthenticationSource</DisplayName>
<TrustFrameworkPolicy
        <DataType>string</DataType>
        <UserHelpText>Specifies whether the user was authenticated at
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
Social IDP or local account.</UserHelpText>
      </ClaimType>
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
      <!-- SECTION II: Claims required to pass on special parameters
xmlns="http://schemas.microsoft.com/online/cpim/schemas/20
(including some query string parameters) to other claims providers -->
      <ClaimType Id="nca">
13/06" PolicySchemaVersion="0.3.0.0"
        <DisplayName>nca</DisplayName>
        <DataType>string</DataType>
TenantId="stellarpmb2c.onmicrosoft.com"
        <UserHelpText>Special parameter passed for local account
authentication to login.microsoftonline.com.</UserHelpText>
PolicyId="B2C_1A_TrustFrameworkLocalization"
      </ClaimType>
      <ClaimType Id="grant_type">
PublicPolicyUri="http://stellarpmb2c.onmicrosoft.com/B2C_1
        <DisplayName>grant_type</DisplayName>
        <DataType>string</DataType>
A_TrustFrameworkLocalization" TenantObjectId="04fcef19-
        <UserHelpText>Special parameter passed for local account
authentication to login.microsoftonline.com.</UserHelpText>
20fe-4655-9498-3e5050b6dda1">
      </ClaimType>
      <ClaimType Id="scope">
        <DisplayName>scope</DisplayName>
        <DataType>string</DataType>
        <UserHelpText>Special parameter passed for local account
authentication to login.microsoftonline.com.</UserHelpText>
      </ClaimType>
      <ClaimType Id="objectIdFromSession">
        <DisplayName>objectIdFromSession</DisplayName>
        <DataType>boolean</DataType>
        <UserHelpText>Parameter provided by the default session
management provider to indicate that the object id has been retrieved
from an SSO session.</UserHelpText>
      </ClaimType>
      <ClaimType Id="isActiveMFASession">
        <DisplayName>isActiveMFASession</DisplayName>
        <DataType>boolean</DataType>
        <UserHelpText>Parameter provided by the MFA session management
to indicate that the user has an active MFA session.</UserHelpText>
      </ClaimType>
      <!-- SECTION III: Additional claims that can be collected from
the users, stored in the directory, and sent in the token. Add
additional claims here. -->
      <ClaimType Id="givenName">
        <DisplayName>Given Name</DisplayName>
        <DataType>string</DataType>
        <DefaultPartnerClaimTypes>
          <Protocol Name="OAuth2" PartnerClaimType="given_name" />
          <Protocol Name="OpenIdConnect" PartnerClaimType="given_name"
/>
          <Protocol Name="SAML2"
PartnerClaimType="http://schemas.xmlsoap.org/ws/2005/05/identity/claim
s/givenname" />
        </DefaultPartnerClaimTypes>
        <UserHelpText>Your given name (also known as first name).
</UserHelpText>
        <UserInputType>TextBox</UserInputType>
      </ClaimType>
      <ClaimType Id="surname">
        <DisplayName>Surname</DisplayName>
        <DataType>string</DataType>
        <DefaultPartnerClaimTypes>
          <Protocol Name="OAuth2" PartnerClaimType="family_name" />
          <Protocol Name="OpenIdConnect"
PartnerClaimType="family_name" />
          <Protocol Name="SAML2"
PartnerClaimType="http://schemas.xmlsoap.org/ws/2005/05/identity/claim
s/surname" />
        </DefaultPartnerClaimTypes>
        <UserHelpText>Your surname (also known as family name or last
name).</UserHelpText>
        <UserInputType>TextBox</UserInputType>
      </ClaimType>
      <ClaimType Id="mail">
        <DisplayName>mail</DisplayName>
        <DataType>string</DataType>
        <DefaultPartnerClaimTypes>
          <Protocol Name="OAuth2" PartnerClaimType="mail" />
          <Protocol Name="OpenIdConnect" PartnerClaimType="mail" />
          <Protocol Name="SAML2"
PartnerClaimType="http://schemas.xmlsoap.org/ws/2005/05/identity/claim
s/mail" />
        </DefaultPartnerClaimTypes>
        <UserHelpText>mail</UserHelpText>
        <UserInputType>TextBox</UserInputType>
      </ClaimType>
      <ClaimType Id="extension_stellar_privilege">
        <DisplayName>stellar_privilege</DisplayName>
        <DataType>string</DataType>

351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437

        <DefaultPartnerClaimTypes>
Your file will look similar to this:
          <Protocol Name="OAuth2" PartnerClaimType="mail" />
          <Protocol Name="OpenIdConnect" PartnerClaimType="mail" />
          <Protocol Name="SAML2" PartnerClaimType="stellar_privilege"
TrustFrameworkLocalization.xml
/>
        </DefaultPartnerClaimTypes>
        <UserHelpText>stellar_privilege</UserHelpText>
        <UserInputType>TextBox</UserInputType>
      </ClaimType>
      <ClaimType Id="extension_stellar_scope">
        <DisplayName>stellar_scope</DisplayName>
        <DataType>string</DataType>
        <DefaultPartnerClaimTypes>
          <Protocol Name="OAuth2" PartnerClaimType="mail" />
          <Protocol Name="OpenIdConnect" PartnerClaimType="mail" />
          <Protocol Name="SAML2" PartnerClaimType="stellar_scope" />
        </DefaultPartnerClaimTypes>
        <UserHelpText>stellar_scope</UserHelpText>
        <UserInputType>TextBox</UserInputType>
      </ClaimType>
      <ClaimType Id="extension_stellar_tenant">
        <DisplayName>stellar_tenant</DisplayName>
        <DataType>string</DataType>
        <DefaultPartnerClaimTypes>
          <Protocol Name="OAuth2" PartnerClaimType="mail" />
          <Protocol Name="OpenIdConnect" PartnerClaimType="mail" />
          <Protocol Name="SAML2" PartnerClaimType="stellar_tenant" />
        </DefaultPartnerClaimTypes>
        <UserHelpText>stellar_tenant</UserHelpText>
        <UserInputType>TextBox</UserInputType>
      </ClaimType>
      <ClaimType Id="extension_stellar_tenant_group">
        <DisplayName>stellar_tenant_group</DisplayName>
        <DataType>string</DataType>
        <DefaultPartnerClaimTypes>
          <Protocol Name="OAuth2" PartnerClaimType="mail" />
          <Protocol Name="OpenIdConnect" PartnerClaimType="mail" />
          <Protocol Name="SAML2"
PartnerClaimType="stellar_tenant_group" />
        </DefaultPartnerClaimTypes>
        <UserHelpText>stellar_tenant_group</UserHelpText>
        <UserInputType>TextBox</UserInputType>
      </ClaimType>
    </ClaimsSchema>
    <ClaimsTransformations>
      <ClaimsTransformation Id="CreateOtherMailsFromEmail"
TransformationMethod="AddItemToStringCollection">
        <InputClaims>
          <InputClaim ClaimTypeReferenceId="email"
TransformationClaimType="item" />
          <InputClaim ClaimTypeReferenceId="otherMails"
TransformationClaimType="collection" />
        </InputClaims>
        <OutputClaims>
          <OutputClaim ClaimTypeReferenceId="otherMails"
TransformationClaimType="collection" />
        </OutputClaims>
      </ClaimsTransformation>
      <ClaimsTransformation Id="AssertAccountEnabledIsTrue"
TransformationMethod="AssertBooleanClaimIsEqualToValue">
        <InputClaims>
          <InputClaim ClaimTypeReferenceId="accountEnabled"
TransformationClaimType="inputClaim" />
        </InputClaims>
        <InputParameters>
          <InputParameter Id="valueToCompareTo" DataType="boolean"
Value="true" />
        </InputParameters>
      </ClaimsTransformation>
    </ClaimsTransformations>
    <ClientDefinitions>
Edit TrustFrameworkExtensions.xml
      <ClientDefinition Id="DefaultWeb">
        <ClientUIFilterFlags>LineMarkers,
MetaRefresh</ClientUIFilterFlags>
Steps
      </ClientDefinition>
    </ClientDefinitions>
1. Some of the edits for this file were completed with the Global edits you made
    <ContentDefinitions>
      <!-- This content definition is to render an error page that
above. Edit the file ending with TrustFrameworkExtensions.xml and ensure
displays unhandled errors. -->
      <ContentDefinition Id="api.error">
the highlighted values were made.
        <LoadUri>~/tenant/templates/AzureBlue/exception.cshtml</LoadUr
i>
        <RecoveryUri>~/common/default_page_error.html</RecoveryUri>
<TrustFrameworkPolicy
        <DataUri>urn:com:microsoft:aad:b2c:elements:contract:globalexc
eption:1.2.1</DataUri>
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        <Metadata>
          <Item Key="DisplayName">Error page</Item>

438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524

        </Metadata>
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
      </ContentDefinition>
      <ContentDefinition Id="api.idpselections">
xmlns="http://schemas.microsoft.com/online/cpim/schemas/20
        <LoadUri>~/tenant/templates/AzureBlue/idpSelector.cshtml</Load
Uri>
13/06" PolicySchemaVersion="0.3.0.0"
        <RecoveryUri>~/common/default_page_error.html</RecoveryUri>
TenantId="stellarpmb2c.onmicrosoft.com"
        <DataUri>urn:com:microsoft:aad:b2c:elements:contract:providers
election:1.2.1</DataUri>
PolicyId="B2C_1A_TrustFrameworkExtensions"
        <Metadata>
          <Item Key="DisplayName">Idp selection page</Item>
PublicPolicyUri="http://stellarpmb2c.onmicrosoft.com/B2C_1
          <Item Key="language.intro">Sign in</Item>
        </Metadata>
A_TrustFrameworkExtensions" TenantObjectId="04fcef19-20fe-
      </ContentDefinition>
      <ContentDefinition Id="api.idpselections.signup">
4655-9498-3e5050b6dda1>
        <LoadUri>~/tenant/templates/AzureBlue/idpSelector.cshtml</Load
Uri>
2. Make the following additional edits, referring to the values you copied to your
        <RecoveryUri>~/common/default_page_error.html</RecoveryUri>
        <DataUri>urn:com:microsoft:aad:b2c:elements:contract:providers
worksheet.
election:1.2.1</DataUri>
        <Metadata>
          <Item Key="DisplayName">Idp selection page</Item>
Replace the values below with the Application (client) ID you saved for the
          <Item Key="language.intro">Sign up</Item>
        </Metadata>
ProxyIdentityExperienceFramework app.
      </ContentDefinition>
      <ContentDefinition Id="api.signuporsignin">
<Item Key="client_id">0c54849b-121f-496e-b1c3-
        <LoadUri>~/tenant/templates/AzureBlue/unified.cshtml</LoadUri>
        <RecoveryUri>~/common/default_page_error.html</RecoveryUri>
406976bec48b</Item>
        <DataUri>urn:com:microsoft:aad:b2c:elements:contract:unifiedss
p:2.1.5</DataUri>
        <Metadata>
<InputClaim ClaimTypeReferenceId="client_id"
          <Item Key="DisplayName">Signin and Signup</Item>
        </Metadata>
DefaultValue="0c54849b-121f-496e-b1c3-406976bec48b" />
      </ContentDefinition>
      <ContentDefinition Id="api.selfasserted">
Replace the values below with the Application (client) ID you saved for the
        <LoadUri>~/tenant/templates/AzureBlue/selfAsserted.cshtml</Loa
dUri>
IdentityExperienceFramework app.
        <RecoveryUri>~/common/default_page_error.html</RecoveryUri>
        <DataUri>urn:com:microsoft:aad:b2c:elements:contract:selfasser
<Item Key="IdTokenAudience">01590824-a092-4271-99a3-
ted:2.1.7</DataUri>
        <Metadata>
f3e37b9f22cc</Item>
          <Item Key="DisplayName">Collect information from user
page</Item>
        </Metadata>
<InputClaim ClaimTypeReferenceId="resource_id"
      </ContentDefinition>
      <ContentDefinition Id="api.selfasserted.profileupdate">
PartnerClaimType="resource" DefaultValue="01590824-a092-
        <LoadUri>~/tenant/templates/AzureBlue/selfAsserted.cshtml</Loa
dUri>
4271-99a3-f3e37b9f22cc" />
        <RecoveryUri>~/common/default_page_error.html</RecoveryUri>
        <DataUri>urn:com:microsoft:aad:b2c:elements:contract:selfasser
Replace the value for ClientId with the Application (client) ID you saved
ted:2.1.7</DataUri>
        <Metadata>
for the b2c-extensions-app.
          <Item Key="DisplayName">Collect information from user
page</Item>
        </Metadata>
<Item Key="ClientId">0c0abe38-79ab-45d3-99fe-
      </ContentDefinition>
9378eec7b16f</Item>
      <ContentDefinition Id="api.localaccountsignup">
        <LoadUri>~/tenant/templates/AzureBlue/selfAsserted.cshtml</Loa
dUri>
Replace the value for ApplicationObjectId with the Object ID you saved
        <RecoveryUri>~/common/default_page_error.html</RecoveryUri>
        <DataUri>urn:com:microsoft:aad:b2c:elements:contract:selfasser
for the b2c-extensions-app.
ted:2.1.7</DataUri>
        <Metadata>
<Item Key="ApplicationObjectId">3c34826e-3bd5-47a2-b44d-
          <Item Key="DisplayName">Local account sign up page</Item>
        </Metadata>
08c09034cef2</Item>
      </ContentDefinition>
      <ContentDefinition Id="api.localaccountpasswordreset">
        <LoadUri>~/tenant/templates/AzureBlue/selfAsserted.cshtml</Loa
dUri>
        <RecoveryUri>~/common/default_page_error.html</RecoveryUri>
        <DataUri>urn:com:microsoft:aad:b2c:elements:contract:selfasser
ted:2.1.7</DataUri>
        <Metadata>
          <Item Key="DisplayName">Local account change password
page</Item>
        </Metadata>
      </ContentDefinition>
      <ContentDefinition Id="api.localaccountsignin">
        <LoadUri>~/tenant/templates/AzureBlue/selfAsserted.cshtml</Loa
dUri>
        <RecoveryUri>~/common/default_page_error.html</RecoveryUri>
        <DataUri>urn:com:microsoft:aad:b2c:elements:contract:selfasser
ted:2.1.7</DataUri>
        <Metadata>
          <Item Key="DisplayName">Collect information from user
page</Item>
        </Metadata>
      </ContentDefinition>

525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611

    </ContentDefinitions>
If you are configuring standard authentication, your file will look similar to this:
  </BuildingBlocks>
  <!--
        A list of all the claim providers that can be used in the
TrustFrameworkExtensions.xml
technical policies. If a claims provider is not listed
        in this section, then it cannot be used in a technical policy.
    -->
  <ClaimsProviders>
    <ClaimsProvider>
      <DisplayName>Local Account SignIn</DisplayName>
      <TechnicalProfiles>
        <TechnicalProfile Id="login-NonInteractive">
          <DisplayName>Local Account SignIn</DisplayName>
          <Protocol Name="OpenIdConnect" />
          <Metadata>
            <Item Key="ProviderName">https://sts.windows.net/</Item>
            <Item
Key="METADATA">https://login.microsoftonline.com/{tenant}/.well-
known/openid-configuration</Item>
            <Item
Key="authorization_endpoint">https://login.microsoftonline.com/{tenant
}/oauth2/token</Item>
            <Item Key="response_types">id_token</Item>
            <Item Key="response_mode">query</Item>
            <Item Key="scope">email openid</Item>
            <!-- <Item Key="grant_type">password</Item> -->
            <!-- Policy Engine Clients -->
            <Item Key="UsePolicyInRedirectUri">false</Item>
            <Item Key="HttpBinding">POST</Item>
            <Item
Key="client_id">ProxyIdentityExperienceFrameworkAppId</Item>
            <Item
Key="IdTokenAudience">IdentityExperienceFrameworkAppId</Item>
          </Metadata>
          <InputClaims>
            <InputClaim ClaimTypeReferenceId="signInName"
PartnerClaimType="username" Required="true" />
            <InputClaim ClaimTypeReferenceId="password"
Required="true" />
            <InputClaim ClaimTypeReferenceId="grant_type"
DefaultValue="password" AlwaysUseDefaultValue="true" />
            <InputClaim ClaimTypeReferenceId="scope"
DefaultValue="openid" AlwaysUseDefaultValue="true" />
            <InputClaim ClaimTypeReferenceId="nca"
PartnerClaimType="nca" DefaultValue="1" />
            <InputClaim ClaimTypeReferenceId="client_id"
DefaultValue="ProxyIdentityExperienceFrameworkAppID" />
            <InputClaim ClaimTypeReferenceId="resource_id"
PartnerClaimType="resource"
DefaultValue="IdentityExperienceFrameworkAppID" />
          </InputClaims>
          <OutputClaims>
            <OutputClaim ClaimTypeReferenceId="objectId"
PartnerClaimType="oid" />
            <OutputClaim ClaimTypeReferenceId="tenantId"
PartnerClaimType="tid" />
            <OutputClaim ClaimTypeReferenceId="givenName"
PartnerClaimType="given_name" />
            <OutputClaim ClaimTypeReferenceId="surName"
PartnerClaimType="family_name" />
            <OutputClaim ClaimTypeReferenceId="displayName"
PartnerClaimType="name" />
            <OutputClaim ClaimTypeReferenceId="userPrincipalName"
PartnerClaimType="upn" />
            <OutputClaim ClaimTypeReferenceId="authenticationSource"
DefaultValue="localAccountAuthentication" />
          </OutputClaims>
        </TechnicalProfile>
        <TechnicalProfile Id="Saml2AssertionIssuer">
          <DisplayName>Token Issuer</DisplayName>
          <Protocol Name="SAML2" />
          <OutputTokenFormat>SAML2</OutputTokenFormat>
          <Metadata>
            <Item
Key="IssuerUri">https://stellarpmb2c.b2clogin.com/stellarpmb2c.onmicro
soft.com/B2C_1A_signup_signin_SAML</Item>
            <Item Key="TokenNotBeforeSkewInSeconds">600</Item>
          </Metadata>
          <CryptographicKeys>
            <Key Id="MetadataSigning"
StorageReferenceId="B2C_1A_SamlIdpCert" />
            <Key Id="SamlMessageSigning"
StorageReferenceId="B2C_1A_SamlIdpCert" />
            <Key Id="SamlAssertionSigning"
StorageReferenceId="B2C_1A_SamlIdpCert" />
          </CryptographicKeys>
          <InputClaims />

612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698

          <OutputClaims />
If you are configuring Azure native multi-factor authentication, your file will look
          <UseTechnicalProfileForSessionManagement ReferenceId="SM-
Saml-issuer" />
        </TechnicalProfile>
        <TechnicalProfile Id="SM-Saml-issuer">
          <DisplayName>Session Management Provider</DisplayName>
          <Protocol Name="Proprietary"
Handler="Web.TPEngine.SSO.SamlSSOSessionProvider, Web.TPEngine,
Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
        </TechnicalProfile>
      </TechnicalProfiles>
    </ClaimsProvider>
    <ClaimsProvider>
      <DisplayName>Azure Active Directory</DisplayName>
      <TechnicalProfiles>
        <TechnicalProfile Id="AAD-Common">
          <DisplayName>Azure Active Directory</DisplayName>
          <Protocol Name="Proprietary"
Handler="Web.TPEngine.Providers.AzureActiveDirectoryProvider,
Web.TPEngine, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null"
/>
          <CryptographicKeys>
            <Key Id="issuer_secret"
StorageReferenceId="B2C_1A_TokenSigningKeyContainer" />
          </CryptographicKeys>
          <!-- We need this here to suppress the SelfAsserted provider
from invoking SSO on validation profiles. -->
          <IncludeInSso>false</IncludeInSso>
          <UseTechnicalProfileForSessionManagement ReferenceId="SM-
Noop" />
        </TechnicalProfile>
        <!-- Technical profiles for local accounts -->
        <TechnicalProfile Id="AAD-UserWriteUsingLogonEmail">
          <Metadata>
            <Item Key="Operation">Write</Item>
            <Item
Key="RaiseErrorIfClaimsPrincipalAlreadyExists">true</Item>
          </Metadata>
          <IncludeInSso>false</IncludeInSso>
          <InputClaims>
            <InputClaim ClaimTypeReferenceId="email"
PartnerClaimType="signInNames.emailAddress" Required="true" />
          </InputClaims>
          <PersistedClaims>
            <!-- Required claims -->
            <PersistedClaim ClaimTypeReferenceId="email"
PartnerClaimType="signInNames.emailAddress" />
            <PersistedClaim ClaimTypeReferenceId="newPassword"
PartnerClaimType="password" />
            <PersistedClaim ClaimTypeReferenceId="displayName"
DefaultValue="unknown" />
            <PersistedClaim ClaimTypeReferenceId="passwordPolicies"
DefaultValue="DisablePasswordExpiration" />
            <!-- Optional claims. -->
            <PersistedClaim ClaimTypeReferenceId="givenName" />
            <PersistedClaim ClaimTypeReferenceId="surname" />
            <PersistedClaim ClaimTypeReferenceId="userPrincipalName"
/>
            <PersistedClaim ClaimTypeReferenceId="mail" />
            <PersistedClaim
ClaimTypeReferenceId="extension_stellar_privilege" />
            <PersistedClaim
ClaimTypeReferenceId="extension_stellar_scope" />
            <PersistedClaim
ClaimTypeReferenceId="extension_stellar_tenant" />
            <PersistedClaim
ClaimTypeReferenceId="extension_stellar_tenant_group" />
          </PersistedClaims>
          <OutputClaims>
            <OutputClaim ClaimTypeReferenceId="objectId" />
            <OutputClaim ClaimTypeReferenceId="newUser"
PartnerClaimType="newClaimsPrincipalCreated" />
            <OutputClaim ClaimTypeReferenceId="authenticationSource"
DefaultValue="localAccountAuthentication" />
            <OutputClaim ClaimTypeReferenceId="userPrincipalName" />
            <OutputClaim
ClaimTypeReferenceId="signInNames.emailAddress" />
          </OutputClaims>
          <IncludeTechnicalProfile ReferenceId="AAD-Common" />
          <UseTechnicalProfileForSessionManagement ReferenceId="SM-
AAD" />
        </TechnicalProfile>
        <TechnicalProfile Id="AAD-UserReadUsingEmailAddress">
          <Metadata>
            <Item Key="Operation">Read</Item>
            <Item
Key="RaiseErrorIfClaimsPrincipalDoesNotExist">true</Item>

699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
747
748
749
750
751
752
753
754
755
756
757
758
759
760
761
762
763
764
765
766
767
768
769
770
771
772
773
774
775
776
777
778
779
780
781
782
783
784
785

          </Metadata>
similar to this:
          <IncludeInSso>false</IncludeInSso>
          <InputClaims>
            <InputClaim ClaimTypeReferenceId="email"
TrustFrameworkExtensions.xml (MFA)
PartnerClaimType="signInNames.emailAddress" Required="true" />
          </InputClaims>
          <OutputClaims>
            <!-- Required claims -->
            <OutputClaim ClaimTypeReferenceId="objectId" />
            <OutputClaim ClaimTypeReferenceId="authenticationSource"
DefaultValue="localAccountAuthentication" />
            <!-- Optional claims -->
            <OutputClaim ClaimTypeReferenceId="userPrincipalName" />
            <OutputClaim ClaimTypeReferenceId="displayName" />
            <OutputClaim ClaimTypeReferenceId="accountEnabled" />
            <OutputClaim ClaimTypeReferenceId="otherMails" />
            <OutputClaim
ClaimTypeReferenceId="signInNames.emailAddress" />
          </OutputClaims>
          <OutputClaimsTransformations>
            <OutputClaimsTransformation
ReferenceId="AssertAccountEnabledIsTrue" />
          </OutputClaimsTransformations>
          <IncludeTechnicalProfile ReferenceId="AAD-Common" />
        </TechnicalProfile>
        <TechnicalProfile Id="AAD-UserWritePasswordUsingObjectId">
          <Metadata>
            <Item Key="Operation">Write</Item>
            <Item
Key="RaiseErrorIfClaimsPrincipalDoesNotExist">true</Item>
          </Metadata>
          <IncludeInSso>false</IncludeInSso>
          <InputClaims>
            <InputClaim ClaimTypeReferenceId="objectId"
Required="true" />
          </InputClaims>
          <PersistedClaims>
            <PersistedClaim ClaimTypeReferenceId="objectId" />
            <PersistedClaim ClaimTypeReferenceId="newPassword"
PartnerClaimType="password" />
          </PersistedClaims>
          <IncludeTechnicalProfile ReferenceId="AAD-Common" />
        </TechnicalProfile>
        <!-- Technical profiles for updating user record using
objectId -->
        <TechnicalProfile Id="AAD-UserWriteProfileUsingObjectId">
          <Metadata>
            <Item Key="Operation">Write</Item>
            <Item
Key="RaiseErrorIfClaimsPrincipalAlreadyExists">false</Item>
            <Item
Key="RaiseErrorIfClaimsPrincipalDoesNotExist">true</Item>
          </Metadata>
          <IncludeInSso>false</IncludeInSso>
          <InputClaims>
            <InputClaim ClaimTypeReferenceId="objectId"
Required="true" />
          </InputClaims>
          <PersistedClaims>
            <!-- Required claims -->
            <PersistedClaim ClaimTypeReferenceId="objectId" />
            <!-- Optional claims -->
            <PersistedClaim ClaimTypeReferenceId="givenName" />
            <PersistedClaim ClaimTypeReferenceId="surname" />
            <PersistedClaim ClaimTypeReferenceId="userPrincipalName"
/>
            <PersistedClaim ClaimTypeReferenceId="mail" />
            <PersistedClaim
ClaimTypeReferenceId="extension_stellar_privilege" />
            <PersistedClaim
ClaimTypeReferenceId="extension_stellar_scope" />
Edit SignUpOrSignin.xml
            <PersistedClaim
ClaimTypeReferenceId="extension_stellar_tenant" />
            <PersistedClaim
Steps
ClaimTypeReferenceId="extension_stellar_tenant_group" />
          </PersistedClaims>
The edits for this file should have been completed with the Global edits you
          <IncludeTechnicalProfile ReferenceId="AAD-Common" />
        </TechnicalProfile>
made above. Edit the file ending with SignUpOrSignIn.xml and ensure the
        <!-- The following technical profile is used to read data
after user authenticates. -->
highlighted values are consistent with the values you recorded on your
        <TechnicalProfile Id="AAD-UserReadUsingObjectId">
          <Metadata>
worksheet.
            <Item Key="Operation">Read</Item>
            <Item
Key="RaiseErrorIfClaimsPrincipalDoesNotExist">true</Item>
          </Metadata>
          <IncludeInSso>false</IncludeInSso>

786
787
788
789
790
791
792
793
794
795
796
797
798
799
800
801
802
803
804
805
806
807
808
809
810
811
812
813
814
815
816
817
818
819
820
821
822
823
824
825
826
827
828
829
830
831
832
833
834
835
836
837
838
839
840
841
842
843
844
845
846
847
848
849
850
851
852
853
854
855
856
857
858
859
860
861
862
863
864
865
866
867
868
869
870
871
872

          <InputClaims>
<TrustFrameworkPolicy
            <InputClaim ClaimTypeReferenceId="objectId"
Required="true" />
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          </InputClaims>
          <OutputClaims>
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
            <!-- Optional claims -->
xmlns="http://schemas.microsoft.com/online/cpim/schemas/20
            <OutputClaim
ClaimTypeReferenceId="signInNames.emailAddress" />
13/06" PolicySchemaVersion="0.3.0.0"
            <OutputClaim ClaimTypeReferenceId="displayName" />
            <OutputClaim ClaimTypeReferenceId="otherMails" />
TenantId="stellarpmb2c.onmicrosoft.com"
            <OutputClaim ClaimTypeReferenceId="givenName" />
            <OutputClaim ClaimTypeReferenceId="surname" />
PolicyId="B2C_1A_signup_signin"
            <OutputClaim ClaimTypeReferenceId="userPrincipalName" />
            <OutputClaim ClaimTypeReferenceId="mail" />
PublicPolicyUri="http://stellarpmb2c.onmicrosoft.com/B2C_1
            <OutputClaim
ClaimTypeReferenceId="extension_stellar_privilege" />
A_signup_signin" TenantObjectId="04fcef19-20fe-4655-9498-
            <OutputClaim
ClaimTypeReferenceId="extension_stellar_scope" />
3e5050b6dda1>
            <OutputClaim
ClaimTypeReferenceId="extension_stellar_tenant" />
and
            <OutputClaim
ClaimTypeReferenceId="extension_stellar_tenant_group" />
          </OutputClaims>
<TenantId>stellarpmb2c.onmicrosoft.com</TenantId>
          <IncludeTechnicalProfile ReferenceId="AAD-Common" />
        </TechnicalProfile>
      </TechnicalProfiles>
    </ClaimsProvider>
    <ClaimsProvider>
      <DisplayName>Self Asserted</DisplayName>
      <TechnicalProfiles>
        <TechnicalProfile Id="SelfAsserted-ProfileUpdate">
          <DisplayName>User ID signup</DisplayName>
          <Protocol Name="Proprietary"
Handler="Web.TPEngine.Providers.SelfAssertedAttributeProvider,
Web.TPEngine, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null"
/>
          <Metadata>
            <Item
Key="ContentDefinitionReferenceId">api.selfasserted.profileupdate</Ite
m>
          </Metadata>
          <IncludeInSso>false</IncludeInSso>
          <InputClaims>
            <InputClaim ClaimTypeReferenceId="userPrincipalName" />
            <!-- Optional claims. These claims are collected from the
user and can be modified. Any claim added here should be updated in
the
                 ValidationTechnicalProfile referenced below so it can
be written to directory after being updated by the user, i.e. AAD-
UserWriteProfileUsingObjectId. -->
            <InputClaim ClaimTypeReferenceId="givenName" />
            <InputClaim ClaimTypeReferenceId="surname" />
            <InputClaim ClaimTypeReferenceId="userPrincipalName" />
            <InputClaim ClaimTypeReferenceId="mail" />
            <InputClaim
ClaimTypeReferenceId="extension_stellar_privilege" />
            <InputClaim ClaimTypeReferenceId="extension_stellar_scope"
/>
            <InputClaim
ClaimTypeReferenceId="extension_stellar_tenant" />
            <InputClaim
ClaimTypeReferenceId="extension_stellar_tenant_group" />
          </InputClaims>
          <OutputClaims>
            <!-- Required claims -->
            <OutputClaim ClaimTypeReferenceId="executed-SelfAsserted-
Input" DefaultValue="true" />
            <!-- Optional claims. These claims are collected from the
user and can be modified. Any claim added here should be updated in
the
                 ValidationTechnicalProfile referenced below so it can
be written to directory after being updated by the user, i.e. AAD-
UserWriteProfileUsingObjectId. -->
            <OutputClaim ClaimTypeReferenceId="givenName" />
            <OutputClaim ClaimTypeReferenceId="surname" />
            <OutputClaim ClaimTypeReferenceId="userPrincipalName" />
            <OutputClaim ClaimTypeReferenceId="mail" />
            <OutputClaim
ClaimTypeReferenceId="extension_stellar_privilege" />
            <OutputClaim
ClaimTypeReferenceId="extension_stellar_scope" />
            <OutputClaim
ClaimTypeReferenceId="extension_stellar_tenant" />
            <OutputClaim
ClaimTypeReferenceId="extension_stellar_tenant_group" />
          </OutputClaims>
          <ValidationTechnicalProfiles>

            <ValidationTechnicalProfile ReferenceId="AAD-
Your file will look similar to this:
UserWriteProfileUsingObjectId" />
          </ValidationTechnicalProfiles>
        </TechnicalProfile>
SignUpOrSignIn
      </TechnicalProfiles>
    </ClaimsProvider>
    <ClaimsProvider>
      <DisplayName>Local Account</DisplayName>
      <TechnicalProfiles>
        <TechnicalProfile Id="LocalAccountSignUpWithLogonEmail">
          <DisplayName>Email signup</DisplayName>
          <Protocol Name="Proprietary"
Handler="Web.TPEngine.Providers.SelfAssertedAttributeProvider,
Web.TPEngine, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null"
/>
          <Metadata>
            <Item Key="IpAddressClaimReferenceId">IpAddress</Item>
            <Item
Key="ContentDefinitionReferenceId">api.localaccountsignup</Item>
          </Metadata>
          <CryptographicKeys>
            <Key Id="issuer_secret"
StorageReferenceId="B2C_1A_TokenSigningKeyContainer" />
          </CryptographicKeys>
          <InputClaims>
            <InputClaim ClaimTypeReferenceId="email" />
          </InputClaims>
          <OutputClaims>
            <OutputClaim ClaimTypeReferenceId="objectId" />

873
874
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
890
891
892
893
894
895
896
897
898
899
900
901
            <OutputClaim ClaimTypeReferenceId="email"
<TrustFrameworkPolicy xmlns:xsi="http://www.w3.org/2001/XMLSchema-
PartnerClaimType="Verified.Email" Required="true" />
            <OutputClaim ClaimTypeReferenceId="newPassword" Required="true"
instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema"
xmlns="http://schemas.microsoft.com/online/cpim/schemas/2013/06"
/>
PolicySchemaVersion="0.3.0.0" TenantId="stellarpmb2c.onmicrosoft.com"
            <OutputClaim ClaimTypeReferenceId="reenterPassword"
PolicyId="B2C_1A_TrustFrameworkBase"
Required="true" />
            <OutputClaim ClaimTypeReferenceId="executed-SelfAsserted-Input"
PublicPolicyUri="http://stellarpmb2c.onmicrosoft.com/B2C_1A_TrustFrame
workBase" TenantObjectId="04fcef19-20fe-4655-9498-3e5050b6dda1">
DefaultValue="true" />
  <BuildingBlocks>
            <OutputClaim ClaimTypeReferenceId="authenticationSource" />
    <ClaimsSchema>
            <OutputClaim ClaimTypeReferenceId="newUser" />
      <!-- The ClaimsSchema is divided into three sections:
            <!-- Optional claims, to be collected from the user -->
           1. Section I lists the minimum claims that are required for
            <OutputClaim ClaimTypeReferenceId="displayName" />
the user journeys to work properly.
            <OutputClaim ClaimTypeReferenceId="givenName" />
           2. Section II lists the claims required for query string
            <OutputClaim ClaimTypeReferenceId="surName" />
parameters and other special parameters
          </OutputClaims>
              to be passed to other claims providers, esp.
          <ValidationTechnicalProfiles>
login.microsoftonline.com for authentication.
            <ValidationTechnicalProfile ReferenceId="AAD-
              Please do not modify these claims.
UserWriteUsingLogonEmail" />
           3. Section III lists any additional (optional) claims that
          </ValidationTechnicalProfiles>
can be collected from the user, stored
          <UseTechnicalProfileForSessionManagement ReferenceId="SM-AAD" />
              in the directory and sent in tokens during sign in. Add
        </TechnicalProfile>
new claims to be collected from the user
        <!-- This technical profile uses a validation technical profile to
              and/or sent in the token in Section III. -->
authenticate the user. -->
      <!-- NOTE: The claims schema contains restrictions on certain
        <TechnicalProfile Id="SelfAsserted-LocalAccountSignin-Email">
claims such as passwords and usernames.
          <DisplayName>Local Account Signin</DisplayName>
           The trust framework policy treats Azure AD as any other
          <Protocol Name="Proprietary"
claims provider and all its restrictions
Handler="Web.TPEngine.Providers.SelfAssertedAttributeProvider, Web.TPEngine,
           are modelled in the policy. A policy could be modified to
Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
add more restrictions, or use another
          <Metadata>
           claims provider for credential storage which will have its
            <Item Key="SignUpTarget">SignUpWithLogonEmailExchange</Item>
own restrictions. -->
            <Item Key="setting.operatingMode">Email</Item>
            <Item
      <!-- SECTION I: Claims required for user journeys to work
properly -->
Key="ContentDefinitionReferenceId">api.localaccountsignin</Item>
      <ClaimType Id="socialIdpUserId">
            <Item Key="IncludeClaimResolvingInClaimsHandling">true</Item>
        <DisplayName>Username</DisplayName>
          </Metadata>
        <DataType>string</DataType>
          <IncludeInSso>false</IncludeInSso>
        <UserHelpText />
          <InputClaims>
        <UserInputType>TextBox</UserInputType>
            <InputClaim ClaimTypeReferenceId="signInName" DefaultValue="
        <Restriction>
{OIDC:LoginHint}" AlwaysUseDefaultValue="true" />
          <Pattern RegularExpression="^[a-zA-Z0-9]+[a-zA-Z0-9_-]*$"
          </InputClaims>
HelpText="The username you provided is not valid. It must begin with
          <OutputClaims>
an alphabet or number and can contain alphabets, numbers and the
            <OutputClaim ClaimTypeReferenceId="signInName" Required="true"
Edit ProfileEdit.xml
following symbols: _ -" />
/>
        </Restriction>
            <OutputClaim ClaimTypeReferenceId="password" Required="true" />
      </ClaimType>
            <OutputClaim ClaimTypeReferenceId="objectId" />
Steps
            <OutputClaim ClaimTypeReferenceId="authenticationSource" />
      <ClaimType Id="tenantId">
        <DisplayName>User's Object's Tenant ID</DisplayName>
          </OutputClaims>
The edits for this file should have been completed with the Global edits you
        <DataType>string</DataType>
          <ValidationTechnicalProfiles>
        <DefaultPartnerClaimTypes>
            <ValidationTechnicalProfile ReferenceId="login-NonInteractive"
made above. Edit the file ending with ProfileEdit.xml and ensure the
          <Protocol Name="OAuth2" PartnerClaimType="tid" />
/>
          <Protocol Name="OpenIdConnect" PartnerClaimType="tid" />
          </ValidationTechnicalProfiles>
highlighted values are consistent with the values you recorded on your
          <Protocol Name="SAML2"
          <UseTechnicalProfileForSessionManagement ReferenceId="SM-AAD" />
PartnerClaimType="http://schemas.microsoft.com/identity/claims/tenanti
        </TechnicalProfile>
worksheet.
d" />
        <!-- This technical profile forces the user to verify the email
        </DefaultPartnerClaimTypes>
address that they provide on the UI. Only after email is verified, the user
        <UserHelpText>Tenant identifier (ID) of the user object in
account is
Azure AD.</UserHelpText>
        read from the directory. -->
      </ClaimType>
        <TechnicalProfile Id="LocalAccountDiscoveryUsingEmailAddress">

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57

      <ClaimType Id="objectId">
          <DisplayName>Reset password using email address</DisplayName>
58
<TrustFrameworkPolicy
          <Protocol Name="Proprietary"
        <DisplayName>User's Object ID</DisplayName>
59
Handler="Web.TPEngine.Providers.SelfAssertedAttributeProvider, Web.TPEngine,
        <DataType>string</DataType>
60
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        <DefaultPartnerClaimTypes>
Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
61
          <Protocol Name="OAuth2" PartnerClaimType="oid" />
          <Metadata>
62
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
            <Item Key="IpAddressClaimReferenceId">IpAddress</Item>
          <Protocol Name="OpenIdConnect" PartnerClaimType="oid" />
63
xmlns="http://schemas.microsoft.com/online/cpim/schemas/20
          <Protocol Name="SAML2"
            <Item
64
PartnerClaimType="http://schemas.microsoft.com/identity/claims/objecti
Key="ContentDefinitionReferenceId">api.localaccountpasswordreset</Item>
65
13/06" PolicySchemaVersion="0.3.0.0"
dentifier" />
          </Metadata>
66
        </DefaultPartnerClaimTypes>
          <CryptographicKeys>
67
TenantId="stellarpmb2c.onmicrosoft.com"
        <UserHelpText>Object identifier (ID) of the user object in
            <Key Id="issuer_secret"
68
Azure AD.</UserHelpText>
StorageReferenceId="B2C_1A_TokenSigningKeyContainer" />
69
PolicyId="B2C_1A_ProfileEdit"
      </ClaimType>
          </CryptographicKeys>
70
          <IncludeInSso>false</IncludeInSso>
      <!-- Claims needed for local accounts. -->
71
PublicPolicyUri="http://stellarpmb2c.onmicrosoft.com/B2C_1
      <ClaimType Id="signInName">
          <OutputClaims>
72
        <DisplayName>Sign in name</DisplayName>
            <OutputClaim ClaimTypeReferenceId="email"
73
A_ProfileEdit" TenantObjectId="04fcef19-20fe-4655-9498-
        <DataType>string</DataType>
PartnerClaimType="Verified.Email" Required="true" />
74
        <UserHelpText />
            <OutputClaim ClaimTypeReferenceId="objectId" />
75
3e5050b6dda1">
        <UserInputType>TextBox</UserInputType>
            <OutputClaim ClaimTypeReferenceId="userPrincipalName" />
76
      </ClaimType>
            <OutputClaim ClaimTypeReferenceId="authenticationSource" />
77
and
      <ClaimType Id="signInNames.emailAddress">
          </OutputClaims>
78
        <DisplayName>Email Address</DisplayName>
          <ValidationTechnicalProfiles>
79
        <DataType>string</DataType>
            <ValidationTechnicalProfile ReferenceId="AAD-
80
<TenantId>stellarpmb2c.onmicrosoft.com</TenantId>
        <UserHelpText>Email address to use for signing in.
UserReadUsingEmailAddress" />
81
</UserHelpText>
          </ValidationTechnicalProfiles>
82
        <UserInputType>TextBox</UserInputType>
        </TechnicalProfile>
83
      </ClaimType>
        <TechnicalProfile Id="LocalAccountWritePasswordUsingObjectId">
84
          <DisplayName>Change password (username)</DisplayName>
      <ClaimType Id="accountEnabled">
85
        <DisplayName>Account Enabled</DisplayName>
          <Protocol Name="Proprietary"
86
Handler="Web.TPEngine.Providers.SelfAssertedAttributeProvider, Web.TPEngine,
        <DataType>boolean</DataType>
87
        <AdminHelpText>Specifies whether the user's account is
Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
88
enabled.</AdminHelpText>
          <Metadata>
89
        <UserHelpText>Specifies whether your account is enabled.
            <Item
90
</UserHelpText>
Key="ContentDefinitionReferenceId">api.localaccountpasswordreset</Item>
91
      </ClaimType>
          </Metadata>
92
      <ClaimType Id="password">
          <CryptographicKeys>
93
        <DisplayName>Password</DisplayName>
            <Key Id="issuer_secret"
94
        <DataType>string</DataType>
StorageReferenceId="B2C_1A_TokenSigningKeyContainer" />
95
        <UserHelpText>Enter password</UserHelpText>
          </CryptographicKeys>
96
        <UserInputType>Password</UserInputType>
          <InputClaims>
97
      </ClaimType>
            <InputClaim ClaimTypeReferenceId="objectId" />
98
      <!-- The claim types newPassword and reenterPassword are
          </InputClaims>
99
considered special, please do not change the names.
100
          <OutputClaims>
           The UI validates that the user correctly re-entered their
            <OutputClaim ClaimTypeReferenceId="newPassword" Required="true"
101
password during account creation based on these
/>
102
           claim types.      -->
103
            <OutputClaim ClaimTypeReferenceId="reenterPassword"
      <ClaimType Id="newPassword">
104
Required="true" />
        <DisplayName>New Password</DisplayName>
105
          </OutputClaims>
        <DataType>string</DataType>
106
          <ValidationTechnicalProfiles>
        <UserHelpText>Enter new password</UserHelpText>
            <ValidationTechnicalProfile ReferenceId="AAD-
107
        <UserInputType>Password</UserInputType>
UserWritePasswordUsingObjectId" />
108
        <Restriction>
109
          </ValidationTechnicalProfiles>
          <Pattern RegularExpression="^((?=.*[a-z])(?=.*[A-Z])(?
        </TechnicalProfile>
110
=.*\d)|(?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9])|(?=.*[a-z])(?=.*\d)(?
111
      </TechnicalProfiles>
=.*[^A-Za-z0-9])|(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]))([A-Za-
112
    </ClaimsProvider>
z\d@#$%^&amp;*\-_+=[\]{}|\\:',?/`~&quot;();!]|\.(?!@)){8,16}$"
    <ClaimsProvider>
113
HelpText="8-16 characters, containing 3 out of 4 of the following:
114
      <DisplayName>Session Management</DisplayName>
Lowercase characters, uppercase characters, digits (0-9), and one or
115
      <TechnicalProfiles>
more of the following symbols: @ # $ % ^ &amp; * - _ + = [ ] { } | \ :
116
        <TechnicalProfile Id="SM-Noop">
' , ? / ` ~ &quot; ( ) ; ." />
117
          <DisplayName>Noop Session Management Provider</DisplayName>
        </Restriction>
          <Protocol Name="Proprietary"
118
      </ClaimType>
Handler="Web.TPEngine.SSO.NoopSSOSessionProvider, Web.TPEngine,
119
      <!-- The password regular expression above is constructed for
120
Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
AAD passwords based on restrictions at https://msdn.microsoft.com/en-
121
        </TechnicalProfile>
us/library/azure/jj943764.aspx
122
        <TechnicalProfile Id="SM-AAD">
123
          <DisplayName>Session Mananagement Provider</DisplayName>
        ^( # one of the following four combinations must appear in the
          <Protocol Name="Proprietary"
124
password
Handler="Web.TPEngine.SSO.DefaultSSOSessionProvider, Web.TPEngine,
125
         (?=.*[a-z])(?=.*[A-Z])(?=.*\d) |            # matches lower
126
Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
case, upper case or digit
127
          <PersistedClaims>
         (?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9]) |  # matches lower
128
            <PersistedClaim ClaimTypeReferenceId="objectId" />
case, upper case or special character (i.e. non-alpha or digit)
129
            <PersistedClaim ClaimTypeReferenceId="signInName" />
         (?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9]) |     # matches lower
            <PersistedClaim ClaimTypeReferenceId="authenticationSource" />
130
case, digit, or special character
131
            <PersistedClaim ClaimTypeReferenceId="identityProvider" />
         (?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9])       # matches upper
132
            <PersistedClaim ClaimTypeReferenceId="newUser" />
case, digit, or special character
133
            <PersistedClaim ClaimTypeReferenceId="executed-SelfAsserted-
        )
134
Input" />
        ( # The password must match the following restrictions
          </PersistedClaims>
135
         [A-Za-z\d@#$%^&*\-_+=[\]{}|\\:',?/`~"();!] |   # The list of
          <OutputClaims>
136
all acceptable characters (without .)
137
            <OutputClaim ClaimTypeReferenceId="objectIdFromSession"
         \.(?!@)                                        # or . can
138
DefaultValue="true" />
appear as long as not followed by @
139
          </OutputClaims>
        ) {8,16}$                                       # the length
140
        </TechnicalProfile>
must be between 8 and 16 chars inclusive
        <!-- Session management technical profile for OIDC based tokens -->
141
142
        <TechnicalProfile Id="SM-jwt-issuer">
143
          <DisplayName>Session Management Provider</DisplayName>
          <Protocol Name="Proprietary"
144

      -->
      <ClaimType Id="reenterPassword">

        <DisplayName>Confirm New Password</DisplayName>
Handler="Web.TPEngine.SSO.OAuthSSOSessionProvider, Web.TPEngine,
145
Your file will look similar to this:
        <DataType>string</DataType>
146
Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
        <UserHelpText>Confirm new password</UserHelpText>
147
        </TechnicalProfile>
        <UserInputType>Password</UserInputType>
148
      </TechnicalProfiles>
ProfileEdit.xml
    </ClaimsProvider>
        <Restriction>
149
          <Pattern RegularExpression="^((?=.*[a-z])(?=.*[A-Z])(?
    <ClaimsProvider>
150
=.*\d)|(?=.*[a-z])(?=.*[A-Z])(?=.*[^A-Za-z0-9])|(?=.*[a-z])(?=.*\d)(?
151
      <DisplayName>Trustframework Policy Engine
=.*[^A-Za-z0-9])|(?=.*[A-Z])(?=.*\d)(?=.*[^A-Za-z0-9]))([A-Za-
152
TechnicalProfiles</DisplayName>
z\d@#$%^&amp;*\-_+=[\]{}|\\:',?/`~&quot;();!]|\.(?!@)){8,16}$"
153
      <TechnicalProfiles>
HelpText=" " />
154
        <TechnicalProfile Id="TpEngine_c3bd4fe2-1775-4013-b91d-
        </Restriction>
35f16d377d13">
155
      </ClaimType>
          <DisplayName>Trustframework Policy Engine Default Technical
156
      <ClaimType Id="passwordPolicies">
157
Profile</DisplayName>
        <DisplayName>Password Policies</DisplayName>
158
          <Protocol Name="None" />
        <DataType>string</DataType>
159
          <Metadata>
        <UserHelpText>Password policies used by Azure AD to determine
            <Item Key="url">{service:te}</Item>
160
password strength, expiry etc.</UserHelpText>
          </Metadata>
161
      </ClaimType>
        </TechnicalProfile>
162
      <ClaimType Id="client_id">
163
      </TechnicalProfiles>
        <DisplayName>client_id</DisplayName>
164
    </ClaimsProvider>
        <DataType>string</DataType>
165
    <ClaimsProvider>
        <AdminHelpText>Special parameter passed to EvoSTS.
166
      <DisplayName>Token Issuer</DisplayName>
</AdminHelpText>
      <TechnicalProfiles>
167
        <UserHelpText>Special parameter passed to EvoSTS.
168
        <TechnicalProfile Id="JwtIssuer">
</UserHelpText>
169
          <DisplayName>JWT Issuer</DisplayName>
      </ClaimType>
170
          <Protocol Name="OpenIdConnect" />
          <OutputTokenFormat>JWT</OutputTokenFormat>
      <ClaimType Id="resource_id">
171
        <DisplayName>resource_id</DisplayName>
          <Metadata>
172
        <DataType>string</DataType>
            <Item Key="client_id">{service:te}</Item>
173
        <AdminHelpText>Special parameter passed to EvoSTS.
174
            <Item
</AdminHelpText>
175
Key="issuer_refresh_token_user_identity_claim_type">objectId</Item>
        <UserHelpText>Special parameter passed to EvoSTS.
176
            <Item Key="SendTokenResponseBodyWithJsonNumbers">true</Item>
</UserHelpText>
          </Metadata>
177
      </ClaimType>
          <CryptographicKeys>
178
      <ClaimType Id="sub">
179
            <Key Id="issuer_secret"
        <DisplayName>Subject</DisplayName>
StorageReferenceId="B2C_1A_TokenSigningKeyContainer" />
180
            <Key Id="issuer_refresh_token_key"
        <DataType>string</DataType>
181
        <DefaultPartnerClaimTypes>
182
StorageReferenceId="B2C_1A_TokenEncryptionKeyContainer" />
          <Protocol Name="OpenIdConnect" PartnerClaimType="sub" />
          </CryptographicKeys>
183
        </DefaultPartnerClaimTypes>
          <UseTechnicalProfileForSessionManagement ReferenceId="SM-jwt-
184
        <UserHelpText />
185
issuer" />
      </ClaimType>
186
        </TechnicalProfile>
      <ClaimType Id="identityProvider">
187
      </TechnicalProfiles>
        <DisplayName>Identity Provider</DisplayName>
188
    </ClaimsProvider>
        <DataType>string</DataType>
  </ClaimsProviders>
189
        <DefaultPartnerClaimTypes>
190
  <UserJourneys>
          <Protocol Name="OAuth2" PartnerClaimType="idp" />
191
    <UserJourney Id="SignUpOrSignIn">
          <Protocol Name="OpenIdConnect" PartnerClaimType="idp" />
192
      <OrchestrationSteps>
          <Protocol Name="SAML2"
193
        <OrchestrationStep Order="1" Type="CombinedSignInAndSignUp"
PartnerClaimType="http://schemas.microsoft.com/identity/claims/identit
ContentDefinitionReferenceId="api.signuporsignin">
194
yprovider" />
          <ClaimsProviderSelections>
195
            <ClaimsProviderSelection
        </DefaultPartnerClaimTypes>
196
        <UserHelpText />
197
ValidationClaimsExchangeId="LocalAccountSigninEmailExchange" />
      </ClaimType>
198
          </ClaimsProviderSelections>
      <ClaimType Id="displayName">
199
          <ClaimsExchanges>
        <DisplayName>Display Name</DisplayName>
            <ClaimsExchange Id="LocalAccountSigninEmailExchange"
200
        <DataType>string</DataType>
201
TechnicalProfileReferenceId="SelfAsserted-LocalAccountSignin-Email" />
        <DefaultPartnerClaimTypes>
202
          </ClaimsExchanges>
          <Protocol Name="OAuth2" PartnerClaimType="unique_name" />
203
        </OrchestrationStep>
          <Protocol Name="OpenIdConnect" PartnerClaimType="name" />
204
        <OrchestrationStep Order="2" Type="ClaimsExchange">
          <Protocol Name="SAML2"
          <Preconditions>
205
PartnerClaimType="http://schemas.xmlsoap.org/ws/2005/05/identity/claim
            <Precondition Type="ClaimsExist" ExecuteActionsIf="true">
206
s/name" />
207
              <Value>objectId</Value>
        </DefaultPartnerClaimTypes>
208
              <Action>SkipThisOrchestrationStep</Action>
        <UserHelpText>Your display name.</UserHelpText>
209
            </Precondition>
        <UserInputType>TextBox</UserInputType>
210
          </Preconditions>
      </ClaimType>
          <ClaimsExchanges>
211
      <ClaimType Id="email">
            <ClaimsExchange Id="SignUpWithLogonEmailExchange"
212
        <DisplayName>Email Address</DisplayName>
213
TechnicalProfileReferenceId="LocalAccountSignUpWithLogonEmail" />
        <DataType>string</DataType>
214
          </ClaimsExchanges>
        <DefaultPartnerClaimTypes>
215
        </OrchestrationStep>
Edit PasswordReset.xml
          <Protocol Name="OpenIdConnect" PartnerClaimType="email" />
216
        <!-- This step reads any user attributes that we may not have
        </DefaultPartnerClaimTypes>
received when in the token. -->
217
        <UserHelpText>Email address that can be used to contact you.
218
        <OrchestrationStep Order="3" Type="ClaimsExchange">
Steps
</UserHelpText>
          <ClaimsExchanges>
219
        <UserInputType>TextBox</UserInputType>
            <ClaimsExchange Id="AADUserReadWithObjectId"
220
The edits for this file should have been completed with the Global edits you
        <Restriction>
221
TechnicalProfileReferenceId="AAD-UserReadUsingObjectId" />
          <Pattern RegularExpression="^[a-zA-Z0-
          </ClaimsExchanges>
222
made above. Edit the file ending with PasswordReset.xml and ensure the
9.!#$%&amp;'^_`{}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$"
        </OrchestrationStep>
223
HelpText="Please enter a valid email address." />
        <OrchestrationStep Order="4" Type="SendClaims"
224
highlighted values are consistent with the values you recorded on your
        </Restriction>
225
CpimIssuerTechnicalProfileReferenceId="JwtIssuer" />
      </ClaimType>
226
      </OrchestrationSteps>
worksheet.
      <ClaimType Id="otherMails">
227
      <ClientDefinition ReferenceId="DefaultWeb" />
        <DisplayName>Alternate Email Addresses</DisplayName>
    </UserJourney>
228
        <DataType>stringCollection</DataType>
229
    <UserJourney Id="ProfileEdit">
      <OrchestrationSteps>
        <UserHelpText>Email addresses that can be used to contact the
230
user.</UserHelpText>
        <OrchestrationStep Order="1" Type="ClaimsProviderSelection"
231

      </ClaimType>
ContentDefinitionReferenceId="api.idpselections">
232
<TrustFrameworkPolicy
      <ClaimType Id="userPrincipalName">
          <ClaimsProviderSelections>
233
        <DisplayName>UserPrincipalName</DisplayName>
234
            <ClaimsProviderSelection
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
TargetClaimsExchangeId="LocalAccountSigninEmailExchange" />
        <DataType>string</DataType>
235
        <DefaultPartnerClaimTypes>
236
          </ClaimsProviderSelections>
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
          <Protocol Name="OAuth2" PartnerClaimType="upn" />
        </OrchestrationStep>
237
xmlns="http://schemas.microsoft.com/online/cpim/schemas/20
          <Protocol Name="OpenIdConnect" PartnerClaimType="upn" />
238
        <OrchestrationStep Order="2" Type="ClaimsExchange">
          <Protocol Name="SAML2"
239
          <ClaimsExchanges>
13/06" PolicySchemaVersion="0.3.0.0"
PartnerClaimType="http://schemas.microsoft.com/identity/claims/userpri
240
            <ClaimsExchange Id="LocalAccountSigninEmailExchange"
ncipalname" />
241
TechnicalProfileReferenceId="SelfAsserted-LocalAccountSignin-Email" />
TenantId="stellarpmb2c.onmicrosoft.com"
        </DefaultPartnerClaimTypes>
          </ClaimsExchanges>
242
        <UserHelpText>Your user name as stored in the Azure Active
        </OrchestrationStep>
243
PolicyId="B2C_1A_PasswordReset"
Directory.</UserHelpText>
244
        <OrchestrationStep Order="3" Type="ClaimsExchange">
      </ClaimType>
245
          <ClaimsExchanges>
PublicPolicyUri="http://stellarpmb2c.onmicrosoft.com/B2C_1
      <ClaimType Id="upnUserName">
246
            <ClaimsExchange Id="AADUserReadWithObjectId"
        <DisplayName>UPN User Name</DisplayName>
247
TechnicalProfileReferenceId="AAD-UserReadUsingObjectId" />
A_PasswordReset" TenantObjectId="04fcef19-20fe-4655-9498-
        <DataType>string</DataType>
          </ClaimsExchanges>
248
        <UserHelpText>The user name for creating user principal name.
        </OrchestrationStep>
249
3e5050b6dda1">
</UserHelpText>
250
        <OrchestrationStep Order="4" Type="ClaimsExchange">
      </ClaimType>
          <ClaimsExchanges>
251
and
      <ClaimType Id="newUser">
252
            <ClaimsExchange Id="B2CUserProfileUpdateExchange"
        <DisplayName>User is new</DisplayName>
TechnicalProfileReferenceId="SelfAsserted-ProfileUpdate" />
253
        <DataType>boolean</DataType>
          </ClaimsExchanges>
254
<TenantId>stellarpmb2c.onmicrosoft.com</TenantId>
        <UserHelpText />
255
        </OrchestrationStep>
      </ClaimType>
256
        <OrchestrationStep Order="5" Type="SendClaims"
      <ClaimType Id="executed-SelfAsserted-Input">
257
CpimIssuerTechnicalProfileReferenceId="JwtIssuer" />
        <DisplayName>Executed-SelfAsserted-Input</DisplayName>
258
      </OrchestrationSteps>
        <DataType>string</DataType>
      <ClientDefinition ReferenceId="DefaultWeb" />
259
        <UserHelpText>A claim that specifies whether attributes were
    </UserJourney>
260
collected from the user.</UserHelpText>
261
    <UserJourney Id="PasswordReset">
      </ClaimType>
262
      <OrchestrationSteps>
      <ClaimType Id="authenticationSource">
263
        <OrchestrationStep Order="1" Type="ClaimsExchange">
        <DisplayName>AuthenticationSource</DisplayName>
264
          <ClaimsExchanges>
        <DataType>string</DataType>
            <ClaimsExchange Id="PasswordResetUsingEmailAddressExchange"
265
        <UserHelpText>Specifies whether the user was authenticated at
266
TechnicalProfileReferenceId="LocalAccountDiscoveryUsingEmailAddress" />
Social IDP or local account.</UserHelpText>
267
          </ClaimsExchanges>
      </ClaimType>
268
        </OrchestrationStep>
      <!-- SECTION II: Claims required to pass on special parameters
269
        <OrchestrationStep Order="2" Type="ClaimsExchange">
(including some query string parameters) to other claims providers -->
          <ClaimsExchanges>
270
      <ClaimType Id="nca">
            <ClaimsExchange Id="NewCredentials"
271
        <DisplayName>nca</DisplayName>
272
TechnicalProfileReferenceId="LocalAccountWritePasswordUsingObjectId" />
        <DataType>string</DataType>
273
          </ClaimsExchanges>
        <UserHelpText>Special parameter passed for local account
274
        </OrchestrationStep>
authentication to login.microsoftonline.com.</UserHelpText>
275
        <OrchestrationStep Order="3" Type="SendClaims"
      </ClaimType>
CpimIssuerTechnicalProfileReferenceId="JwtIssuer" />
276
      <ClaimType Id="grant_type">
277
      </OrchestrationSteps>
        <DisplayName>grant_type</DisplayName>
      <ClientDefinition ReferenceId="DefaultWeb" />
278
        <DataType>string</DataType>
279
    </UserJourney>
        <UserHelpText>Special parameter passed for local account
280
  </UserJourneys>
authentication to login.microsoftonline.com.</UserHelpText>
</TrustFrameworkPolicy>
281
      </ClaimType>
282
      <ClaimType Id="scope">
283
        <DisplayName>scope</DisplayName>
284
        <DataType>string</DataType>
285
        <UserHelpText>Special parameter passed for local account
286
authentication to login.microsoftonline.com.</UserHelpText>
287
      </ClaimType>
288
      <ClaimType Id="objectIdFromSession">
289
        <DisplayName>objectIdFromSession</DisplayName>
290
        <DataType>boolean</DataType>
291
        <UserHelpText>Parameter provided by the default session
292
management provider to indicate that the object id has been retrieved
293
from an SSO session.</UserHelpText>
294
      </ClaimType>
295
      <ClaimType Id="isActiveMFASession">
296
        <DisplayName>isActiveMFASession</DisplayName>
297
        <DataType>boolean</DataType>
298
        <UserHelpText>Parameter provided by the MFA session management
299
to indicate that the user has an active MFA session.</UserHelpText>
300
      </ClaimType>
301
      <!-- SECTION III: Additional claims that can be collected from
302
the users, stored in the directory, and sent in the token. Add
303
additional claims here. -->
304
      <ClaimType Id="givenName">
305
        <DisplayName>Given Name</DisplayName>
306
        <DataType>string</DataType>
307
        <DefaultPartnerClaimTypes>
308
          <Protocol Name="OAuth2" PartnerClaimType="given_name" />
309
          <Protocol Name="OpenIdConnect" PartnerClaimType="given_name"
310
/>
311
          <Protocol Name="SAML2"
312
PartnerClaimType="http://schemas.xmlsoap.org/ws/2005/05/identity/claim
313
s/givenname" />
314
        </DefaultPartnerClaimTypes>
315
        <UserHelpText>Your given name (also known as first name).
316
</UserHelpText>
317
        <UserInputType>TextBox</UserInputType>
318

319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405

      </ClaimType>
Your file will look similar to this:
      <ClaimType Id="surname">
        <DisplayName>Surname</DisplayName>
        <DataType>string</DataType>
PasswordReset.xml
        <DefaultPartnerClaimTypes>
          <Protocol Name="OAuth2" PartnerClaimType="family_name" />
          <Protocol Name="OpenIdConnect"
PartnerClaimType="family_name" />
          <Protocol Name="SAML2"
PartnerClaimType="http://schemas.xmlsoap.org/ws/2005/05/identity/claim
s/surname" />
        </DefaultPartnerClaimTypes>
        <UserHelpText>Your surname (also known as family name or last
name).</UserHelpText>
        <UserInputType>TextBox</UserInputType>
      </ClaimType>
      <ClaimType Id="mail">
        <DisplayName>mail</DisplayName>
        <DataType>string</DataType>
        <DefaultPartnerClaimTypes>
          <Protocol Name="OAuth2" PartnerClaimType="mail" />
          <Protocol Name="OpenIdConnect" PartnerClaimType="mail" />
          <Protocol Name="SAML2"
PartnerClaimType="http://schemas.xmlsoap.org/ws/2005/05/identity/claim
s/mail" />
        </DefaultPartnerClaimTypes>
        <UserHelpText>mail</UserHelpText>
        <UserInputType>TextBox</UserInputType>
      </ClaimType>
      <ClaimType Id="extension_stellar_privilege">
        <DisplayName>stellar_privilege</DisplayName>
        <DataType>string</DataType>
        <DefaultPartnerClaimTypes>
          <Protocol Name="OAuth2" PartnerClaimType="mail" />
          <Protocol Name="OpenIdConnect" PartnerClaimType="mail" />
          <Protocol Name="SAML2" PartnerClaimType="stellar_privilege"
/>
        </DefaultPartnerClaimTypes>
        <UserHelpText>stellar_privilege</UserHelpText>
        <UserInputType>TextBox</UserInputType>
      </ClaimType>
      <ClaimType Id="extension_stellar_scope">
        <DisplayName>stellar_scope</DisplayName>
        <DataType>string</DataType>
        <DefaultPartnerClaimTypes>
          <Protocol Name="OAuth2" PartnerClaimType="mail" />
          <Protocol Name="OpenIdConnect" PartnerClaimType="mail" />
          <Protocol Name="SAML2" PartnerClaimType="stellar_scope" />
        </DefaultPartnerClaimTypes>
        <UserHelpText>stellar_scope</UserHelpText>
        <UserInputType>TextBox</UserInputType>
      </ClaimType>
      <ClaimType Id="extension_stellar_tenant">
        <DisplayName>stellar_tenant</DisplayName>
        <DataType>string</DataType>
        <DefaultPartnerClaimTypes>
          <Protocol Name="OAuth2" PartnerClaimType="mail" />
          <Protocol Name="OpenIdConnect" PartnerClaimType="mail" />
          <Protocol Name="SAML2" PartnerClaimType="stellar_tenant" />
        </DefaultPartnerClaimTypes>
        <UserHelpText>stellar_tenant</UserHelpText>
        <UserInputType>TextBox</UserInputType>
      </ClaimType>
      <ClaimType Id="extension_stellar_tenant_group">
        <DisplayName>stellar_tenant_group</DisplayName>
        <DataType>string</DataType>
        <DefaultPartnerClaimTypes>
          <Protocol Name="OAuth2" PartnerClaimType="mail" />
          <Protocol Name="OpenIdConnect" PartnerClaimType="mail" />
          <Protocol Name="SAML2"
PartnerClaimType="stellar_tenant_group" />
Edit SignUporSigninSAML.xml
        </DefaultPartnerClaimTypes>
        <UserHelpText>stellar_tenant_group</UserHelpText>
        <UserInputType>TextBox</UserInputType>
Steps
      </ClaimType>
    </ClaimsSchema>
    <ClaimsTransformations>
      <ClaimsTransformation Id="CreateOtherMailsFromEmail"
made above. Edit the file ending with SignUpOrSigninSAML.xml and ensure
TransformationMethod="AddItemToStringCollection">
        <InputClaims>
the highlighted values are consistent with the values you recorded on your
          <InputClaim ClaimTypeReferenceId="email"
TransformationClaimType="item" />
worksheet.
          <InputClaim ClaimTypeReferenceId="otherMails"
TransformationClaimType="collection" />
        </InputClaims>
        <OutputClaims>
          <OutputClaim ClaimTypeReferenceId="otherMails"

1. The edits for this file should have been completed with the Global edits you

406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492

2. Locate the line containing PartnerEntity, and replace the hostname portion

TransformationClaimType="collection" />
<TrustFrameworkPolicy
        </OutputClaims>
      </ClaimsTransformation>
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      <ClaimsTransformation Id="AssertAccountEnabledIsTrue"
TransformationMethod="AssertBooleanClaimIsEqualToValue">
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
        <InputClaims>
xmlns="http://schemas.microsoft.com/online/cpim/schemas/20
          <InputClaim ClaimTypeReferenceId="accountEnabled"
TransformationClaimType="inputClaim" />
13/06" PolicySchemaVersion="0.3.0.0"
        </InputClaims>
        <InputParameters>
TenantId="stellarpmb2c.onmicrosoft.com"
          <InputParameter Id="valueToCompareTo" DataType="boolean"
Value="true" />
PolicyId="B2C_1A_signup_signin_saml"
        </InputParameters>
      </ClaimsTransformation>
PublicPolicyUri="http://stellarpmb2c.onmicrosoft.com/B2C_1
    </ClaimsTransformations>
    <ClientDefinitions>
A_signup_signin_saml" TenantObjectId="04fcef19-20fe-4655-
      <ClientDefinition Id="DefaultWeb">
        <ClientUIFilterFlags>LineMarkers,
9498-3e5050b6dda1">
MetaRefresh</ClientUIFilterFlags>
      </ClientDefinition>
and
    </ClientDefinitions>
    <ContentDefinitions>
      <!-- This content definition is to render an error page that
<TenantId>stellarpmb2c.onmicrosoft.com</TenantId>
displays unhandled errors. -->
      <ContentDefinition Id="api.error">
        <LoadUri>~/tenant/templates/AzureBlue/exception.cshtml</LoadUr
i>
with the URL of your Stellar Cyber DP host.
        <RecoveryUri>~/common/default_page_error.html</RecoveryUri>
        <DataUri>urn:com:microsoft:aad:b2c:elements:contract:globalexc
eption:1.2.1</DataUri>
<Item
        <Metadata>
          <Item Key="DisplayName">Error page</Item>
Key="PartnerEntity">https://testdp.stellarcyber.ai/sso/sam
        </Metadata>
l/metadata</Item>
      </ContentDefinition>
      <ContentDefinition Id="api.idpselections">
        <LoadUri>~/tenant/templates/AzureBlue/idpSelector.cshtml</Load
3. If you are configuring Authentication for a specific Stellar Cyber tenant, then
Uri>
        <RecoveryUri>~/common/default_page_error.html</RecoveryUri>
additionally modify that line as indicated below, using the Stellar Cyber Tenant
        <DataUri>urn:com:microsoft:aad:b2c:elements:contract:providers
election:1.2.1</DataUri>
ID (not your Microsoft Entra ID (formerly Azure AD) Tenant ID) you noted before
        <Metadata>
you began configuration. The cust_id/tenant ensures that the configuration
          <Item Key="DisplayName">Idp selection page</Item>
          <Item Key="language.intro">Sign in</Item>
is applicable to just that specific Stellar Cyber tenant.
        </Metadata>
      </ContentDefinition>
      <ContentDefinition Id="api.idpselections.signup">
<Item
        <LoadUri>~/tenant/templates/AzureBlue/idpSelector.cshtml</Load
Uri>
Key="PartnerEntity">https://testdp.stellarcyber.ai/sso/sam
        <RecoveryUri>~/common/default_page_error.html</RecoveryUri>
        <DataUri>urn:com:microsoft:aad:b2c:elements:contract:providers
l/metadata/cust_id/<Stellar Cyber tenant ID></Item>
election:1.2.1</DataUri>
        <Metadata>
Example:
          <Item Key="DisplayName">Idp selection page</Item>
          <Item Key="language.intro">Sign up</Item>
        </Metadata>
      </ContentDefinition>
      <ContentDefinition Id="api.signuporsignin">
        <LoadUri>~/tenant/templates/AzureBlue/unified.cshtml</LoadUri>
        <RecoveryUri>~/common/default_page_error.html</RecoveryUri>
        <DataUri>urn:com:microsoft:aad:b2c:elements:contract:unifiedss
p:2.1.5</DataUri>
        <Metadata>
          <Item Key="DisplayName">Signin and Signup</Item>
        </Metadata>
      </ContentDefinition>
      <ContentDefinition Id="api.selfasserted">
        <LoadUri>~/tenant/templates/AzureBlue/selfAsserted.cshtml</Loa
You would enter this: <Item
dUri>
Key="PartnerEntity">https://testdp.stellarcyber.ai/sso/saml/meta
        <RecoveryUri>~/common/default_page_error.html</RecoveryUri>
        <DataUri>urn:com:microsoft:aad:b2c:elements:contract:selfasser
data/cust_id/29443942</Item>
ted:2.1.7</DataUri>
        <Metadata>
          <Item Key="DisplayName">Collect information from user
page</Item>
        </Metadata>
      </ContentDefinition>
      <ContentDefinition Id="api.selfasserted.profileupdate">
        <LoadUri>~/tenant/templates/AzureBlue/selfAsserted.cshtml</Loa
dUri>
        <RecoveryUri>~/common/default_page_error.html</RecoveryUri>
        <DataUri>urn:com:microsoft:aad:b2c:elements:contract:selfasser
ted:2.1.7</DataUri>
        <Metadata>
          <Item Key="DisplayName">Collect information from user
page</Item>
        </Metadata>
      </ContentDefinition>

493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579

      <ContentDefinition Id="api.localaccountsignup">
If you are configuring standard authentication, your file will look similar to this:
        <LoadUri>~/tenant/templates/AzureBlue/selfAsserted.cshtml</Loa
dUri>
        <RecoveryUri>~/common/default_page_error.html</RecoveryUri>
SignUpOrSignInSAML.xml
        <DataUri>urn:com:microsoft:aad:b2c:elements:contract:selfasser
ted:2.1.7</DataUri>
        <Metadata>
          <Item Key="DisplayName">Local account sign up page</Item>
        </Metadata>
      </ContentDefinition>
      <ContentDefinition Id="api.localaccountpasswordreset">
        <LoadUri>~/tenant/templates/AzureBlue/selfAsserted.cshtml</Loa
dUri>
        <RecoveryUri>~/common/default_page_error.html</RecoveryUri>
        <DataUri>urn:com:microsoft:aad:b2c:elements:contract:selfasser
ted:2.1.7</DataUri>
        <Metadata>
          <Item Key="DisplayName">Local account change password
page</Item>
        </Metadata>
      </ContentDefinition>
      <ContentDefinition Id="api.localaccountsignin">
        <LoadUri>~/tenant/templates/AzureBlue/selfAsserted.cshtml</Loa
dUri>
        <RecoveryUri>~/common/default_page_error.html</RecoveryUri>
        <DataUri>urn:com:microsoft:aad:b2c:elements:contract:selfasser
ted:2.1.7</DataUri>
        <Metadata>
          <Item Key="DisplayName">Collect information from user
page</Item>
        </Metadata>
      </ContentDefinition>
    </ContentDefinitions>
  </BuildingBlocks>
  <!--
        A list of all the claim providers that can be used in the
technical policies. If a claims provider is not listed
        in this section, then it cannot be used in a technical policy.
    -->
  <ClaimsProviders>
    <ClaimsProvider>
      <DisplayName>Local Account SignIn</DisplayName>
      <TechnicalProfiles>
        <TechnicalProfile Id="login-NonInteractive">
          <DisplayName>Local Account SignIn</DisplayName>
          <Protocol Name="OpenIdConnect" />
          <Metadata>
            <Item Key="ProviderName">https://sts.windows.net/</Item>
            <Item
Key="METADATA">https://login.microsoftonline.com/{tenant}/.well-
known/openid-configuration</Item>
            <Item
Key="authorization_endpoint">https://login.microsoftonline.com/{tenant
}/oauth2/token</Item>
            <Item Key="response_types">id_token</Item>
            <Item Key="response_mode">query</Item>
            <Item Key="scope">email openid</Item>
            <!-- <Item Key="grant_type">password</Item> -->
            <!-- Policy Engine Clients -->
            <Item Key="UsePolicyInRedirectUri">false</Item>
            <Item Key="HttpBinding">POST</Item>
            <Item
Key="client_id">ProxyIdentityExperienceFrameworkAppId</Item>
            <Item
Key="IdTokenAudience">IdentityExperienceFrameworkAppId</Item>
          </Metadata>
          <InputClaims>
            <InputClaim ClaimTypeReferenceId="signInName"
PartnerClaimType="username" Required="true" />
            <InputClaim ClaimTypeReferenceId="password"
Required="true" />
            <InputClaim ClaimTypeReferenceId="grant_type"
DefaultValue="password" AlwaysUseDefaultValue="true" />
            <InputClaim ClaimTypeReferenceId="scope"
DefaultValue="openid" AlwaysUseDefaultValue="true" />
            <InputClaim ClaimTypeReferenceId="nca"
PartnerClaimType="nca" DefaultValue="1" />
            <InputClaim ClaimTypeReferenceId="client_id"
DefaultValue="ProxyIdentityExperienceFrameworkAppID" />
            <InputClaim ClaimTypeReferenceId="resource_id"
PartnerClaimType="resource"
DefaultValue="IdentityExperienceFrameworkAppID" />
          </InputClaims>
          <OutputClaims>
            <OutputClaim ClaimTypeReferenceId="objectId"
PartnerClaimType="oid" />
            <OutputClaim ClaimTypeReferenceId="tenantId"

580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666

PartnerClaimType="tid" />
If you are configuring Azure native multi-factor authentication, your file will look
            <OutputClaim ClaimTypeReferenceId="givenName"
PartnerClaimType="given_name" />
            <OutputClaim ClaimTypeReferenceId="surName"
PartnerClaimType="family_name" />
            <OutputClaim ClaimTypeReferenceId="displayName"
PartnerClaimType="name" />
            <OutputClaim ClaimTypeReferenceId="userPrincipalName"
PartnerClaimType="upn" />
            <OutputClaim ClaimTypeReferenceId="authenticationSource"
DefaultValue="localAccountAuthentication" />
          </OutputClaims>
        </TechnicalProfile>
        <TechnicalProfile Id="Saml2AssertionIssuer">
          <DisplayName>Token Issuer</DisplayName>
          <Protocol Name="SAML2" />
          <OutputTokenFormat>SAML2</OutputTokenFormat>
          <Metadata>
            <Item
Key="IssuerUri">https://stellarpmb2c.b2clogin.com/stellarpmb2c.onmicro
soft.com/B2C_1A_signup_signin_SAML</Item>
            <Item Key="TokenNotBeforeSkewInSeconds">600</Item>
          </Metadata>
          <CryptographicKeys>
            <Key Id="MetadataSigning"
StorageReferenceId="B2C_1A_SamlIdpCert" />
            <Key Id="SamlMessageSigning"
StorageReferenceId="B2C_1A_SamlIdpCert" />
            <Key Id="SamlAssertionSigning"
StorageReferenceId="B2C_1A_SamlIdpCert" />
          </CryptographicKeys>
          <InputClaims />
          <OutputClaims />
          <UseTechnicalProfileForSessionManagement ReferenceId="SM-
Saml-issuer" />
        </TechnicalProfile>
        <TechnicalProfile Id="SM-Saml-issuer">
          <DisplayName>Session Management Provider</DisplayName>
          <Protocol Name="Proprietary"
Handler="Web.TPEngine.SSO.SamlSSOSessionProvider, Web.TPEngine,
Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
        </TechnicalProfile>
      </TechnicalProfiles>
    </ClaimsProvider>
    <ClaimsProvider>
      <DisplayName>Azure Active Directory</DisplayName>
      <TechnicalProfiles>
        <TechnicalProfile Id="AAD-Common">
          <DisplayName>Azure Active Directory</DisplayName>
          <Protocol Name="Proprietary"
Handler="Web.TPEngine.Providers.AzureActiveDirectoryProvider,
Web.TPEngine, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null"
/>
          <CryptographicKeys>
            <Key Id="issuer_secret"
StorageReferenceId="B2C_1A_TokenSigningKeyContainer" />
          </CryptographicKeys>
          <!-- We need this here to suppress the SelfAsserted provider
from invoking SSO on validation profiles. -->
          <IncludeInSso>false</IncludeInSso>
          <UseTechnicalProfileForSessionManagement ReferenceId="SM-
Noop" />
        </TechnicalProfile>
        <!-- Technical profiles for local accounts -->
        <TechnicalProfile Id="AAD-UserWriteUsingLogonEmail">
          <Metadata>
            <Item Key="Operation">Write</Item>
            <Item
Key="RaiseErrorIfClaimsPrincipalAlreadyExists">true</Item>
          </Metadata>
          <IncludeInSso>false</IncludeInSso>
          <InputClaims>
            <InputClaim ClaimTypeReferenceId="email"
PartnerClaimType="signInNames.emailAddress" Required="true" />
          </InputClaims>
          <PersistedClaims>
            <!-- Required claims -->
            <PersistedClaim ClaimTypeReferenceId="email"
PartnerClaimType="signInNames.emailAddress" />
            <PersistedClaim ClaimTypeReferenceId="newPassword"
PartnerClaimType="password" />
            <PersistedClaim ClaimTypeReferenceId="displayName"
DefaultValue="unknown" />
            <PersistedClaim ClaimTypeReferenceId="passwordPolicies"
DefaultValue="DisablePasswordExpiration" />
            <!-- Optional claims. -->
            <PersistedClaim ClaimTypeReferenceId="givenName" />

667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
747
748
749
750
751
752
753

            <PersistedClaim ClaimTypeReferenceId="surname" />
similar to this:
            <PersistedClaim ClaimTypeReferenceId="userPrincipalName"
/>
            <PersistedClaim ClaimTypeReferenceId="mail" />
SignUpOrSigninSAML.xml (MFA)
            <PersistedClaim
ClaimTypeReferenceId="extension_stellar_privilege" />
            <PersistedClaim
ClaimTypeReferenceId="extension_stellar_scope" />
            <PersistedClaim
ClaimTypeReferenceId="extension_stellar_tenant" />
            <PersistedClaim
ClaimTypeReferenceId="extension_stellar_tenant_group" />
          </PersistedClaims>
          <OutputClaims>
            <OutputClaim ClaimTypeReferenceId="objectId" />
            <OutputClaim ClaimTypeReferenceId="newUser"
PartnerClaimType="newClaimsPrincipalCreated" />
            <OutputClaim ClaimTypeReferenceId="authenticationSource"
DefaultValue="localAccountAuthentication" />
            <OutputClaim ClaimTypeReferenceId="userPrincipalName" />
            <OutputClaim
ClaimTypeReferenceId="signInNames.emailAddress" />
          </OutputClaims>
          <IncludeTechnicalProfile ReferenceId="AAD-Common" />
          <UseTechnicalProfileForSessionManagement ReferenceId="SM-
AAD" />
        </TechnicalProfile>
        <TechnicalProfile Id="AAD-UserReadUsingEmailAddress">
          <Metadata>
            <Item Key="Operation">Read</Item>
            <Item
Key="RaiseErrorIfClaimsPrincipalDoesNotExist">true</Item>
          </Metadata>
          <IncludeInSso>false</IncludeInSso>
          <InputClaims>
            <InputClaim ClaimTypeReferenceId="email"
PartnerClaimType="signInNames.emailAddress" Required="true" />
          </InputClaims>
          <OutputClaims>
            <!-- Required claims -->
            <OutputClaim ClaimTypeReferenceId="objectId" />
            <OutputClaim ClaimTypeReferenceId="authenticationSource"
DefaultValue="localAccountAuthentication" />
            <!-- Optional claims -->
            <OutputClaim ClaimTypeReferenceId="userPrincipalName" />
            <OutputClaim ClaimTypeReferenceId="displayName" />
            <OutputClaim ClaimTypeReferenceId="accountEnabled" />
            <OutputClaim ClaimTypeReferenceId="otherMails" />
            <OutputClaim
ClaimTypeReferenceId="signInNames.emailAddress" />
          </OutputClaims>
          <OutputClaimsTransformations>
            <OutputClaimsTransformation
ReferenceId="AssertAccountEnabledIsTrue" />
          </OutputClaimsTransformations>
          <IncludeTechnicalProfile ReferenceId="AAD-Common" />
        </TechnicalProfile>
        <TechnicalProfile Id="AAD-UserWritePasswordUsingObjectId">
          <Metadata>
            <Item Key="Operation">Write</Item>
            <Item
Key="RaiseErrorIfClaimsPrincipalDoesNotExist">true</Item>
          </Metadata>
          <IncludeInSso>false</IncludeInSso>
          <InputClaims>
            <InputClaim ClaimTypeReferenceId="objectId"
Required="true" />
          </InputClaims>
          <PersistedClaims>
            <PersistedClaim ClaimTypeReferenceId="objectId" />
            <PersistedClaim ClaimTypeReferenceId="newPassword"
PartnerClaimType="password" />
Upload Custom Policies
          </PersistedClaims>
          <IncludeTechnicalProfile ReferenceId="AAD-Common" />
        </TechnicalProfile>
Steps
        <!-- Technical profiles for updating user record using
objectId -->
        <TechnicalProfile Id="AAD-UserWriteProfileUsingObjectId">
 If you stop and return to any of the procedures in this configuration process,
          <Metadata>
            <Item Key="Operation">Write</Item>
ensure that you switch to the correct directory before you continue so that you
            <Item
Key="RaiseErrorIfClaimsPrincipalAlreadyExists">false</Item>
are working on the correct Azure AD B2C Tenant container.
            <Item
Key="RaiseErrorIfClaimsPrincipalDoesNotExist">true</Item>
          </Metadata>
          <IncludeInSso>false</IncludeInSso>
          <InputClaims>

754
755
756
757
758
759
760
761
762
763
764
765
766
767
768
769
770
771
772
773
774
775
776
777
778
779
780
781
782
783
784
785
786
787
788
789
790
791
792
793
794
795
796
797
798
799
800
801
802
803
804
805
806
807
808
809
810
811
812
813
814
815
816
817
818
819
820
821
822
823
824
825
826
827
828
829
830
831
832
833
834
835
836
837
838
839
840

a. TrustFrameworkBase.xml

3. Click the button for Custom Policies.

2. From the Overview page, select Identity Experience Framework.

1. Access All services from the top-left corner of the Azure portal, and then

5. Upload each of the policies you modified above. You must upload these in

            <InputClaim ClaimTypeReferenceId="objectId"
Required="true" />
          </InputClaims>
search for and select Azure AD B2C.
          <PersistedClaims>
            <!-- Required claims -->
            <PersistedClaim ClaimTypeReferenceId="objectId" />
            <!-- Optional claims -->
            <PersistedClaim ClaimTypeReferenceId="givenName" />
            <PersistedClaim ClaimTypeReferenceId="surname" />
            <PersistedClaim ClaimTypeReferenceId="userPrincipalName"
/>
            <PersistedClaim ClaimTypeReferenceId="mail" />
            <PersistedClaim
ClaimTypeReferenceId="extension_stellar_privilege" />
            <PersistedClaim
ClaimTypeReferenceId="extension_stellar_scope" />
            <PersistedClaim
ClaimTypeReferenceId="extension_stellar_tenant" />
            <PersistedClaim
ClaimTypeReferenceId="extension_stellar_tenant_group" />
          </PersistedClaims>
          <IncludeTechnicalProfile ReferenceId="AAD-Common" />
4. Select Upload Custom Policy
        </TechnicalProfile>
        <!-- The following technical profile is used to read data
after user authenticates. -->
        <TechnicalProfile Id="AAD-UserReadUsingObjectId">
          <Metadata>
            <Item Key="Operation">Read</Item>
            <Item
Key="RaiseErrorIfClaimsPrincipalDoesNotExist">true</Item>
          </Metadata>
          <IncludeInSso>false</IncludeInSso>
          <InputClaims>
            <InputClaim ClaimTypeReferenceId="objectId"
Required="true" />
          </InputClaims>
          <OutputClaims>
            <!-- Optional claims -->
the order shown below. The template files are numbered to help you ensure
            <OutputClaim
ClaimTypeReferenceId="signInNames.emailAddress" />
correct ordering.
            <OutputClaim ClaimTypeReferenceId="displayName" />
            <OutputClaim ClaimTypeReferenceId="otherMails" />
            <OutputClaim ClaimTypeReferenceId="givenName" />
            <OutputClaim ClaimTypeReferenceId="surname" />
            <OutputClaim ClaimTypeReferenceId="userPrincipalName" />
            <OutputClaim ClaimTypeReferenceId="mail" />
            <OutputClaim
ClaimTypeReferenceId="extension_stellar_privilege" />
c. TrustFrameworkExtensions.xml
            <OutputClaim
ClaimTypeReferenceId="extension_stellar_scope" />
            <OutputClaim
ClaimTypeReferenceId="extension_stellar_tenant" />
            <OutputClaim
ClaimTypeReferenceId="extension_stellar_tenant_group" />
          </OutputClaims>
          <IncludeTechnicalProfile ReferenceId="AAD-Common" />
        </TechnicalProfile>
      </TechnicalProfiles>
g. SignUpOrSigninSAML.xml
    </ClaimsProvider>
    <ClaimsProvider>
      <DisplayName>Self Asserted</DisplayName>
6. After the policy files are uploaded, Azure AD B2C uses the configuration
      <TechnicalProfiles>
information to generate the metadata URL that Stellar Cyber will use; it
        <TechnicalProfile Id="SelfAsserted-ProfileUpdate">
          <DisplayName>User ID signup</DisplayName>
contains information such as the sign-in methods and certificates. The Azure
          <Protocol Name="Proprietary"
Handler="Web.TPEngine.Providers.SelfAssertedAttributeProvider,
AD B2C metadata is available at the following URL, where <tenant-name> is
Web.TPEngine, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null"
/>
the name of your Azure AD B2C tenant and <policy-name> is the name (ID) of
          <Metadata>
            <Item
the policy.
Key="ContentDefinitionReferenceId">api.selfasserted.profileupdate</Ite
m>
https://<Azure AD B2C tenant-name>.b2clogin.com/<Azure
          </Metadata>
          <IncludeInSso>false</IncludeInSso>
AD B2C tenant-name>.onmicrosoft.com/<policy-
          <InputClaims>
            <InputClaim ClaimTypeReferenceId="userPrincipalName" />
name>/samlp/metadata
            <!-- Optional claims. These claims are collected from the
user and can be modified. Any claim added here should be updated in
the
Example:
                 ValidationTechnicalProfile referenced below so it can
be written to directory after being updated by the user, i.e. AAD-
https://stellarpmb2c.b2clogin.com/stellarpmb2c.onmicrosoft
UserWriteProfileUsingObjectId. -->
            <InputClaim ClaimTypeReferenceId="givenName" />
.com/B2C_1A_signup_signin_saml/samlp/metadata
            <InputClaim ClaimTypeReferenceId="surname" />
            <InputClaim ClaimTypeReferenceId="userPrincipalName" />
            <InputClaim ClaimTypeReferenceId="mail" />
            <InputClaim

b. TrustFrameworkLocalization.xml

d. SignUpOrSignin.xml

f. PasswordReset.xml

e. ProfileEdit.xml

7. Make note of this Metadata URL in your worksheet for later use configuring in

ClaimTypeReferenceId="extension_stellar_privilege" />
            <InputClaim ClaimTypeReferenceId="extension_stellar_scope"
/>
Stellar Cyber.
            <InputClaim
ClaimTypeReferenceId="extension_stellar_tenant" />
Proceed to the next step...
            <InputClaim
ClaimTypeReferenceId="extension_stellar_tenant_group" />
          </InputClaims>
          <OutputClaims>
            <!-- Required claims -->
            <OutputClaim ClaimTypeReferenceId="executed-SelfAsserted-
Input" DefaultValue="true" />
            <!-- Optional claims. These claims are collected from the
user and can be modified. Any claim added here should be updated in
the
                 ValidationTechnicalProfile referenced below so it can
be written to directory after being updated by the user, i.e. AAD-
UserWriteProfileUsingObjectId. -->
            <OutputClaim ClaimTypeReferenceId="givenName" />
            <OutputClaim ClaimTypeReferenceId="surname" />
            <OutputClaim ClaimTypeReferenceId="userPrincipalName" />
            <OutputClaim ClaimTypeReferenceId="mail" />
            <OutputClaim
ClaimTypeReferenceId="extension_stellar_privilege" />
            <OutputClaim
ClaimTypeReferenceId="extension_stellar_scope" />
            <OutputClaim
ClaimTypeReferenceId="extension_stellar_tenant" />
            <OutputClaim
ClaimTypeReferenceId="extension_stellar_tenant_group" />
          </OutputClaims>
          <ValidationTechnicalProfiles>
            <ValidationTechnicalProfile ReferenceId="AAD-
UserWriteProfileUsingObjectId" />
          </ValidationTechnicalProfiles>
        </TechnicalProfile>
      </TechnicalProfiles>
    </ClaimsProvider>
    <ClaimsProvider>
      <DisplayName>Local Account</DisplayName>
      <TechnicalProfiles>
        <TechnicalProfile Id="LocalAccountSignUpWithLogonEmail">
          <DisplayName>Email signup</DisplayName>
          <Protocol Name="Proprietary"
Handler="Web.TPEngine.Providers.SelfAssertedAttributeProvider,
Web.TPEngine, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null"
/>
          <Metadata>
            <Item Key="IpAddressClaimReferenceId">IpAddress</Item>
            <Item
Key="ContentDefinitionReferenceId">api.localaccountsignup</Item>
          </Metadata>
          <CryptographicKeys>
            <Key Id="issuer_secret"
StorageReferenceId="B2C_1A_TokenSigningKeyContainer" />
          </CryptographicKeys>
          <InputClaims>
            <InputClaim ClaimTypeReferenceId="email" />
          </InputClaims>
          <OutputClaims>
            <OutputClaim ClaimTypeReferenceId="objectId" />
            <OutputClaim ClaimTypeReferenceId="email"
PartnerClaimType="Verified.Email" Required="true" />
            <OutputClaim ClaimTypeReferenceId="newPassword"
Required="true" />
            <OutputClaim ClaimTypeReferenceId="reenterPassword"
Required="true" />
            <OutputClaim ClaimTypeReferenceId="executed-SelfAsserted-
Input" DefaultValue="true" />
            <OutputClaim ClaimTypeReferenceId="authenticationSource"
/>
            <OutputClaim ClaimTypeReferenceId="newUser" />
            <!-- Optional claims, to be collected from the user -->
            <OutputClaim ClaimTypeReferenceId="displayName" />
            <OutputClaim ClaimTypeReferenceId="givenName" />
            <OutputClaim ClaimTypeReferenceId="surName" />
          </OutputClaims>
          <ValidationTechnicalProfiles>
            <ValidationTechnicalProfile ReferenceId="AAD-
UserWriteUsingLogonEmail" />
          </ValidationTechnicalProfiles>

841
842
843
844
845
846
847
848
849
850
851
852
853
854
855
856
857
858
859
860
861
862
863
864
865
866
867
868
869
870
871
872
873
874
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
890
891
892
893
894
895
896
897
898
899
900
901
902
903
904
905
906
907
908
909
910
911
912
913
914
915
916
917
918
919
920
921
          <UseTechnicalProfileForSessionManagement ReferenceId="SM-AAD" />
<TrustFrameworkPolicy xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        </TechnicalProfile>
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
        <!-- This technical profile uses a validation technical profile to
xmlns="http://schemas.microsoft.com/online/cpim/schemas/2013/06"
authenticate the user. -->
PolicySchemaVersion="0.3.0.0" TenantId="stellarpmb2c.onmicrosoft.com"
        <TechnicalProfile Id="SelfAsserted-LocalAccountSignin-Email">
PolicyId="B2C_1A_TrustFrameworkLocalization"
          <DisplayName>Local Account Signin</DisplayName>

1
2
3
4
5

6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92

PublicPolicyUri="http://stellarpmb2c.onmicrosoft.com/B2C_1A_TrustFrameworkLoca
          <Protocol Name="Proprietary"
lization" TenantObjectId="04fcef19-20fe-4655-9498-3e5050b6dda1">
Handler="Web.TPEngine.Providers.SelfAssertedAttributeProvider, Web.TPEngine,
  <BasePolicy>
Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
    <TenantId>stellarpmb2c.onmicrosoft.com</TenantId>
          <Metadata>
    <PolicyId>B2C_1A_TrustFrameworkBase</PolicyId>
            <Item Key="SignUpTarget">SignUpWithLogonEmailExchange</Item>
  </BasePolicy>
            <Item Key="setting.operatingMode">Email</Item>
  <BuildingBlocks>
            <Item
    <ContentDefinitions>
Key="ContentDefinitionReferenceId">api.localaccountsignin</Item>
      <ContentDefinition Id="api.signuporsignin">
            <Item Key="IncludeClaimResolvingInClaimsHandling">true</Item>
        <LocalizedResourcesReferences MergeBehavior="Prepend">
          </Metadata>
          <LocalizedResourcesReference Language="en"
          <IncludeInSso>false</IncludeInSso>
LocalizedResourcesReferenceId="api.signuporsignin.en" />
          <InputClaims>
          <!-- Add more languages here -->
            <InputClaim ClaimTypeReferenceId="signInName" DefaultValue="
        </LocalizedResourcesReferences>
{OIDC:LoginHint}" AlwaysUseDefaultValue="true" />
      </ContentDefinition>
          </InputClaims>
      <ContentDefinition Id="api.localaccountsignup">
          <OutputClaims>
        <LocalizedResourcesReferences MergeBehavior="Prepend">
            <OutputClaim ClaimTypeReferenceId="signInName" Required="true"
          <LocalizedResourcesReference Language="en"
/>
LocalizedResourcesReferenceId="api.localaccountsignup.en" />
            <OutputClaim ClaimTypeReferenceId="password" Required="true" />
          <!-- Add more languages here -->
            <OutputClaim ClaimTypeReferenceId="objectId" />
        </LocalizedResourcesReferences>
            <OutputClaim ClaimTypeReferenceId="authenticationSource" />
      </ContentDefinition>
            <OutputClaim ClaimTypeReferenceId="extension_stellar_privilege"
      <ContentDefinition Id="api.selfasserted">
/>
        <LocalizedResourcesReferences MergeBehavior="Prepend">
            <OutputClaim ClaimTypeReferenceId="extension_stellar_scope" />
          <LocalizedResourcesReference Language="en"
            <OutputClaim ClaimTypeReferenceId="extension_stellar_tenant" />
LocalizedResourcesReferenceId="api.selfasserted.en" />
            <OutputClaim
          <!-- Add more languages here -->
ClaimTypeReferenceId="extension_stellar_tenant_group" />
          </OutputClaims>
        </LocalizedResourcesReferences>
      </ContentDefinition>
          <ValidationTechnicalProfiles>
      <ContentDefinition Id="api.localaccountpasswordreset">
            <ValidationTechnicalProfile ReferenceId="login-NonInteractive"
        <LocalizedResourcesReferences MergeBehavior="Prepend">
/>
          <LocalizedResourcesReference Language="en"
          </ValidationTechnicalProfiles>
LocalizedResourcesReferenceId="api.localaccountpasswordreset.en" />
          <UseTechnicalProfileForSessionManagement ReferenceId="SM-AAD" />
          <!-- Add more languages here -->
        </TechnicalProfile>
        </LocalizedResourcesReferences>
        <!-- This technical profile forces the user to verify the email
      </ContentDefinition>
address that they provide on the UI. Only after email is verified, the user
      <ContentDefinition Id="api.idpselections">
account is
        <LocalizedResourcesReferences MergeBehavior="Prepend">
        read from the directory. -->
          <LocalizedResourcesReference Language="en"
        <TechnicalProfile Id="LocalAccountDiscoveryUsingEmailAddress">
LocalizedResourcesReferenceId="api.idpselections.en" />
          <DisplayName>Reset password using email address</DisplayName>
          <!-- Add more languages here -->
          <Protocol Name="Proprietary"
        </LocalizedResourcesReferences>
Handler="Web.TPEngine.Providers.SelfAssertedAttributeProvider, Web.TPEngine,
      </ContentDefinition>
Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
      <ContentDefinition Id="api.localaccountsignin">
          <Metadata>
        <LocalizedResourcesReferences MergeBehavior="Prepend">
            <Item Key="IpAddressClaimReferenceId">IpAddress</Item>
          <LocalizedResourcesReference Language="en"
            <Item
LocalizedResourcesReferenceId="api.localaccountsignin.en" />
Key="ContentDefinitionReferenceId">api.localaccountpasswordreset</Item>
          <!-- Add more languages here -->
          </Metadata>
        </LocalizedResourcesReferences>
          <CryptographicKeys>
      </ContentDefinition>
            <Key Id="issuer_secret"
      <ContentDefinition Id="api.selfasserted.profileupdate">
StorageReferenceId="B2C_1A_TokenSigningKeyContainer" />
        <LocalizedResourcesReferences MergeBehavior="Prepend">
          </CryptographicKeys>
          <LocalizedResourcesReference Language="en"
          <IncludeInSso>false</IncludeInSso>
LocalizedResourcesReferenceId="api.selfasserted.profileupdate.en" />
          <OutputClaims>
          <!-- Add more languages here -->
            <OutputClaim ClaimTypeReferenceId="email"
        </LocalizedResourcesReferences>
PartnerClaimType="Verified.Email" Required="true" />
      </ContentDefinition>
            <OutputClaim ClaimTypeReferenceId="objectId" />
    </ContentDefinitions>
            <OutputClaim ClaimTypeReferenceId="userPrincipalName" />
    <Localization Enabled="true">
            <OutputClaim ClaimTypeReferenceId="authenticationSource" />
      <SupportedLanguages DefaultLanguage="en" MergeBehavior="Append">
          </OutputClaims>
        <SupportedLanguage>en</SupportedLanguage>
          <ValidationTechnicalProfiles>
      </SupportedLanguages>
            <ValidationTechnicalProfile ReferenceId="AAD-
      <LocalizedResources Id="api.signuporsignin.en">
UserReadUsingEmailAddress" />
        <LocalizedStrings>
          </ValidationTechnicalProfiles>
          <LocalizedString ElementType="ClaimType" ElementId="signInName"
        </TechnicalProfile>
        <TechnicalProfile Id="LocalAccountWritePasswordUsingObjectId">
StringId="DisplayName">Email Address</LocalizedString>
          <LocalizedString ElementType="UxElement" StringId="heading">Sign
          <DisplayName>Change password (username)</DisplayName>
in</LocalizedString>
          <Protocol Name="Proprietary"
          <LocalizedString ElementType="UxElement"
Handler="Web.TPEngine.Providers.SelfAssertedAttributeProvider, Web.TPEngine,
StringId="local_intro_generic">Sign in with your {0}</LocalizedString>
Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
          <LocalizedString ElementType="ClaimType" ElementId="password"
          <Metadata>
StringId="DisplayName">Password</LocalizedString>
            <Item
          <LocalizedString ElementType="UxElement"
Key="ContentDefinitionReferenceId">api.localaccountpasswordreset</Item>
StringId="requiredField_password">Please enter your password</LocalizedString>
          </Metadata>
          <LocalizedString ElementType="UxElement"
          <CryptographicKeys>
StringId="requiredField_generic">Please enter your {0}</LocalizedString>
            <Key Id="issuer_secret"
          <LocalizedString ElementType="UxElement"
StorageReferenceId="B2C_1A_TokenSigningKeyContainer" />
StringId="invalid_generic">Please enter a valid {0}</LocalizedString>
          </CryptographicKeys>
          <LocalizedString ElementType="UxElement"
          <InputClaims>
StringId="createaccount_one_link">Sign up now</LocalizedString>
            <InputClaim ClaimTypeReferenceId="objectId" />
          <LocalizedString ElementType="UxElement"
          </InputClaims>
StringId="createaccount_two_links">Sign up with {0} or {1}</LocalizedString>
          <OutputClaims>
          <LocalizedString ElementType="UxElement"
            <OutputClaim ClaimTypeReferenceId="newPassword" Required="true"
StringId="createaccount_three_links">Sign up with {0}, {1}, or {2}
/>
</LocalizedString>
            <OutputClaim ClaimTypeReferenceId="reenterPassword"
          <LocalizedString ElementType="UxElement"
Required="true" />
StringId="forgotpassword_link">Forgot your password?</LocalizedString>
          </OutputClaims>

93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179

          <LocalizedString ElementType="UxElement"
          <ValidationTechnicalProfiles>
StringId="button_signin">Sign in</LocalizedString>
            <ValidationTechnicalProfile ReferenceId="AAD-
          <LocalizedString ElementType="UxElement"
UserWritePasswordUsingObjectId" />
StringId="createaccount_intro">Don't have an account?</LocalizedString>
          </ValidationTechnicalProfiles>
          <LocalizedString ElementType="UxElement" StringId="unknown_error">We
        </TechnicalProfile>
are having trouble signing you in. Please try again later.</LocalizedString>
      </TechnicalProfiles>
          <!-- Uncomment the remember_me only if the keep me signed in is
    </ClaimsProvider>
activated.
    <ClaimsProvider>
          <LocalizedString ElementType="UxElement" StringId="remember_me">Keep
      <DisplayName>Session Management</DisplayName>
me signed in</LocalizedString> -->
      <TechnicalProfiles>
          <LocalizedString ElementType="ClaimsProvider"
        <TechnicalProfile Id="SM-Noop">
StringId="FacebookExchange">Facebook</LocalizedString>
          <DisplayName>Noop Session Management Provider</DisplayName>
          <LocalizedString ElementType="ErrorMessage"
          <Protocol Name="Proprietary"
StringId="ResourceOwnerFlowInvalidCredentials">Your password is incorrect.
Handler="Web.TPEngine.SSO.NoopSSOSessionProvider, Web.TPEngine,
</LocalizedString>
Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
          <LocalizedString ElementType="ErrorMessage"
        </TechnicalProfile>
StringId="UserMessageIfInvalidPassword">Your password is incorrect.
        <TechnicalProfile Id="SM-AAD">
</LocalizedString>
          <DisplayName>Session Mananagement Provider</DisplayName>
          <LocalizedString ElementType="ErrorMessage"
          <Protocol Name="Proprietary"
StringId="UserMessageIfPasswordExpired">Your password has expired.
Handler="Web.TPEngine.SSO.DefaultSSOSessionProvider, Web.TPEngine,
</LocalizedString>
Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
          <LocalizedString ElementType="ErrorMessage"
          <PersistedClaims>
StringId="UserMessageIfClaimsPrincipalDoesNotExist">We can't seem to find your
            <PersistedClaim ClaimTypeReferenceId="objectId" />
account.</LocalizedString>
            <PersistedClaim ClaimTypeReferenceId="signInName" />
            <PersistedClaim ClaimTypeReferenceId="authenticationSource" />
          <LocalizedString ElementType="ErrorMessage"
StringId="UserMessageIfOldPasswordUsed">Looks like you used an old password.
            <PersistedClaim ClaimTypeReferenceId="identityProvider" />
</LocalizedString>
            <PersistedClaim ClaimTypeReferenceId="newUser" />
            <PersistedClaim ClaimTypeReferenceId="executed-SelfAsserted-
          <LocalizedString ElementType="ErrorMessage"
StringId="DefaultMessage">Invalid username or password.</LocalizedString>
Input" />
          <LocalizedString ElementType="ErrorMessage"
          </PersistedClaims>
StringId="UserMessageIfUserAccountDisabled">Your account has been locked.
          <OutputClaims>
Contact your support person to unlock it, then try again.</LocalizedString>
            <OutputClaim ClaimTypeReferenceId="objectIdFromSession"
          <LocalizedString ElementType="ErrorMessage"
DefaultValue="true" />
StringId="UserMessageIfUserAccountLocked">Your account is temporarily locked
          </OutputClaims>
to prevent unauthorized use. Try again later.</LocalizedString>
        </TechnicalProfile>
        <!-- Session management technical profile for OIDC based tokens -->
          <LocalizedString ElementType="ErrorMessage"
StringId="AADRequestsThrottled">There are too many requests at this moment.
        <TechnicalProfile Id="SM-jwt-issuer">
Please wait for some time and try again.</LocalizedString>
          <DisplayName>Session Management Provider</DisplayName>
        </LocalizedStrings>
          <Protocol Name="Proprietary"
      </LocalizedResources>
Handler="Web.TPEngine.SSO.SamlSSOSessionProvider, Web.TPEngine,
      <!--Local account sign-up page English-->
Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
      <LocalizedResources Id="api.localaccountsignup.en">
          <Metadata>
        <LocalizedStrings>
            <Item
          <LocalizedString ElementType="ClaimType" ElementId="email"
Key="PartnerEntity">https://testdp.stellarcyber.ai/sso/saml/metadata</Item>
StringId="DisplayName">Email Address</LocalizedString>
          </Metadata>
          <LocalizedString ElementType="ClaimType" ElementId="email"
          <OutputClaims>
StringId="UserHelpText">Email address that can be used to contact you.
            <OutputClaim ClaimTypeReferenceId="userPrincipalName"
</LocalizedString>
PartnerClaimType="upn" />
          <LocalizedString ElementType="ClaimType" ElementId="email"
            <OutputClaim ClaimTypeReferenceId="extension_stellar_privilege"
StringId="PatternHelpText">Please enter a valid email address.
/>
</LocalizedString>
            <OutputClaim ClaimTypeReferenceId="extension_stellar_scope" />
          <LocalizedString ElementType="ClaimType" ElementId="newPassword"
            <OutputClaim ClaimTypeReferenceId="extension_stellar_tenant" />
StringId="DisplayName">New Password</LocalizedString>
            <OutputClaim
ClaimTypeReferenceId="extension_stellar_tenant_group" />
          <LocalizedString ElementType="ClaimType" ElementId="newPassword"
StringId="UserHelpText">Enter new password</LocalizedString>
          </OutputClaims>
          <LocalizedString ElementType="ClaimType" ElementId="newPassword"
          <SubjectNamingInfo ClaimType="upn" ExcludeAsClaim="true" />
StringId="PatternHelpText">8-16 characters, containing 3 out of 4 of the
        </TechnicalProfile>
following: Lowercase characters, uppercase characters, digits (0-9), and one
      </TechnicalProfiles>
or more of the following symbols: @ # $ % ^ &amp; * - _ + = [ ] { } | \ : ' ,
    </ClaimsProvider>
? / ` ~ " ( ) ; .</LocalizedString>
    <ClaimsProvider>
          <LocalizedString ElementType="ClaimType" ElementId="reenterPassword"
      <DisplayName>Trustframework Policy Engine
StringId="DisplayName">Confirm New Password</LocalizedString>
TechnicalProfiles</DisplayName>
          <LocalizedString ElementType="ClaimType" ElementId="reenterPassword"
      <TechnicalProfiles>
StringId="UserHelpText">Confirm new password</LocalizedString>
        <TechnicalProfile Id="TpEngine_c3bd4fe2-1775-4013-b91d-
          <LocalizedString ElementType="ClaimType" ElementId="reenterPassword"
35f16d377d13">
StringId="PatternHelpText">8-16 characters, containing 3 out of 4 of the
          <DisplayName>Trustframework Policy Engine Default Technical
following: Lowercase characters, uppercase characters, digits (0-9), and one
Profile</DisplayName>
or more of the following symbols: @ # $ % ^ &amp; * - _ + = [ ] { } | \ : ' ,
          <Protocol Name="None" />
? / ` ~ " ( ) ; .</LocalizedString>
          <Metadata>
          <LocalizedString ElementType="ClaimType" ElementId="displayName"
            <Item Key="url">{service:te}</Item>
StringId="DisplayName">Display Name</LocalizedString>
          </Metadata>
          <LocalizedString ElementType="ClaimType" ElementId="displayName"
        </TechnicalProfile>
StringId="UserHelpText">Your display name.</LocalizedString>
      </TechnicalProfiles>
          <LocalizedString ElementType="ClaimType" ElementId="surname"
    </ClaimsProvider>
StringId="DisplayName">Surname</LocalizedString>
    <ClaimsProvider>
          <LocalizedString ElementType="ClaimType" ElementId="surname"
      <DisplayName>Token Issuer</DisplayName>
StringId="UserHelpText">Your surname (also known as family name or last name).
      <TechnicalProfiles>
</LocalizedString>
        <TechnicalProfile Id="JwtIssuer">
          <LocalizedString ElementType="ClaimType" ElementId="givenName"
          <DisplayName>JWT Issuer</DisplayName>
StringId="DisplayName">Given Name</LocalizedString>
          <Protocol Name="OpenIdConnect" />
          <LocalizedString ElementType="ClaimType" ElementId="givenName"
          <!--Protocol Name="SAML2" /-->
StringId="UserHelpText">Your given name (also known as first name).
          <OutputTokenFormat>JWT</OutputTokenFormat>
</LocalizedString>
          <Metadata>
          <LocalizedString ElementType="UxElement"
            <!--Item
StringId="button_continue">Create</LocalizedString>
Key="PartnerEntity">https://testdp.stellarcyber.ai/sso/saml/metadata</Item--
          <LocalizedString ElementType="UxElement"
>
StringId="error_fieldIncorrect">One or more fields are filled out incorrectly.
            <Item Key="client_id">{service:te}</Item>

180
Please check your entries and try again.</LocalizedString>
            <Item
181
          <LocalizedString ElementType="UxElement"
Key="issuer_refresh_token_user_identity_claim_type">objectId</Item>
182
StringId="error_passwordEntryMismatch">The password entry fields do not match.
            <Item Key="SendTokenResponseBodyWithJsonNumbers">true</Item>
183
Please enter the same password in both fields and try again.</LocalizedString>
          </Metadata>
184
          <LocalizedString ElementType="UxElement"
          <CryptographicKeys>
185
StringId="error_requiredFieldMissing">A required field is missing. Please fill
            <!--Key Id="issuer_secret"
186
out all required fields and try again.</LocalizedString>
StorageReferenceId="B2C_1A_TokenSigningKeyContainer" />
187
          <LocalizedString ElementType="UxElement"
            <Key Id="issuer_refresh_token_key"
188
StringId="helplink_text">What is this?</LocalizedString>
StorageReferenceId="B2C_1A_TokenEncryptionKeyContainer" /-->
189
          <LocalizedString ElementType="UxElement"
            <Key Id="MetadataSigning"
190
StringId="initial_intro">Please provide the following details.
StorageReferenceId="B2C_1A_SamlIdpCert" />
191
</LocalizedString>
            <Key Id="SamlMessageSigning"
192
          <LocalizedString ElementType="UxElement"
StorageReferenceId="B2C_1A_SamlIdpCert" />
193
StringId="preloader_alt">Please wait</LocalizedString>
            <Key Id="SamlAssertionSigning"
194
          <LocalizedString ElementType="UxElement"
StorageReferenceId="B2C_1A_SamlIdpCert" />
195
StringId="required_field">This information is required.</LocalizedString>
          </CryptographicKeys>
196
          <LocalizedString ElementType="UxElement"
          <UseTechnicalProfileForSessionManagement ReferenceId="SM-jwt-
197
StringId="button_cancel">Cancel</LocalizedString>
issuer" />
198
          <LocalizedString ElementType="UxElement"
        </TechnicalProfile>
199
StringId="ver_but_edit">Change e-mail</LocalizedString>
      </TechnicalProfiles>
200
          <LocalizedString ElementType="UxElement"
    </ClaimsProvider>
201
StringId="ver_but_resend">Send new code</LocalizedString>
  </ClaimsProviders>
202
          <LocalizedString ElementType="UxElement"
  <UserJourneys>
203
StringId="ver_but_send">Send verification code</LocalizedString>
    <UserJourney Id="SignUpOrSignIn1">
204
          <LocalizedString ElementType="UxElement"
      <OrchestrationSteps>
205
StringId="ver_but_verify">Verify code</LocalizedString>
        <OrchestrationStep Order="1" Type="CombinedSignInAndSignUp"
206
          <LocalizedString ElementType="UxElement"
ContentDefinitionReferenceId="api.signuporsignin">
207
StringId="ver_fail_code_expired">That code is expired. Please request a new
          <ClaimsProviderSelections>
208
code.</LocalizedString>
            <ClaimsProviderSelection
209
          <LocalizedString ElementType="UxElement"
ValidationClaimsExchangeId="LocalAccountSigninEmailExchange" />
210
StringId="ver_fail_no_retry">You've made too many incorrect attempts. Please
          </ClaimsProviderSelections>
211
try again later.</LocalizedString>
          <ClaimsExchanges>
212
            <ClaimsExchange Id="LocalAccountSigninEmailExchange"
          <LocalizedString ElementType="UxElement"
213
StringId="ver_fail_retry">That code is incorrect. Please try again.
TechnicalProfileReferenceId="SelfAsserted-LocalAccountSignin-Email" />
214
</LocalizedString>
          </ClaimsExchanges>
215
          <LocalizedString ElementType="UxElement"
        </OrchestrationStep>
216
StringId="ver_fail_server">We are having trouble verifying your email address.
        <OrchestrationStep Order="2" Type="ClaimsExchange">
217
Please enter a valid email address and try again.</LocalizedString>
          <Preconditions>
218
          <LocalizedString ElementType="UxElement"
            <Precondition Type="ClaimsExist" ExecuteActionsIf="true">
219
StringId="ver_fail_throttled">There have been too many requests to verify this
              <Value>objectId</Value>
220
email address. Please wait a while, then try again.</LocalizedString>
              <Action>SkipThisOrchestrationStep</Action>
221
          <LocalizedString ElementType="UxElement"
            </Precondition>
222
StringId="ver_info_msg">Verification code has been sent to your inbox. Please
          </Preconditions>
223
copy it to the input box below.</LocalizedString>
          <ClaimsExchanges>
224
          <LocalizedString ElementType="UxElement"
            <ClaimsExchange Id="SignUpWithLogonEmailExchange"
StringId="ver_input">Verification code</LocalizedString>
TechnicalProfileReferenceId="LocalAccountSignUpWithLogonEmail" />
          <LocalizedString ElementType="UxElement"
<TrustFrameworkPolicy xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          </ClaimsExchanges>
1
StringId="ver_intro_msg">Verification is necessary. Please click Send button.
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
        </OrchestrationStep>
2
xmlns="http://schemas.microsoft.com/online/cpim/schemas/2013/06"
</LocalizedString>
        <!-- This step reads any user attributes that we may not have
3
PolicySchemaVersion="0.3.0.0" TenantId="stellarpmb2c.onmicrosoft.com"
          <LocalizedString ElementType="UxElement" StringId="ver_success_msg">E-mail
received when in the token. -->
4
PolicyId="B2C_1A_TrustFrameworkExtensions"
address verified. You can now continue.</LocalizedString>
        <OrchestrationStep Order="3" Type="ClaimsExchange">
5
PublicPolicyUri="http://stellarpmb2c.onmicrosoft.com/B2C_1A_TrustFrameworkExten
          <LocalizedString ElementType="ErrorMessage"
          <ClaimsExchanges>
6
sions" TenantObjectId="04fcef19-20fe-4655-9498-3e5050b6dda1">
            <ClaimsExchange Id="AADUserReadWithObjectId"
StringId="ServiceThrottled">There are too many requests at this moment. Please wait
7
  <BasePolicy>
for some time and try again.</LocalizedString>
TechnicalProfileReferenceId="AAD-UserReadUsingObjectId" />
8
    <TenantId>stellarpmb2c.onmicrosoft.com</TenantId>
          <LocalizedString ElementType="ErrorMessage"
          </ClaimsExchanges>
9
    <PolicyId>B2C_1A_TrustFrameworkLocalization</PolicyId>
StringId="UserMessageIfClaimNotVerified">Claim not verified: {0}</LocalizedString>
10
        </OrchestrationStep>
  </BasePolicy>
        <OrchestrationStep Order="4" Type="SendClaims"
11
          <LocalizedString ElementType="ErrorMessage"
  <BuildingBlocks></BuildingBlocks>
12
StringId="UserMessageIfClaimsPrincipalAlreadyExists">A user with the specified ID
CpimIssuerTechnicalProfileReferenceId="JwtIssuer" />
  <ClaimsProviders>
13
already exists. Please choose a different one.</LocalizedString>
      </OrchestrationSteps>
      <ClientDefinition ReferenceId="DefaultWeb" />
    <ClaimsProvider>
14
          <LocalizedString ElementType="ErrorMessage"
    </UserJourney>
      <DisplayName>Local Account SignIn</DisplayName>
StringId="UserMessageIfIncorrectPattern">Incorrect pattern for: {0}
15
      <TechnicalProfiles>
</LocalizedString>
    <UserJourney Id="ProfileEdit">
16
        <TechnicalProfile Id="login-NonInteractive">
17
          <LocalizedString ElementType="ErrorMessage"
      <OrchestrationSteps>
          <Metadata>
18
StringId="UserMessageIfInvalidInput">{0} has invalid input.</LocalizedString>
        <OrchestrationStep Order="1" Type="ClaimsProviderSelection"
            <Item Key="client_id">01590824-a092-4271-99a3-f3e37b9f22cc</Item>
19
          <LocalizedString ElementType="ErrorMessage"
ContentDefinitionReferenceId="api.idpselections">
            <Item Key="IdTokenAudience">0c54849b-121f-496e-b1c3-
StringId="UserMessageIfMissingRequiredElement">Missing required element: {0}
20
          <ClaimsProviderSelections>
406976bec48b</Item>
</LocalizedString>
            <ClaimsProviderSelection
21
          </Metadata>
          <LocalizedString ElementType="ErrorMessage"
TargetClaimsExchangeId="LocalAccountSigninEmailExchange" />
22
StringId="UserMessageIfValidationError">Error in validation by: {0}
          <InputClaims>
23
          </ClaimsProviderSelections>
            <InputClaim ClaimTypeReferenceId="client_id"
24
</LocalizedString>
        </OrchestrationStep>
DefaultValue="01590824-a092-4271-99a3-f3e37b9f22cc" />
25
        </LocalizedStrings>
        <OrchestrationStep Order="2" Type="ClaimsExchange">
            <InputClaim ClaimTypeReferenceId="resource_id"
26
      </LocalizedResources>
          <ClaimsExchanges>
PartnerClaimType="resource" DefaultValue="0c54849b-121f-496e-b1c3-406976bec48b"
      <!-- Self-asserted page English-->
            <ClaimsExchange Id="LocalAccountSigninEmailExchange"
27
/>
28
      <LocalizedResources Id="api.selfasserted.en">
TechnicalProfileReferenceId="SelfAsserted-LocalAccountSignin-Email" />
          </InputClaims>
29
        <LocalizedStrings>
          </ClaimsExchanges>
        </TechnicalProfile>
30
          <LocalizedString ElementType="ErrorMessage"
        </OrchestrationStep>
      </TechnicalProfiles>
31
StringId="UserMessageIfClaimsPrincipalAlreadyExists">You are already registered,
        <OrchestrationStep Order="3" Type="ClaimsExchange">
    </ClaimsProvider>
please press the back button and sign in instead.</LocalizedString>
          <ClaimsExchanges>
32
    <ClaimsProvider>
        </LocalizedStrings>
            <ClaimsExchange Id="AADUserReadWithObjectId"
33
      <DisplayName>Azure Active Directory</DisplayName>
34
      </LocalizedResources>
TechnicalProfileReferenceId="AAD-UserReadUsingObjectId" />
      <TechnicalProfiles>
35
      <!-- Password reset page English-->
          </ClaimsExchanges>
        <TechnicalProfile Id="AAD-Common">
36
      <LocalizedResources Id="api.localaccountpasswordreset.en">
        </OrchestrationStep>
          <Metadata>
        <LocalizedStrings>
37
        <OrchestrationStep Order="4" Type="ClaimsExchange">
            <!--Insert b2c-extensions-app application ID here, for example:
          <LocalizedString ElementType="ClaimType" ElementId="email"
          <ClaimsExchanges>
38
11111111-1111-1111-1111-111111111111-->
39
StringId="DisplayName">Email Address</LocalizedString>
            <ClaimsExchange Id="B2CUserProfileUpdateExchange"
            <Item Key="ClientId">0c0abe38-79ab-45d3-99fe-9378eec7b16f</Item>
40
          <LocalizedString ElementType="ClaimType" ElementId="email"
TechnicalProfileReferenceId="SelfAsserted-ProfileUpdate" />
            <!--Insert b2c-extensions-app application ObjectId here, for
StringId="UserHelpText">Email address that can be used to contact you.
          </ClaimsExchanges>
41

example: 22222222-2222-2222-2222-222222222222-->
</LocalizedString>
        </OrchestrationStep>
<TrustFrameworkPolicy xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          <LocalizedString ElementType="ClaimType" ElementId="email"
            <Item Key="ApplicationObjectId">3c34826e-3bd5-47a2-b44d-
        <OrchestrationStep Order="5" Type="SendClaims"
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
StringId="PatternHelpText">Please enter a valid email address.</LocalizedString>
08c09034cef2</Item>
CpimIssuerTechnicalProfileReferenceId="JwtIssuer" />
xmlns="http://schemas.microsoft.com/online/cpim/schemas/2013/06"
          <LocalizedString ElementType="ClaimType" ElementId="newPassword"
          </Metadata>
      </OrchestrationSteps>
PolicySchemaVersion="0.3.0.0" TenantId="stellarpmb2c.onmicrosoft.com"
StringId="DisplayName">New Password</LocalizedString>
        </TechnicalProfile>
      <ClientDefinition ReferenceId="DefaultWeb" />
PolicyId="B2C_1A_TrustFrameworkExtensions"
      </TechnicalProfiles>
          <LocalizedString ElementType="ClaimType" ElementId="newPassword"
    </UserJourney>
PublicPolicyUri="http://stellarpmb2c.onmicrosoft.com/B2C_1A_TrustFrameworkExte
StringId="UserHelpText">Enter new password</LocalizedString>
    </ClaimsProvider>
    <UserJourney Id="PasswordReset">
  </ClaimsProviders>
nsions" TenantObjectId="04fcef19-20fe-4655-9498-3e5050b6dda1">
          <LocalizedString ElementType="ClaimType" ElementId="newPassword"
      <OrchestrationSteps>
  <BasePolicy>
        <OrchestrationStep Order="1" Type="ClaimsExchange">
  <!--UserJourneys>
StringId="PatternHelpText">8-16 characters, containing 3 out of 4 of the following:
    <TenantId>stellarpmb2c.onmicrosoft.com</TenantId>
Lowercase characters, uppercase characters, digits (0-9), and one or more of the
          <ClaimsExchanges>
    </UserJourneys-->
    <PolicyId>B2C_1A_TrustFrameworkLocalization</PolicyId>
following symbols: @ # $ % ^ &amp; * - _ + = [ ] { } | \ : ' , ? / ` ~ " ( ) ; .
            <ClaimsExchange Id="PasswordResetUsingEmailAddressExchange"
  </BasePolicy>
</TrustFrameworkPolicy>
</LocalizedString>
TechnicalProfileReferenceId="LocalAccountDiscoveryUsingEmailAddress" />
  <!--BuildingBlocks></BuildingBlocks-->
          <LocalizedString ElementType="ClaimType" ElementId="reenterPassword"
          </ClaimsExchanges>
  <BuildingBlocks>
StringId="DisplayName">Confirm New Password</LocalizedString>
        </OrchestrationStep>
    <ClaimsSchema>
          <LocalizedString ElementType="ClaimType" ElementId="reenterPassword"
        <OrchestrationStep Order="2" Type="ClaimsExchange">
          <ClaimsExchanges>
      <!--TOTP claims-->
StringId="UserHelpText">Confirm new password</LocalizedString>
            <ClaimsExchange Id="NewCredentials"
      <ClaimType Id="emails">
          <LocalizedString ElementType="ClaimType" ElementId="reenterPassword"
        <DisplayName>Email Addresses</DisplayName>
StringId="PatternHelpText">8-16 characters, containing 3 out of 4 of the following:
TechnicalProfileReferenceId="LocalAccountWritePasswordUsingObjectId" />
Lowercase characters, uppercase characters, digits (0-9), and one or more of the
        <DataType>stringCollection</DataType>
          </ClaimsExchanges>
        <AdminHelpText>Email addresses of the user.</AdminHelpText>
following symbols: @ # $ % ^ &amp; * - _ + = [ ] { } | \ : ' , ? / ` ~ " ( ) ; .
        </OrchestrationStep>
        <UserHelpText>Your email addresses.</UserHelpText>
        <OrchestrationStep Order="3" Type="SendClaims"
</LocalizedString>
      </ClaimType>
          <LocalizedString ElementType="UxElement"
CpimIssuerTechnicalProfileReferenceId="JwtIssuer" />
      <ClaimType Id="ReadOnlyEmail">
StringId="error_passwordEntryMismatch">The password entry fields do not match.
      </OrchestrationSteps>
        <DisplayName>ReadOnlyEmail</DisplayName>
Please enter the same password in both fields and try again.</LocalizedString>
      <ClientDefinition ReferenceId="DefaultWeb" />
        <DataType>string</DataType>
          <LocalizedString ElementType="UxElement"
    </UserJourney>
        <UserHelpText>Add help text here</UserHelpText>
StringId="error_fieldIncorrect">One or more fields are filled out incorrectly.
  </UserJourneys>
        <UserInputType>Readonly</UserInputType>
Please check your entries and try again.</LocalizedString>
</TrustFrameworkPolicy>
      </ClaimType>
          <LocalizedString ElementType="UxElement"
      <ClaimType Id="totpIdentifier">
StringId="button_continue">Continue</LocalizedString>
        <DisplayName>UserId, Phone number or Email which can present the
          <LocalizedString ElementType="UxElement"
StringId="button_cancel">Cancel</LocalizedString>
user's identity</DisplayName>
        <DataType>string</DataType>
          <LocalizedString ElementType="ErrorMessage"
        <AdminHelpText>UserId, Phone number or Email which can be used to
StringId="UserMessageIfClaimsPrincipalDoesNotExist">An account could not be found
create QR code identity.</AdminHelpText>
for the provided user ID.</LocalizedString>
        <UserInputType>Paragraph</UserInputType>
          <LocalizedString ElementType="ErrorMessage"
      </ClaimType>
StringId="UserMessageIfClaimsTransformationBooleanValueIsNotEqual">Your account has
been locked. Contact your support person to unlock it, then try again.
      <ClaimType Id="numberOfAvailableDevices">
        <DisplayName>Number of available devices:</DisplayName>
</LocalizedString>
        <DataType>string</DataType>
          <LocalizedString ElementType="UxElement" StringId="required_field">This
        <UserInputType>Paragraph</UserInputType>
information is required.</LocalizedString>
      </ClaimType>
          <LocalizedString ElementType="UxElement" StringId="ver_but_edit">Change e-
      <ClaimType Id="QrCodeScanInstruction">
mail</LocalizedString>
        <DisplayName>Once you've downloaded the Authenticator app, you can use
          <LocalizedString ElementType="UxElement" StringId="ver_but_resend">Send
any of the methods below to continue with enrollment.</DisplayName>
new code</LocalizedString>
        <DataType>string</DataType>
          <LocalizedString ElementType="UxElement" StringId="ver_but_send">Send
        <UserInputType>Paragraph</UserInputType>
verification code</LocalizedString>
      </ClaimType>
          <LocalizedString ElementType="UxElement" StringId="ver_but_verify">Verify
      <ClaimType Id="QrCodeVerifyInstruction">
code</LocalizedString>
        <DisplayName>Enter the verification code from your authenticator app .
          <LocalizedString ElementType="UxElement"
</DisplayName>
StringId="ver_fail_code_expired">That code is expired. Please request a new code.
        <DataType>string</DataType>
</LocalizedString>
        <UserInputType>Paragraph</UserInputType>
          <LocalizedString ElementType="UxElement"
      </ClaimType>
StringId="ver_fail_no_retry">You've made too many incorrect attempts. Please try
      <ClaimType Id="qrCodeContent">
again later.</LocalizedString>
        <DisplayName>QR Code Text</DisplayName>
          <LocalizedString ElementType="UxElement" StringId="ver_fail_retry">That
        <DataType>string</DataType>
code is incorrect. Please try again.</LocalizedString>
        <UserHelpText>QR code text</UserHelpText>
          <LocalizedString ElementType="UxElement" StringId="ver_fail_server">We are
        <UserInputType>Paragraph</UserInputType>
having trouble verifying your email address. Please enter a valid email address and
      </ClaimType>
try again.</LocalizedString>
      <ClaimType Id="secretKey">
          <LocalizedString ElementType="UxElement"
        <DisplayName>If you cant't scan the image, enter the Secret Key:
StringId="ver_fail_throttled">There have been too many requests to verify this email
</DisplayName>
address. Please wait a while, then try again.</LocalizedString>
        <DataType>string</DataType>
          <LocalizedString ElementType="UxElement"
        <UserHelpText>QR code secret</UserHelpText>
StringId="ver_info_msg">Verification code has been sent to your inbox. Please copy
        <UserInputType>Paragraph</UserInputType>
it to the input box below.</LocalizedString>
      </ClaimType>
          <LocalizedString ElementType="UxElement" StringId="ver_input">Verification
      <ClaimType Id="otpCode">
code</LocalizedString>
        <DisplayName>Enter your code</DisplayName>
          <LocalizedString ElementType="UxElement"
        <DataType>string</DataType>
StringId="ver_intro_msg">Verification is necessary. Please click Send button.
        <UserHelpText>Enter the 6-digit verification code generated by the the
</LocalizedString>
Authenticator app in the box</UserHelpText>
          <LocalizedString ElementType="UxElement" StringId="ver_success_msg">E-mail
        <UserInputType>TextBox</UserInputType>
address verified. You can now continue.</LocalizedString>
        <Restriction>
          <LocalizedString ElementType="ErrorMessage"
StringId="ServiceThrottled">There are too many requests at this moment. Please wait
          <Pattern RegularExpression="^[0-9]{6}$" HelpText="Enter the 6-digit
verification code generated by the the Authenticator app in the box" />
for some time and try again.</LocalizedString>
        </Restriction>
          <LocalizedString ElementType="ErrorMessage"
      </ClaimType>
StringId="UserMessageIfClaimNotVerified">Claim not verified: {0}</LocalizedString>
      <ClaimType Id="uriLabel">
          <LocalizedString ElementType="ErrorMessage"
        <DisplayName>Uri Label</DisplayName>
StringId="UserMessageIfClaimsPrincipalAlreadyExists">A user with the specified ID
        <DataType>string</DataType>
already exists. Please choose a different one.</LocalizedString>
      </ClaimType>
          <LocalizedString ElementType="ErrorMessage"
      <ClaimType Id="issuer">
StringId="UserMessageIfIncorrectPattern">Incorrect pattern for: {0}
        <DisplayName>Issuer</DisplayName>
</LocalizedString>
        <DataType>string</DataType>
          <LocalizedString ElementType="ErrorMessage"
      </ClaimType>
StringId="UserMessageIfInvalidInput">{0} has invalid input.</LocalizedString>
          <LocalizedString ElementType="ErrorMessage"
      <ClaimType Id="UserId">
        <DisplayName>Username</DisplayName>
StringId="UserMessageIfMissingRequiredElement">Missing required element: {0}

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86

        <DataType>string</DataType>
87
</LocalizedString>
        <AdminHelpText />
88
          <LocalizedString ElementType="ErrorMessage"
        <UserHelpText>Your username.</UserHelpText>
89
StringId="UserMessageIfValidationError">Error in validation by: {0}
        <UserInputType>TextBox</UserInputType>
90
</LocalizedString>
        <Restriction>
        </LocalizedStrings>
91
          <Pattern RegularExpression="^[a-zA-Z0-9]+[a-zA-Z0-9_-]*$"
92
      </LocalizedResources>
HelpText="The username you have provided is not valid. It must begin with an
93
      <!-- Edit profile sign-in page English-->
alphabetical character or number, and can only contain alphanumeric characters
94
      <LocalizedResources Id="api.idpselections.en">
and the following symbols: _ -" />
95
        <LocalizedStrings>
        </Restriction>
96
          <LocalizedString ElementType="UxElement" StringId="intro">Sign
      </ClaimType>
97
in</LocalizedString>
      <!--End of TOTP Claims-->
          <LocalizedString ElementType="ClaimsProvider"
98
    </ClaimsSchema>
StringId="LocalAccountSigninEmailExchange">Local Account Signin</LocalizedString>
99
    <ClaimsTransformations>
100
          <LocalizedString ElementType="ClaimsProvider"
      <!--TOTP Claim Transforms-->
101
StringId="FacebookExchange">Facebook</LocalizedString>
      <ClaimsTransformation Id="GetEmailFromReadOnlyEmail"
102
        </LocalizedStrings>
      </LocalizedResources>
TransformationMethod="CopyClaim">
103
        <InputClaims>
      <!-- Edit profile sign-in with local account English-->
104
          <InputClaim ClaimTypeReferenceId="ReadOnlyEmail"
105
      <LocalizedResources Id="api.localaccountsignin.en">
TransformationClaimType="inputClaim" />
106
        <LocalizedStrings>
        </InputClaims>
107
          <LocalizedString ElementType="ClaimType" ElementId="signInName"
        <OutputClaims>
108
StringId="DisplayName">Email Address</LocalizedString>
          <OutputClaim ClaimTypeReferenceId="email"
          <LocalizedString ElementType="ClaimType" ElementId="password"
109
TransformationClaimType="outputClaim" />
110
StringId="DisplayName">Password</LocalizedString>
        </OutputClaims>
          <LocalizedString ElementType="UxElement"
111
      </ClaimsTransformation>
112
StringId="button_continue">Continue</LocalizedString>
      <ClaimsTransformation Id="GetEmailFromEmails"
113
          <LocalizedString ElementType="UxElement"
TransformationMethod="GetSingleItemFromStringCollection">
StringId="button_cancel">Cancel</LocalizedString>
114
        <InputClaims>
          <LocalizedString ElementType="ErrorMessage"
115
          <InputClaim ClaimTypeReferenceId="emails"
116
StringId="ResourceOwnerFlowInvalidCredentials">Your password is incorrect.
TransformationClaimType="collection" />
117
</LocalizedString>
        </InputClaims>
118
          <LocalizedString ElementType="ErrorMessage"
StringId="UserMessageIfInvalidPassword">Your password is incorrect.
        <OutputClaims>
119
          <OutputClaim ClaimTypeReferenceId="ReadOnlyEmail"
</LocalizedString>
120
TransformationClaimType="extractedItem" />
          <LocalizedString ElementType="ErrorMessage"
121
        </OutputClaims>
122
StringId="UserMessageIfPasswordExpired">Your password has expired.</LocalizedString>
      </ClaimsTransformation>
123
          <LocalizedString ElementType="ErrorMessage"
      <!-- Create a TOPT secret key-->
124
StringId="UserMessageIfClaimsPrincipalDoesNotExist">We can't seem to find your
      <ClaimsTransformation Id="CreateSecret"
account.</LocalizedString>
125
TransformationMethod="CreateOtpSecret">
          <LocalizedString ElementType="ErrorMessage"
126
        <OutputClaims>
127
StringId="UserMessageIfOldPasswordUsed">Looks like you used an old password.
          <OutputClaim ClaimTypeReferenceId="secretKey"
128
</LocalizedString>
TransformationClaimType="outputClaim" />
          <LocalizedString ElementType="ErrorMessage"
129
        </OutputClaims>
130
StringId="DefaultMessage">Invalid username or password.</LocalizedString>
      </ClaimsTransformation>
          <LocalizedString ElementType="ErrorMessage"
131
      <!-- Create the TOTP issuer name. The issuer name is your tenant name,
132
StringId="UserMessageIfUserAccountDisabled">Your account has been locked. Contact
such as "Contoso demo" -->
133
your support person to unlock it, then try again.</LocalizedString>
          <LocalizedString ElementType="ErrorMessage"
      <ClaimsTransformation Id="CreateIssuer"
134
TransformationMethod="CreateStringClaim">
135
StringId="UserMessageIfUserAccountLocked">Your account is temporarily locked to
        <InputParameters>
prevent unauthorized use. Try again later.</LocalizedString>
136
          <InputParameter Id="value" DataType="string" Value="
          <LocalizedString ElementType="ErrorMessage"
137
{AuthenticatorIssuer}" />
138
StringId="AADRequestsThrottled">There are too many requests at this moment. Please
        </InputParameters>
139
wait for some time and try again.</LocalizedString>
        <OutputClaims>
140
        </LocalizedStrings>
          <OutputClaim ClaimTypeReferenceId="issuer"
141
      </LocalizedResources>
TransformationClaimType="createdClaim" />
      <!-- Edit profile page English-->
142
        </OutputClaims>
143
      <LocalizedResources Id="api.selfasserted.profileupdate.en">
      </ClaimsTransformation>
144
        <LocalizedStrings>
      <!-- Create the TOTP URI label. The label is a combination of the
145
          <LocalizedString ElementType="ClaimType" ElementId="displayName"
totpIdentifier and the issuer name:
146
StringId="DisplayName">Display Name</LocalizedString>
           For example, Contoso demo:emily@fabrikam.com-->
          <LocalizedString ElementType="ClaimType" ElementId="displayName"
147
      <ClaimsTransformation Id="CreateUriLabel"
StringId="UserHelpText">Your display name.</LocalizedString>
148
TransformationMethod="FormatStringMultipleClaims">
149
          <LocalizedString ElementType="ClaimType" ElementId="surname"
        <InputClaims>
150
StringId="DisplayName">Surname</LocalizedString>
          <InputClaim ClaimTypeReferenceId="issuer"
151
          <LocalizedString ElementType="ClaimType" ElementId="surname"
TransformationClaimType="inputClaim1" />
152
StringId="UserHelpText">Your surname (also known as family name or last name).
          <InputClaim ClaimTypeReferenceId="totpIdentifier"
</LocalizedString>
153
TransformationClaimType="inputClaim2" />
          <LocalizedString ElementType="ClaimType" ElementId="givenName"
154
        </InputClaims>
StringId="DisplayName">Given Name</LocalizedString>
155
        <InputParameters>
156
          <LocalizedString ElementType="ClaimType" ElementId="givenName"
          <InputParameter Id="stringFormat" DataType="string" Value="{0}:{1}"
157
StringId="UserHelpText">Your given name (also known as first name).
/>
158
</LocalizedString>
        </InputParameters>
          <LocalizedString ElementType="UxElement"
159
        <OutputClaims>
160
StringId="button_continue">Continue</LocalizedString>
          <LocalizedString ElementType="UxElement"
          <OutputClaim ClaimTypeReferenceId="uriLabel"
161
TransformationClaimType="outputClaim" />
162
StringId="button_cancel">Cancel</LocalizedString>
        </OutputClaims>
163
        </LocalizedStrings>
      </ClaimsTransformation>
      </LocalizedResources>
164
      <!-- Create the TOTP URI. The label is a combination of the
      <!-- Add more languages here -->
165
CreateUriLabel and the secret key:
166
    </Localization>
      For example, otpauth://totp/Contoso%20demo:emily@fabrikam.com?
167
  </BuildingBlocks>
secret=fay2lj7ynpntjgqa&issuer=Contoso+demo
</TrustFrameworkPolicy>
168
      This URI is later converted into a QR code that is presented to the
169
user-->
170
      <ClaimsTransformation Id="CreateUriString"
171
TransformationMethod="BuildUri">
172
        <InputClaims>
173

174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
254
255
256
257
258
259
260

          <InputClaim ClaimTypeReferenceId="uriLabel"
TransformationClaimType="path" />
          <InputClaim ClaimTypeReferenceId="secretKey"
TransformationClaimType="query.secret" />
        </InputClaims>
        <InputParameters>
          <InputParameter Id="scheme" DataType="string" Value="otpauth" />
          <InputParameter Id="host" DataType="string" Value="totp" />
          <InputParameter Id="query.issuer" DataType="string" Value="
{AuthenticatorIssuer}" />
        </InputParameters>
        <OutputClaims>
          <OutputClaim ClaimTypeReferenceId="qrCodeContent"
TransformationClaimType="outputClaim" />
        </OutputClaims>
      </ClaimsTransformation>
      <!-- Copy the signInName to the totpIdentifier -->
      <ClaimsTransformation Id="SignInNameToTotpIdentifier"
TransformationMethod="CopyClaim">
        <InputClaims>
          <InputClaim ClaimTypeReferenceId="signInName"
TransformationClaimType="inputClaim" />
        </InputClaims>
        <OutputClaims>
          <OutputClaim ClaimTypeReferenceId="totpIdentifier"
TransformationClaimType="outputClaim" />
        </OutputClaims>
      </ClaimsTransformation>
      <!-- Copy the email to the totpIdentifier -->
      <ClaimsTransformation Id="EmailToTotpIdentifier"
TransformationMethod="CopyClaim">
        <InputClaims>
          <InputClaim ClaimTypeReferenceId="email"
TransformationClaimType="inputClaim" />
        </InputClaims>
        <OutputClaims>
          <OutputClaim ClaimTypeReferenceId="totpIdentifier"
TransformationClaimType="outputClaim" />
        </OutputClaims>
      </ClaimsTransformation>
      <!-- Copy the UserId to the totpIdentifier -->
      <ClaimsTransformation Id="UserIdToLogonIdentifier"
TransformationMethod="CopyClaim">
        <InputClaims>
          <InputClaim ClaimTypeReferenceId="UserId"
TransformationClaimType="inputClaim" />
        </InputClaims>
        <OutputClaims>
          <OutputClaim ClaimTypeReferenceId="totpIdentifier"
TransformationClaimType="outputClaim" />
        </OutputClaims>
      </ClaimsTransformation>
      <!--Claim if Phone SignIn is used-->
      <!--<ClaimsTransformation Id="PhoneNumberIdToLogonIdentifier"
TransformationMethod="CopyClaim">
      <InputClaims>
        <InputClaim ClaimTypeReferenceId="phoneNumber"
TransformationClaimType="inputClaim" />
      </InputClaims>
      <OutputClaims>
        <OutputClaim ClaimTypeReferenceId="totpIdentifier"
TransformationClaimType="outputClaim" />
      </OutputClaims>
    </ClaimsTransformation>-->
      <!-- end of TOTP Claims Transforms-->
    </ClaimsTransformations>
    <ContentDefinitions>
      <ContentDefinition Id="api.selfasserted.totp">
        <LoadUri>~/tenant/templates/AzureBlue/selfAsserted.cshtml</LoadUri>
        <RecoveryUri>~/common/default_page_error.html</RecoveryUri>
        <DataUri>urn:com:microsoft:aad:b2c:elements:contract:selfasserted:2.1.
9</DataUri>
        <Metadata>
          <Item Key="DisplayName">Collect information from user page</Item>
        </Metadata>
        <LocalizedResourcesReferences>
          <LocalizedResourcesReference Language="en"
LocalizedResourcesReferenceId="api.selfasserted.totp.en" />
        </LocalizedResourcesReferences>
      </ContentDefinition>
    </ContentDefinitions>
    <Localization>
      <!-- TOTP localized strings (English) -->
      <LocalizedResources Id="api.selfasserted.totp.en">
        <LocalizedStrings>
          <LocalizedString ElementType="DisplayControl"
ElementId="authenticatorAppIconControl" StringId="title_text">Download the

261
262
263
264
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
315
316
317
318
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
344
345
346
347

Microsoft Authenticator using the download links for iOS and Android or use
any other authenticator app of your choice.</LocalizedString>
          <LocalizedString ElementType="DisplayControl"
ElementId="authenticatorAppIconControl" StringId="instruction_text">Once
you've downloaded the Authenticator app, you can use any of the methods below
to continue with enrollment.</LocalizedString>
          <LocalizedString ElementType="ClaimType"
ElementId="QrCodeScanInstruction" StringId="DisplayName">Once you've
downloaded the Authenticator app, you can use any of the methods below to
continue with enrollment.</LocalizedString>
          <LocalizedString ElementType="DisplayControl"
ElementId="totpQrCodeControl" StringId="title_text">Scan the QR
code</LocalizedString>
          <LocalizedString ElementType="DisplayControl"
ElementId="totpQrCodeControl" StringId="info_msg">You can download the
Microsoft Authenticator app or use any other authenticator app of your choice.
</LocalizedString>
          <LocalizedString ElementType="DisplayControl"
ElementId="totpQrCodeControl" StringId="link_text">Can't scan? Try
this</LocalizedString>
          <LocalizedString ElementType="DisplayControl"
ElementId="authenticatorInfoControl" StringId="title_text">Enter the account
details manually</LocalizedString>
          <LocalizedString ElementType="DisplayControl"
ElementId="authenticatorInfoControl" StringId="account_name">Account Name:
</LocalizedString>
          <LocalizedString ElementType="DisplayControl"
ElementId="authenticatorInfoControl"
StringId="display_prefix">Secret</LocalizedString>
          <LocalizedString ElementType="DisplayControl"
ElementId="authenticatorInfoControl" StringId="collapse_text">Still having
trouble?</LocalizedString>
          <!-- Verification -->
          <LocalizedString ElementType="ClaimType"
ElementId="QrCodeVerifyInstruction" StringId="DisplayName">Enter the
verification code from your authenticator app .</LocalizedString>
          <LocalizedString ElementType="ClaimType" ElementId="otpCode"
StringId="DisplayName">Enter your code.</LocalizedString>
          <!-- <LocalizedString ElementType="UxElement"
StringId="button_continue">Verify</LocalizedString> -->
        </LocalizedStrings>
      </LocalizedResources>
    </Localization>
    <DisplayControls>
      <!-- Render the authenticator apps icon. -->
      <DisplayControl Id="authenticatorAppIconControl"
UserInterfaceControlType="AuthenticatorAppIconControl" />
      <!-- Render the QR code. It takes the URI (qrCodeContent) input claim
and renders it as a QR code-->
      <DisplayControl Id="totpQrCodeControl"
UserInterfaceControlType="QrCodeControl">
        <InputClaims>
          <InputClaim ClaimTypeReferenceId="qrCodeContent" />
        </InputClaims>
        <DisplayClaims>
          <DisplayClaim ClaimTypeReferenceId="qrCodeContent"
ControlClaimType="QrCodeContent" />
        </DisplayClaims>
      </DisplayControl>
      <!-- Render the TOTP information. It takes the totpIdentifier and the
secretKey input claims and renders as a plan text-->
      <DisplayControl Id="authenticatorInfoControl"
UserInterfaceControlType="AuthenticatorInfoControl">
        <InputClaims>
          <InputClaim ClaimTypeReferenceId="totpIdentifier" />
          <InputClaim ClaimTypeReferenceId="secretKey" />
        </InputClaims>
        <DisplayClaims>
          <DisplayClaim ClaimTypeReferenceId="totpIdentifier" />
          <DisplayClaim ClaimTypeReferenceId="secretKey" />
        </DisplayClaims>
      </DisplayControl>
    </DisplayControls>
    <!--End of TOTP contols-->
  </BuildingBlocks>
  <ClaimsProviders>
    <!--Start TOTP-->
    <ClaimsProvider>
      <DisplayName>TOTP</DisplayName>
      <TechnicalProfiles>
        <!-- Begin the TOTP verification process.
             This technical profile is called right before the AzureMfa-
VerifyOTP technical profile-->
        <TechnicalProfile Id="AzureMfa-BeginVerifyOTP">
          <DisplayName>Create Device</DisplayName>
          <Protocol Name="Proprietary"
Handler="Web.TPEngine.Providers.AzureMfaProtocolProvider, Web.TPEngine,

348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434

Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
          <Metadata>
            <Item Key="Operation">BeginVerifyOTP</Item>
          </Metadata>
          <InputClaims>
            <InputClaim ClaimTypeReferenceId="secretKey" />
            <InputClaim ClaimTypeReferenceId="objectId" />
            <InputClaim ClaimTypeReferenceId="userPrincipalName" />
          </InputClaims>
        </TechnicalProfile>
        <!-- Verify the TOTP verification process.
             This technical profile is called immediately after the AzureMfa-
BeginVerifyOTP technical profile-->
        <TechnicalProfile Id="AzureMfa-VerifyOTP">
          <DisplayName>Verify OTP</DisplayName>
          <Protocol Name="Proprietary"
Handler="Web.TPEngine.Providers.AzureMfaProtocolProvider, Web.TPEngine,
Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
          <Metadata>
            <Item Key="Operation">VerifyOTP</Item>
          </Metadata>
          <InputClaims>
            <InputClaim ClaimTypeReferenceId="otpCode" />
          </InputClaims>
        </TechnicalProfile>
        <!-- Check the number of devices available for the user.
             If the number of available devices is zero it indicates the user
hasn't enrolled yet -->
        <TechnicalProfile Id="AzureMfa-GetAvailableDevices">
          <DisplayName>Get Available Devices</DisplayName>
          <Protocol Name="Proprietary"
Handler="Web.TPEngine.Providers.AzureMfaProtocolProvider, Web.TPEngine,
Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
          <Metadata>
            <Item Key="Operation">GetAvailableDevices</Item>
          </Metadata>
          <InputClaims>
            <InputClaim ClaimTypeReferenceId="userPrincipalName" />
          </InputClaims>
          <OutputClaims>
            <OutputClaim ClaimTypeReferenceId="numberOfAvailableDevices" />
          </OutputClaims>
        </TechnicalProfile>
        <!-- TOTP session manager-->
        <TechnicalProfile Id="SM-MFA-TOTP">
          <DisplayName>Session Mananagement Provider</DisplayName>
          <Protocol Name="Proprietary"
Handler="Web.TPEngine.SSO.DefaultSSOSessionProvider, Web.TPEngine,
Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
          <PersistedClaims>
            <PersistedClaim ClaimTypeReferenceId="totpIdentifier" />
            <PersistedClaim ClaimTypeReferenceId="issuer" />
          </PersistedClaims>
        </TechnicalProfile>
        <!-- Self-asserted technical profile that asks the user to enroll to
the TOTP MFA. The technical profile:
              1) Creates the TOTP secret
              2) Sets the issuer name and the URI
              3) Renders the QR code and the authentication URI
             -->
        <TechnicalProfile Id="EnableOTPAuthentication">
          <DisplayName>Sign up with Authenticator app</DisplayName>
          <Protocol Name="Proprietary"
Handler="Web.TPEngine.Providers.SelfAssertedAttributeProvider, Web.TPEngine,
Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
          <Metadata>
            <Item
Key="ContentDefinitionReferenceId">api.selfasserted.totp</Item>
            <Item Key="language.button_continue">Continue</Item>
          </Metadata>
          <CryptographicKeys>
            <!--Key Id="issuer_secret"
StorageReferenceId="B2C_1A_TokenSigningKeyContainer" /-->
            <Key Id="MetadataSigning" StorageReferenceId="B2C_1A_SamlIdpCert"
/>
            <Key Id="SamlMessageSigning"
StorageReferenceId="B2C_1A_SamlIdpCert" />
            <Key Id="SamlAssertionSigning"
StorageReferenceId="B2C_1A_SamlIdpCert" />
          </CryptographicKeys>
          <InputClaimsTransformations>
            <InputClaimsTransformation ReferenceId="CreateSecret" />
            <InputClaimsTransformation ReferenceId="CreateIssuer" />
            <InputClaimsTransformation ReferenceId="CreateUriLabel" />
            <InputClaimsTransformation ReferenceId="CreateUriString" />
          </InputClaimsTransformations>
          <InputClaims>

435
436
437
438
439
440
441
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521

            <InputClaim ClaimTypeReferenceId="qrCodeContent" />
            <InputClaim ClaimTypeReferenceId="secretKey" />
          </InputClaims>
          <DisplayClaims>
            <DisplayClaim
DisplayControlReferenceId="authenticatorAppIconControl" />
            <DisplayClaim ClaimTypeReferenceId="QrCodeScanInstruction" />
            <DisplayClaim DisplayControlReferenceId="totpQrCodeControl" />
            <DisplayClaim DisplayControlReferenceId="authenticatorInfoControl"
/>
          </DisplayClaims>
          <OutputClaims>
            <OutputClaim ClaimTypeReferenceId="objectId" />
            <OutputClaim ClaimTypeReferenceId="secretKey" />
          </OutputClaims>
          <UseTechnicalProfileForSessionManagement ReferenceId="SM-MFA-TOTP"
/>
        </TechnicalProfile>
        <!-- Self-asserted technical profile that verifies the TOTP-->
        <TechnicalProfile Id="OTPVerification">
          <DisplayName>Sign in with Authenticator app</DisplayName>
          <Protocol Name="Proprietary"
Handler="Web.TPEngine.Providers.SelfAssertedAttributeProvider, Web.TPEngine,
Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
          <Metadata>
            <Item
Key="ContentDefinitionReferenceId">api.selfasserted.totp</Item>
            <Item Key="language.button_continue">Verify</Item>
          </Metadata>
          <CryptographicKeys>
            <!--Key Id="issuer_secret"
StorageReferenceId="B2C_1A_TokenSigningKeyContainer" /-->
            <Key Id="MetadataSigning" StorageReferenceId="B2C_1A_SamlIdpCert"
/>
            <Key Id="SamlMessageSigning"
StorageReferenceId="B2C_1A_SamlIdpCert" />
            <Key Id="SamlAssertionSigning"
StorageReferenceId="B2C_1A_SamlIdpCert" />
          </CryptographicKeys>
          <InputClaims></InputClaims>
          <DisplayClaims>
            <DisplayClaim ClaimTypeReferenceId="QrCodeVerifyInstruction" />
            <DisplayClaim ClaimTypeReferenceId="otpCode" Required="true" />
          </DisplayClaims>
          <OutputClaims>
            <OutputClaim ClaimTypeReferenceId="objectId" />
            <OutputClaim ClaimTypeReferenceId="otpCode" Required="true" />
          </OutputClaims>
          <ValidationTechnicalProfiles>
            <ValidationTechnicalProfile ReferenceId="AzureMfa-BeginVerifyOTP"
/>
            <ValidationTechnicalProfile ReferenceId="AzureMfa-VerifyOTP" />
          </ValidationTechnicalProfiles>
          <UseTechnicalProfileForSessionManagement ReferenceId="SM-MFA-TOTP"
/>
        </TechnicalProfile>
        <!-- Set the number of devices to 0 (default value) -->
        <TechnicalProfile Id="SetTotpDefaultValue">
          <DisplayName>Set Totp Default Values</DisplayName>
          <Protocol Name="Proprietary"
Handler="Web.TPEngine.Providers.ClaimsTransformationProtocolProvider,
Web.TPEngine, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
          <OutputClaims>
            <OutputClaim ClaimTypeReferenceId="numberOfAvailableDevices"
DefaultValue="0" />
          </OutputClaims>
        </TechnicalProfile>
        <!-- Copy the UserId to the totpIdentifier -->
        <TechnicalProfile Id="CreateTotpIdentifier-UserId">
          <DisplayName>Set Totp Default Values</DisplayName>
          <Protocol Name="Proprietary"
Handler="Web.TPEngine.Providers.ClaimsTransformationProtocolProvider,
Web.TPEngine, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
          <OutputClaims>
            <OutputClaim ClaimTypeReferenceId="totpIdentifier" />
          </OutputClaims>
          <OutputClaimsTransformations>
            <OutputClaimsTransformation ReferenceId="UserIdToLogonIdentifier"
/>
          </OutputClaimsTransformations>
        </TechnicalProfile>
        <!-- Copy the SignInName to the totpIdentifier -->
        <TechnicalProfile Id="CreateTotpIdentifier-SignInName">
          <DisplayName>Set Totp Default Values</DisplayName>
          <Protocol Name="Proprietary"
Handler="Web.TPEngine.Providers.ClaimsTransformationProtocolProvider,
Web.TPEngine, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />

522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608

          <OutputClaims>
            <OutputClaim ClaimTypeReferenceId="totpIdentifier" />
          </OutputClaims>
          <OutputClaimsTransformations>
            <OutputClaimsTransformation
ReferenceId="SignInNameToTotpIdentifier" />
          </OutputClaimsTransformations>
        </TechnicalProfile>
        <!-- Copy the Email to the totpIdentifier -->
        <TechnicalProfile Id="CreateTotpIdentifier-Email">
          <DisplayName>Set Totp Default Values</DisplayName>
          <Protocol Name="Proprietary"
Handler="Web.TPEngine.Providers.ClaimsTransformationProtocolProvider,
Web.TPEngine, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
          <OutputClaims>
            <OutputClaim ClaimTypeReferenceId="totpIdentifier" />
          </OutputClaims>
          <OutputClaimsTransformations>
            <OutputClaimsTransformation ReferenceId="EmailToTotpIdentifier" />
          </OutputClaimsTransformations>
        </TechnicalProfile>
        <TechnicalProfile Id="GetEmailFromReadOnlyEmail">
          <DisplayName>Get Email From ReadOnlyEmail</DisplayName>
          <Protocol Name="Proprietary"
Handler="Web.TPEngine.Providers.ClaimsTransformationProtocolProvider,
Web.TPEngine, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
          <OutputClaims>
            <OutputClaim ClaimTypeReferenceId="email" />
          </OutputClaims>
          <OutputClaimsTransformations>
            <OutputClaimsTransformation
ReferenceId="GetEmailFromReadOnlyEmail" />
          </OutputClaimsTransformations>
        </TechnicalProfile>
        <TechnicalProfile Id="GetEmailAddress">
          <DisplayName>Get Email Address</DisplayName>
          <Protocol Name="Proprietary"
Handler="Web.TPEngine.Providers.ClaimsTransformationProtocolProvider,
Web.TPEngine, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
          <OutputClaims>
            <OutputClaim ClaimTypeReferenceId="ReadOnlyEmail" />
          </OutputClaims>
          <OutputClaimsTransformations>
            <OutputClaimsTransformation ReferenceId="GetEmailFromEmails" />
          </OutputClaimsTransformations>
        </TechnicalProfile>
        <!--end of TOTP-->
      </TechnicalProfiles>
    </ClaimsProvider>
    <ClaimsProvider>
      <DisplayName>Azure Active Directory</DisplayName>
      <TechnicalProfiles>
        <TechnicalProfile Id="AAD-UserReadUsingObjectId">
          <OutputClaims>
            <!-- The userPrincipalName is required for the
AzureMfaProtocolProvider technical profiles-->
            <OutputClaim ClaimTypeReferenceId="userPrincipalName" />
          </OutputClaims>
        </TechnicalProfile>
      </TechnicalProfiles>
    </ClaimsProvider>
    <ClaimsProvider>
      <DisplayName>Local Account</DisplayName>
      <TechnicalProfiles>
        <TechnicalProfile Id="LocalAccountSignUpWithLogonEmail">
          <OutputClaims>
            <!-- The userPrincipalName is required for the
AzureMfaProtocolProvider technical profiles-->
            <OutputClaim ClaimTypeReferenceId="userPrincipalName" />
          </OutputClaims>
        </TechnicalProfile>
        <TechnicalProfile Id="SelfAsserted-LocalAccountSignin-Email">
          <OutputClaims>
            <!-- The userPrincipalName is required for the
AzureMfaProtocolProvider technical profiles-->
            <OutputClaim ClaimTypeReferenceId="userPrincipalName" />
          </OutputClaims>
        </TechnicalProfile>
      </TechnicalProfiles>
    </ClaimsProvider>
    <ClaimsProvider>
      <DisplayName>Local Account SignIn</DisplayName>
      <TechnicalProfiles>
        <TechnicalProfile Id="login-NonInteractive">
          <Metadata>
            <Item Key="client_id">0c54849b-121f-496e-b1c3-406976bec48b</Item>
            <Item Key="IdTokenAudience">01590824-a092-4271-99a3-

609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
641
642
643
644
645
646
647
648
649
650
651
652
653
654
655
656
657
658
659
660
661
662
663
664
665
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
694
695

f3e37b9f22cc</Item>
          </Metadata>
          <InputClaims>
            <InputClaim ClaimTypeReferenceId="client_id"
DefaultValue="0c54849b-121f-496e-b1c3-406976bec48b" />
            <InputClaim ClaimTypeReferenceId="resource_id"
PartnerClaimType="resource" DefaultValue="01590824-a092-4271-99a3-
f3e37b9f22cc" />
          </InputClaims>
        </TechnicalProfile>
      </TechnicalProfiles>
    </ClaimsProvider>
    <ClaimsProvider>
      <DisplayName>Azure Active Directory</DisplayName>
      <TechnicalProfiles>
        <TechnicalProfile Id="AAD-Common">
          <Metadata>
            <!--Insert b2c-extensions-app application ID here, for example:
11111111-1111-1111-1111-111111111111-->
            <Item Key="ClientId">0c0abe38-79ab-45d3-99fe-9378eec7b16f</Item>
            <!--Insert b2c-extensions-app application ObjectId here, for
example: 22222222-2222-2222-2222-222222222222-->
            <Item Key="ApplicationObjectId">3c34826e-3bd5-47a2-b44d-
08c09034cef2</Item>
          </Metadata>
        </TechnicalProfile>
      </TechnicalProfiles>
    </ClaimsProvider>
  </ClaimsProviders>
  <UserJourneys>
    <UserJourney Id="PasswordResetWithTOTP">
      <OrchestrationSteps>
        <OrchestrationStep Order="1" Type="ClaimsExchange">
          <ClaimsExchanges>
            <ClaimsExchange Id="PasswordResetUsingEmailAddressExchange"
TechnicalProfileReferenceId="LocalAccountDiscoveryUsingEmailAddress" />
          </ClaimsExchanges>
        </OrchestrationStep>
        <!-- Call the TOTP enrollment ub journey. If user already enrolled the
sub journey will not ask the user to enroll -->
        <OrchestrationStep Order="2" Type="InvokeSubJourney">
          <JourneyList>
            <Candidate SubJourneyReferenceId="TotpFactor-Input" />
          </JourneyList>
        </OrchestrationStep>
        <!-- Call the TOTP validation sub journey-->
        <OrchestrationStep Order="3" Type="InvokeSubJourney">
          <JourneyList>
            <Candidate SubJourneyReferenceId="TotpFactor-Verify" />
          </JourneyList>
        </OrchestrationStep>
        <OrchestrationStep Order="4" Type="ClaimsExchange">
          <ClaimsExchanges>
            <ClaimsExchange Id="NewCredentials"
TechnicalProfileReferenceId="LocalAccountWritePasswordUsingObjectId" />
          </ClaimsExchanges>
        </OrchestrationStep>
        <OrchestrationStep Order="5" Type="SendClaims"
CpimIssuerTechnicalProfileReferenceId="JwtIssuer" />
        <!--OrchestrationStep Order="5" Type="SendClaims"
CpimIssuerTechnicalProfileReferenceId="Saml2AssertionIssuer" /-->
      </OrchestrationSteps>
      <ClientDefinition ReferenceId="DefaultWeb" />
    </UserJourney>
    <UserJourney Id="SignUpOrSignInTOTP">
      <OrchestrationSteps>
        <OrchestrationStep Order="1" Type="CombinedSignInAndSignUp"
ContentDefinitionReferenceId="api.signuporsignin">
          <ClaimsProviderSelections>
            <ClaimsProviderSelection
ValidationClaimsExchangeId="LocalAccountSigninEmailExchange" />
          </ClaimsProviderSelections>
          <ClaimsExchanges>
            <ClaimsExchange Id="LocalAccountSigninEmailExchange"
TechnicalProfileReferenceId="SelfAsserted-LocalAccountSignin-Email" />
          </ClaimsExchanges>
        </OrchestrationStep>
        <OrchestrationStep Order="2" Type="ClaimsExchange">
          <Preconditions>
            <Precondition Type="ClaimsExist" ExecuteActionsIf="true">
              <Value>objectId</Value>
              <Action>SkipThisOrchestrationStep</Action>
            </Precondition>
          </Preconditions>
          <ClaimsExchanges>
            <ClaimsExchange Id="SignUpWithLogonEmailExchange"
TechnicalProfileReferenceId="LocalAccountSignUpWithLogonEmail" />

696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
747
748
749
750
751
752
753
754
755
756
757
758
759
760
761
762
763
764
765
766
767
768
769
770
771
772
773
774
775
776
777
778
779
780
781
782

          </ClaimsExchanges>
        </OrchestrationStep>
        <OrchestrationStep Order="3" Type="ClaimsExchange">
          <ClaimsExchanges>
            <ClaimsExchange Id="AADUserReadWithObjectId"
TechnicalProfileReferenceId="AAD-UserReadUsingObjectId" />
          </ClaimsExchanges>
        </OrchestrationStep>
        <!-- Call the TOTP enrollment ub journey. If user already enrolled the
sub journey will not ask the user to enroll -->
        <OrchestrationStep Order="4" Type="InvokeSubJourney">
          <JourneyList>
            <Candidate SubJourneyReferenceId="TotpFactor-Input" />
          </JourneyList>
        </OrchestrationStep>
        <!-- Call the TOTP validation sub journey-->
        <OrchestrationStep Order="5" Type="InvokeSubJourney">
          <JourneyList>
            <Candidate SubJourneyReferenceId="TotpFactor-Verify" />
          </JourneyList>
        </OrchestrationStep>
        <OrchestrationStep Order="6" Type="SendClaims"
CpimIssuerTechnicalProfileReferenceId="JwtIssuer" />
      </OrchestrationSteps>
    </UserJourney>
  </UserJourneys>
  <SubJourneys>
    <!--TOTP subjourneys-->
    <!-- Set the required claims numberOfAvailableDevices and totpIdentifier--
>
    <SubJourney Id="SetTotpInitialValue" Type="Call">
      <OrchestrationSteps>
        <!-- If number of available device claim not exists, set the value to
0-->
        <OrchestrationStep Order="1" Type="ClaimsExchange">
          <Preconditions>
            <Precondition Type="ClaimsExist" ExecuteActionsIf="true">
              <Value>numberOfAvailableDevices</Value>
              <Action>SkipThisOrchestrationStep</Action>
            </Precondition>
          </Preconditions>
          <ClaimsExchanges>
            <ClaimsExchange Id="SetTotpDefaultValue"
TechnicalProfileReferenceId="SetTotpDefaultValue" />
          </ClaimsExchanges>
        </OrchestrationStep>
        <!-- The following orchestration steps try to get the user identifier
for different
             type of authentication, such as local and social account.-->
        <!-- Try to get the identifier from UserId-->
        <OrchestrationStep Order="2" Type="ClaimsExchange">
          <Preconditions>
            <Precondition Type="ClaimsExist" ExecuteActionsIf="true">
              <Value>totpIdentifier</Value>
              <Action>SkipThisOrchestrationStep</Action>
            </Precondition>
            <Precondition Type="ClaimsExist" ExecuteActionsIf="false">
              <Value>UserId</Value>
              <Action>SkipThisOrchestrationStep</Action>
            </Precondition>
          </Preconditions>
          <ClaimsExchanges>
            <ClaimsExchange Id="SetTotpIdentifierAsUserId"
TechnicalProfileReferenceId="CreateTotpIdentifier-UserId" />
          </ClaimsExchanges>
        </OrchestrationStep>
        <!-- Get the identifier from email-->
        <OrchestrationStep Order="3" Type="ClaimsExchange">
          <Preconditions>
            <Precondition Type="ClaimsExist" ExecuteActionsIf="true">
              <Value>totpIdentifier</Value>
              <Action>SkipThisOrchestrationStep</Action>
            </Precondition>
            <Precondition Type="ClaimsExist" ExecuteActionsIf="false">
              <Value>email</Value>
              <Action>SkipThisOrchestrationStep</Action>
            </Precondition>
          </Preconditions>
          <ClaimsExchanges>
            <ClaimsExchange Id="SetTotpIdentifierAsEmail"
TechnicalProfileReferenceId="CreateTotpIdentifier-Email" />
          </ClaimsExchanges>
        </OrchestrationStep>
        <!-- Get the identifier from the user's emails -->
        <OrchestrationStep Order="4" Type="InvokeSubJourney">
          <Preconditions>
            <Precondition Type="ClaimsExist" ExecuteActionsIf="true">

              <Value>totpIdentifier</Value>
              <Action>SkipThisOrchestrationStep</Action>
            </Precondition>
            <Precondition Type="ClaimsExist" ExecuteActionsIf="false">
              <Value>emails</Value>
              <Action>SkipThisOrchestrationStep</Action>
            </Precondition>
          </Preconditions>
          <JourneyList>
            <Candidate
SubJourneyReferenceId="ExtractEmailFromEmailsForTotpIdentifier" />
          </JourneyList>

783
784
785
786
787
788
789
790
791
792
793
794
        </OrchestrationStep>
<TrustFrameworkPolicy xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        <!-- Get the identifier from local account sign-in name-->
1
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
        <OrchestrationStep Order="5" Type="ClaimsExchange">
2
xmlns="http://schemas.microsoft.com/online/cpim/schemas/2013/06"
          <Preconditions>
3
PolicySchemaVersion="0.3.0.0" TenantId="stellarpmb2c.onmicrosoft.com"
            <Precondition Type="ClaimsExist" ExecuteActionsIf="true">
4
PolicyId="B2C_1A_signup_signin"
              <Value>totpIdentifier</Value>
5
PublicPolicyUri="http://stellarpmb2c.onmicrosoft.com/B2C_1A_signup_signin"
              <Action>SkipThisOrchestrationStep</Action>
6
TenantObjectId="04fcef19-20fe-4655-9498-3e5050b6dda1">
            </Precondition>
7
  <BasePolicy>
            <Precondition Type="ClaimsExist" ExecuteActionsIf="false">
8
    <TenantId>stellarpmb2c.onmicrosoft.com</TenantId>
              <Value>signInName</Value>
9
    <PolicyId>B2C_1A_TrustFrameworkExtensions</PolicyId>
              <Action>SkipThisOrchestrationStep</Action>
10
            </Precondition>
  </BasePolicy>
11
  <RelyingParty>
12
          </Preconditions>
    <DefaultUserJourney ReferenceId="SignUpOrSignIn" />
13
          <ClaimsExchanges>
    <TechnicalProfile Id="PolicyProfile">
14
            <ClaimsExchange Id="SetTotpIdentifierAsSignInName"
      <DisplayName>PolicyProfile</DisplayName>
TechnicalProfileReferenceId="CreateTotpIdentifier-SignInName" />
15
      <Protocol Name="OpenIdConnect" />
          </ClaimsExchanges>
16
      <OutputClaims>
17
        </OrchestrationStep>
        <OutputClaim ClaimTypeReferenceId="displayName" />
18
      </OrchestrationSteps>
        <OutputClaim ClaimTypeReferenceId="givenName" />
19
    </SubJourney>
        <OutputClaim ClaimTypeReferenceId="surname" />
20
    <!-- Get the identifier from the user's emails -->
        <OutputClaim ClaimTypeReferenceId="email" />
    <SubJourney Id="ExtractEmailFromEmailsForTotpIdentifier" Type="Call">
21
        <OutputClaim ClaimTypeReferenceId="objectId" PartnerClaimType="sub" />
22
      <OrchestrationSteps>
23
        <OutputClaim ClaimTypeReferenceId="tenantId"
        <OrchestrationStep Order="1" Type="ClaimsExchange">
          <Preconditions>
AlwaysUseDefaultValue="true" DefaultValue="{Policy:TenantObjectId}" />
<TrustFrameworkPolicy xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            <Precondition Type="ClaimsExist" ExecuteActionsIf="false">
      </OutputClaims>
1
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
      <SubjectNamingInfo ClaimType="sub" />
              <Value>emails</Value>
2
xmlns="http://schemas.microsoft.com/online/cpim/schemas/2013/06"
              <Action>SkipThisOrchestrationStep</Action>
    </TechnicalProfile>
3
PolicySchemaVersion="0.3.0.0" TenantId="stellarpmb2c.onmicrosoft.com"
            </Precondition>
  </RelyingParty>
4
PolicyId="B2C_1A_ProfileEdit"
</TrustFrameworkPolicy>
          </Preconditions>
5
PublicPolicyUri="http://stellarpmb2c.onmicrosoft.com/B2C_1A_ProfileEdit"
          <ClaimsExchanges>
6
TenantObjectId="04fcef19-20fe-4655-9498-3e5050b6dda1">
            <ClaimsExchange Id="GetEmailAddress"
7
  <BasePolicy>
TechnicalProfileReferenceId="GetEmailAddress" />
8
    <TenantId>stellarpmb2c.onmicrosoft.com</TenantId>
          </ClaimsExchanges>
9
    <PolicyId>B2C_1A_TrustFrameworkExtensions</PolicyId>
10
        </OrchestrationStep>
  </BasePolicy>
11
        <OrchestrationStep Order="2" Type="ClaimsExchange">
  <RelyingParty>
          <Preconditions>
12
    <DefaultUserJourney ReferenceId="ProfileEdit" />
            <Precondition Type="ClaimsExist" ExecuteActionsIf="false">
13
    <TechnicalProfile Id="PolicyProfile">
              <Value>ReadOnlyEmail</Value>
14
      <DisplayName>PolicyProfile</DisplayName>
              <Action>SkipThisOrchestrationStep</Action>
15
      <Protocol Name="OpenIdConnect" />
16
            </Precondition>
      <OutputClaims>
          </Preconditions>
17
        <OutputClaim ClaimTypeReferenceId="objectId" PartnerClaimType="sub" />
18
          <ClaimsExchanges>
        <OutputClaim ClaimTypeReferenceId="tenantId"
            <ClaimsExchange Id="GetEmailFromReadOnlyEmail"
19
TechnicalProfileReferenceId="GetEmailFromReadOnlyEmail" />
AlwaysUseDefaultValue="true" DefaultValue="{Policy:TenantObjectId}" />
<TrustFrameworkPolicy xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
          </ClaimsExchanges>
      </OutputClaims>
1
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
        </OrchestrationStep>
      <SubjectNamingInfo ClaimType="sub" />
2
xmlns="http://schemas.microsoft.com/online/cpim/schemas/2013/06"
        <OrchestrationStep Order="3" Type="ClaimsExchange">
    </TechnicalProfile>
3
PolicySchemaVersion="0.3.0.0" TenantId="stellarpmb2c.onmicrosoft.com"
  </RelyingParty>
          <Preconditions>
4
PolicyId="B2C_1A_PasswordReset"
</TrustFrameworkPolicy>
            <Precondition Type="ClaimsExist" ExecuteActionsIf="false">
5
PublicPolicyUri="http://stellarpmb2c.onmicrosoft.com/B2C_1A_PasswordReset"
              <Value>email</Value>
6
TenantObjectId="04fcef19-20fe-4655-9498-3e5050b6dda1">
              <Action>SkipThisOrchestrationStep</Action>
7
  <BasePolicy>
            </Precondition>
8
    <TenantId>stellarpmb2c.onmicrosoft.com</TenantId>
          </Preconditions>
9
    <PolicyId>B2C_1A_TrustFrameworkExtensions</PolicyId>
          <ClaimsExchanges>
10
  </BasePolicy>
            <ClaimsExchange Id="SetTotpIdentifierAsEmail"
11
TechnicalProfileReferenceId="CreateTotpIdentifier-Email" />
  <RelyingParty>
12
    <DefaultUserJourney ReferenceId="PasswordReset" />
          </ClaimsExchanges>
13
    <TechnicalProfile Id="PolicyProfile">
14
        </OrchestrationStep>
      <DisplayName>PolicyProfile</DisplayName>
15
        <OrchestrationStep Order="4" Type="ClaimsExchange">
      <Protocol Name="OpenIdConnect" />
          <Preconditions>
16
      <OutputClaims>
17
            <Precondition Type="ClaimsExist" ExecuteActionsIf="false">
        <OutputClaim ClaimTypeReferenceId="email" />
18
              <Value>signInName</Value>
19
        <OutputClaim ClaimTypeReferenceId="objectId" PartnerClaimType="sub" />
              <Action>SkipThisOrchestrationStep</Action>
        <OutputClaim ClaimTypeReferenceId="tenantId" AlwaysUseDefaultValue="true"
            </Precondition>
<TrustFrameworkPolicy xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
DefaultValue="{Policy:TenantObjectId}" />
          </Preconditions>
1
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
      </OutputClaims>
          <ClaimsExchanges>
2
xmlns="http://schemas.microsoft.com/online/cpim/schemas/2013/06"
            <ClaimsExchange Id="SetTotpIdentifierAsSignInName"
      <SubjectNamingInfo ClaimType="sub" />
3
PolicySchemaVersion="0.3.0.0" TenantId="stellarpmb2c.onmicrosoft.com"
TechnicalProfileReferenceId="CreateTotpIdentifier-SignInName" />
    </TechnicalProfile>
4
PolicyId="B2C_1A_signup_signin_saml"
          </ClaimsExchanges>
  </RelyingParty>
5
PublicPolicyUri="http://stellarpmb2c.onmicrosoft.com/B2C_1A_signup_signin_saml"
</TrustFrameworkPolicy>
        </OrchestrationStep>
6
TenantObjectId="04fcef19-20fe-4655-9498-3e5050b6dda1">
      </OrchestrationSteps>
7
  <BasePolicy>
    </SubJourney>
8
    <TenantId>stellarpmb2c.onmicrosoft.com</TenantId>
    <!-- TOTP verification sub journey-->
9
    <PolicyId>B2C_1A_TrustFrameworkExtensions</PolicyId>
    <SubJourney Id="TotpFactor-Verify" Type="Call">
10

  </BasePolicy>
      <OrchestrationSteps>
11
  <UserJourneys>
12
        <!-- Set the required claims numberOfAvailableDevices and totpIdentifier-->
    <UserJourney Id="SignUpOrSignIn">
13
        <OrchestrationStep Order="1" Type="InvokeSubJourney">
      <OrchestrationSteps>
14
          <JourneyList>
            <Candidate SubJourneyReferenceId="SetTotpInitialValue" />
        <OrchestrationStep Order="4" Type="SendClaims"
15
CpimIssuerTechnicalProfileReferenceId="Saml2AssertionIssuer" />
          </JourneyList>
16
        </OrchestrationStep>
      </OrchestrationSteps>
17
    </UserJourney>
18
        <!-- If current user is not a new one (this is a sign-in flow, and not sign-
  </UserJourneys>
19
up),
  <RelyingParty>
20
             check the number of available devices. -->
    <DefaultUserJourney ReferenceId="SignUpOrSignIn" />
        <OrchestrationStep Order="2" Type="ClaimsExchange">
21
    <TechnicalProfile Id="PolicyProfile">
          <Preconditions>
22
      <DisplayName>PolicyProfile</DisplayName>
23
            <Precondition Type="ClaimEquals" ExecuteActionsIf="true">
      <Protocol Name="SAML2" />
              <Value>newUser</Value>
24
      <Metadata>
25
              <Value>True</Value>
    <Item
26
              <Action>SkipThisOrchestrationStep</Action>
Key="PartnerEntity">https://testdp.stellarcyber.ai/sso/saml/metadata</Item>
            </Precondition>
27
      </Metadata>
          </Preconditions>
28
      <OutputClaims>
          <ClaimsExchanges>
29
        <OutputClaim ClaimTypeReferenceId="userPrincipalName"
30
            <ClaimsExchange Id="CheckAvailableDevices"
PartnerClaimType="upn" />
31
TechnicalProfileReferenceId="AzureMfa-GetAvailableDevices" />
32
        <OutputClaim ClaimTypeReferenceId="extension_stellar_privilege" />
          </ClaimsExchanges>
        <OutputClaim ClaimTypeReferenceId="extension_stellar_scope" />
        </OrchestrationStep>
<TrustFrameworkPolicy xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        <!-- If the number of available devices isn't zero (user has enrolled
        <OutputClaim ClaimTypeReferenceId="extension_stellar_tenant" />
1
        <OutputClaim ClaimTypeReferenceId="extension_stellar_tenant_group" />
xmlns:xsd="http://www.w3.org/2001/XMLSchema"
before),
2
xmlns="http://schemas.microsoft.com/online/cpim/schemas/2013/06"
             render the TOTP verification page -->
      </OutputClaims>
3
PolicySchemaVersion="0.3.0.0" TenantId="stellarpmb2c.onmicrosoft.com"
        <OrchestrationStep Order="3" Type="ClaimsExchange">
      <SubjectNamingInfo ClaimType="upn" ExcludeAsClaim="true" />
4
PolicyId="B2C_1A_signup_signin_saml"
    </TechnicalProfile>
          <Preconditions>
5
PublicPolicyUri="http://stellarpmb2c.onmicrosoft.com/B2C_1A_signup_signin_saml"
  </RelyingParty>
            <Precondition Type="ClaimEquals" ExecuteActionsIf="true">
6
</TrustFrameworkPolicy>
TenantObjectId="04fcef19-20fe-4655-9498-3e5050b6dda1">
              <Value>numberOfAvailableDevices</Value>
7
  <BasePolicy>
              <Value>0</Value>
8
    <TenantId>stellarpmb2c.onmicrosoft.com</TenantId>
              <Action>SkipThisOrchestrationStep</Action>
9
            </Precondition>
    <PolicyId>B2C_1A_TrustFrameworkExtensions</PolicyId>
10
  </BasePolicy>
          </Preconditions>
11
  <!--UserJourneys>
12
          <ClaimsExchanges>
    <UserJourney Id="SignUpOrSignIn">
13
            <ClaimsExchange Id="AuthenticatorForSignIn"
      <OrchestrationSteps>
TechnicalProfileReferenceId="OTPVerification" />
14
        <OrchestrationStep Order="4" Type="SendClaims"
15
          </ClaimsExchanges>
CpimIssuerTechnicalProfileReferenceId="Saml2AssertionIssuer" />
        </OrchestrationStep>
16
      </OrchestrationSteps>
      </OrchestrationSteps>
17
    </UserJourney>
18
    </SubJourney>
  </UserJourneys-->
19
    <!-- TOTP enrollment sub journey-->
  <RelyingParty>
20
    <SubJourney Id="TotpFactor-Input" Type="Call">
    <DefaultUserJourney ReferenceId="SignUpOrSignInTOTP" />
      <OrchestrationSteps>
21
    <TechnicalProfile Id="PolicyProfile">
        <!-- Set the required claims numberOfAvailableDevices and totpIdentifier-->
22
      <DisplayName>PolicyProfile</DisplayName>
23
        <OrchestrationStep Order="1" Type="InvokeSubJourney">
      <Protocol Name="SAML2" />
24
          <JourneyList>
      <Metadata>
25
            <Candidate SubJourneyReferenceId="SetTotpInitialValue" />
        <Item
          </JourneyList>
26
        </OrchestrationStep>
Key="PartnerEntity">https://testdp.stellarcyber.ai/sso/saml/metadata</Item>
27
      </Metadata>
        <!-- If current user is not a new one (this is a sign-in flow, and not sign-
28
      <OutputClaims>
29
up),
        <OutputClaim ClaimTypeReferenceId="userPrincipalName"
30
             check the number of available devices. -->
PartnerClaimType="upn" />
31
        <OrchestrationStep Order="2" Type="ClaimsExchange">
32
        <OutputClaim ClaimTypeReferenceId="extension_stellar_privilege" />
          <Preconditions>
        <OutputClaim ClaimTypeReferenceId="extension_stellar_scope" />
            <Precondition Type="ClaimEquals" ExecuteActionsIf="true">
              <Value>newUser</Value>
        <OutputClaim ClaimTypeReferenceId="extension_stellar_tenant" />
              <Value>True</Value>
        <OutputClaim ClaimTypeReferenceId="extension_stellar_tenant_group" />
              <Action>SkipThisOrchestrationStep</Action>
      </OutputClaims>
            </Precondition>
      <SubjectNamingInfo ClaimType="upn" ExcludeAsClaim="true" />
    </TechnicalProfile>
          </Preconditions>
  </RelyingParty>
          <ClaimsExchanges>
</TrustFrameworkPolicy>
            <ClaimsExchange Id="CheckAvailableDevices"
TechnicalProfileReferenceId="AzureMfa-GetAvailableDevices" />
          </ClaimsExchanges>
        </OrchestrationStep>
        <!-- If the number of available devices is zero (user hasn't enrolled
before),
            render the TOTP enrollment page to scan the QR code that starts the
enrollment process -->
        <OrchestrationStep Order="3" Type="ClaimsExchange">
          <Preconditions>
            <Precondition Type="ClaimEquals" ExecuteActionsIf="false">
              <Value>numberOfAvailableDevices</Value>
              <Value>0</Value>
              <Action>SkipThisOrchestrationStep</Action>
            </Precondition>
          </Preconditions>
          <ClaimsExchanges>
            <ClaimsExchange Id="AuthenticatorForSignUp"
TechnicalProfileReferenceId="EnableOTPAuthentication" />
          </ClaimsExchanges>
        </OrchestrationStep>
        <!-- If the number of available devices is zero (user hasn't enrolled
before),
             render the TOTP verification page.  -->
        <OrchestrationStep Order="4" Type="ClaimsExchange">

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

Stellar Cyber version 6.6.0s

          <Preconditions>
            <Precondition Type="ClaimEquals" ExecuteActionsIf="false">
              <Value>numberOfAvailableDevices</Value>
              <Value>0</Value>
              <Action>SkipThisOrchestrationStep</Action>
            </Precondition>
          </Preconditions>
          <ClaimsExchanges>
            <ClaimsExchange Id="AuthenticatorForSignIn"
TechnicalProfileReferenceId="OTPVerification" />
          </ClaimsExchanges>
        </OrchestrationStep>
      </OrchestrationSteps>
    </SubJourney>
  </SubJourneys>
  <!--UserJourneys>

    </UserJourneys-->
</TrustFrameworkPolicy>

