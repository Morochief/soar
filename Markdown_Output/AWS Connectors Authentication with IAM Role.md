Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

AWS Connectors Authentication with IAM Role

The Stellar Cyber AWS connectors support the IAM Role authentication method, which is also
referred to as assume role or IAM role assume.

This authentication method temporarily takes on a set of credentials used to access AWS
resources. The temporary credentials can be used to make API calls to any AWS service. The
role is created with two policies: a role trust policy that specifies who can assume the role and a
permissions policy that specifies what the role can do.

For example, when configuring the AWS CloudWatch connector, you select IAM Role and then
configure the fields associated with the role.

The following Stellar Cyber connectors support the IAM Role Auth Method:

Generic S3

AWS CloudWatch

AWS GuardDuty

AWS CloudTrail

AWS Inspector

Amazon Security Lake (this connector only supports assume role authentication where
Stellar Cyber maintains the account that assumes the provided role)

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

