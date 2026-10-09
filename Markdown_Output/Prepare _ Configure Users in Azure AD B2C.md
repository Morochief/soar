Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Azure AD B2C SSO: Prepare / Configure Users

 If you stop and return to any of the procedures in this configuration process, ensure that you
switch to the correct directory before you continue so that you are working on the correct
Azure AD B2C Tenant container.

Create or Select Azure AD B2C Users

Configure Azure AD B2C for Multi-factor Authentication (Optional)

Configure Authorization Attributes (Optional)

 The order in which you perform certain steps matters. Perform the steps in exactly the order

shown.

Create or Select Azure AD B2C Users

1. Navigate to Azure AD B2C > Manage > Users view.

2. When the list of users is displayed, click the name of each user you want to integrate

with Stellar Cyber.

3. Depending how the user account was created, and whether you are also configuring
Authorization, you may need to note two pieces of information in the worksheet. To
ensure you note all the required information, click the link for Issuer.

4. In the dialog that opens, you will see either one or two rows. If the user was created

using the Create Azure AD B2C wizard, you will see a row with an email address and a
row with a unique ID for userPrincipalName. Make note of both values. If the user was
not created this way, then the email address and userPrincipalName are the same. You
only need note the one value in that case.



Note:

The email address is required to configure the user in Stellar Cyber when
you are configuring Authentication Only or configuring per-tenant SSO.

The userPrincipalName is required as the ID when you use Microsoft
Graph to assign values to the Authorization Attributes for each user.

These fields are case-sensitive.

If you need guidance adding users, refer to Microsoft documentation .

Configure Azure AD B2C for Multi-factor Authentication
(Optional)
If you will be enabling 2FA for SSO in Stellar Cyber, take a moment to review whether your Azure
AD B2C deployment is configured to support this. Configuration of this capability on the Stellar
Cyber server is covered later.

 If you are configuring per-tenant SSO, and the overall Global Settings for the Stellar Cyber
DP are configured to make 2FA mandatory, then all users on the server are required to have
2FA enabled.

Refer to the following Microsoft documentation for guidance, if needed, to enable MFA. If you
need to enable this feature, ensure you do it AFTER you have configured and uploaded the
policies since MFA is applied to the sign-in policy.

Enabling Azure AD B2C Multi-factor Authentication  

Enabling Azure AD Security Defaults 

Configure Authorization Attributes (Optional)
If you plan to have Az ure AD B2C control both Authentication and Authorization, follow the
steps in this procedure. If you are using it for Authentication only, or you are configuring per-
tenant SSO, skip this section.

Set Up Stellar Cyber Attributes in Azure AD B2C

1. Prepare the server for the custom attributes that you want to use for authorization, if you

are using this feature in Stellar Cyber.

T

e

n

a

n

t-

s

p

e

c

if

i

c

S

S

O

N

ot

a

p

pl

ic

a

bl

e

Global SSO

Required for Authorization

Required for Authorization

C

u

st

o

m

A

tt

ri

b

u

te

N

a

m

e

s

t

e

l

l

a

r

_

s

c

o

p

e

s

t

e

l

l

a

r

_

p

r

i

V

a

l

u

e

s

(

s

e

t

l

a

t

e

r

)

r

o

o

t

p

a

r

t

n

e

r

t

e

n

a

n

t

s

u

p

e

r

_

a

d

m

i

n

v

i

l

e

g

e

s

t

e

l

l

a

r

_

t

e

n

a

p

l

a

t

f

o

r

m

_

a

d

m

i

n

s

e

c

u

r

i

t

y

_

a

d

m

i

n

u

s

e

r

I

D

n

u

m

b

e

r

fo

r

c

o

nf

(Optional) Specify an individual tenant ID, not name. The ID is available on the Tenants List page.

n

t

s

t

e

l

l

a

r

_

t

e

n

a

n

t

_

g

r

o

u

p

ig

u

r

e

d

te

n

a

nt

I

D

 n

u

m

b

e

r

fo

r

a

n

y

c

o

nf

ig

u

r

e

d

te

n

a

nt

g

r

o

u

p



(Optional) Specify a tenant group ID, not name. This is typically available for use by MSSP users with the

Partner role. The Tenant Group ID is displayed on the Tenant Groups page.

Values in these fields are case sensitive and syntax matters. Use the
exact indicated syntax and verify that you have made no typos

If you have created a custom privilege with spaces or dashes, use an
underscore instead. Example: A custom privilege of STML-Super Admin
must be entered as STML_Super_Admin.

2. Navigate to the Azure AD B2C > Overview page.

3. Select User attributes, and then select Add.

4. For each of the attributes you want to manage, add the Name and set the Data Type to

String, then click Create.

5. For Authorization to work, you must add an attribute for both stellar_scope and

stellar_privilege. The other two settings are optional.

 Syntax and case matters for these names.

Assign Values for Stellar Cyber Attributes in Azure AD B2C

1. Add values to these attributes for every user that will be accessing the Stellar Cyber DP.

Azure AD B2C does not provide a GUI-based mechanism to modify the attribute values.
This procedure uses Microsoft Graph Explorer to edit and validate the attributes.

a. To set the attribute values, retrieve the list of User Principal Names you

saved above.

b. Open Microsoft Graph and log in with your administrator Azure AD B2C

Credentials (https://developer.microsoft.com/en-us/graph/graph-explorer ).

c. In the query pane, change the GET action menu to PATCH.

d. Now enter this query URL, replacing the <user principal name> below with a
User Principal Name you saved earlier. For Azure AD B2C this must be the
value in the userPrincipalName field, which may be an atypical looking email
address.

https://graph.microsoft.com/beta/users/<user principal
name>

e. Enter the following content as the Request Body, replacing the attribute

values with one of the supported values in the table above:

 Take care when entering the required attributes and values. Typos in

either mean that users are not authenticated and cannot log in. Typos in
the optional attributes and values mean that users are not assigned to the
appropriate Stellar Cyber tenant or tenant group (but are authenticated).

For Azure AD B2C, you assign permissions to the application the user has
access to, with the following syntax. Use the Application ID you obtained
earlier and noted on your worksheet, but remove the hyphens. (example:
 0c0abe38-79ab-45d3-99fe-9378eec7b16f ). The Syntax is:

extension_<Azure AD B2C extensions app Application ID without
hyphens>_<custom attribute>: < custom attribute value>

    "extension_0c0abe3879ab45d399fe9378eec7b16f_stellar_scope":

"root",

    "extension_0c0abe3879ab45d399fe9378eec7b16f_stellar_privilege":

"security_admin"

}

f. Click Run Query to set the values.

g. To verify the values were set correctly, change the query type back to GET.

h. Now enter this query URL, replacing the <user principal name> below with
the same User Principal Name (Azure AD B2C login) you just set above.

https://graph.microsoft.com/beta/users/<user principal
name>?$select=onPremisesExtensionAttributes

i. Click Run Query and review the list of extensionAttributes to verify the values

were set.

Proceed to the next step...

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

