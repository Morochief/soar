Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Generic S3 Connectors

This connector allows Stellar Cyber to pull data sent to S3 and add the records to the data lake.

The Generic S3 connector uses Amazon Simple Queue Service (SQS) queues and S3 buckets
to pull data. The SQS queue gets information about newly added S3 objects. Stellar Cyber reads
from the queue to get information about the S3 bucket and key for the newly added files. When
there is a new upload, notifications are sent to the SQS queue URL.

This is a generic S3 connector that can support a wide-range of data sources. Sample sources
are included with this connector but new sources can also be added. This requires some
additional information to be configured and uploaded for each new source from which you want
to pull data. Contact Stellar Cyber Customer Support to assist with this.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Generic S3

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: Yes*

Runs on: DP

Interval: 5 minutes (if there is no data) or, reads notifications from the SQS queue (if there is
data)

Collected Data

Content Type

Index

Locating Records

N/A

(collects all data in the provided SQS
Queue URL)

Syslog (for
CrowdStrike
(JSON), Fortinet
Lacework CNAPP

msg_class:

generic_s3_cloudt
rail (for

Content Type

Index

Locating Records

(JSON), Generic
(JSON), Proofpoint
(JSON), Teleport
(JSON), Cato
Networks (JSON),
and AWS Config
(JSON))

AWS Events (for
AWS CloudTrail
(JSON))

Assets (for Fortinet
Lacework CNAPP
(JSON)
machine_details
file type)

Traffic (for Cato
Networks (JSON))

IDPS/Malware
Sandbox Events
(for Cato Networks
(JSON))

AWS CloudTrail
(JSON))

generic_s3_crowds
trike_log (for
CrowdStrike (JSON))

generic_s3_fortin
et_lacework_<file
_type> for example,
generic_s3_fortin
et_lacework_alert
_details (for
Fortinet Lacework
CNAPP (JSON))

generic_s3_log (for
Generic (JSON))

generic_s3_proofp
oint_log (for
Proofpoint (JSON))

generic_s3_telepo
rt_log (for Teleport
(JSON))

cato_generic_s3
(for Cato Networks
(JSON))

generic_s3_aws_co
nfig (for
AWS Config (JSON))

msg_origin.source:

s3 (for AWS
CloudTrail (JSON),
CrowdStrike (JSON),
Fortinet Lacework
CNAPP (JSON),
Generic (JSON),
Proofpoint (JSON),
Teleport (JSON), and
AWS Config (JSON))

cato_networks (for
Cato Networks
(JSON))

msg_origin.vendor:

aws (for
AWS CloudTrail
(JSON), Generic
(JSON), and
AWS Config (JSON))

crowdstrike (for
CrowdStrike (JSON))

fortinet (for
Fortinet Lacework

Content Type

Index

Locating Records

CNAPP (JSON))

proofpoint (for
Proofpoint (JSON))

teleport (for
Teleport (JSON))

cato_networks (for
Cato Networks
(JSON))

msg_origin.category:

paas (for
AWS CloudTrail
(JSON), CrowdStrike
(JSON), Generic
(JSON), Proofpoint
(JSON), Teleport
(JSON), and
AWS Config (JSON))

cloudsec (for
Fortinet Lacework
CNAPP (JSON))

sase (for Cato
Networks (JSON))

Domain

<SQS Queue URL>

where <SQS Queue URL> is a variable from the configuration of this connector

Response Actions

N/A

Third Party Native Alert Integration Details

*For Fortinet Lacework

This connector pulls data sent to S3 for Fortinet Lacework to get the raw alerts that are stored in the
Syslog index.

Stellar Cyber maps Fortinet Lacework alerts. The alerts are read from the Syslog index, enriched with
Stellar Cyber fields, and mapped (with deduplication) to the Alerts index.

Deduplication is by tenantid and fortinet_lacework.EVENT_ID.

For details, see Integration of Third Party Native Alerts.

Required Credentials and Configurations

For Access Key / Secret Key Auth Method: Access Key and Secret Key, plus Region,
SQS Queue URL, File Type, and Log Source

For IAM Role Auth Method: Source Account Access Key, Source Account Secret Key, and IAM
Role ARN, plus Region, SQS Queue URL, File Type, and Log Source

Locating Records

To search the alerts in the Alerts index or the Original Records in the Syslog index, use the
query: msg_class: generic_s3_fortinet_lacework_alert_details AND _exists_:
event.threat.name

Adding a Generic S3 Connector
To add a Generic S3 connector:

1. Obtain credentials
2. (Optional) Creating an IAM Role Auth Method
3. Configure S3 event notifications
4. Add the connector in Stellar Cyber
5. Test the connector
6. Verify ingestion

Obtaining Credentials
To obtain the required credentials, refer to the following sections:

Permissions

Prerequisites

Configuring a Bucket for Notifications (SQS Queue)

Adding an AWS User for Stellar Cyber

Obtaining the Access Key and Secret Key

Permissions

You need the following permissions to create the SQS queue:

s3:GetBucketNotification

s3:PutBucketNotification

sqs:CreateQueue

sqs:DeleteQueue

sqs:GetQueueAttributes

sqs:GetQueueUrl

sqs:SetQueueAttributes

You also need the following permissions to perform actions:

s3:GetObject

s3:ListBucket

iam:CreateRole

iam:DeleteRolePolicy

iam:GetRole

iam:PutRolePolicy

Prerequisites

The prerequisite for the following procedure is that you are already sending data to an S3 bucket.

The S3 bucket is limited to data from only one log source.

Configuring the Bucket for Notifications (SQS Queue)

The procedures in this document are for an S3 bucket and SQS queue that are created in the
same AWS account.

Have the following information handy:

AWS account ID

S3 bucket name

In this procedure you create an SQS queue, attach an access policy to the queue, and add a
notification configuration to the bucket.

Configure only one SQS queue URL per S3 bucket.

1. Log in to the Amazon SQS console at https://console.aws.amazon.com/sqs/.

2. In the navigation pane, choose Queues.

3. Click Create queue.

a. For Type, the Standard queue type is set by default.

b. Enter a Name for your queue.

c. For Server-side encryption, Enabled is set by default.

d. For Encryption key type, Amazon SQS key (SSE-SQS) is set by default.

e. Click Create queue.

f. Note the URL. This is the SQS Queue URL, which you will need when

configuring the connector in Stellar Cyber.

g. Note the ARN. This is the SQS-queue-ARN, which you will need when

configuring the access policy in the following step.

4. Replace the access policy attached to the queue:

a. In the Amazon SQS console, in the Queues list, select the queue name.

b. Click Edit.

c. Replace the access policy attached to the queue. Provide the following:

Amazon SQS ARN you noted above

your AWS account ID for <bucket-owner-account-id>

your source S3 bucket name for <your-S3-bucket-name>

{
  "Version": "2012-10-17",
  "Id": "example-ID",
  "Statement": [
    {
      "Sid": "example-statement-ID",
      "Effect": "Allow",
      "Principal": {
        "Service": "s3.amazonaws.com"
      },
      "Action": "SQS:SendMessage",
      "Resource": "arn:aws:sqs:<aws-region:account-id:queue-name>",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "<bucket-owner-account-id>"
        },
        "ArnLike": {
          "aws:SourceArn": "arn:aws:s3:::<your-S3-bucket-name>"
        }
      }
    }
  ]
}

d. Click Save.

5. Add a notification configuration to your bucket.

a. In the Amazon S3 Buckets console, locate your S3 bucket.

b. Double-click your bucket name.

c. Click the Properties tab.

d. Scroll down to Event notifications and click Create event notification.

e. Enter an Event name.

f. For Event types, select All object create events.

g. Scroll down to Destination:

For Destination, select SQS queue.

For Specify SQS queue, select Enter SQS queue ARN.

For SQS queue, enter the ARN.

h. Click Save changes.

Adding an AWS User for Stellar Cyber

Create an IAM user in the same AWS account as the SQS queue. You will need the SQS-queue-
ARN you noted above for the policy.

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

Generic S3 policy

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
25
26
27

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "sqs:DeleteMessage",
                "sqs:ReceiveMessage"
            ],
            "Resource": [
                "arn:aws:sqs:<aws-region:account-id:queue-name>"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::<your-S3-bucket-name>",
                "arn:aws:s3:::<your-S3-bucket-name>/*"
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

Obtaining the Access Key and Secret Key

To obtain the access key and secret key:

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

(Optional) Creating an IAM Role Auth Method
The procedures in this section are required for users who want to use the IAM Role Auth Method
for the AWS resources.

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

Stellar-SQS-policy

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
25
26
27
28

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "sqs:DeleteMessage",
                "sqs:ReceiveMessage"
            ],
            "Resource": [
                "<SQS ARN>"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "<S3 BUCKET ARN",
                "<S3 BUCKET ARN>/*"
            ]
        }
    ]
}

10. Give your policy a name to associate it with Stellar Cyber, for example, Stellar-SQS-

policy.

11. Click Create policy.

Create an IAM Role with Trusted Entities

1. From the IAM navigation pane, choose Roles and then click Create Role.

2. Choose Custom trust policy.

3. Using the example below as a guide, edit the custom trust policy document.

 The following is just an EXAMPLE. You must modify this JSON to match the

resources in your own environment.

Trusted entities

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

Configuring S3 Event Notifications
You can check the S3 bucket event notification configuration to ensure that only object creation
events are being sent to the SQS queue. This can be done either by creating a new event
notification or by modifying an existing one to include only the appropriate event types.

If an object delete event is sent to the SQS queue, rather than an object create event, the result
could be a 404 error when you attempt to retrieve the file.

To configure only object creation events for S3 bucket event notification for the Generic S3
connector:

1. Go to the S3 bucket in the AWS Console.

2. Navigate to the Properties tab.

3. Scroll to Event notifications.

4. Either create a new event notification or edit an existing one.

5. For Event types, select All object create events only.

6. For Destination, choose SQS Queue and then select your queue.

7. Click Save.

Adding the Connector in Stellar Cyber
With the access information handy, you can add a Generic S3 connector in Stellar Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose PaaS from the Category dropdown.

5. Choose Generic S3 from the Type dropdown.

The asterisk (*) indicates a required field.

6. For this connector, the supported Function is Collect, which is enabled already.

7. Enter a Name.



Notes:

This field does not accept multibyte characters.
It is recommended that you follow a naming convention such as
tenantname-connectortype.

8. Choose a Tenant Name. This identifies which tenant is allowed to use the connector.

9. Choose the device on which to run the connector.

10. (Optional) When the Function is Collect, you can apply Log Filters. For information,

see Managing Log Filters.

11. Click Next. The Configuration tab appears.

The asterisk (*) indicates a required field.

12. Choose the Auth Method to use Access Key / Secret Key or IAM Role.

For Access Key / Secret Key Auth Method:

a. Enter the Access Key you noted above in Obtaining the Access Key and

Secret Key.

b. Enter the Secret Key you noted above.

For IAM Role Auth Method:

The asterisk (*) indicates a required field.

a. Enter the Source Account Access Key.

b. Enter the Source Account Secret Key.

c. Enter the IAM Role ARN you noted above in (Optional) Creating an IAM Role

Auth Method.

13. Choose the Region from the available AWS regions in the dropdown.

14. Enter the SQS Queue URL you noted above. It has the following format:

https://<aws-region>.amazonaws.com/<account-id>/<queue-name>

15. Choose the File Type. This refers to the specific data within the S3 object. The
supported file types are gzip and text. The only supported format is JSON. For
example, if the File Type is text, the file must contain a properly formatted JSON object
and have a .json extension.

 The SQS queue should only get data in the selected format. Mixed gzip and raw
JSON files will cause issues for the connector, regardless of the log source.

16. (Optional) If the specified File Type contains multiple JSON objects in the file, select the
Multiple Logs per File checkbox. For example, if there are multiple JSON objects in
the file, one per line, with each line being a single JSON object, then select this
checkbox. Your file contents will look like this:

Do not select this checkbox if there is only a single JSON object in the file and your file
contents looks like this:

17. Choose the Log Source. The supported log sources are:

AWS Config (JSON)

AWS CloudTrail (JSON)

Cato Networks (JSON)

CrowdStrike (JSON)

Fortinet Lacework CNAPP (JSON)
Application Protection Platform)

 (CNAPP is the Cloud-Native

Generic (JSON)

Proofpoint (JSON)

Teleport (JSON)

Only one log source can be configured per connector.

 In addition, there may be other Log Sources listed in this dropdown menu. Contact
the Stellar Cyber Customer Support team if you have a log source you want added.

18. Click Next. The final confirmation tab appears.

19. Click Submit.

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

If this occurs unexpectedly or too often, work with

your API provider to investigate the server limits,

user licensing, or quotas.

For a full list of codes, refer to HTTP response status codes .

Verifying Ingestion
To verify ingestion:

1. Select Threat Hunting.

The Interflow Search tab appears.

2. Change the Indices for the type of log source:

Change the Indices to Syslog.

For AWS CloudTrail (JSON) only, change the Indices to AWS Events.

For Fortinet Lacework CNAPP (JSON) only, change the Indices to Assets
(msg_class: generic_s3_fortinet_lacework_machine_details).

For Cato Networks only, change the Indices to Traffic.

For Cato Networks only, change the Indices to IDPS/Malware Sandbox
Events.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

