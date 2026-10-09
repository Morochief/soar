Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

ATH Example: Notifications for Case Scores

Configure an Automated Threat Hunting (ATH) playbook to send email or Slack notifications
when a case exceeds a specified score threshold, enabling timely response to high-risk threats.

Background: What Your Playbook Searches For
Before you create the playbook to notify on case scores over a threshold, it's important to
understand what you're searching for. The first time a case score passes the threshold of 50,
Stellar Cyber creates a special document in the aella-syslog index with a msg_class of
incident_score_change. This is the document your playbook searches for so that it can send
an email or Slack message with information on the case and a link to its detail page in Stellar
Cyber.

Keep in mind the following important points:

The threshold of 50 is hard-coded and cannot be changed.

The document is only created once for a given case. New documents are not created if
a case score falls below 50 and then increases above it again.

The document is created for a case that enters the system with a score over 50. This is
considered as a score change from 0 to a score greater than 50.

Configure the Alert
Create an alert that runs a query every 5 minutes on the Syslog index.

1. Navigate to Automation | Automation and select the Createbutton to add a playbook.

2. Enter the following in the Alert Configuration section:

Name: Case Score Monitor

Description: Alert from querying the Syslog index every 5 minutes for case
scores over 50 or 80

Schedule type: interval

Run every: 5 minute(s) over all selected tenants

Schedule: Toggle off (default setting)

Mute: Toggle off (default setting)

Tenants: All Tenants

Indices: Syslog

Rule Type: Query

Build a Query
Create a query that looks for new documents with a msg_class of incident_score_change
when the score is greater than 80.

1. Select New Query.

2. Enter the following:

Query Name: Score Change

Description: Query for new documents with a msg_class of
incident_score_change

Find documents where ALL of the following criteria are met.

Select + Add condition and enter msg_class, is, incident_score_change.

So far, the query just checks for any new documents with a msg_class of
incident_score_change. However, you now add a second query condition so that it
only matches cases over a specified threshold greater than 80 using the following logic:

Stellar Cyber only creates a document with a msg_class of
incident_score_change for a case when its score crosses the hard-coded
threshold of 50.

You next add a second query condition that matches cases over a score of 80.

 Keep in mind that because a document with a msg_class of

incident_score_change is only created once for a given case, this query
only matches cases that are either initially created with a score over 80 or
increased from below 50 to over 80.

3. Select + Add condition and enter metadata.score, greater than, 80.

 The metadata.score you specify must be greater than 50 because this is the

threshold where the document with a msg_class of incident_score_change is
created.

4. Select Save to save your query.

Configure a Condition
In the Condition Configuration section, configure a condition that triggers an action if there are
any hits.

Condition Name: Any Hits

Type: Compare Value

Comparison: Total Hits, is greater than or equal to, 1

Configure Actions
Configure Stellar Cyber to send an email or Slack message when a case score change is
detected. The configuration for both types of message is shown below.

 Refer to Configure Actions for details on configuring each type of action.

Configure an Email Message as the Action

Configure Stellar Cyber to send an email when a case score change is detected.

1. Set Trigger on condition to Any Hits.

2. Enter the following to set up email messages:

Type: Email

Recipients: Either type in an email address to use or choose a previously configured
recipient from the drop-down list.

 Refer to Adding a Recipient for information on managing recipients globally.

Subject: Case Score Change

Priority: Normal

Include Interflow: (clear)

Email Body: Enter the following:

The following cases exceeded the score threshold of

{{ctx.payload.hits.hits.0._source.metadata.score_threshold}}:

{{#ctx.payload.hits.hits}}

Case {{_source.metadata.cust_name}}-{{_source.metadata.ticket_id}}

({{_source.metadata.name}}) reached a score of

{{_source.metadata.incident_score}} at

{{_source.metadata.timestamp_readable}}

https://<dp-hostname-or-ip>/cases/case-detail/{{_source.metadata.id}}?

cust_id={{_source.metadata.cust_id}}&view=graph

{{/ctx.payload.hits.hits}}

 The sample text provides a link to the case. You must edit the text highlighted in
red to use the hostname or IP address of your Stellar Cyber Data Processor (DP)
for this to work

Mute: (disable)

3. Select Submit to save and immediately run the playbook.

Your new playbook appears in the playbook list. You can use the Last Status option in
the context menu at the far right of its entry to check how the rules are executing.

Here is a sample email sent by our ATH playbook, complete with a link to the case with
the changed score:

Configure a Slack Message as the Action

Configure Stellar Cyber to send a Slack message when a case score change is detected.

1. Set Trigger on condition to Any Hits.

2. Enter the following to set up email messages:

Type: Slack

Use Recipients: (select, and choose one or more Slack recipients from the list)

 Refer to Adding a Recipient for information on adding recipients. You need a Slack
Web URL from your Slack administrator to add a Slack repicient. Refer to the
instructions on webhooks in the Slack documentation  for details.

Message: Enter the following:

The following case(s) exceeded the score threshold of
{{ctx.payload.hits.hits.0._source.metadata.score_threshold}}:

{{#ctx.payload.hits.hits}}

Case {{_source.metadata.cust_name}}-{{_source.metadata.ticket_id}}
({{_source.metadata.name}}) reached a score of
{{_source.metadata.incident_score}} at
{{_source.metadata.timestamp_readable}} https://<dp-hostname-or-
ip>/cases/case-detail/{{_source.metadata.id}}?cust_id=
{{_source.metadata.cust_id}}&view=graph

{{/ctx.payload.hits.hits}}

 The sample text provides a link to the case and is formatted to make it easy to see
the plain text and the code. Note that you need to edit the text highlighted in red to
use the hostname or IP address of your Stellar Cyber Data Processor (DP) for this
to work.

Mute: (disable)

3. Select Submit to save and immediately run the playbook.

The new playbook appears in the Automated Threat Hunting Playbooks list. You can
use the Last Status option in the context menu at the far right of its entry to check how
the rules are executing.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

