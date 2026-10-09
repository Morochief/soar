Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Viewing Endpoint Actions

The Automation | Action History | Endpoint Actions tab displays the endpoint actions taken
manually from the Event Display or automatically by Automated Threat Hunting. In the example
below, the Status column will show that the action failed, for example, if the selected device is
not registered (see the Error Message column) with the selected connector.

Endpoint Actions Table
The Endpoint Actions table displays up to 1000 endpoint actions by default.

See the Tables page for more information on working with tables.

The Status can be:

Waiting—The action is queued. This should take less than a minute.

In Progress—The action is being communicated to the connector.

Succeeded—The action was successfully implemented.

Failed—The action failed. An Error Message relayed from the connector provides
details.

Expiring—The action is being removed from the connector.

Expired—The action is no longer active.

You can revert some actions:

If the host was contained, you can click Revert to lift the containment from a host. This
triggers a new endpoint action Lift Containment to appear in the table.

If the host has a Lift Containment, you can click Revert. This triggers a new endpoint
action Contain Host to appear in the table.

If the host was hidden, you can click Revert to unhide a hidden host.

If the host was disconnected, you can click Revert to reconnect the host to the network.

 You cannot revert (or edit) a failed action. If the action failed, you must recreate the action.

 Depending on the originating connector, you may be able to revert a host containment from
Stellar Cyber. If this is supported, a Revert button is displayed in the row for the containment
action of the Automation | Action History | Endpoint Actions table. For supported connectors,
using Revert triggers a Lift Containment action that is displayed in the same table. If the
API for the managing service does not support a revert option then you need to use that
product's UI to manage the host state.

 Blackberry Cylance connector's Contain Host action automatically expires upon the

requested duration but this action is not reported back to Stellar Cyber. The Endpoint Actions
table reports that the containment was successful, but not expired.

 If you use a Cynet connector to perform a response action on a host that is not in your Cynet
list of hosts, the Automation | Action History | Endpoint Actions row for the action will indicate
that with an error message such as: The remote server returned an
error: (422) Unprocessable Entity.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

