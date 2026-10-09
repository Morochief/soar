Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring F5 BIG-IP Telemetry

You can send F5 BIG-IP telemetry data to a sensor using API calls:

1. Install an API client.
2. Install the AS3 and telemetry packages.
3. Create a telemetry entry.
4. Authorize the telemetry.
5. Configure the sensor to receive the telemetry.
6. Subscribe the Sensor to the Telemetry Service.

You can also configure an F5 BIG-IP connector.

Install an API Client
You must use an API client to send the calls to the F5 BIG-IP firewall. We used Postman for this
procedure, but other clients should also work.

Install the AS3 and Telemetry Packages
To install the AS3 and telemetry packages in your BIG-IP firewall:

1. Download the AS3 script file from the F5 GitHub repository:

https://github.com/F5Networks/f5-appsvcs-extension/releases/tag/v3.27.0  .

2. Download the telemetry script file from the F5 GitHub repository:

https://github.com/F5Networks/f5-telemetry-streaming/releases  .

3. Log in to your BIG-IP firewall.

4. Select iApps.

5. Select Package Management LX.

6. Select Import.

7. Import the two scripts that you downloaded earlier.

Creating a Telemetry Entry
To create a telemetry entry in your BIG-IP firewall:

1. Log in to Postman.

2. Make a POST to https://<IP address of firewall>:

<port>/mgmt/shared/appsvcs/declare.

3. Enter this for the body:

{

   "class": "ADC",
   "schemaVersion": "3.10.0",
   "remark": "Example depicting creation of BIG-IP module log profiles",
   "Common": {
      "class": "Tenant",
      "Shared": {
         "class": "Application",
         "template": "shared",
         "telemetry_local_rule": {
            "remark": "Only required when TS is a local listener",
            "class": "iRule",
            "iRule": "when CLIENT_ACCEPTED {\n node 127.0.0.1 6514\n}"
         },
         "telemetry_local": {
            "remark": "Only required when TS is a local listener",
            "class": "Service_TCP",
            "virtualAddresses": [
               "255.255.255.254"
            ],
            "virtualPort": 6514,
            "iRules": [
               "telemetry_local_rule"
            ]
         },
         "telemetry": {
            "class": "Pool",
            "members": [
               {
                  "enable": true,
                  "serverAddresses": [
                     "255.255.255.254"
                  ],
                  "servicePort": 6514
               }
            ],
            "monitors": [
               {
                  "bigip": "/Common/tcp"
               }
            ]
         },
         "telemetry_hsl": {
            "class": "Log_Destination",
            "type": "remote-high-speed-log",
            "protocol": "tcp",
            "pool": {
               "use": "telemetry"
            }
         },
         "telemetry_formatted": {
            "class": "Log_Destination",
            "type": "splunk",
            "forwardTo": {
               "use": "telemetry_hsl"
            }
         },
         "telemetry_publisher": {
            "class": "Log_Publisher",
            "destinations": [
               {
                  "use": "telemetry_formatted"
               }
            ]
         },
          "telemetry_traffic_log_profile": {
4. Select Send.
            "class": "Traffic_Log_Profile",
            "requestSettings": {
               "requestEnabled": true,
               "requestProtocol": "mds-tcp",
Authorize Telemetry
               "requestPool": {
                  "use": "telemetry"
               },
To authorize the BIG-IP firewall to send telemetry:
               "requestTemplate":
"event_source=\"request_logging\",hostname=\"$BIGIP_HOSTNAME\",client_ip=\"$

5. Select Send.

4. Select the request you just sent.

Configure the Modular Sensor to Receive Telemetry
To configure the Modular Sensor to receive telemetry:

1. Log in to your BIG-IP firewall as the admin user.

1. Log in to Stellar Cyber and then navigate to System |

 DATA SOURCE MANAGEMENT | Sensors | Sensor Profiles.

2. Select  for the Modular Sensor that you want to receive telemetry.

CLIENT_IP\",server_ip=\"$SERVER_IP\",http_method=\"$HTTP_METHOD\",http_uri=\
"$HTTP_URI\",virtual_name=\"$VIRTUAL_NAME\",event_timestamp=\"$DATE_HTTP\"
            }
2. Select Collections.
         },
         "telemetry_afm_security_log_profile": {
            "class": "Security_Log_Profile",
3. Select Big IP to expand the list of requests.
            "application": {
               "localStorage": false,
               "remoteStorage": "splunk",
               "protocol": "tcp",
               "servers": [
                  {
                     "address": "255.255.255.254",
                     "port": "6514"
                  }
               ],
               "storageFilter": {
                   "requestType": "illegal-including-staged-signatures"
               }
            },
            "network": {
               "publisher": {
                  "use": "telemetry_publisher"
               },
               "logRuleMatchAccepts": false,
               "logRuleMatchRejects": true,
               "logRuleMatchDrops": true,
The Edit Sensor Profile screen appears.
               "logIpErrors": true,
               "logTcpErrors": true,
               "logTcpEvents": true
3. Expand Log Forwarder to view the options.
            }
         },
         "telemetry_asm_security_log_profile": {
            "class": "Security_Log_Profile",
            "application": {
               "localStorage": false,
               "remoteStorage": "splunk",
               "servers": [
                  {
                     "address": "255.255.255.254",
                     "port": "6514"
                  }
               ],
               "storageFilter": {
                  "requestType": "all"
               }
            }
         }
      }
1. Log in to Postman.
   }

Subscribe the Sensor to the Telemetry Service
To subscribe the sensor IP address to the telemetry service:

4. Enable HTTP JSON Parser.

5. Select Submit.

2. Make a POST to https://<IP address of firewall>:

}

<Port>/mgmt/shared/telemetry/declare.

3. Enter this for the body (using the IP address of your sensor):

{
   "class": "Telemetry",
   "My_System": {
      "class": "Telemetry_System",
      "systemPoller": {
         "interval": 60
      }
   },
   "My_Listener": {
      "class": "Telemetry_Listener",
      "port": 6514
   },

   "My_Consumer": {
      "class": "Telemetry_Consumer",
      "type": "Generic_HTTP",
      "host": "<IP address of sensor>",
      "protocol": "http",
      "port": 5200,
      "path": "/httpjson",
      "method": "POST",
      "headers": [
         {
            "name": "content-type",
            "value": "application/json"
         }
      ]

   }
}

4. Make a GET to https://<IP address of firewall>:

<Port>/mgmt/shared/telemetry/declare to confirm that the data is saved in the
firewall.

5. You should see a result similar to the following:

"message": "success",
"declaration": {
   "class": "Telemetry",
   "My_System": {
      "class": "Telemetry_System",
      "systemPoller": {
         "interval": 60,
         "enable": true,
         "actions": [
            {
               "setTag": {
                  "tenant": "`T`",
                  "application": "`A`"
               },
               "enable": true
            }
         ]
      },
      "enable": true,
      "host": "localhost",
      "port": 8100,
      "protocol": "http",
      "allowSelfSignedCert": false
   },
      "My_Listener": {
         "class": "Telemetry_Listener",
         "port": 6514,
         "enable": true,
         "trace": false,
         "match": "",
         "actions": [
            {
               "setTag": {
                  "tenant": "`T`",
                  "application": "`A`"
               },
               "enable": true
            }
         ]
      },
      "My_Consumer": {
         "class": "Telemetry_Consumer",
         "type": "Generic_HTTP",
         "host": "192.168.200.10",
         "protocol": "http",
         "port": 5200,
         "path": "/httpjson",
         "method": "POST",
         "headers": [
            {
               "name": "content-type",
               "value": "application/json"
            }
         ],
         "enable": true,
         "trace": false,
         "allowSelfSignedCert": false
      },
      "My_Consumer2": {
         "class": "Telemetry_Consumer",
         "type": "Generic_HTTP",
         "host": "192.168.1.192",
         "protocol": "http",
         "port": 5200,
         "path": "/httpjson",
         "method": "POST",
         "headers": [
            {
<Port>/mgmt/shared/telemetry/declare:
               "name": "content-type",
               "value": "application/json"
            }
         ],

body

6. To delete telemetry, issue this POST to https://<IP address of firewall>:

{

         "enable": true,
         "trace": false,
         "allowSelfSignedCert": false
      },
      "schemaVersion": "1.17.0"
   }

   "class": "Telemetry"

}

}

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

