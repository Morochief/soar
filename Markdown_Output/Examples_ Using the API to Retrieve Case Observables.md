Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Examples: Using the API to Retrieve Case
Observables

You can use the Stellar Cyber API to query the DP for a detailed list of the observables
associated with a specified case ID. Observables include the hosts, users, processes, files,
registry keys, sensors, services, external hosts, and URLs associated with the case.

 Refer to Configuring API Authentication for general requirements to use the API.

API Syntax for Retrieving Case Details
The syntax for retrieving case details via the API is as follows:

https://URL/connect/api/v1/cases/<case_id>/observables

Finding the Case ID for the Observables Query

To query for an case's observables, you must first have the case's ID. You can retrieve an case's
ID using either of the following techniques:

Navigate to the Detail display for the case whose ID you want to retrieve. The case's
ID is included in the URL for the Detail page, as shown below.

You can also retrieve the case ID through the cases API. Refer to the examples and
instructions in Examples: Using the API to Retrieve Case Details for details on how
to fetch cases through the API.

Once you've retrieved an case whose observables you want to fetch, locate the "_id":
"{case_id}" field. This is the ID you must supply when querying for observables.

Examples
The following examples show how to use the API to fetch a specified case's observables. There
are separate Python scripts and cURL commands using the following details:

Stellar Cyber DP IP Address –192.168.11.11

Username:API Key – ohtani:N-YrP02Xl6yHO-
1HW1gi1nems2g319Q3wLNpOAxWx9_ttbMw3pyB5qPvSVl3qt9CmgvOhHhtDCuEs5Kc
In6mWw
Case ID – 6434c0ae91fad4e0b52bee0a

These items are shown in bold in the examples below. Replace them with your own values when
constructing similar queries.

cURL

curl -k -u admin:EjbWSBPJ2DW9ynJmUZm-SXNvHVbd6iPJoItrKasnY6h-
i5vz4a983FANCm55fhhsIwrcA0taKzfIEw1kLbJCjQ -i -H "Accept: application/json" -H
"Content-Type: application/json" -X GET
'https://10.11.190.88/connect/api/v1/cases/6434c0ae91fad4e0b52bee0a/observable
s'

Python

#!/usr/bin/env python

import json

import requests

headers={'Accept': 'application/json', 'Content-type':
'application/json'}

url
='https://10.11.190.88/connect/api/v1/cases/6434c0ae91fad4e0b52bee0a/ob
servables'

response = requests.get(url, auth=('admin', 'EjbWSBPJ2DW9ynJmUZm-
SXNvHVbd6iPJoItrKasnY6h-i5vz4a983FANCm55fhhsIwrcA0taKzfIEw1kLbJCjQ'),
headers = headers, verify=False)

print (response.text)

Case Information Returned by the API
The API returns the following information on the observables for the specified case. Observables
are returned in field:value pairs, with fields separated from values by a colon. Separate
field:value pairs are separated with commas for easy import. If a field:value pair has multiple
sub-entries, they are enclosed in regular brackets. Refer to Sample Output for an example.

 Refer to About the Observables Panel for information on working with the observables for

an case in the user interface.

API Field Name Description

host

user

{ip: name, hostname: label}

{username: name}

process

{process_name: name}

file

registry

sensor

service

{file_name: name}

{key: name}

{id: name}

{service_name: name}

external_host

{ip: name, hostname: label}

url

{url: name}

Sample Output
The text below shows sample output of an API call for an case's observables:

"observables":{"external_host":
[{"hostname":"192.34.20.100","ip":"192.34.20.100"}],"service":
[{"service_name":"azure_ad"}],"user":
[{"username":"qa@aella.onmicrosoft.com"}]},"total":3}

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

