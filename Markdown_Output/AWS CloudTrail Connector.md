Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring AWS CloudTrail Connectors

This connector allows Stellar Cyber to collect data from external sources and add the records to
the data lake. The incoming information is included in Interflow records in the AWS Events
index.

Integration with AWS and S3 enables organizations to securely store and manage their data
while providing real-time threat detection and response capabilities through Stellar Cyber's
advanced security analytics and machine learning algorithms.

You can have any number of AWS connectors active in the system. You will typically have one or
two connectors for each account being used by anyone in the network.

However, if you have AWS Control Tower  set up, you can use an asterisk as a wildcard
character instead of a specific Account ID in the Prefix field. You can also use wildcards in
Advanced Prefix.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: AWS CloudTrail

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: 5 minutes

Collected Data

Content Type

Index

cloudtrail

AWS Events (non-traffic)

Locating
Records

msg
_cla

Content Type

Index

Locating
Records

vpcflow

waf

Traffic (VPC flow)

Domain

https://s3.amazonaws.com

https://s3-<Region>.amazonaws.com

https://<Bucket>.s3.amazonaws.com

ss:

clo
udt
rai
l

vpc
flo
w

aws
_wa
f

msg
_orig
in.so
urce:

clo
udt
rai
l

aws_
waf
(for
aws
_waf
)

msg
_orig
in.ve
ndor:

aws

msg
_orig
in.ca
tegor
y:

paa
s

waf
(for
aws
_waf
)

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

For Access Key / Secret Key Auth Method: Access Key, Secret Key, Sub Type, Bucket, plus
Prefix type (Prefix or Advanced Prefix), and File Type

For IAM Role Auth Method: Source Account Access Key, Source Account Secret Key, IAM Role
ARN, Sub Type, Bucket, plus Prefix type (Prefix or Advanced Prefix), and File Type

Adding an AWS CloudTrail Connector
To add an AWS CloudTrail connector:

1. Create an AWS CloudTrail trail
2. Add a user with the appropriate permissions
3. Create an access key
4. (Optional) Create an IAM role in same AWS account
5. (Optional) Create an IAM role across AWS accounts
6. Get the required information
7. (Optional) Set up AWS Control Tower
8. Add the connector in Stellar Cyber
9. Test the connector

10. Verify ingestion

Creating the AWS CloudTrail Trail
To create an AWS CloudTrail trail:

 Use our example as a guideline, as you might be using a different software version.

1. Log in to your AWS Management Console at https://aws.amazon.com  .

2. In Find Services, start entering cloudtrail. As you type, suggestions appear. Click on

CloudTrail.

The CloudTrail Dashboard appears.

3. Click Create trail. The Choose trail attributes page appears.

4. Enter a Trail name.
5. Leave the default configurations for the various event information settings.
6. Under Storage location, choose Yes for Create a new S3 bucket.

7. Enter the name.

Make note of this, as you need the bucket name when configuring the connector in
Stellar Cyber.

8. Enter the AWS KMS alias.
9. Leave the remaining options at the default settings.

10. Click Next. The Choose log events page appears.

11. Choose the events you want to send to Stellar Cyber. We recommend choosing all of

them.

12. Click Next. The Review and create page appears.
13. Click Create trail. The trail is added, and displayed on the Trails page.

Adding a User with the Appropriate Permissions
To add a user with the appropriate permissions:

1. Log in to your AWS Management Console at https://aws.amazon.com/console .

View the services in the Console Home or choose View all services.

2. Choose IAM. The IAM Dashboard appears.

3. Choose Policies and then choose Create Policy.

4. In the Create policy pane, choose the JSON tab.

5. Using the example below as a guide, edit the JSON policy document.

 The following is just an EXAMPLE. You must modify this JSON to match the

resources in your own environment.

CloudTrail policy

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

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::stellarcybercloudtrail",
                "arn:aws:s3:::stellarcybercloudtrail/*"
            ]
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

In the following example, aws-cloudtrail-logs-001xxxxxx433-f361378d is the S3
bucket to store the AWS CloudTrail data.

CloudTrail policy - IAM Role - same AWS account

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

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::aws-cloudtrail-logs-001xxxxxx433-
f361378d",
                "arn:aws:s3:::aws-cloudtrail-logs-001xxxxxx433-
f361378d/*"
            ]
        }

    ]
}

10. Click Next.

11. Give your policy a name to associate it with Stellar Cyber, for example, Stellar-

cloudtrail-policy.

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
5
6
7
8
9
10
11
12
13

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": {
                "AWS": "<User ARN>"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

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

CloudTrail policy - IAM Role - across AWS accounts

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

CloudTrail policy - IAM Role - allow destination AWS account

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
                "arn:aws:iam::001xxxxxx433:role/Stellar-cloudtrail-
role"
            ]
        }
    ]

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

In the following example, aws-cloudtrail-logs-001xxxxxx433-f361378d is the S3
bucket to store the AWS CloudTrail data.

CloudTrail policy - Stellar-cloudtrail-policy

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
}

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::aws-cloudtrail-logs-001xxxxxx433-
f361378d",
                "arn:aws:s3:::aws-cloudtrail-logs-001xxxxxx433-
f361378d/*"
            ]
        }
    ]

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
            "Sid": "Statement1",
            "Effect": "Allow",
            "Principal": {
                "AWS": "<User ARN>"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}

4. Click Next.

5. On the Add permissions page, select the permissions policy created earlier.

6. Click Next.

7. On the Name, review, and create page, enter a Role name.

8. Review the trusted entities and permissions, then click Create Role.

9. On the Roles page, use the Search box to find your role name.

10. Click your role name.

11. Copy your ARN, which you will need when configuring the connector in Stellar Cyber.

Getting the Required Information
To add the connector in Stellar Cyber you need the following for the Access Key / Secret Key
Auth Method:

Access key and Secret Access key—See Creating an Access Key
Bucket—See Creating the AWS CloudTrail Trail
Prefix—See Getting the Prefix

To add the connector in Stellar Cyber you need the following for the IAM Role Auth Method:

Source Account Access Key, Source Account Secret Key, and Bucket—See
(Optional) Create an IAM role in same AWS account or (Optional) Create an IAM role
across AWS accounts
Prefix—See Getting the Prefix

Getting the Prefix

To get the prefix:

1. In the CloudTrail Dashboard, click Trails. The existing trails appear.

2. For the trail you are using, the Bucket is the name in the S3 bucket column.

3. Click the bucket name. The bucket info appears.

4. Click the CloudTrail object.

The regional objects appear.

5. Click your region.

6. Click Copy S3 URI. The Prefix is the path starting with AWSLogs (the default) and

ending with the region.

 Do not copy the trailing "/" symbol.

If you're configuring an AWS WAF connector and you have a custom prefix  , use
your custom prefix. If you are using a date in your custom prefix, you must replace static
numbers with variables, converting the prefix to a pattern that Stellar Cyber can
recognize. Following are the variables.

Variable

//YYYY//

//m//

//mm//

//d//

//dd//

//H//

//HH//

//M//

//MM//

Definition

4 digit year

1 or 2 digit month

2 digit month

1 or 2 digit day

2 digit day

1 or 2 digit hour

2 digit hour

1 or 2 digit minute

2 digit minute

For example, CustomPrefix/year=/2020/month=/10/day=/27/ becomes
CustomPrefix/year=///YYYY///month=///mm///day=///dd//.

For the CloudTrail connector, the supported prefix syntax may also include Organization ID, as
shown here:

Without Organization ID:

optional_prefix_name/AWSLogs/Account ID/<CloudTrail>/region

optional_prefix_name/AWSLogs/Account ID/<vpcflowlogs>/region

With Organization ID:

optional_prefix_name/AWSLogs/OU-ID/Account
ID/<CloudTrail>/region

optional_prefix_name/AWSLogs/OU-ID/Account
ID/<vpcflowlogs>/region

(Optional) Setting up AWS Control Tower

There are two types of AWS Control Tower: SSE-S3 encryption (default) and SSE-KMS
encryption.

To set up the default AWS Control Tower (SSE-S3 encryption), refer to the AWS Control Tower
documentation .

To set up the AWS Control Tower with SSE-KMS encryption, follow these procedures:

Create symmetric encryption KMS keys

Set up the AWS Control Tower on your management account

Create an IAM User

Creating Symmetric Encryption KMS Keys

To create symmetric encryption KMS keys:

1. Log in to your management account (YOUR-MANAGEMENT-ACCOUNT).

2. Follow the guidance in the AWS documentation  to create your KMS key (YOUR-

KMS-KEY-ID).

3. Using the example below as a guide, edit the JSON policy document.

 The following is just an EXAMPLE. You must modify this JSON to match the

resources in your own environment.

Policy

{
    "Version": "2012-10-17",
    "Id": "CustomKMSPolicy",
    "Statement": [
        {
        ... YOUR-EXISTING-POLICIES ...
        },
        {
            "Sid": "Allow Config to use KMS for encryption",
            "Effect": "Allow",
            "Principal": {
                "Service": "config.amazonaws.com"
            },
            "Action": [
                "kms:Decrypt",
                "kms:GenerateDataKey"
            ],
            "Resource": "arn:aws:kms:YOUR-HOME-REGION:YOUR-MANAGEMENT-
ACCOUNT-ID:key/YOUR-KMS-KEY-ID"
        },
        {
            "Sid": "Allow CloudTrail to use KMS for encryption",
            "Effect": "Allow",
            "Principal": {
                "Service": "cloudtrail.amazonaws.com"
            },
            "Action": [
                "kms:GenerateDataKey*",
                "kms:Decrypt"
              ],
            "Resource": "arn:aws:kms:YOUR-HOME-REGION:YOUR-MANAGEMENT-
ACCOUNT-ID:key/YOUR-KMS-KEY-ID",
            "Condition": {
                "StringEquals": {
                    "aws:SourceArn": "arn:aws:cloudtrail:YOUR-HOME-
REGION:YOUR-MANAGEMENT-ACCOUNT-ID:trail/aws-controltower-BaselineCloudTrail"
                },
                "StringLike": {
                    "kms:EncryptionContext:aws:cloudtrail:arn":
"arn:aws:cloudtrail:*:YOUR-MANAGEMENT-ACCOUNT-ID:trail/*"
                }
            }

        },
        {
            "Sid": "Allow user to use KMS for encryption",
            "Effect": "Allow",
            "Principal": {
                "AWS": "<user ARN>"
            },
            "Action": "kms:Decrypt",
            "Resource": "arn:aws:kms:YOUR-HOME-REGION:YOUR-MANAGEMENT-
ACCOUNT-ID:key/YOUR-KMS-KEY-ID"
        }
    ]
}

4. In various places in the JSON policy document, provide the following:

YOUR-HOME-REGION

YOUR-MANAGEMENT-ACCOUNT-ID

YOUR-KMS-KEY-ID

<user ARN> (the user that will be used for the connector)

Setting up the AWS Control Tower on your Management Account

You can now set up the AWS Control Tower on your management account with the KMS key you
created earlier.

1. Log in to AWS CloudTrail with your AWS account (YOUR-MANAGEMENT-ACCOUNT).

2. Follow the guidance in the following documentation  to deploy a landing zone with

AWS Control Tower.

3. In the following graphic, YOUR-MANAGEMENT-ACCOUNT ends in 4429. The
CloudTrail S3 bucket is in the 9809 AWS account (the Log-archive account).

Creating an IAM User

Next, create an IAM user. You can refer to Adding a User with the Appropriate Permissions.

1. Log into the Log-archive account (9809).

2. Using the example below as a guide, edit the JSON policy document.

 The following is just an EXAMPLE. You must modify this JSON to match the

resources in your own environment.

Policy for the user

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket",

            ],
            "Resource": [
                "<S3 bucket ARN>",
                "<S3 bucket ARN>/*"
            ]
        },
        {
            "Sid": "KMSDecryptionPermission",
            "Effect": "Allow",
            "Action": [
                "kms:Decrypt"
            ],
            "Resource": [
                "arn:aws:kms:YOUR-HOME-REGION:YOUR-MANAGEMENT-ACCOUNT-
ID:key/YOUR-KMS-KEY-ID"
            ]
        }
    ]
}

3. In the JSON policy document, provide the following:

YOUR-HOME-REGION

YOUR-MANAGEMENT-ACCOUNT-ID

YOUR-KMS-KEY-ID

<S3 bucket ARN>

4. Generate the access key and security key for this user. You can refer to Creating an

Access Key.

Adding the Connector in Stellar Cyber
With the required information handy, you can add the AWS CloudTrail connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose PaaS from the Category dropdown.

5. Choose AWS Cloudtrail from the Type dropdown.

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

a. Enter the Access Key from IAM.

b. Enter the Secret Key from IAM.

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

c. Enter the IAM Role ARN.

13. Choose a Sub Type.

cloudtrail—feeds account activity information, including actions taken through
the AWS Management Console and various AWS SDKs and command line
tools. See the AWS CloudTrail   documentation for details.

vpcflow—provides network-level information. See the AWS VPC  
documentation for details.

waf—provides Web Application Firewall information. See the AWS WAF  
documentation for details.

14. (Optional) Enter the Proxy URI, if you have one.

15. Enter the Bucket you noted above.

16. Choose a Prefix type (Prefix or Advanced Prefix).

For Prefix, ensure the Prefix does not include a trailing "/" symbol.

The supported prefix syntax is as follows:

Without Organization ID: optional_prefix_name/AWSLogs/Account
ID/<CloudTrail or vpcflowlogs>/region

With Organization ID: optional_prefix_name/AWSLogs/OU-ID/Account
ID/<CloudTrail or vpcflowlogs>/region

With AWS Control Tower: optional_prefix_name/OU-ID/AWSLogs/OU-
ID/*/<CloudTrail or vpcflowlogs>/region

 The Sub Type must be cloudtrail or vpcflow.

For Advanced Prefix, wildcard characters are supported in any prefix format. But use
caution as this may cause performance issues. If the wildcard expression matches too
many files, this will cause the collector to examine too many files. It is better to have the
format expression as specific as possible in order to limit the number of files examined.

 Examples of advanced prefixes are:

AWSLogs/Account ID/vpcflowlogs/us-west-2/2025/05/11/*.gz

AWSLogs/Account ID/CloudTrail/us-west-2/2025/06/*1/*

AWSLogs/Account ID/WAFLogs/us-west-2/*

 The Advanced Prefix format must be fully matching. For example,

AWSLogs/Account ID/WAFLogs/us-west-2/ is a partial match and no
files will be retrieved.

17. Enter the File Type. The cloudtrail and vpcflow sub types should always be gzip. The

waf sub type can be gzip or text.

18. (Optional) Choose a Region from the available regions in the dropdown.

19. Click Next. The final confirmation tab appears.

20. Click Submit.

The new connector is immediately active and starts collecting logs.

Testing the Connector
If you have AWS Control Tower, the Test button tests all account IDs.

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

user licensing, or quotas.

For a full list of codes, refer to HTTP response status codes .

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices to include either or both of AWS Events or Traffic.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

