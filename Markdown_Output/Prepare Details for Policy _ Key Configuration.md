Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Azure AD B2C SSO: Prepare Details for Policy / Key
Configuration

The steps in this section are critical to perform first. Here, you obtain and note details for configuring the polices in the
next section. You must also prepare the environment with certain keys and applications before you do that
configuration.

 If you stop and return to any of the procedures in this configuration process, ensure that you switch to the correct

directory before you continue so that you are working on the correct Azure AD B2C Tenant container.

Before You Begin
Set Azure AD B2C Directory & Obtain Tenant ID / Domain Name
Create Azure AD B2C Signing and Encryption Keys
Configure an IdentityExperienceFramework Application
Configure a ProxyIdentityExperienceFramework Application
Register the Stellar Cyber SAML Application
Obtain IDs from the b2c-extensions-app
Verify Preparations

 The order in which you perform certain steps matters. Perform the steps in exactly the order shown.

Before You Begin

Make note of the FQDN of your Stellar Cyber Platform. You will be using for assorted configurations in this
topic.

Obtain the following from your Stellar Cyber configuration:

A server pem certificate and the private key for the server hosting your Stellar Cyber Platform. This
will be uploaded in the Stellar Cyber Certificates screen.
Prepare a .pfx file which combines the certificate and the private key, for uploading to the Azure
AD B2C server.

 IMPORTANT: Self-signed server certificates are not supported for configuration with Azure AD B2C.

If you are configuring per-tenant SSO, obtain the Stellar Cyber ID of that tenant (System |
 ORGANIZATION MANAGEMENT | Tenants):

The following worksheet may be helpful to track certain values that you will use during configuration,
especially in the policy files. Note that the syntax / case matters for all of these values (see printable
HTML version or Word version).

ATTRIBUTE

EXAMPLE

Stellar Cyber Server Information (obtain before you begin)

DP FQDN

testdp.stellarcyber.ai

M

Y

V

A

L

U

E

S

ATTRIBUTE

EXAMPLE

M

Y

V

A

L

U

E

S

ATTRIBUTE

EXAMPLE

M

Y

V

A

L

U

E

S

Tenant ID (for per tenant-SSO only)

29443942

stellar_scope (authorization only)

root

stellar_privilege (authorization only)

super_admin

stellar_tenant (optional) (authorization only)

a112c31c04734b7ba5243e5e5432bfe6

stellar_tenant_group (optional) (authorization
only)

25320755

Azure AD B2C Server Information (in order of occurrence)

Domain / Primary Domain

stellarpmb2c.onmicrosoft.com

Tenant ID / Tenant (Object ID)

04fcef19-20fe-4655-9498-3e5050b6dda1

Application (Client) ID for
IdentityExperienceFramework

Application (Client) ID for
ProxyIdentityExperienceFramework

01590824-a092-4271-99a3-f3e37b9f22cc

0c54849b-121f-496e-b1c3-406976bec48b

SAML App Name

Stellar_SAML

identifierUris

https://<Azure AD B2C tenant name>.onmicrosoft.com/<SAML application
name>

http://stellarpmb2c.onmicrosoft.com/Stellar_SAML

Application ID URI

https://stellarpmb2c.b2clogin.com/stellarpmb2c.onmicrosoft.com

b2c-extensions-app: Application (Client) ID

0c0abe38-79ab-45d3-99fe-9378eec7b16f

b2c-extensions-app: Object ID

3c34826e-3bd5-47a2-b44d-08c09034cef2

ATTRIBUTE

EXAMPLE

M

Y

V

A

L

U

E

S

Metadata URL

https://stellarpmb2c.b2clogin.com/stellarpmb2c.onmicrosoft.com/B2C_1A_s
ignup_signin_saml/samlp/metadata

Issuer URL

http://testdp.stellarcyber.ai

replyUrlsWithType

Global SSO:

https://testdp.stellarcyber.ai/saml/login/callback

Per-tenant SSO:

https://testdp.stellarcyber.ai/saml/login/callback/cust_id/a112c31c04734b7b
a5243e5e5432bfe6

Azure AD B2C User IDs (email & Issuer ID, if
different)

SoCguy@stellarpmb2c.onmicrosoft.com

Example of issuer assigned ID that is not the same as email:

AnalystTwo@stellarpmb2c.onmicrosoft.com,
6b744a55-9031-4b8c-ad6f-81dac5e74055@stellarpmb2c.onmicrosoft.com

Set Azure AD B2C Directory & Obtain Tenant ID / Domain Name
Steps

Ensure you are operating in the correct Azure AD B2C tenant area before you begin.

1. Sign in to the Azure portal .

2. Ensure you have selected the Azure AD B2C directory that contains the Microsoft Entra ID (formerly Azure
AD) tenant that will be used to access Stellar Cyber. Navigate to the Directory selector using one of the
following options:

Select the Directories + subscriptions icon in the portal toolbar.

Navigate to https://portal.azure.com/#settings/directory 

Select the icon from your profile, then select Switch.

3. When the Portal settings | Directories + subscriptions page displays the list of directories, if there is only

one directory listed, then no other step is required. If there is more than one directory, and the directory
housing the tenant you are configuring for use with Stellar Cyber. is not currently active, click the Switch
button on that row.

4. Now obtain the account identifying details that you will use throughout this configuration process. Navigate

to the Microsoft Entra ID > Overview page.

5. Make note of the Tenant ID and Primary Domain and copy them to your worksheet for use in configuration

later.

Create Azure AD B2C Signing and Encryption Keys

Steps

Generate two keys (one for signature and the other for encryption) in the Identity Experience Framework.

 If you stop and return to any of the procedures in this configuration process, ensure that you switch to the correct

directory before you continue so that you are working on the correct Azure AD B2C Tenant container.

1. Access All services from the top-left corner of the Azure portal.

2. Search for and select Azure AD B2C.

3. From the left navigation section for Policies, select Identity Experience Framework.

4. Select Policy Keys .

5. Select Add.

6. Create the first of two keys, the Signing Key, using the following settings:

Options: Select Generate

Name: Enter TokenSigningKeyContainer.

Activation date (optional)

Expiration date (optional)

Key type: Select RSA

Key usage: Enable Signature

7. Select Create to create the signing key which will be used in the Azure AD B2C custom policies later.

The prefix B2C_1A_is automatically added to the name of your key.

The Policy Keys page is refreshed and displays the key you created.

8. Select Add again to create the second key.

9. Create the Encryption Key using the following settings:

Options: Select Generate

Name: Enter TokenEncryptionKeyContainer . The prefix B2C_1A_is added automatically to the
name of your key.

Activation date (optional)

Expiration date (optional)

Key type: Select RSA.

Key usage: Enable Encryption.

10. Select Create to create the encryption key which will be used in the Azure AD B2C custom policies later.

The prefix B2C_1A_is automatically added to the name of your key.

The Policy Keys page is refreshed and displays the key you created.

Configure an IdentityExperienceFramework Application
Steps

 If you stop and return to any of the procedures in this configuration process, ensure that you switch to the correct

directory before you continue so that you are working on the correct Azure AD B2C Tenant container.

Create the IdentityExperienceFramework Application

1. Navigate to All services > Azure AD B2C > Select App registrations.

2. Select New registration.

3. Create a new application with the following information:

Name: Enter IdentityExperienceFramework

Supported account types: Select Accounts in this organizational directory only (Single
tenant)

Redirect URI: Set the following values:

Web

https://<Azure AD B2C tenant name>.b2clogin.com/<Azure AD B2C tenant
name>.onmicrosoft.com

where tenant name is your Azure AD B2C tenant domain name.

Example: https://stellarpmb2c.b2clogin.com/stellarpmb2c.onmicrosoft.com

Permissions: select the Grant admin consent to openid and offline_access permissions
check box

4. Select Register.

The application is created.

5. Make note of the Application (client) ID on your worksheet.

The ID will be used when you Expose an API and when you customize the
TrustFrameworkExtensions.xml file later.

Example value: Application (client) ID: 01590824-a092-4271-99a3-f3e37b9f22cc

Expose API for the IdentityExperienceFramework Application

1. With the App registrations page still displayed, select Expose an API from the Manage menu.

2. Select Add a scope.

The dialog displays with an application ID URI. Do not modify this.

3. Select Save and continue to accept the default value.

4. Make note of the Application ID URI in your worksheet.

Example: https://stellarpmb2c.onmicrosoft.com/01590824-a092-4271-99a3-f3e37b9f22cc for use
later.

5. In the Scopes dialog, enter the following values to allow custom policy execution in your Azure AD B2C

tenant:

Scope name: Specify user_impersonation.

Admin consent display name: Enter Access IdentityExperienceFramework.

Admin consent description: Enter Allow the application to access
IdentityExperienceFramework on behalf of the signed-in user.

State:Ensure it is set to Enabled.

6. Select Add scope.

The IdentityExperienceFramework application is updated with the scope.

Configure a ProxyIdentityExperienceFramework Application
Steps

 If you stop and return to any of the procedures in this configuration process, ensure that you switch to the correct

directory before you continue so that you are working on the correct Azure AD B2C Tenant container.

Create the ProxyIdentityExperienceFramework Application

1. Navigate to All services > Azure AD B2C > Select App registrations.

2. Select New registration.

3. Create a new application with the following information:

Name: Enter ProxyIdentityExperienceFramework

Supported account types: Select Accounts in this organizational directory only (Single
tenant).

Redirect URI: Set the following values:

Public client/native (mobile & desktop)

myapp://auth

Permissions: Select Grant admin consent to openid and offline_access permissions.

4. Select Register.

The application is created.

5. Make note of the Application (client) ID on your worksheet. The ID will be used when you customize the

TrustFrameworkExtensions.xml file later.

Example value: Application (client) ID: 0c54849b-121f-496e-b1c3-406976bec48b

Configure the ProxyIdentityExperienceFramework Application

1. With the ProxyIdentityExperienceFramework application still displayed, select Authentication from the

Manage menu.

2. In the dialog box that appears, locate the section for Advanced settings > Allow public client flows.

3. Toggle on (Yes) Enable the following mobile and desktop flows.

4. Select Save.

5. To verify that the setting is updated, select Manifest and locate the value for allowPublicClient to check

that the value is true.

6. While the ProxyIdentityExperienceFramework application is still selected, give the

ProxyIdentityExperienceFramework access to the API you defined for the IdentityExperienceFrarmework
Application by selecting API permissions.

7. Select Add a permission.

8. In the dialog box that opens, select the tab labeled My APIs.

9. Select the row with IdentityExperienceFramework.

10. In the dialog box that opens, select the user_impersonation permission you created earlier for the

IdentityExperienceFramework.

11. Select Add permission.

The API is added to the application but additional steps are required.

12. Select Grant Admin consent that is located next to Add a permission.

13. Select Yes to grant use of the API to the accounts in the current tenant.

The API/Permissions status changes to Granted.

Register the Stellar Cyber SAML Application
Steps

 If you stop and return to any of the procedures in this configuration process, ensure that you switch to the correct

directory before you continue so that you are working on the correct Azure AD B2C Tenant container.

1. Navigate to All Services > Azure AD B2C.

2. Select App registrations, and then select New registration.

3. Use the following guidelines to configure the new application:

Name: Enter Stellar_SAML.

Supported account types: Select Accounts in this organizational directory only.

Redirect URI: Specify Web and https://localhost (The URI will be updated below).

Permissions: Leave Grant admin consent to openid and offline_access permissions selected.

4. Select Register.

The application details are displayed.

5. With the Stellar_SAML application still displayed, select the menu option for Manage and select Manifest to

open the manifest editor for the application.

6. Locate and update (or add, if needed) the identifierUris attribute using the following syntax:

"identifierUris": [https://<your-Azure-AD-B2C-tenant-
name>.onmicrosoft.com/<your-SAML-app-name>

7. Locate and update (or add, if needed) the samlMetadataUrl attribute using the following syntax:

If you are configuring global SSO:

"samlMetadataUrl":
"https://<your.stellar.cyber.address>/sso/saml/metadata"

If you are configuring per-tenant SSO:

"samlMetadataUrl":
"https://<your.stellar.cyber.address>/sso/saml/metadata/cust_id/<tenant-
ID>"

8. Locate and update (or add, if needed) the replyUrlsWithType attribute, using the following syntax:

If you are configuring global SSO:

"url": "https://<your.stellar.cyber.address>/saml/login/callback"

If you are configuring per-tenant SSO:

"url":
"https://<your.stellar.cyber.address>/saml/login/callback/cust_id/<tenant
-ID>

9. When you are finished, the fields in the manifest will look similar to the following samples:

If you are configuring Global SSO

{
    (snip)
    "identifierUris": [
        "https://stellarpmb2c.onmicrosoft.com/Stellar_SAML"
    ],
    (snip)
    "name": "Stellar_SAML",
    (snip)
    "publisherDomain": "stellarpmb2c.onmicrosoft.com",
    "replyUrlsWithType": [
        {
            "url": "https://testdp.stellarcyber.ai/saml/login/callback",
            "type": "Web"
        }
    ],
    (snip)
    "samlMetadataUrl": "https://testdp.stellarcyber.ai/sso/saml/metadata",
    (snip)
}

If you are configuring Per-tenant SSO

{
    (snip)
    "identifierUris": [
        "https://stellarpmb2c.onmicrosoft.com/Stellar_SAML"
    ],
    (snip)
    "name": "Stellar_SAML",
    (snip)
    "publisherDomain": "stellarpmb2c.onmicrosoft.com",
    "replyUrlsWithType": [
        {
            "url":
"https://testdp.stellarcyber.ai/saml/login/callback/cust_id/046ee23f3b4f4595858d925f45
1af980",
            "type": "Web"
        }
    ],
    (snip)
    "samlMetadataUrl":
"https://testdp.stellarcyber.ai/sso/saml/metadata/cust_id/046ee23f3b4f4595858d925f451a
f980",
    (snip)
}

If you have syntax issues, compare the file below:

Sample Manifest

{
    "id": "aed035fa-1456-4a5a-b01a-e26817ac12e9",
    "acceptMappedClaims": null,
    "accessTokenAcceptedVersion": null,
    "addIns": [],
    "allowPublicClient": null,
    "appId": "74a51233-2158-410f-9ca7-809f27f0a8c7",
    "appRoles": [],
    "oauth2AllowUrlPathMatching": false,
    "createdDateTime": "2022-09-14T17:25:07Z",
    "description": null,
    "certification": null,
    "disabledByMicrosoftStatus": null,
    "groupMembershipClaims": null,
    "identifierUris": ["https://stellarpmb2c.onmicrosoft.com/Stellar_SAML"],
    "informationalUrls": {
        "termsOfService": null,
        "support": null,
        "privacy": null,
        "marketing": null
    },
    "keyCredentials": [],
    "knownClientApplications": [],
    "logoUrl": null,
    "logoutUrl": null,
    "name": "Stellar_SAML",
    "notes": null,
    "oauth2AllowIdTokenImplicitFlow": false,
    "oauth2AllowImplicitFlow": false,
    "oauth2Permissions": [],
    "oauth2RequirePostResponse": false,
    "optionalClaims": null,
    "orgRestrictions": [],
    "parentalControlSettings": {
        "countriesBlockedForMinors": [],
        "legalAgeGroupRule": "Allow"
    },
    "passwordCredentials": [],
    "preAuthorizedApplications": [],
    "publisherDomain": "stellarpmb2c.onmicrosoft.com",
    "replyUrlsWithType": [
        {
            "url": "https://testdp.stellarcyber.ai/saml/login/callback",
            "type": "Web"
        }
    ],
    "requiredResourceAccess": [
        {
            "resourceAppId": "00000003-0000-0000-c000-000000000000",
            "resourceAccess": [
                {
                    "id": "37f7f235-527c-4136-accd-4a02d197296e",
                    "type": "Scope"
                },
                {
                    "id": "7427e0e9-2fba-42fe-b0c0-848c9e6a8182",
                    "type": "Scope"
                }
            ]
        }
    ],
    "samlMetadataUrl": "https://testdp.stellarcyber.ai/sso/saml/metadata",
    "signInUrl": null,
    "signInAudience": "AzureADMyOrg",
    "tags": [],
    "tokenEncryptionKeyId": null
}Obtain IDs from the b2c-extensions-app
Steps

 If you stop and return to any of the procedures in this configuration process, ensure that you switch to the correct

directory before you continue so that you are working on the correct Azure AD B2C Tenant container.

1. From All Services >  Azure AD B2C >Overview screen, then select App Registrations.

2. From the App Registrations pane, ensure that the All Applications sub-tab is selected.

3. Select the application named: b2c-extensions-app. Do not modify. Used by AADB2C for storing user

data.

4. From the screen that displays, copy the Application ID and Object ID and save those to your worksheet.

you will use these to modify the policy files later.

Enable Security Defaults for MFA (Optional)

If you plan to configure your environment to prompt for multi-factor authentication from Azure AD B2C, you must
enable Security Defaults.

1. Browse to Microsoft Entra ID > Properties.

2. Select Manage security defaults.

3. Set the Enable security defaults toggle to Yes.

4. Select Save.

The remaining MFA configurations are accommodated in the sample templates provided in the next section.

Verify Preparations
Before you proceed to the next section, review your worksheet and ensure you have obtained information that you
will use to configure the policies.

Proceed to the next step...

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

