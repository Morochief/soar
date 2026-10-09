Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Related Events for Alert Types

Related Events are available for the SentinelOne alert type. Related Events enhance Stellar
Cyber's alert integration and provide more context for SentinelOne Deep Visibility events. For a
security event, you can view when and how the security threat developed and you can
investigate events on the Stellar Cyber platform without going to the SentinelOne console.

To support Related Events, this feature uses SentinelOne Threat Detection alerts as a source of
information and SentinelOne Deep Visibility events as the data for high level summarization.
Correlated Deep Visibility events must belong to the same tenant and organization.

 Stellar Cyber performance may vary depending on the amount of Deep Visibility logs you

ingest.

See the following:

Using the Related Events Tab

Using the Jump to Events Table

Using the Related Events Tab
For a SentinelOne alert, click the Related Events tab to see a summary of related SentinelOne
Deep Visibility events. The information in the tab provides a high level summarization of the
events related to the alert and the entities involved.

 The summarization only happens once. If there are no Deep Visibility events available when
the data is ingested from SentinelOne, the summary may be empty. If new Deep Visibility
events come in, the summary will not be updated.

To help you understand the high level scope of the security event, the following fields are
displayed in Related Events:

Storyline ID—a unique ID associated with a security event and used to get SentinelOne
Deep Visibility data

Summarization time range—the timestamps of the start and end of the summarization

Aggregation of—a count of the involved entities, such as process or user activities

Involved processes—the processes involved in the event, such as an endpoint process

Involved registries—the registries involved in the event, such as an endpoint registry

Involved hosts—the hosts involved in the event, such as a source host or destination
host

Involved users—the users involved in the event, such as a user ID or user name

Involved files—the files involved in the event, such as a file name

Involved URLs—the URLs involved in the event, such as a URL

Using the Jump to Events Table
To help you understand the potential impact of the security event, click the link to Jump to
Events table to view the events in Threat Hunting.

The Threat Hunting page opens.

The events table contains fields for each event. The column headings on the left are common
fields that exist in all SentinelOne Deep Visibility data. The Selected Fields on the right show
important attributes that are presented dynamically in the table based on the event category.

The common fields in the Events table include: Event Time, Event Type, SentinelOne Agent
UUID, SentinelOne Source Process User, SentinelOne OS Source Process UID, and
SentinelOne Source Process Storyline ID.

The Selected Fields are based on each event category as follows:

Event Category

Column Headings for the Selected Fields for this Event Category

Cloud Activity

Event Outcome Result, Event Outcome Reason, External Threat Value

Event Category

Column Headings for the Selected Fields for this Event Category

Cross Process

Target Process Relation, Source Process UID, Source Process Command Line, Target

Process UID, Target Process Command Line

Command Script

Agent UUID, Source Process UID, OS Source Process UID, Command Script Content,

DNS

Driver

File

Firmware

Identity

Indicators

IP

Logins

Module

Named Pipe

Process

Source Command Script, Source Process Command Line

Agent UUID, Source Process UID, OS Source Process UID, DNS Request, DNS Request

Agent UUID, Source Process UID, Target File Path, Driver Load Verdict

Agent UUID, Source Process UID, OS Source Process UID, Target File Path, Target File

Old Path, Target File Size

Agent UUID, Source Process UID, OS Source Process UID

Actor Alternate ID, Actor Display Name, Login Account Name

Agent UUID, Source Process UID, OS Source Process UID, Indicator Name, Indicator

Category, Indicator Description, Indicator Metadata

Agent UUID, Source Process UID, OS Source Process UID, Source IP Address, Source

Port Number, Destination IP Address, Destination Port Number, Network Direction, Network

Connection Status

Agent UUID, Source Process UID, OS Source Process UID, Source Endpoint IP Address,

Login User Name, Login Base Type

Agent UUID, Source Process UID, OS Source Process UID, Module Path

Agent UUID, Source Process UID, OS Source Process UID

Agent UUID, Source Process UID, OS Source Process UID, Target Process UID, Source

Process Command Line, Source Process User, Target Process Command Line, Target

Process User

Registry

Agent UUID, Source Process UID, OS Source Process UID, Registry Key Path, Registry

Value

Scheduled Task

Agent UUID, Source Process UID, OS Source Process UID, Task Name, Task Path

Threat Intelligence Indicators

Agent UUID, Source Process UID, OS Source Process UID, TI Indicator Source, TI

Indicator Value

URL

Agent UUID, Source Process UID, OS Source Process UID, URL Address, URL Action

Column Headings

Click Columns to see all the available column headings. You can add or remove columns using
check boxes. To exit, click Columns again.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

