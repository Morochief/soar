Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring AWS GuardDuty Connectors

The AWS GuardDuty connector allows Stellar Cyber to collect Amazon GuardDuty logs. Use
these instructions to obtain credentials and set up the connector.

 You can also use an AWS CloudWatch connector to ingest logs from Amazon GuardDuty
findings by exporting those logs to your AWS CloudWatch service. Refer to Amazon's
documentation for configuration of this
export: https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_exportfindings.html  .

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: AWS GuardDuty

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: Yes

Runs on: DP

Interval: Configurable

Collected Data

Content Type

GuardDuty Findings (not
configurable in the user interface)

Index

Syslog

Locating Records

msg_class:

aws_guardduty_f
inding

msg_origin.source:

aws_guardduty

msg_origin.vendor:

Content Type

Index

Locating Records

aws

msg_origin.category:

paas

Domain

N/A

Response Actions

N/A

Third Party Native Alert Integration Details

This connector ingests logs from AWS GuardDuty to get the raw alerts that are stored in the Syslog index.

Stellar Cyber maps AWS GuardDuty alerts. The alerts are read from the Syslog index, enriched with
Stellar Cyber fields, and mapped (with deduplication) to the Alerts index.

Deduplication is by tenantid and aws_guardduty_id.

In the logs, the msg_class aws_guardduty_finding will have different values for
aws_guarduty.Resource.ResourceType. The resource types are Instance, AccessKey, S3Bucket,
KubernetesCluster, ECSCluster, Container, RDSDBInstance, or Lambda.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

For Access Key / Secret Key Auth Method: Access Key and Secret Key, plus Region

For IAM Role Auth Method: Source Account Access Key, Source Account Secret Key, and IAM
Role ARN, plus Region

Locating Records

To search the alerts in the Alerts index or to search the Original Records in the Syslog index, use the
query: msg_class: aws_guardduty_finding AND exists:event.threat.name

Adding an AWS GuardDuty Connector
To add an AWS GuardDuty connector:

1. Add an AWS user
2. Create an access key
3. (Optional) Create an IAM role in same AWS account
4. (Optional) Create an IAM role across AWS accounts
5. Enable AWS GuardDuty in a region
6. Add the connector in Stellar Cyber
7. Test the connector
8. Verify ingestion

Adding an AWS User for Stellar Cyber

 Use our example as a guideline, as you might be using a different software version.

To add a user with the appropriate permissions:

1. Log in to your AWS Management Console at https://aws.amazon.com/console .

View the services in the Console Home or choose View all services.

2. Choose IAM. The IAM Dashboard appears.

3. Choose Policies and then choose Create Policy.

4. In the Create policy pane, choose the JSON tab.

5. Using the example below as a guide, edit the JSON policy document.

 The following is just an EXAMPLE. You must modify this JSON to match the

resources in your own environment.

GuardDuty policy

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

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "guardduty:GetFindings",
                "guardduty:ListDetectors",
                "guardduty:ListFindings",
                "guardduty:GetDetector"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestedRegion": [
                        "us-west-1",
                        "us-west-2"
                    ]
                }
            }
        }
    ]
}

24
25

6. Choose Next.

7. Give your policy a name to associate it with Stellar Cyber, then choose Create policy.

The policy can now be attached to a user.

8. From the IAM navigation pane, choose Users and then choose Create user.

9. On the Specify user details page for User details, enter a User name for the new

user.

10. Choose Provide user access to the – AWS Management Console optional to

produce login credentials for the new user, such as a password.

11. Choose how you want to create the Console password and then choose Next.

12. On the Set permissions page, choose Attach policies directly. Then search for the

policy you created above.

13. Select the checkbox to the left of the policy name, then choose Next.

14. On the Review and create page, verify the information and then choose Create user.

Creating an Access Key
The procedures in this section are for the Access Key / Secret Key Auth Method in Stellar Cyber.

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

(Optional) Creating an IAM Role in Same AWS Account
The procedures in this section are required for users who want to use the IAM Role Auth Method
for the AWS resources, for an IAM role that is created in the same AWS account.

Create an IAM User Without Permissions and Create IAM Policy

1. Log in to your AWS Management Console at https://aws.amazon.com/console .

View the services in the Console Home or choose View all services.

2. Choose IAM. The IAM Dashboard appears.

3. From the IAM navigation pane, choose Users and then click Create user.

4. On the Specify user details page, enter a User name for the new user.

5. Choose Provide user access to the – AWS Management Console optional to

produce login credentials for the new user, such as a password.

6. Choose how you want to create the Console password and then choose Next.

7. On the Set permissions page, choose Attach policies directly and click Create

policy.

8. On the Specify permissions page, choose the JSON tab.

9. Using the example below as a guide, edit the JSON policy document.

 The following is just an EXAMPLE. You must modify this JSON to match the

resources in your own environment.

GuardDuty policy - IAM Role - same AWS account

1
2
3
4
5
6

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",

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

            "Action": [
                "guardduty:GetFindings",
                "guardduty:ListDetectors",
                "guardduty:ListFindings",
                "guardduty:GetDetector"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestedRegion": [
                        "us-west-1",
                        "us-west-2"
                    ]
                }
            }
        }
    ]
}

10. Click Next.

11. Give your policy a name to associate it with Stellar Cyber.

12. Click Create policy.

Create an IAM Role with Trusted Entities

1. From the IAM navigation pane, choose Roles and then click Create Role.

2. Choose Custom trust policy.

3. Using the example below as a guide, edit the custom trust policy document.

 The following is just an EXAMPLE. You must modify this JSON to match the

resources in your own environment.

Trusted entities - same AWS account

1
2
3
4

{
    "Version": "2012-10-17",
    "Statement": [
        {

5
6
7
8
9
10
11
12
13
}

            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::001******433:user/jzhang-
connector"
            },
            "Action": "sts:AssumeRole"
        }
    ]

4. Click Next.

5. In the Permissions tab, click Add permissions and select Attach policies.

6. Click the checkbox to select the GuardDuty policy that you created earlier.

7. Click Add permissions.

8. On the Name, review, and create page, enter a Role name.

9. Review the trusted entities and permissions, then click Create Role.

10. On the Roles page, use the Search box to find your role name.

11. Click your role name.

12. Copy your ARN, which you will need when configuring the connector in Stellar Cyber.

(Optional) Creating an IAM Role Across AWS accounts
The procedures in this section are required for users who want to use the IAM Role Auth Method
for the AWS resources, for an IAM role that is created across AWS accounts.

Create an IAM User for Source AWS Account and Create IAM Policy

Create this IAM user if you have a source AWS account like an MSSP AWS account.

When configuring the connector in Stellar Cyber, you will need the source AWS account (MSSP
account) and the access key and secret key.

1. Log in to your AWS Management Console at https://aws.amazon.com/console .

View the services in the Console Home or choose View all services.

2. Choose IAM. The IAM Dashboard appears.

3. From the IAM navigation pane, choose Users and then click Create user.

4. On the Specify user details page, enter a User name for the new user.

5. Choose Provide user access to the – AWS Management Console optional to

produce login credentials for the new user, such as a password.

6. Choose how you want to create the Console password and then choose Next.

7. Choose Attach policies directly and click Create policy.

8. On the Specify permissions page, choose the JSON tab.

9. Using the example below as a guide, edit the JSON policy document.

 The following is just an EXAMPLE. You must modify this JSON to match the

resources in your own environment.

GuardDuty policy - IAM Role - across AWS accounts

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

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole"
            ],
            "Resource": [
                "*"
            ]
        }
    ]
}

10. (Optional) To only allow the particular destination AWS account IAM role, using the

example below as a guide, edit the JSON policy document.

 The following is just an EXAMPLE. You must modify this JSON to match the

resources in your own environment.

GuardDuty policy - IAM Role - allow destination AWS account

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

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole"
            ],
            "Resource": [
                "arn:aws:iam::001******433:role/Stellar-guardduty-role"
            ]
        }
    ]
}

11. Click Next.

12. Give your policy a name to associate it with Stellar Cyber, then choose Create policy.

(Optional) Create an IAM User for Destination AWS Account and Create
IAM Policy

Create this IAM user if you have a destination AWS account like an MSSP's tenant AWS
account.

When configuring the connector in Stellar Cyber, you will need the destination AWS account
(MSSP's tenant account) and the IAM role ARN.

1. Log in to your AWS Management Console at https://aws.amazon.com/console .

View the services in the Console Home or choose View all services.

2. Choose IAM. The IAM Dashboard appears.

3. From the IAM navigation pane, choose Users and then click Create user.

4. On the Specify user details page, enter a User name for the new user.

5. Choose Provide user access to the – AWS Management Console optional to

produce login credentials for the new user, such as a password.

6. Choose how you want to create the Console password and then choose Next.

7. Choose Attach policies directly and click Create policy.

8. On the Specify permissions page, choose the JSON tab.

9. Using the example below as a guide, edit the JSON policy document.

 The following is just an EXAMPLE. You must modify this JSON to match the

resources in your own environment.

GuardDuty policy - Stellar-guardduty-policy

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

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "guardduty:GetFindings",
                "guardduty:ListDetectors",
                "guardduty:ListFindings",
                "guardduty:GetDetector"
            ],
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestedRegion": [
                        "us-west-1",
                        "us-west-2"
                    ]
                }
            }
        }
    ]
}

10. Click Next.

11. Give your policy a name to associate it with Stellar Cyber, then choose Create policy.

Create an IAM Role with Trusted Entities

1. From the IAM navigation pane, choose Roles and then click Create Role.

2. Choose Custom trust policy.

3. Using the example below as a guide, edit the custom trust policy document.

 The following is just an EXAMPLE. You must modify this JSON to match the

resources in your own environment.

Trusted entities - across AWS accounts

1
2
3
4

{
    "Version": "2012-10-17",
    "Statement": [
        {

5
6
7
8
9
10
11
12
13
}

            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::001******433:user/jzhang-
connector"
            },
            "Action": "sts:AssumeRole"
        }
    ]

4. Click Next.

5. In the Permissions tab, click Add permissions and select Attach policies.

6. Click the checkbox to select the GuardDuty policy that you created earlier.

7. Click Add permissions.

8. On the Name, review, and create page, enter a Role name.

9. Review the trusted entities and permissions, then click Create Role.

10. On the Roles page, use the Search box to find your role name.

11. Click your role name.

12. Copy your ARN, which you will need when configuring the connector in Stellar Cyber.

Enabling AWS GuardDuty in a Region
You must enable AWS GuardDuty in the AWS console in a selected region. This automatically
creates a detector, which is needed for the configuration.

1. Open the AWS GuardDuty console: https://console.aws.amazon.com/guardduty/ .

2. Choose Get Started.

3. Choose Enable GuardDuty.

If you are redirected to the Get started page when you open the AWS GuardDuty console,
AWS GuardDuty is not enabled in the selected region.

When AWS GuardDuty is enabled, to verify that you have a detector for your current region,
navigate to the Settings page in the AWS GuardDuty console.

Adding the Connector in Stellar Cyber
With the credential and log information available, you can now add the AWS GuardDuty
connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose PaaS from the Category dropdown.

5. Choose AWS GuardDuty from the Type dropdown.

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

a. Enter the Access Key you noted above in Creating an Access Key.

b. Enter the Secret Key you noted above.

For IAM Role Auth Method:

The asterisk (*) indicates a required field.

a. Enter the Source Account Access Key.

b. Enter the Source Account Secret Key.



The IAM role can be across multiple AWS accounts:

For the source account, provide the trusted IAM user's access
key and secret key. Refer to Creating an Access Key.

For the destination account, provide the AWS IAM role, in which
this role is trusting the source account IAM user. Refer to
(Optional) Creating an IAM Role Across AWS Accounts.

c. Enter the IAM Role ARN you noted above.

13. Choose a Region from the available regions in the dropdown.

14. Choose the Interval (min). This is how often the logs are collected.

15. Click Next. The final confirmation tab appears.

16. Click Submit.

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

