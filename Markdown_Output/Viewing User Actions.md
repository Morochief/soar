Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Viewing User Actions

The Automation | Action History | User Actions tab displays the user actions taken by Stellar
Cyber. If a user is disabled manually from the Event Display or automatically by Automated
Threat Hunting, that action appears here.

User Actions Table
The User Actions table displays up to 1000 user actions by default.

The Status can be:

Waiting – The action is queued. This should take less than a minute.
In Progress – The action is being communicated to the firewall.
Succeeded – The action was successfully implemented on the firewall.
Failed – The action failed. An Error Message relayed from the firewall provides details.
Expiring – The action is being removed from the firewall.
Expired – The action is no longer active.

You can revert some actions using the Revert button.

 You cannot revert (or edit) a failed action. If the action failed, you must recreate the action.

See the Tables page for more information on working with tables.

Create a Disable User Action
To create a Disable User action:

1. Select Create.

The DISABLE USER screen appears.

2. Choose a Connector from the drop-down list.

You can select either Active Directory or Microsoft Entra ID (formerly Azure Active
Directory) connectors.

3. Choose a Duration of either Forever or Limited.

If you choose Limited, then enter Days, Hours, and Minutes.

4. Choose a user name from the UserPrincipalName dropdown or type the name of the

user to disable.

5. Select Submit.

The request to disable a user is sent. Check the Status column in the table to see if the
request succeeded or failed. Then check the Error Message column.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

