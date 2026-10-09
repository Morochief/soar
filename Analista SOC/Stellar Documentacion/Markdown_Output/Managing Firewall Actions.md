Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Managing Firewall Actions

The Automation | Action History | Firewall Actions tab displays the firewall actions taken
manually from the Event Display or automatically by Automated Threat Hunting. The rules
pushed from Stellar Cyber can tell the firewall to block network traffic that is suspected (or
proved) to be a security breach. The rules can be temporary or permanent. This page displays
the firewall actions taken by Stellar Cyber and allows you to add and revert actions.

Firewall Actions Table
The Firewall Actions table displays up to 1000 firewall actions by default.

The Status can be one of the following:

Waiting – The action is queued. This normally takes less than a minute.
In Progress – The action is being communicated to the firewall.
Succeeded – The action was successfully implemented on the firewall.
Failed – The action failed.
Expiring – The action is being removed from the firewall.
Expired – The action is no longer active.

You can view status details in the Status Message.

On the Firewall Actions table you can take these actions:

Create to add a new firewall action.
Revert to revert the action.

 Stellar Cyber does not automatically delete rules when they expire. Sort the table by

execution time to see which rules are in effect and which can be reverted.

See the Tables page for more information on working with tables.

Adding a Firewall Action

To add a firewall action:

1. Select the Create button.

The ADD FIREWALL ACTION screen appears.

2. Choose a Firewall Name from the drop-down list.

The list contains all firewalls configured in your Stellar Cyber Platform. If you don't see a
firewall you need, add the firewall to Stellar Cyber.

3. Choose an Action.

Add – Adds the rule to the firewall

Remove – Removes the rule from the firewall

4. Enter the IP Address affected by the rule.

5. Choose the Direction.

6. Set the Duration.

You can choose any number of Minutes, Hours, Days, or Forever.

7. Select Submit.

The action goes into effect immediately and appears in the Firewall Actions table.

You can also add firewall actions from the Event Display.

Reverting a Firewall Action
To disable a firewall action, select the Revert button.

A new row for the rule is added to the table, with the action of Removed. The progress of the
rule update to the firewall is reported in the Status column. Use the Refresh button to monitor
progress. A Status Message of Successfully unblocked IP <address> is reported when the
rule update is completed.

 You cannot revert (or edit) a failed action. If the action failed, you must recreate the action.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

