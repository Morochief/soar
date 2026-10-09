Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Forescout Connectors

Use the Forescout connector to perform Respond actions on systems registered in your
Forescout account. Forescout connectors in Stellar Cyber are used for response only, not
collection of event data. This connector is supported with Forescout v8.2.2 and Forescout's
EyeExtend Connect Module v1.9.0 or later. Refer to the following documentation, if needed,
during this procedure:

Connect Plugin Application Building and Deployment Guide 

 The devices you want to use with this connector must be registered in the Forescout

Enterprise Console (CounterACT devices) and associated with the application module that
will be creating for communication to Stellar Cyber.

Connector Overview: Forescout

Capabilities

Collect: No

Respond: Yes

Native Alerts Mapped: No

Runs on: DP or Sensor

Interval: N/A

Collected Data

N/A

Domain

https://<Hostname or IP>

where <Hostname or IP> is a variable from the configuration of this connector

Response Actions

Action

Update Device

Required Fields

srcip, dstip, srcmac, or dstmac

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

Hostname or IP, Username, Password, and App Name

Adding a Forescout Connector
To add a Forescout connector:

1. Set up Stellar Cyber access in the Forescout Console
2. Adding the connector in Stellar Cyber
3. Test the Connector
4. Use the Connector

 Use our example as a guideline, as you might be using a different software version.

Preparing for Setup
Perform the following steps on the system from where you will be running the Forescout
Enterprise Console:

1. Open a browser and access the Forescout Customer Support portal Downloads

page (https://forescout.force.com/support/s/downloads).

2. Download the eyeExtend Connect Module, v1.9.0 or later. This .fpi file allows you to

install a web API connector to configure for communication with Stellar Cyber.

3. You will also need the StellarCyberActionAPI app to enable Stellar Cyber to trigger an
action using the Connect framework. Access one of the following pages to download the
StellarCyberActionAPI.zip file:

Download link: https://github.com/Forescout/eyeExtend-
Connect/tree/master/StellarCyberActionApi 

4. Before you proceed, you will need to make note of the following information to use

throughout this procedure.

Host address for your Forescout Enterprise Manager and Connecting
CounterACT Device (the CounterACT "device" is a middleman that forwards
queries and requests to and from third-party instances)

An administrative login and password to that host console

You will create and use the following on both the Forescout side and Stellar
Cyber side:

app module name

username for app module

password for that user

Setting up the Stellar Cyber App in Forescout

1. Log into the Forescout Enterprise Console as an administrative user.

2. Use the Help>About menu to verify that your Forescout version is v8.2.2, or later.

3. From the Forescout Console, open the Tools > Options menu.

4. In the Options dialog that opens, select the Modules block.

5. Click the blue Install button to begin the process of loading and installing the web

connector file you downloaded above.

6. The install dialog displays. Check the box to Agree to the licensing terms, then click

Install.

 The installation begins immediately and cannot be interrupted or canceled.

7. When the installation completes, click the Close button and return to the

Options>Modules window. Expand the Connect row and make sure all the services
are running.

8. In the Forescout Console's Options dialog, access the Connect > Configuration

pane. You can access this two ways:

Click Modules from the navigation list, then expand the Connect module and
select the Connect row element, then click Configure.

Click Connect directly from the navigation list at the left of the dialog.

9. When the Connect configure pane is displayed, click Import and select the

StellarCyberActionAPI.zip you had downloaded from GitHub, above, or your custom
module.

10. When the import process has completed, click Close from the import dialog.

11. A dialog now displays that allows you to specify the username and password for this

module to communicate with Stellar Cyber. Enter the username and password you want
to use, and make note of those for use with the Stellar Cyber connector. Then click OK.

 The password should not include non-ASCII special characters.

12. A system description dialog now opens, allowing you to optionally define custom sets of

devices to associate with this application. Click Add to create at least one setup
definition. In the dialog that displays, specify a name for the setup, then click Next.

13. The second pane allows you to specify which CounterACT Devices to associate with

this app. After selecting a specific device or all of them, click Finish. The new
application is added to the Connect pane. Click Apply to save the configuration.

14. Make note of the module Name displayed in the Connect dialog.  This was loaded from

the file you imported and is used when you configure the Stellar Cyber connector.

You are now ready to configure your Stellar Cyber Forescout Connector.

Adding the Connector in Stellar Cyber

With the configuration information handy, you can add the Forescout connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Endpoint Security from the Category dropdown.

5. Choose Forescout from the Type dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Respond, which is enabled already.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.

  The name must match the name of the module you imported in the previous

section.

8. Choose a Tenant Name. The Interflow records created by this connector include this

tenant name.

9. Choose the device on which to run the connector.

10. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.

11. Enter the Hostname or IP. Do not include https in the Hostname. This is the address of
the Forescout Connecting CounterACT Device; it forwards all the queries and requests
to and from Stellar Cyber. (Forescout recommends that you not use the address of the
Enterprise Manager Console.) The following parameters are the name and
authentication attributes you used when you imported the action module.

12. Enter the Username you noted above.

13. Enter the Password you noted above.

14. Enter the App Name you noted above.

15. (Optional) App Action JSON. If there is a standard response action you want to take
with this connector, or a default JSON parameters you want saved, you can add that
now. The JSON content will be saved for use by anyone using the connector to run an
External Action | Update Device action from the Event Details pane. You can
alternatively enter JSON at the time you run the action but that JSON is not saved. For
syntax guidance, refer to the section: Updating Devices with the Forescout
Connector.

16. Click Next. The final confirmation tab appears.

17. Click Submit.

The new connector is immediately active.

Testing the Connector
When you add (or edit) a connector, we recommend that you run a test to validate the
connectivity parameters you entered. The test validates authentication and connectivity.

 For connectors running on a sensor, Stellar Cyber recommends that you allow 30-60

seconds for new or modified configuration details to be propagated to the sensor before
performing a test.

1. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

2. Locate the connector by name that you added, or modified, or that you want to test.

3. Click Test at the right side of that row. The test runs immediately.

 Note that you may run only one test at a time.

Stellar Cyber conducts a basic connectivity test for the connector and reports a success or failure
result. A successful test indicates that you entered all of the connector information correctly.

To aid troubleshooting your connector, the dialog remains open until you explicitly close it by
using the X button. If the test fails, you can select the   button from the same row to review and
correct issues.

 The connector status is updated every five (5) minutes. A successful test clears the
connector status, but if issues persist, the status reverts to failed after a minute.

Repeat the test as needed.

Display sample messages...

Success !

Failure with summary of issue:

Show More example detail:

If the test fails, the common HTTP status error codes are as follows:

HTTP E

HTTP Stan

rror

dard Error

Explanation

Recommendation

Code

Name

400

Bad

This error occurs when there is an error in the

Request

connector configuration.

Did you configure the connector correctly?

401

Unauthorize

d

This error occurs when an authentication credential is

Did you enter your credentials correctly?

invalid or when a user does not have sufficient

privileges to access a specific API.

Are your credentials expired?

Are your credentials entitled or licensed for that

specific resource?

HTTP E

HTTP Stan

rror

dard Error

Explanation

Recommendation

Code

Name

403

Forbidden

This error occurs when the permission or scope is not

correct in a valid credential.

Did you enter your credentials correctly?

Do you have the required role or permissions for

that credential?

404

Not Found

This error occurs when a URL path does not resolve

Did you enter your API URL correctly?

to an entity.

429

Too Many

Requests

This error occurs when the API server receives too

The server or user license/quota will eventually

much traffic or if a user’s license or entitlement quota

recover. The connector will periodically retry the

is exceeded.

query.

If this occurs unexpectedly or too often, work with

your API provider to investigate the server limits,

user licensing, or quotas.

For a full list of codes, refer to HTTP response status codes .

Updating Devices with the Forescout Connector
When an event has occurred on a host known to the Forescout connector, you can use this
connector to perform an action on that host.

1. Access the Event Details Display:

a. Select Threat Hunting.

The Interflow Search tab appears.

b. Select the Indices for Traffic.

c. Select an event and click the More Info button.

2. From the event display, select the Actions tab, and click Update Device.

3. From the Connector menu, select the Forescout connector.

4. The Target menu lists the addresses associated with this event. Select the host on

which you want to run the Forescout connector update action. The target can be one of
these: Source Host, Destination Host, Source MAC, or Destination MAC. The Target
Value is updated automatically from the event data. These two fields are required
default parameters for the Forescout action and should not be specified in the
JSON added in the next step.

5. If your connector was created with default JSON, you can customize it now, or skip this
step. Populate the JSON field with the action you want the connector to transmit to the
Forescout app configured in the beginning of this procedure. Note that Stellar Cyber
verifies general format of the JSON, not the logic. Following is an example based on
ActionAPI's supported JSON properties:

{

"connect_actionapi_vlan_assign":true,

"connect_actionapi_vlan_assign_id":"vlan233"

}



Do not include the IP or MAC address, as that is added automatically based on
your selection in the previous step. The JSON that is transmitted to Forescout will
include the IP or MAC and the property tag, similar to the sample below.

{

"mac":"009027390a7c",

"properties":{

"connect_actionapi_vlan_assign":true,

"connect_actionapi_vlan_assign_id":"vlan233"

}

}

Refer to Forescout documentation for supported fields and syntax details.

6. Click Submit. The connector runs the update action one time.

For more information on working with the events and the actions on them, refer to Understanding
Event Details.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

