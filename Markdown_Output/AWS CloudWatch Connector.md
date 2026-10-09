Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring AWS CloudWatch Connectors

The AWS CloudWatch connector allows Stellar Cyber to collect AWS ECS/EKS, WAF, VPC Flow,
and Amazon GuardDuty logs. Use these instructions to obtain credentials and set up the
connector.

 Although the AWS CloudWatch connector may successfully import other logs, only

AWS Elastic Container Service (ECS)/Elastic Kubernetes Service (EKS), Web Application
Firewall (WAF), VPC Flow, and Amazon GuardDuty logs are supported in this release due to
performance issues that can occur with other log types. Stellar Cyber is working on
enhancements for other log types in future releases.

 You can use an AWS CloudWatch connector to ingest logs from Amazon GuardDuty findings
by exporting those logs to your AWS CloudWatch service. Refer to Amazon's documentation
for configuration of this
export: https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_exportfindings.html  .

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: AWS CloudWatch

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: Configurable

Collected Data

Content Type

N/A

Index

Syslog

Traffic (VPC flow)

Locating Records

msg_class:

aws_cloudwatch_
log

aws_cloudwatch_wa
f (for WAF logs)

aws_guardduty (for
GuardDuty logs)

aws_cloudwatch_vp
cflow (for VPC Flow
logs. Select the
VPC Flow Logs
checkmark also.)

msg_origin.source:

aws_cloudwatch

aws_guardduty

msg_origin.vendor:

aws

msg_origin.category:

paas

waf (for WAF logs)

Domain

https://logs.<Region>.amazonaws.com/

where <Region> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

For Access Key / Secret Key Auth Method: Access Key and Secret Key, plus Region, and Log
Group(s)

For IAM Role Auth Method: Source Account Access Key, Source Account Secret Key, and IAM
Role ARN, plus Region, and Log Group(s)

Adding an AWS CloudWatch Connector
To add an AWS CloudWatch connector:

1. Add an AWS user
2. Create an access key

3. Identify CloudWatch log groups
4. (Optional) Create an IAM role in same AWS account
5. (Optional) Create an IAM role across AWS accounts
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

CloudWatch policy

1
2
3
4
5

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",

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

            "Effect": "Allow",
            "Action": [
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams",
                "logs:GetLogEvents",
                "logs:FilterLogEvents"
            ],
            "Resource": "*",
            "Condition": {
                "ForAnyValue:StringEquals": {
                    "aws:RequestedRegion": "us-west-2"
                }
            }
        }
    ]
}

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

Identifying AWS CloudWatch Log Groups
For this connector, you will specify one or more log groups to ingest. Use this procedure to locate
the group names (this procedure assumes that you have already configured your CloudWatch
instances and log groups).

1. Log in to your AWS CloudWatch Console at

https://console.aws.amazon.com/cloudwatch/  .

2. Navigate to the Logs section of the left hand navigation pane.

3. Select Log Groups.

4. Make note of the groups you want to ingest to Stellar Cyber.

(Optional) Creating an IAM Role in Same AWS Account
The procedures in this section are required for users who want to use the IAM Role Auth Method
for the AWS resources, for an IAM role that is created in the same AWS account.

Create an IAM User Without Permissions and Create IAM Policy

1. Log in to your AWS Management Console at https://aws.amazon.com/console .

View the services in the Console Home or choose View all services.

2. Choose IAM. The IAM Dashboard appears.

3. From the IAM navigation pane, choose Users and then click Create user.

4. On the Specify user details page for User details, enter a User name for the new

user.

5. Choose Provide user access to the – AWS Management Console optional to

produce login credentials for the new user, such as a password.

6. Choose how you want to create the Console password and then choose Next.

7. On the Set permissions page, choose Attach policies directly and click Create

policy.

8. On the Specify permissions page, choose the JSON tab.

9. Using the example below as a guide, edit the JSON policy document.

 The following is just an EXAMPLE. You must modify this JSON to match the

resources in your own environment.

CloudWatch policy - IAM Role - same AWS account

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
}

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams",
                "logs:GetLogEvents",
                "logs:FilterLogEvents"
            ],
            "Resource": "arn:aws:logs:us-west-2:001xxxxxx433:log-
group:vpc-flow:*"
        }
    ]

10. Click Next.

11. Give your policy a name to associate it with Stellar Cyber, then choose Create policy.

12. Note that in the example policy above, vpc-flow is the AWS CloudWatch log group

name. To find your log group name, see Identifying AWS CloudWatch Log Groups.

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

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::001xxxxxx433:user/jzhang-
connector"
            },
            "Action": "sts:AssumeRole"
        }
    ]

4. Click Next.

5. On the Add permissions page, select the permissions policy created earlier.

6. Click Next.

7. On the Name, review, and create page, enter a Role name.

8. Review the trusted entities and permissions, then click Create Role.

9. On the Roles page, use the Search box to find your role name.

10. Click your role name.

11. Copy your ARN, which you will need when configuring the connector in Stellar Cyber.

(Optional) Creating an IAM Role Across AWS Accounts
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

CloudWatch policy - IAM Role - across AWS accounts

1
2
3
4
5
6
7
8

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole"
            ],

9
10
11
12
13
14

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

CloudWatch policy - IAM Role - allow destination AWS account

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
}

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "sts:AssumeRole"
            ],
            "Resource": [
                "arn:aws:iam::578xxxxxx273:role/Stellar-cloudwatch-
role"
            ]
        }
    ]

11. Click Next.

12. Give your policy a name to associate it with Stellar Cyber, then choose Create policy.

13. To find your log group name, see Identifying AWS CloudWatch Log Groups.

(Optional) Create an IAM User for Destination AWS Account and Create
IAM Policy

Create this IAM user if you have a destination AWS account like an MSSP's tenant AWS
account.

When configuring the connector in Stellar Cyber, you will need the destination AWS account
(MSSP's tenant account), the IAM role ARN, as well as the CloudWatch log group name.

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

CloudWatch policy - Stellar-cloudwatch-policy

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

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams",
                "logs:GetLogEvents",
                "logs:FilterLogEvents"
            ],
            "Resource": "arn:aws:logs:us-west-2:578xxxxxx273:log-
group:System:*:*"
        }
    ]
}

10. Click Next.

11. Give your policy a name to associate it with Stellar Cyber, then choose Create policy.

12. To find your log group name, see Identifying AWS CloudWatch Log Groups.

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
}

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": {
                "AWS": "arn:aws:iam::001xxxxxx433:user/jzhang-
connector"
            },
            "Action": "sts:AssumeRole"
        }
    ]

4. Click Next.

5. On the Add permissions page, select the permissions policy created earlier.

6. Click Next.

7. On the Name, review, and create page, enter a Role name.

8. Review the trusted entities and permissions, then click Create Role.

9. On the Roles page, use the Search box to find your role name.

10. Click your role name.

11. Copy your ARN, which you will need when configuring the connector in Stellar Cyber.

Adding the Connector in Stellar Cyber
With the credential and log information available, you can now add the AWS CloudWatch
connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose PaaS from the Category dropdown.

5. Choose AWS CloudWatch from the Type dropdown.

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

14. Enter the Log Group(s) as named in your AWS CloudWatch console. To enter multiple

log group names, press Enter after each name.

 If you want to enter Log Stream(s) in the optional step below, you can only enter

one Log Group in this step.

15. (Optional) Enter the Log Stream(s). Provide a list of log stream(s) that correspond to
the provided log group. To enter multiple log stream names, press Enter after each
name. If log streams are not specifically listed, every log stream within the provided log
group is automatically searched.

16. (Optional) Click the checkmark for VPC Flow Logs if you are collecting VPC flow logs.

17. Choose the Interval (min). This is how often the logs are collected.

18. Click Next. The final confirmation tab appears.

19. Click Submit.

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

Did you configure the connector correctly?

Request

connector configuration.

401

Unauthorize

d

This error occurs when an authentication credential is

Did you enter your credentials correctly?

invalid or when a user does not have sufficient

privileges to access a specific API.

Are your credentials expired?

403

Forbidden

This error occurs when the permission or scope is not

correct in a valid credential.

Are your credentials entitled or licensed for that

specific resource?

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

HTTP E

HTTP Stan

rror

dard Error

Explanation

Recommendation

Code

Name

If this occurs unexpectedly or too often, work with

your API provider to investigate the server limits,

user licensing, or quotas.

For a full list of codes, refer to HTTP response status codes .

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices for the type of content you collected:

Change the Indices to Syslog.

For VPC flow logs only, change the Indices to Traffic.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

