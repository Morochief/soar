Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Importing Assets

Stellar Cyber tracks assets in your system and analyzes their behavior to detect security events.
Stellar Cyber can discover both IP and MAC addresses and associate them with hosts. You can
also import assets from a CSV file. Stellar Cyber recommends downloading its template to use
so that the formatting of the file is correct. Stellar Cyber merges your imported data with the
discovered asset information. Imported data takes priority over discovered data but will not be
deleted if there's no matching imported field. When you import another CSV of assets, Stellar
Cyber adds new assets to previously imported assets and updates matching records. Stellar
Cyber does not delete records.

You can do the following:

Get and edit the template
Import assets
Clear imported assets
Download imported assets

Getting and Editing the Asset Import Template
To get the asset import template:

1. Select Assets | Asset Analytics.

The assets dashboard appears.

2. Select Asset Imports.

The most recent asset imports appear.

3. Select Import Assets.

The Import Assets dialog appears.

4. Select Download Template.

Stellar Cyber recommends using its template so that the formatting of the file is correct.

Depending on your browser and system, the file is either immediately downloaded to
your Downloads folder or you are prompted for a location. You can now edit the
template to add up to 10,000 assets.

Importing Assets
Assets are imported from a CSV file. To import assets:

1. Select Assets | Asset Analytics.

The assets dashboard appears.

2. Select Asset Imports.

The most recent asset imports appear.

3. Select Import Assets.

The Import Assets dialog box appears.

4. Choose a tenant.

5. Select Choose File, navigate to the file you want to import, select it, and then select

Open.

Stellar Cyber checks the file to make sure the hostname, ip, and mac fields are
included and that no reserved fields (such as vlan, risk_score, and vuln_score)
were added. If the file is valid, the Import button activates.

6. Select Import.

A Task List panel pops up showing the progress of the import until it finishes.

7. When the import operations completes, see the import details by selecting Show

Report.

Imported assets list CSV as a Data Source on the Asset Details page.

You can remove any columns you want except these (and at least one of them must a
value):

hostname
ip
mac

To add additional information, simply add a new column with the exact metadata field as
the column heading. Some metadata fields (such as vlan, risk_score, and
vuln_score) cannot be overwritten, so if you include these in your CSV file, you cannot
upload your file.

Clearing Imported Assets
You can clear (that is, delete) asset information that you imported. If the imported data was
merged with discovered data, only the imported data is cleared. To clear all imported assets:

1. Select Assets | Asset Analytics.

The assets dashboard appears.

2. Select Asset Imports.

The most recent asset imports appear.

3. Select Clear Imported Assets.

The Asset Deletion Confirmation appears.

4. Choose a specific tenant or All Tenants and then select Yes.

A Task List panel pops up showing the progress of the deletion until it finishes.

Downloading Imported Assets
To download imported assets:

1. Select Assets | Asset Analytics.

The assets dashboard appears.

2. Select Asset Imports.

The most recent asset imports appear.

3. Select Download for the import you'd like to download.

The download dialog appears.

4. Choose a location to download the imported assets to and then Save.

A Task List panel pops up showing the progress of the download until it finishes.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

