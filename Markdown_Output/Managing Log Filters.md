Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Managing Log Filters

You can create log filters that are used by sensor profiles to drop logs before they are transmitted
to the Data Processor. Use this topic to understand how to define a log filter from the System
menu or from data in the Event Display.

For best practices, refer to Best Practices for Log Filtering.

 You can also use the Log Filters created in this page as Event Filters in a Windows Server
Sensor profile or in Connectors. The Windows tab in the Create Standard Sensor Profile
wizard includes Event Filter panels to include or excludematching events.

Creating or Editing Log Filters from Log Filters Table

 You must have Root scope to use this feature.

1. Select System | DATA SOURCE MANAGEMENT | Data Filters | Log Filters.

A table for managing Log filters appears.

2. Select + Add to add a new filter, or select the Edit icon to edit an existing filter.

The Add A Log Filter settings appear.

3. Enter a Log Filter Name.

 To improve usability, Stellar Cyber recommends that you use unique names for log

filter names across all tenants. This way, when users with access to multiple
tenants select a log filter, they do not have to contend with duplicate names.

4. Choose a Tenant.

You can choose a specific tenant or All Tenants for your organization.

5. Choose an optional Log Source.

Use this field if you want to apply the filter to a log forwarder.

 Leave this field empty if you want to apply the filter to a connector or to a Windows

sensor event log.

6. Select  Condition.

You can add multiple conditions, all of which are AND conditions.

7. Choose a Field.

If the field you want to use is not listed, type it in manually.

8. Choose an Operator and enter the Values for your condition.

After you type in a value, press the Enter key to complete the entry.

9. Select Submit.

The filter is immediately available but is not active until you include it in a sensor profile.

Applying Log Filters in Different Places

To add a log filter to a modular sensor profile, navigate to System | DATA SOURCE
MANAGEMENT | Sensors | Sensor Profiles, select the Edit icon for a previously
configured modular sensor profile, and then select Log Forwarder | Data Filtering.

To add a log filter to a standard sensor profile, navigate to System | DATA SOURCE
MANAGEMENT | Sensors | Sensor Profiles, select the Edit icon for a previously
configured standard sensor profile, and then select Feature Customization | Sensor |
 Log Forwarder.

To add a log filter as an Event Filter for Windows Server Sensors, open the Windows
tab of a standard sensor profile.

To add a log filter as an exclude filter to a collection connector (System |
 INTEGRATIONS | Connectors), select the name of a filter in the Log Filters field at
the bottom of the General configuration page—if your connector includes this field.

 You can view statistics for each connector content type for each filter by choosing the

Sensor Monitoring index in Threat Hunting.

Log Filter Maximums

Keep in mind the following maximums when creating log filters:

The maximum number of Conditions (rules) per log filter is 10.

The maximum number of log filters that can be applied to a single connector is 10.
Connectors only support Exclude filters.

Keeping Tabs on Log Filter Statistics

You can keep tabs on statistics related to log filters using the show logfilter and show
logfilter <filter-id> commands in the sensor CLI. The show logfilter-id command
shows the details of the last matching event during filtering and can be useful when evaluating
filter performance.

In addition, log filter statistics are sent to the Sensor Monitoring index (aella-ade-*) on the
DP using msgtype:41 and can be viewed in the Threat Hunting page with Indices set to Sensor
Monitoring. See below for the schema.

Expand to see the schema for log filter statistics

{
    "msgtype": 41,
    "msg_origin": {
        "processor": {
            "type": "log_forwarder", "winlog", "fim", "log_collector", or,
"aella_flow"
            "name": # Optional. It is <connector_name> when type is "connector".
            "id": # Optional. NG-SaaS, connector has id.
        }
    }
    "engid": # For connector running on DP, it is <connector type>_<connector
name>
    "engid_name": # For connector running on DP, it is <connector type>_<connector
name>
    "tenantid":
    "filter_id":
    "filter_name":
    "timestamp": # epoch ms
    "exclude_hits_delta": # Optional. The number of exclude hits of the filter by
the processor since last report
    "exclude_bytes_delta": # Optional. The size of excluded logs matched the
filter by the processor since last report
    "include_hits_delta": # Optional. The number of include hits of the filter by
the processor since last report
    "include_bytes_delta": # Optional. The size of included logs matched the
filter by the processor since last report
    "last_log": # Optional. The string of the latest log which was matched the
filter
}

Log Filter Rules

Keep in mind the following rules when creating log filters:

Log filters work on raw log fields and do not support fields enriched by Stellar Cyber.

Log filters do not work on fields with a list of objects (for example, the msg_data field).

Manual configuration is required to correctly filter ColorTokens logs.

The ColorTokens parser generates multiple device types (colortokens,
colortokens_xshield, colortokens_gatekeeper, colortokens_xprotect),

which differs from typical parsers that produce a single device type. Because of this,
automatic log filter creation does not work for ColorTokens logs.

To configure a log filter for ColorTokens:

1. Send a ColorTokens log message to the Stellar Cyber Platform.

2. Select Threat Hunting Search | Interflow Search and search for an

Interflow record generated from a ColorTokens message.

You might search by “colortokens”, source IP address, or other fields if
necessary.

3. View the record details and find the msg_origin.source field.

4. Select Create in System | DATA SOURCE MANAGEMENT | Data Filters |
Log Filters and create a manual log filter rule by setting the device type
(dev_type) to match the msg_origin.source value.

For example, if the msg_origin.source value is
colortokens_gatekeeper, set the dev_type to
colortokens_gatekeeper.

5. Manual configuration is required to filter ColorTokens logs correctly.

Keeping Track of Log Filter Performance
The Log Filters table provides the following columns to help you track log filter performance:

In Use – Shows you how many sensor profiles are using a particular log filter.

Hit count – Shows you how many logs have been excluded by the log filter in the time
window specified by the global filters at the top of the display. You can select the entry
to see the hit counts broken out by tenant.

Hit count size – Shows you the total size of the logs excluded by the log filter in the
time window specified by the global filters at the top of the display. You can select the
entry to see the volume of logs excluded by the log filter broken out by tenant.

Creating Log Filters from the Event Display
You can also create log filters directly from the Event Display interface. This lets you pre-
populate the log filter settings from the selected Interflow data. Note that this feature is only
available when working with Interflow data from the Syslog, Traffic, IDPS/Malware Sandbox
Events, or Win Events indices.

The following example illustrates setting a log filter directly from the Event Display interface:

1. Navigate to Threat Hunting and select the Interflow Search tab.

2. Set the Indices option to IDPS/Malware Sandbox Events, Syslog, Traffic, or

Windows Events.

For example, select Syslog.

3. Scroll down to the table of events from the Syslog index and select the More Info icon

in the Action column for the entry you want to use as the source of a log filter.

The Event Display appears.

4. Select Actions and then select the Add a Log Filter button to display the standard

Add a Log Filter interface.

Stellar Cyber automatically pre-populates the Tenant field from the Event Display data.
In addition, whenever you add a Field to the log filter, Stellar Cyber automatically pre-
populates its setting from the associated Interflow data. For example, the illustration
below shows a source IP address pre-populated from the Interflow data of a syslog
event.

5. Select Submit.

The filter is immediately available but is not active until you include it in a sensor profile.

You can add the filter to a modular sensor profile under Log Forwarder | Data
Filtering.

You can add the filter to a standard sensor profile under Feature
Customization | Sensor | Log Forwarder.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

