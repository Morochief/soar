✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Examples: Using the API with Tenant Groups
You can use the Stellar Cyber API to perform the following tasks for tenants:
Create a new tenant group
Delete an existing tenant group
Update an existing tenant group's settings
List all tenant groups
Retrieve a tenant group's information using its tenant ID

Refer to Configuring API Authentication for general requirements to use the API.
Tenant Group API Syntax
The tenant group API is available at the following location:
https://<DP url>/connect/api/v1/tenant_groups
The table below lists the available methods for the tenants API, along with the corresponding
syntax. Following the table, separate sections provide the schema for each method along with a
corresponding example.
| Task | Method | Syntax         |
| ---- | ------ | -------------- |
|      | GET    | /tenant_groups |
Get All Tenant Groups
/tenant_groups/{id}
| Get a Specific Tenant Group | GET |     |
| --------------------------- | --- | --- |

|     | DELETE | /tenant_groups/{id} |
| --- | ------ | ------------------- |
Delete a Specific Tenant Group
|     | POST | /tenant_groups/ |
| --- | ---- | --------------- |
Create a Tenant Group
|     | PATCH | /tenant_groups/{id} |
| --- | ----- | ------------------- |
Update a Tenant Group's Configuration

Get All Tenant Groups
The following example uses cURL with basic authentication to query for all tenant groups with a
GET command using the following details:
Username:API Key – ohtani:N-YrP02Xl6yHO-
1HW1gi1nems2g319Q3wLNpOAxWx9_ttbMw3pyB5qPvSVl3qt9CmgvOhHhtDCuEs5Kc
In6mWw
Stellar Cyber DP IP Address –192.168.11.11
curl -k -u ohtani:N-YrP02Xl6yHO-
1HW1gi1nems2g319Q3wLNpOAxWx9_ttbMw3pyB5qPvSVl3qt9CmgvOhHhtDCuEs5KcIn6mWw -i -H
"Accept: application/json" -H "Content-Type: application/json" -X GET
https://192.168.11.11/connect/api/v1/tenant_groups
Values in bold are the values you must supply as part of a similar query.
Get a Specific Tenant Group
The following example uses cURL to query for a specific tenant group with a GET command
using the following details:
Username:API Key – ohtani:N-YrP02Xl6yHO-
1HW1gi1nems2g319Q3wLNpOAxWx9_ttbMw3pyB5qPvSVl3qt9CmgvOhHhtDCuEs5Kc
In6mWw
Stellar Cyber DP IP Address –192.168.11.11
Tenant Group ID – 08990563
 You can find the tenant group ID in System | ORGANIZATION MANAGEMENT |
Tenant Groups. Select the in the Group ID column and use the Copy to
Clipboard command in the context menu that appears to copy the Tenant ID.
curl -k -u ohtani:N-YrP02Xl6yHO-
1HW1gi1nems2g319Q3wLNpOAxWx9_ttbMw3pyB5qPvSVl3qt9CmgvOhHhtDCuEs5KcIn6mWw -i -H
"Accept: application/json" -H "Content-Type: application/json" -X GET
https://192.168.11.11/connect/api/v1/tenant_groups/08990563
In response, the API returns configuration details for the specified tenant, similar to the following:
{"data":{"org_id":"default-organization","tenants":
["47784549"],"tgrp_id":"08990563","tgrp_logo":"","tgrp_name":"sentinelone","created_a
t":1612832242,"updated_at":1650927522}}
The "field":"value" pairs returned by the API are same options you set when creating a
tenant group manually in System | ORGANIZATION MANAGEMENT | Tenant Groups. and are
described in the schema in Create a Tenant Group.
Delete a Specific Tenant Group
The following example uses cURL to delete a specific tenant group with a DELETE command
using the following details:

Username:API Key – ohtani:N-YrP02Xl6yHO-
1HW1gi1nems2g319Q3wLNpOAxWx9_ttbMw3pyB5qPvSVl3qt9CmgvOhHhtDCuEs5Kc
In6mWw
Stellar Cyber DP IP Address –192.168.11.11
Tenant Group ID – 8f8f3396c7fa444a8f7b8b55e2b75a04
 You can find the tenant group ID in System | ORGANIZATION MANAGEMENT |
Tenant Groups. Right-click in the ID column and use the Copy to Clipboard
command in the context menu that appears to copy the Tenant ID.
curl -k -u ohtani:N-YrP02Xl6yHO-
1HW1gi1nems2g319Q3wLNpOAxWx9_ttbMw3pyB5qPvSVl3qt9CmgvOhHhtDCuEs5KcIn6mWw -i -H
"Accept: application/json" -H "Content-Type: application/json" -X DELETE
'https://192.168.11.11/connect/api/v1/tenant_groups/8f8f3396c7fa444a8f7b8b55e2b75a04'
In response, the API returns a success (200 OK) or failure message.
 Deleting a tenant group via the API does not delete the tenant group members themselves. It
only deletes the tenant group container. The member tenants still appear in the Tenants
page after the group is deleted.
Create a Tenant Group
This section describes how to create a new tenant group in the API. The schema for the tenant
groups API lets you specify all of the same configuration details you would when creating a new
tenant group in the user interface. The available fields are as follows:
{
"tgrp_name": "string",
"tenants": [
"string"
],
"tgrp_logo": "string"
}
Your call must have the header and the /connect/api/v1/tenant_groups path. In addition, the
following fields are mandatory:
tgrp_name – The name of the tenant group to be created
tenants – Must include the tenant ID of at least one valid tenant on the server
Sample Update Tenant Group Script
Here is a sample Python script with arguments filled in. Note that any arguments that you don't
supply values for are left at their default settings, as described in Using Tenant Groups
#!/usr/bin/env python
import json
import requests
headers={'Accept': 'application/json', 'Content-type': 'application/json'}
elastic_url ='https://192.168.11.11/connect/api/v1/tenant_groups'
json_data = {
"tgrp_name": "Grouped Up",
"tenants": [
"9d1549f33689454bb290d7811d51d321",
"3accb209d68949f1a99b4c27ead50974",
],
}

query = json.dumps(json_data)
response = requests.post(elastic_url, auth=('ohtani','N-YrP02Xl6yHO-
1HW1gi1nems2g319Q3wLNpOAxWx9_ttbMw3pyB5qPvSVl3qt9CmgvOhHhtDCuEs5KcIn6mWw'),
data=query, verify=False, headers = headers)
print (response.text)
This example performs a POST call as the user ohtaniwith the API key shown in the text. The
call is to the Stellar Cyber server at 192.168.11.11to create a tenant with the following fields:
tgrp_name – Grouped Up
tenants– 9d1549f33689454bb290d7811d51d321 and
3accb209d68949f1a99b4c27ead50974
 Tenant IDs can be retrieved from System | ORGANIZATION MANAGEMENT |
Tenants.
All other fields are left at their default values.
Update a Tenant Group
This section describes how update the settings for an existing tenant group. You can use a
PATCH to the tenant groups API to change any of the configuration details available when
creating a new tenant group in the user interface. The only mandatory fields are the Tenant ID
and the Tenant Name (cust_name). The available fields are the same as described in Create a
Tenant Group.
Your call must have the header and the
/connect/api/v1/tenant_groups/<tenant_group_id> path, and must have the tgrp_name
field, in addition to any optional fields shown in the schema above that you want to change.
Sample Update Tenant Group Script
This script takes the tenant group we created in Create a Tenant Group and adds an additional
tenant.
#!/usr/bin/env python
import json
import requests
headers={'Accept': 'application/json', 'Content-type': 'application/json'}
elastic_url
='https://192.168.11.11/connect/api/v1/tenant_groups/aa57276476b9434b88a512d600a915d
d'
json_data = {
"tgrp_name": "Grouped Up",
"tenants": [
"294df931be1f436c8de7d0b106cc0b9f",
"9d1549f33689454bb290d7811d51d321",
"3accb209d68949f1a99b4c27ead50974",
],
}
query = json.dumps(json_data)
response = requests.patch(elastic_url, auth=('ohtani','N-YrP02Xl6yHO-
1HW1gi1nems2g319Q3wLNpOAxWx9_ttbMw3pyB5qPvSVl3qt9CmgvOhHhtDCuEs5KcIn6mWw'),
data=query, verify=False, headers = headers)
print (response.text)
This example performs a PATCH as the user ohtaniwith the API key shown in the text. The call
is to the Stellar Cyber server at 192.168.11.11to add an additional tenant to the group:
Tenant Group ID – aa57276476b9434b88a512d600a915dd

 The Tenant ID can be retrieved from System | ORGANIZATION MANAGEMENT |
Tenants and included in the URL.
tgrp_name – Grouped Up
tenants–
294df931be1f436c8de7d0b106cc0b9f
9d1549f33689454bb290d7811d51d321
3accb209d68949f1a99b4c27ead50974
Note that our update script included both the existing tenants in the group and the one we
wanted to add. If we'd just included the new tenant, the other two would have been removed
from the group.
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support | Contact Us |  