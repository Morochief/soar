Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Recipients

Use the System | Recipients page to manage recipients of alerts from Stellar Cyber. Instead of
entering an email address in multiple locations, you can use this page to manage recipients
centrally, making maintenance much easier. If a recipient's email address changes, you only
need to change it in one place.

Recipients can receive messages using any of the following methods:

Email
Slack
Webhook

Recipients Table
When you select System | Recipients, Stellar Cyber displays a table listing all currently
configured Recipients, as in the example below.

For the definitions of the columns, see the following section on adding and editing records.

Actions that can be taken include:

Select Create to add a new recipient to the table. See the section below.

Select

 to edit the corresponding recipient. See the section below.

 Note that you cannot edit an existing recipient's Message Type. Create a new

recipient of the desired type instead.

Select

 to delete the recipient.

 Note: You cannot delete a recipient that is in use (for example, by an

ATH Playbook or a Scheduled Report).

See the Tables page for more information on working with tables.

Adding or Editing a Recipient
The dialog box used to add or edit a recipient includes the following fields:

Name – Each recipient is assigned a unique name by the user. This is the value that is
referred to in configuration forms elsewhere in the system. This field does not support
multibyte characters.

Tenant Name – The name of the tenant to which the recipient belongs or All Tenants.

Message Type – This is a selection box with the type of media that will be used when
sending messages to the recipient (Email, Slack, or Webhook). The rest of the dialog
box provides different options depending on the selection here, as described below.

 Note that you cannot edit an existing recipient's Message Type. Create a new

recipient of the desired type instead.

Options for Email Message Types

Email Address – The email address to which Stellar Cyber sends messages. This
appears when Message Type is set to email.

Options for Slack Message Types

Slack Web URL – The URL to use when sending Slack messages. This field appears
when Message Type is set to slack.

Options for Webhook Message Types

Protocol – Select either HTTP or HTTPS

Basic Authentication – Select this check box to use Basic Authentication.

If you enable Basic Authentication, additional fields for a Username and
Password appear. The password is masked as you enter it and is not shown in
the summary table of configured recipients.

Keep in mind the following rules for webhook usernames and passwords:

For versions prior to 5.03:

Enter the username without the @ or period (.) characters.

Enter the password without any non-alphanumeric
characters except for the underscore (_).

From v5.0.3 and later, you can use any non-alphanumeric characters
in both the username and password fields, including the @ and
period (.) characters.

If you do not enable Basic Authentication, the Webhook uses bearer token
authentication instead.

Host – The host where the webhook message is sent. This can be either a hostname or
an IP address.

Port – The port where the webhook message is sent. If you do not specify a port, the
default ports for the selected Protocol are used (HTTP/80 or HTTPS/443).

Path – The path where the webhook message is sent on the specified host. If you do
not specify a path, the message is sent to the base URL.

Stellar Cyber uses these fields to construct the URL where the webhook message is sent using
the following formula:

http://<host>:<port>/path

For example, consider the settings in the image below:

These settings result in the following Webhook URL:

https://testrecipient.com/webhook

Select Submit to save your changes. Alternatively, you can select the X button in the upper right
corner of the dialog box to cancel the entry.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

