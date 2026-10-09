Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Credential Management

The System | INTEGRATIONS | Credential Management page lets you configure third-party
credentials that the Stellar Cyber Platform uses for threat enrichment. For phishing email triage
and Alert Auto Triage, the primary use is to enable optional integration with VirusTotal, a widely
used threat intelligence provider.

 The automatic triage of user-reported phishing is only supported on Stellar Cyber in SaaS
deployments and requires an add-on license, which you can request from your sales
representative. If you used this feature through participation in the Early Access Program,
contact your sales representative to continue with an add-on license or to request that the
service be disabled.

When a credential for VirusTotal is configured and assigned to a tenant, the platform uses it to
query the VirusTotal Premium API during triage. This enhances observables—such as URLs,
domains, and attachments—with additional context, increasing the accuracy and confidence of
threat assessments.

 A VirusTotal Premium API account is required. Free-tier API keys are not supported for Auto

Triage enrichment.

Adding a VirusTotal Credential
To configure a new VirusTotal credential:

1. Navigate to System | INTEGRATIONS | Credential Management and select + Create.

2. On the Create Credential page that appears, select Create under VirusTotal.

This opens the Create Credential dialog box.

3. Enter the following and then select Create:

Name: Enter a unique, descriptive name for the credential. This name appears later
when selecting a VirusTotal credential in an Auto Triage configuration.

Tenant: Select the tenant to which this credential applies. If you are a super admin, you
can assign the credential to All Tenants.

API Key: Enter your VirusTotal Premium API key into this field. This key is required for
the Stellar Cyber Platform to perform external enrichment through VirusTotal.

 A VirusTotal Premium API account is required. Free-tier API keys are not

supported for Auto Triage enrichment.

The new credential appears in the Credential Management table and is available for
selection in Auto Triage configurations.

Using the Credential Management Table
The table on the Credential Management page displays all configured credentials. Each row
corresponds to one credential and includes the following columns:

Name: The user-defined name for the credential.

Vendor & App: Identifies the associated service, such as virustotal.

Tenant: Indicates which tenant (or All Tenants) is allowed to use the credential.

Created Time: Timestamp when the credential was created.

Last Modified: Timestamp of the most recent update to the credential.

Actions: Includes icons for two actions:

Edit: Opens the credential in a dialog to change the name, tenant, or API key.

Delete: Permanently removes the credential from the system.

Editing a Credential
To update a credential:

1. Select the Edit icon in the Actions column.

2. Modify the Name and API Key field values as needed.

 The Tenant field cannot be modified after the credential is created. This is by
design to ensure tenant-level isolation and integrity of access controls by
preventing credentials from being reassigned across tenant boundaries.

3. Select Save to apply changes.

All edits take effect immediately and are reflected in the Credential Management table.

Deleting a Credential
To delete a credential, select the Delete icon in the Actions column and then confirm the deletion
when prompted.

 If the credential is in use—for example, in an Auto Triage Configuration—deleting it will

interrupt threat enrichment. Assign a replacement credential first, if needed.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

