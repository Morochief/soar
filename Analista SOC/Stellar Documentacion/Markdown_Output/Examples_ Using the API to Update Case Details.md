Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Examples: Using the API to Update Case
Details

You can use Stellar Cyber's Cases API to update any combination of a specified case's severity,
status, assignee, or tags. Any changes you make via the API to these fields are visible in the
Case Details display for the event.

 Refer to Configuring API Authentication for general requirements to use the API.

Cases API URL
The Cases API is available at the following URL. Note that the ID of the case to be updated is
included as a parameter in the URL:

/connect/api/v1/cases/<case_id>

Finding the ID for an Case
Using the API to update an case always requires the ID of the case to be updated as part of the
URL. The easiest way to find the ID for an case is to use the cases API to retrieve details. Refer
to Examples: Using the API to Retrieve Case Details. Once you have retrieved case details,
search on the _id field to find the case ID.

Updating Case Details with the API
You can use PUT calls to update any combination of the severity, status, assignee, tags, or
description for a specified case.

You can use any language to make the call. For our example, we use Python.

 For a PUT call you need the ID of the event whose fields you want to update.

Your call must have the header, the /connect/api/v1/cases path, and at least one of the
severity, status, assignee, or tags parameters. These are the different case details you an
update using the API. Enter your own information for the arguments in the table below.

Argument

userid

API Key (Refresh Token)

HOST

ID

status

severity

assignee

tags

Description

User name of the admin making the call. Sample script below uses

myuser@stellarcyber.ai.

API key for the user, retrieved from the user interface. Sample script below uses

2iRpBAyQYEfv77R2QtATlJN6Nvq6uzftBdzotSy2pjT-IvJTLw9aiHyh7Y2mo12IDSWc-

FfHwUyPpmiHQnJrSH.

The URL or IP address of your Stellar Cyber server. Sample script below uses

myserver@stellarcyber.cloud.

The ID of the case to update. The ID is included in the URL as a parameter and is not

part of the data payload. For example:

/connect/api/v1/cases/<case_id>

Changes the status to one of the following values:

New

In Progress

Resolved

Cancelled

Changes the severity to one of the following values:

Critical

High

Medium

Low

Changes the assignee to any valid user in the Stellar Cyber system.

Adds or deletes the specified tag to the list of tags for the case, depending on the

operator specified:

To add a tag:

"tags": {

"add": [ "my added tag"],

},

To delete a tag:

"tags": {

"delete": [ "my deleted tag"],

},

Sample Script

The sample script below works as follows:

The script sets the host and refresh_token parameters in Step 1 in the sample.

Because JWTs expire ten minutes after they are generated, this script includes logic
that generates and uses a fresh JWT every time the script is run. The script runs the

getAccessToken procedure to generate the new JWT (Step 2 in the sample).

The script uses the generated JWT to make a PUT to the cases API in the putCase
procedure (Step 3 in the sample). The script adds the tag October-event to the case
with the ID of 1674728869334287aba4486901d24c4189a6fe8eab6efe05:

The script also prints the generated JWT to the screen. This, however, is not strictly
necessary since the getAccessToken procedure already prints the status code for the
call to the access_token API (200 for success; 401 for failure).

#!/usr/bin/python3

import requests
import base64
import json
import time
from urllib.parse import urlunparse
requests.packages.urllib3.disable_warnings()

# Step 1
# Add DP IP/hostname and refresh token from GUI here
HOST = "myserver.stellarcyber.cloud"
refresh_token =
"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhcGlfa2V5Ijp7ImtleV9pZCI6ImY3NGYzYyIsInVzZX
JfaWQiOiI1YjdlNTA5ZjMyYmM0MmEzYWU5MTZiNDY0NzRmZGE0YyIsIm9yZ19pZCI6IjhlYTJiOWU3OTcxYj
QyZjZhNzJmZTYyODYyOTEwN2JmIiwiZXhwIjo0ODkyOTE0MzY3fSwiaWF0IjoxNzM5MzE0MzY3fQ._2Senlw
UTvmoAj4gFOehLyGtrKLRp8XfFrn8U35TOIo"

def getAccessToken(refresh_token):
    headers = {
        "Authorization": "Bearer " + refresh_token
    }
    url = urlunparse(("https", HOST, "/connect/api/v1/access_token", "", "", ""))
    res = requests.post(url, headers=headers, verify=False)
    print(res.status_code)
    return res.json()["access_token"]

def putCase(token):
    headers = {"Authorization": "Bearer " + token, 'content-type':
'application/json' }
    url = urlunparse(("https", HOST,
"/connect/api/v1/cases/1674728869334287aba4486901d24c4189a6fe8eab6efe05", "", "",
""))
    json_data = {
      "tags": {
    "add": [ "October-event"],
    },
    }
    query = json.dumps(json_data)
    res = requests.put(url, data=query, headers=headers, verify=False)
    print(res.text)
    print(res.status_code)
    return res.json()

if __name__ == "__main__":

    # Step 2: Use getAccessToken with supplied credentials to generate JWT
    jwt = getAccessToken(refresh_token)
    print("------------ jwt -------------")
    print(jwt)
    print("------------ jwt  end -------------")

    # Step 3: use JWT token to call public API
    data = putCase(jwt)
    print("------------ show result of put case -------------")
    print(data)
    print("------------ end api results -------------")

Using the API to Verify the Update
You can always use the Stellar Cyber user interface to check whether your updates were
successful – just navigate to the Case Details display for the event you changed and check the
fields for your updates. The History tab even indicates which changes were made via the API:

Alternatively, you can make a query using the cases API to make sure your PUT call worked. For
example, we just used our script in Updating Case Details with the API to set a tag called
October-event. Let's query for all cases matching that tag:

https://192.168.1.24/connect/api/v1/cases?tags=October-event

In response, the API returns something similar to the following:

{
  "data": {
    "cases": [
      {
        "_id": "62fceb4a48be7776c793a02a",
        "acknowledged": 1660826741467,
        "assignee": "826ef6979788454297c85cbba4a51c08",
        "closed": 0,
        "created_at": 1660742474343,
        "created_by": "System",
        "cust_id": "",
        "modified_at": 1660835991789,
        "modified_by": "ohtani",
        "name": "Carbon Black:XDR Endpoint Indicator of Threat and 16 others",
        "score": 25,
        "severity": "Medium",
        "size": 17,
        "status": "New",
        "tags": [
          "October-event"
        ],
        "ticket_id": 67535,
        "version": 17
      }
    ],
    "total": 1
  }
}

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

