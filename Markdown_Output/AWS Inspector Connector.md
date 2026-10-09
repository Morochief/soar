Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring AWS Inspector Connectors

The AWS Inspector connector allows Stellar Cyber to ingest scan events from AWS Inspector.

Amazon Inspector is a vulnerability management service. It discovers and scans Amazon EC2
instances, container images in Amazon ECR, and Lambda functions. When Amazon Inspector
detects a software vulnerability or unintended network exposure, it creates a finding, which is a
detailed report about the issue.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: AWS Inspector

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

Index

Locating Records

Inspector Findings (not configurable
in the user interface)

Syslog

msg_class:

aws_inspector_f
inding

msg_origin.source:

aws_inspector

msg_origin.vendor:

Content Type

Index

Locating Records

aws

msg_origin.category:

security_scan

Domain

N/A

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

For Access Key / Secret Key Auth Method: Access Key and Secret Key, plus Region

For IAM Role Auth Method: Source Account Access Key, Source Account Secret Key, and IAM
Role ARN, plus Region

Adding an AWS Inspector Connector
To add an AWS Inspector connector:

1. Obtain AWS Inspector credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining AWS Inspector Credentials
There are two authentication methods: Access Key / Secret Key or IAM Role (IAM Assume
Role).

Configuring Credentials for Access Key / Secret Key

To configure the credentials for Access Key / Secret Key Auth Method:

1. Log in to the IAM Console with your AWS account ID, your IAM user name, and

password. You must have the permissions required to create access keys for a user.

2. Choose Users, then click the user name, and click Security credentials.

3. In the Access keys section, choose Create access key. Access keys have two

parts: an access key and a secret access key. Click Create access key.

4. On the Access key best practices & alternatives page, choose Other and then

choose Next.

5. (Optional) On the Set description tag page, enter a description.

6. Click Create access key.

7. On the Retrieve access keys page, choose Show to reveal the value of the user's

secret access key. Save the access key and secret access key in a secure location. You
will need them when configuring the connector in Stellar Cyber.

8. Click Done.

 For Access Key / Secret Key Auth Method, attach the policy to the user. See Attach

Permissions Policies to User. For IAM Role Auth Method, attach the policy to the IAM role.
See Configuring Credentials for IAM Role.

Attach Permissions Policies to User

1. In the AWS Management Console, Services, navigate to Identity and Access

Management (IAM) and click Users.

2. Find your user on the Users page and select it.

3. In the Permissions tab, click Add permissions > Add permissions.

4. Select Attach policies directly.

5. Select the following permissions: AmazonInspectorReadOnlyAccess and

AmazonInspector2ReadOnlyAccess. (In the Search box, you can type inspector.)

6. Click Next.

7. Click Add permissions.

8. The Permissions policies are attached to the user.

Configuring Credentials for IAM Role

To configure the credentials for IAM Role (IAM Assume Role) Auth Method:

1. In the AWS Management Console, Services, navigate to Identity and Access

Management (IAM) and click Roles.

2. Click Create Role.

3. Click Custom trust policy.

4. Using the example below as a guide, edit the JSON policy document.

 The following is just an EXAMPLE. You must modify this JSON to match the

resources in your own environment.

AWS Inspector custom trust policy

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::001xxxxxx433:user/<username>"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

5. Click Next.

6. Select the following permissions: AmazonInspectorReadOnlyAccess and

AmazonInspector2ReadOnlyAccess. (In the Search box, you can type inspector.)

7. Click Next.

8. Enter a Role name.

9. Click Create role.

10. Find your role name on the Roles page and select it.

11. Copy your ARN, which you will need when configuring the connector in Stellar Cyber.

Adding the Connector in Stellar Cyber
With the credential and log information available, you can now add the AWS Inspector connector
in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Vulnerability Scanner from the Category dropdown.

5. Choose AWS Inspector from the Type dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Collect, which is enabled already.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.

8. Choose a Tenant Name. The Interflow records created by this connector include this

tenant name.

9. Choose the device on which to run the connector.

10. (Optional) When the Function is Collect, you can apply Log Filters. For information,

see Managing Log Filters.

11. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.

12. Choose the Auth Method to use Access Key / Secret Key or IAM Role.

For Access Key / Secret Key Auth Method:

a. Enter the Access Key you noted above in Configuring Credentials for Access

Key / Secret Key.

b. Enter the Secret Key you noted above.

For IAM Role Auth Method:

The asterisk (*) indicates a required field.

a. Enter the Source Account Access Key you noted above in Configuring

Credentials for Access Key / Secret Key.

b. Enter the Source Account Secret Key.

c. Enter the IAM Role ARN that you noted above in Configuring Credentials for

IAM Role.

13. Choose a Region from the available regions in the dropdown.

14. Choose the Interval (min). This is how often the logs are collected.

15. (Optional) Click Disable SSL Certificate Verification if you want to disable SSL

certificate verification. Only disable SSL certificates if you have a necessary reason to,
otherwise, it is not a good security practice and may expose the connection to security
risks.

16. Click Next. The final confirmation tab appears.

17. Click Submit.

The new connector is immediately active and starts collecting logs.

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

403

Forbidden

This error occurs when the permission or scope is not

Did you enter your credentials correctly?

correct in a valid credential.

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

HTTP E

HTTP Stan

rror

dard Error

Explanation

Recommendation

Code

Name

user licensing, or quotas.

For a full list of codes, refer to HTTP response status codes .

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices to Syslog.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

