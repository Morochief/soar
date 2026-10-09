Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Amazon Security Lake Connectors

This connector allows Stellar Cyber to ingest logs from the Amazon Security Lake and add the
records to the Stellar Cyber data lake.

Integration with Amazon Security Lake enables organizations to securely store and manage their
security data, providing real-time threat detection and response capabilities through Stellar
Cyber's advanced security analytics and machine learning algorithms.

This connector uses the standardized format for Open Cybersecurity Schema Framework
(OCSF). It supports OCSF versions 1.0.0 and 1.1.0.

The data in OCSF format, which is sent and pulled by third party vendors, is stored in the
Amazon Security Lake. This connector is a subscriber integration that pulls data from the lake.

 Stellar Cyber connectors with the Collect function (collectors) may skip collecting some data
when the ingestion volume is large, which potentially can lead to data loss. This can happen
when the processing capacity of the collector is exceeded.

Connector Overview: Amazon Security Lake

Capabilities

Collect: Yes

Respond: No

Native Alerts Mapped: No

Runs on: DP

Interval: N/A

Collected Data

Content Type

Index

Locating Records

OCSF-formatted data from
Amazon Security Lake

Syslog (default)

msg_class:

Traffic (for vpcflow)

AWS Events (for
cloudtrail)

<metadata.produ
ct.feature.name
>

Default msg_class:

Content Type

Index

Locating Records

amazon_security
_lake_log

Examples:

management_data_a
nd_insights (for
default)

vpcflow (if
metadata.product.
name is Amazon
VPC)

cloudtrail (if
metadata.product.
name is CloudTrail)

msg_origin.source:

<metadata.produ
ct.name>

Default
msg_origin.source:

amazon_security
_lake

Example:

cloudtrail (if
metadata.product.
name is Amazon
VPC)

msg_origin.vendor:

<metadata.produ
ct.vendor_name>

Example:

aws

msg_origin.category:

websecurity (for
default)

paas (for Amazon
VPC or CloudTrail)

msg_origin.processor
.type:

log_collector

msg_origin.processor
.name:

amazon_security
_lake

 This connector can have

several different

Content Type

Index

Locating Records

msg_class and
msg_origin_source
values. The values are
assigned dynamically
based on the original data
source.

Domain

N/A

Response Actions

N/A

Third Party Native Alert Integration Details

N/A

Required Credentials and Configurations

AWS Role ID, External ID, and SQS Queue URL, plus Region

Adding an Amazon Security Lake Connector
To add an Amazon Security Lake connector:

1. Obtain Amazon Security Lake credentials
2. Add the connector in Stellar Cyber
3. Test the connector
4. Verify ingestion

Obtaining Amazon Security Lake Credentials
This connector uses Amazon Simple Queue Service (SQS) queues and S3 buckets to pull data
from the Amazon Security Lake.

Follow guidance on Amazon Security Lake  documentation.

Permissions

You need the following permissions to create the SQS queue:

s3:GetBucketNotification

s3:PutBucketNotification

sqs:CreateQueue

sqs:DeleteQueue

sqs:GetQueueAttributes

sqs:GetQueueUrl

sqs:SetQueueAttributes

 When you set up data access for the Amazon Security Lake subscriber in the Enabling

Subscriber Data Access procedure, the SQS queue is automatically created.

You will also need the following permissions to perform actions:

iam:CreateRole

iam:DeleteRolePolicy

iam:GetRole

iam:PutRolePolicy

lakeformation:GrantPermissions

lakeformation:ListPermissions

lakeformation:RegisterResource

lakeformation:RevokePermissions

ram:GetResourceShareAssociations

ram:GetResourceShares

ram:UpdateResourceShare

Use IAM to verify your permissions. Review the IAM policies that are attached to your IAM
identity. Then, compare the information in those policies to the list of (permissions) actions that
you must have to notify subscribers when new data is written to the data lake.

Enabling Subscriber Data Access

To enable subscriber data access:

1. Log in as an administrative user to the Security Lake console at

https://console.aws.amazon.com/securitylake .

2. Use the AWS Region dropdown to choose a Region in which to create the subscriber.

3. Choose Subscribers.

4. Click Create subscriber.

5. For Subscriber details, enter a Subscriber name. You can also enter an optional

Description.

 The Region is automatically populated as your currently selected AWS Region. It

cannot be changed.

6. For Log and event sources, select All log and event sources.
7. For Data access method, choose S3.

8. For Subscriber credentials, enter Account Id and External Id.

The Account Id is the ID of the AWS account on which Stellar Cyber is
running.

The External Id is a unique identifier. The suggested External Id is the Stellar
Cyber tenant ID of the tenant running the connector. To find your tenant ID,
navigate to System | ORGANIZATION MANAGEMENT | Tenants and locate
it in the table.

9. For Notification details, choose SQS queue.

10. Click Create.

11. Navigate to Subscribers | Details. Copy the AWS role ID and the Subscription
endpoint. You will need them when configuring the connector in Stellar Cyber.

12. Navigate to Amazon SQS | Queues.

13. For the specific Subscription endpoint noted above, copy the SQS queue URL. You

will need it when configuring the connector in Stellar Cyber.

Adding the Connector in Stellar Cyber
With the access information handy, you can add an Amazon Security Lake connector in Stellar
Cyber:

1. Log in to Stellar Cyber.

2. Click System | INTEGRATIONS | Connectors. The Connector Overview appears.

3. Click Create and select Connector.

The General tab of the Add Connector screen appears. The information on this tab
cannot be changed after you add the connector.

4. Choose Web Security from the Category dropdown.

5. Choose Amazon Security Lake from the Type dropdown.

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

12. Enter the AWS Role ID you noted above in Obtain your Amazon Security Lake

credentials.

13. Enter the External ID you noted above.

14. Choose the Region from the available AWS regions in the dropdown.

15. Enter the SQS Queue URL you noted above.

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

2. Change the Indices depending on the type of data received:

For the default, change the Indices to Syslog.
For a msg_class of vpcflow, change the Indices to Traffic.
For a msg_class of cloudtrail, change the Indices to AWS Events.

The table immediately updates to show ingested Interflow records.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

