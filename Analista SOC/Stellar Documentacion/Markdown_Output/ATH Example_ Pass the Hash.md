Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

ATH Example: Pass the Hash

Create an Automated Threat Hunting (ATH) playbook that detects potential pass-the-hash
attacks in your environment. A pass-the-hash attack allows an adversary to authenticate using
hashed credentials without needing the plaintext password. Detecting this activity helps identify
lateral movement attempts within your network. This playbook queries authentication events that
match known pass-the-hash patterns and alerts you when a match occurs.

Configure the Alert
Configure an alert that runs every five minutes against the Windows Events index to identify
suspicious logins that may indicate pass-the-hash activity. Running this check frequently ensures
timely detection of credential misuse.

1. Navigate to Automation | Automation and click the Createbutton to add a playbook.

2. Enter the following in the Alert Configuration section:

Name: Pass the Hash Attack

Description: Alert when evidence of Pass-the-Hash attacks is detected

Schedule type: interval

Run every: 5 minute(s) over all selected tenants

Schedule: Toggle off (default setting)

Mute: Toggle off (default setting)

Tenants: All Tenants

Indices: Windows Events

Rule Type: Query

Build a Query
Build a query that identifies logins using New Technology LAN Manager (NTLM), a legacy
Windows authentication protocol. The query focuses on logins that use cached credentials and
no session key, which is behavior consistent with common pass-the-hash techniques. The query
also includes both successful and failed login attempts to ensure broader visibility into potentially
unauthorized access.

1. Select New Query.

2. Enter the following:

Query Name: Pass the Hash

Description: Query for login behaviors indicative of pass-the-hash
attacks

Find documents where ALL of the following criteria are met.

Select + Add condition and enter msg_origin.source, is, windows_agent.

3. Select + Add condition and enter event_data.AuthenticationPackageName, is,

NTLM.

4. Select + Add condition and enter event_data.LogonType, is, 9.

This login type (9) indicates a login using cached credentials.

5. Select + Add condition and enter event_data.KeyLength, is, 0.

This (0) indicates that no session key was requested.

6. Select + Add Inner Group.

7. Change the condition type from AND to OR.

8. Select + Add condition within the inner group and enter event_id, is, 4624.

This indicates a successful login.

9. Still within the inner group, select + Add condition and enter event_id, is, 4625.

This indicates a failed login.

10. Select Save to save the query.

Configure a Condition
Define a condition that triggers the playbook actions if at least one matching event is found. This
allows the playbook to respond immediately to any signs of pass-the-hash activity.

Condition Name: Any Hits

Type: Compare Value

Comparison: Total Hits, is greater than or equal to, 1

Configure an Email Message as the Action
Specify the actions to take when the condition is met. In this example, the playbook sends an
email notification that includes relevant details for investigation, including Interflow data to
support deeper analysis.

1. Set the Trigger on condition to Any Hits.

2. Enter the following to set up email messages:

Type: Email

Recipients: Either type in an email address to use or choose a previously
configured recipient from the drop-down list.

 Refer to Adding a Recipient for information on managing recipients

globally.

Subject: Pass the Hash?

Priority: Normal

Include Interflow: (select to attach Interflow records to the email)

Email Body: Enter the following:

This alert was triggered by behavior consistent with pass-the-hash

authentication. A login attempt using NTLM with cached credentials

and no session key was detected.

Details:

Source IP: {{srcip}}

Username: {{username}}

Host: {{hostname}}

Logon Type: {{logon_type}}

Event Time: {{timestamp}}

Please review these details in Interflow and investigate whether the

activity is authorized or indicative of credential misuse or lateral

movement.

Mute: (disable)

 See Configure Actions for details on configuring each type of action.

Save & Run the Playbook
Select Submit to save and immediately run the playbook.

The new playbook appears in the Automated Threat Hunting Playbooks list.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

