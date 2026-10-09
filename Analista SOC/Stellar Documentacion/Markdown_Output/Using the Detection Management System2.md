Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Using the Detection Management System

 Only Super Admin or Platform Admin users with Root scope can make changes in Detection

Management.

The Detection Management System is a collection of related features on how to view and
manage detections across the network. Detections identify suspicious patterns in the data or
deviations from normal behavior, and raise alerts if necessary. Alert types categorize different
alerts.

Using the Detection Management System, you can:

access detections easily

manage detections

gain visibility and control over detection settings and status

manage tenants through profiles (see Multi-Tenant Support)

The main capabilities of the Detection Management System are:

Customizable settings for newly released detections:

Benefit—Provides SOC teams with the flexibility to customize how each tier (Tier 1,
Tier 2, and Experimental) of newly released detections behaves in terms of alert
generation and visibility.

Why it Matters—SOC teams often grapple with complex systems and the integration of
new tools. A streamlined process reduces operational complexity, enabling faster and
more efficient updates and rule management that directly impacts response times in
critical security situations.

See Using the Settings & Profiles Page.

Enhanced visibility and control over detections:

Benefit—Offers granular control over the activation state of all detection types (On, Off,
or Silent), and comprehensive visibility into the performance of each detection through

hit statistics.

Tailored Detection Alerting:

On—Activates the rule, generating alerts as designed. This setting is essential
for high-priority rules where immediate attention is needed.

Silent—The rule is active but does not send real-time alerts. This setting is
valuable for Tier 2 rules where oversight is necessary, but real-time response
may not be.

Off—Completely disables the rule, preventing it from running or generating
alerts. This setting is for experimental rules that may generate high volumes of
false positives or are in a testing phase.

Hits—Counts the number of times the detection was triggered (or would have
been triggered for Silent mode) over the past seven days. The counter
refreshes every hour. The count reflects alerts before filtering, but after alert
suppression. The hit count statistics are useful for monitoring and collecting
data without overwhelming the SOC with notifications.

See Detection Management Table for Sigma Rule Based Detections.

 Considerations for manual event generation: Due to the nature of Stellar Cyber's
alert correlation and machine learning models, manually generated or ad-hoc
events may not always trigger the expected alert or case creation. The Stellar
Cyber platform is designed to analyze and correlate multiple events over time,
assessing patterns and context to determine the severity of a potential threat. As a
result, isolated or artificial events might not meet the criteria for high-severity alerts
or case generation, and may not be representative of the system's full detection
capabilities in real-world threat scenarios.

Insight into possible data sources:

Benefit—Provides a comprehensive list of data sources that could contribute to the
detection of various types of security alerts within an organization's IT ecosystem.

See Detections Panels.

See the following:

Using the Detection Management Page

Using the Settings & Profiles Page

Multi-Tenant Support

Multi-tenant support tailors security for MSSP/MDR partners to provide granular control over
detection settings to meet the security needs of individual tenants. MSSP/MDR partners can
customize detection settings to align with tenant needs.

You manage tenants through Detection Profiles in which you create tenant-specific detection
configurations. Detection Profiles empower you to manage tenant environments with greater
accuracy, simplicity, and scale.

Within an organization, there can be multiple Detection Profiles with each tenant assigned to a
profile.

See the following:

Configuring Profiles

Configuring Tenant Assignment

Evidence Preservation for Silent Mode Alerts

Stellar Cyber provides evidence storage for detections suppressed by silent mode. When a
detection is suppressed by silent mode, the corresponding signal can be found in the aella-
interim-* index with the stellar.suppressed_reason field set to SILENT_MODE. This
preserves visibility into detections that were triggered but silenced.

You can investigate silenced detections by using the Kibana Plugin to search the aella-
interim-* index for records with the stellar.suppressed_reason field set to SILENT_MODE,
as demonstrated in the example below.

Example: Using Kibana to Search for Detections Suppressed by Silent

Mode

1. Navigate to System | Kibana Plugin.

2. Select the Index Pattern dropdown and choose the aella-interim-* index you

want to search.

3. Select +Add filter and set the following options.

Set Field to stellar.suppressed_reason.

Set Operator to is.

Set Value to SILENT_MODE.

4. Select Save.

The display updates to show the records for suppressed alerts in the selected time
range, as illustrated in the image below.

 If you do not see the suppressed alerts you expect, try increasing the time range

and selecting Refresh.

Using the Detection Management Page
To use Detection Management, select Detections | Detection Management. The Detection
Management page is displayed. It has three panels on the top and a table below.

See the following:

Detection Management Panels

Detection Management Table

Detection Preferences

Detection Management Panels

The panels at the top of the Detection Management page are for the following detection types:

3rd Party Integrations—third party alert integrations

ML Detections—machine learning (ML) alert types

Rule Based Detections—rule based alert types, including Sigma rules and analytical
rules

The panels let you see the detection types at a high level and provide summary statistics. In
addition, you can easily filter by type by selecting one of the panels.

For example, to see only ML Detections, select the ML Detections panel. The panel is highlighted
and the table below displays only the ML alert types.

Click the panel again to stop filtering by that detection type. The highlighting is removed and the
table shows all the alert types.

Each of the three panels contains the following statistics:

count of the number of detections

running status:

Ready:

For 3rd Party Integrations, the backend pipelines are ready to detect
an anomaly.

For ML Detections, the job is ready to detect anomalies.

For Rule Based Detections, the detection is running and can produce
alerts.

Not ready:

For 3rd Party Integrations, the backend pipelines have some errors or
were never started for the job or rule.

For ML Detections, the backend pipelines have some errors or were
never started for the job.

 When a job is in training, the running status is Not ready.

Training time may require two weeks. Refer to Alert Type Model
Summary.

For Rule Based Detections, the detection is not running or is
preparing to run.

For ML Detections, the detection service is running, but no relevant
data has been received from the configured data sources. Verify that
your data sources are active and properly configured.

 When there are no alerts in the data store for 7 days, the No

data status is shown. If there is one alert created within 7 days,
the ML detection will trigger the training process and switch the
No data status to Ready.

No data:

user-specified state of the detection:

On—detections are fully active. On activates detections to monitor and
produce real-time alerts when triggered. On is typically used for high-
confidence Tier 1 detections that require immediate attention.

Off—detections are inactive. Off disables detections, halting monitoring and
alert triggering, which reduces system noise and conserves resources.
Detections can be reactivated as needed. Off is suitable for managing lower
priority (Tier 2) or experimental grades.

Silent—detections are active but do not produce alerts when triggered,
allowing for passive monitoring. Silent detections operate silently, gathering
data and allowing for performance evaluation to ensure minimal false positives
and optimal effectiveness.

Mixed—detections that are a mix of On, Off, or Silent. Mixed mode is only
available for Rule Based Detections, as this state is based on the state of the
individual rules within the Rule Based Detection.

For example, selecting the 3rd Party Integrations panel displays:

count = 62

Ready = 57

Not ready = 5

On = 60

Off = 1

Silent = 1

For example, selecting the ML Detections panel displays:

count = 72

Ready = 72

Not ready = 0

No data = 0

On = 70

Off = 1

Silent = 1

For example, selecting the Rule Based Detections panel displays:

count = 201

Ready = 201

Not ready = 0

On = 171

Off = 4

Silent = 25

Mixed = 1

Detection Management Table

The Detection Management table has the following columns:

Name—Name of the detection (with a link to the detection). (You can search on this
field. See Using Search.)

Description—Description of the detection. (You can search on this field. See Using
Search.)

Type—Type of detection as 3rd party, ML, or RULE.

Status—Status of the alert type as Ready or Not Ready or No data (only for
ML Detections).

Tags—Tags that identify the detection such as External, Internal, Analytics, Sigma, or
Malware.

Release Date—Date in which the detection was released in the Stellar Cyber platform.

Release Version—Version in which the detection was released in the Stellar Cyber
platform.

Update Version—Version in which the detection was updated in the Stellar Cyber
platform.

Alert Types—Display name of the alert type. (You can search on this field. See Using
Search.)

Update Date—Date in which the detection was updated in the Stellar Cyber platform.

Hits Count—Number of times the detection was triggered (or would have been triggered
for Silent mode) over the past seven days.

Actions—Actions for 3rd Party Integrations, ML Detections and Rule Based Detections
to toggle an alert type ON, OFF, or SILENT.

Use the Detection Management table for the following:

Using Search

Selecting Columns

Using Filters

Performing Bulk Actions

Exporting CSV

Selecting View

Using Search

Use the Search box to search for content in the table.

In the Detection Management table, the following fields can be searched:

Name

Description

Alert Types

For example, type microsoft to search for all Microsoft entries in the table.

For rules, the following fields can be searched:

Rule

Description

Grade

For example, type tier1 to search for all the rules that have a tier1 Grade. At least one rule in the
resulting detection(s) will have that Grade.

To clear the search criteria, click Clear All.

Selecting Columns

Click the Columns icon (

) to add or remove columns in the table using check boxes.

You can also type the name of a column in the Search box.

To exit, click the Columns icon (

) again.

Using Filters

Click the Filters icon (

) to use defined filters.

To use defined filters:

For Status, select the status using the check boxes. The number of alerts of each
status is displayed on the right.

You can also use the search box to search for a specific status.

For Tags, select the tags using the check boxes. The number of alerts of each tag is
displayed on the right. A scroll bar is available on the right when there are more tags in
the list than can be displayed.

You can also use the search box to search for a specific tag.

For Release Date, select a release date using the check boxes. The number of alerts of
each release date is displayed on the right. A scroll bar is available on the right when
there are more release dates in the list than can be displayed.

You can also use the search box to search for a specific release date.

For Release Version, select the release version using the check boxes. The number of
alerts of each release version is displayed on the right. A scroll bar is available on the
right when there are more release versions in the list than can be displayed.

For Update Date, select an update date using the check boxes. The number of alerts of
each update date is displayed on the right. A scroll bar is available on the right when
there are more update dates in the list than can be displayed.

You can also use the search box to search for a specific update date.

For Update Version, select an update version using the check boxes. The number of
alerts of each update version is displayed on the right. A scroll bar is available on the
right when there are more update versions in the list than can be displayed.

You can also use the search box to search for a specific update version.

You can click the Add new filter search box to deselect a filter in the dropdown menu.

You can also type in the Add new filter search box to search for a filter by name.

To exit, click the Filters icon (
table and the results are displayed in the table.

) again. The configured filters are displayed at the top of the

To clear an individual filter, click the icon to the right of the filter (

).

To clear all filters, click Clear All.

Performing Bulk Actions

The Detection Management table has check boxes on the left that let you select multiple
detections. You can change the state for multiple detections at the same time. For all detection
types, you can select a state of ON, OFF, or SILENT. Then click Apply.

Click Clear all to clear the check box selections.

Exporting CSV

Click Export CSV to export the table as a spreadsheet. The spreadsheet lists the active
detections for the selected profile.

You can export Selected Columns or All Columns. The spreadsheet is downloaded to your
Downloads folder.

Selecting View

Click Select View to preserve a table layout. See Saved View Configurations for details.

Detection Management Table for Sigma Rule Based Detections

The Detection Management table for Rule Based Detections (only for Sigma rules) has an
expand feature because there can be many rules within a rule based detection.

To see the individual rules, click the icon (

) to expand the row.

The table has the following columns:

Rule—Name of the rule. (You can search on this field. See Using Search.)

Description—Description of the rule. (You can search on this field. See Using Search.)

Grade—Grade of the rule as follows. (You can search on this field. See Using Search.)

Tier 1—detections that are stable and in production

Tier 2—detections that are in development or test

Experimental—experimental detections

Actions—Actions for rule based detections include toggles for ON, OFF, or SILENT for
an individual rule.

At the bottom of the expanded rule based detection, the View all link takes you to the Detection
Panel for Rule Detections.

Detections Panels

The Name column in the Detection Management table has links to the detection. When you click
the link, a panel is displayed on the right.

The top part of the panel has the following:

Previous and Next icons (
the next detection in the table.

Name of the detection.

) at the top left to move to the previous detection or

Toggle for ON, OFF, or SILENT (or Mixed for Rule Based Detections).

Tabs for Overview, Rules (only for Rule type of detections), and Possible Data
Sources. The latter two tabs have counts, for example, Rules (1) and Possible Data
Sources (1).

The lower part of the panel displays information depending on the type of detection. All detection
types display Possible Data Sources that may support the detection.

Overview Tab

The Overview tab has the following:

Description of the detection.

Tags that identify the detection, for example, Sigma, Azure, External, Identity Detection.

Hits that count the number of alerts triggered in the past seven days or since the last
Reset hit stats was performed. The stats are refreshed every hour.

Type of the detection: 3rd party, ML, or RULE.

Alert types and count:

For ML and Rule Based Detections, the Alert Types are predefined.

For 3rd party alert integrations, the Alert Types are dynamically generated.

 There may not be a link if the alert type has not triggered yet.

Click the Alert Types link(s) to go to the Alerts page.

Rules Tab

The Rules tab is described in Detection Panel for Sigma Rules.

Possible Data Sources

The Possible Data Sources tab shows all data sources that are possible across an
organization.

A green check mark is displayed on a data source when it has been active in the past five (5)
days and has an event contributing to the detection. The data can come from any tenant in the
organization.

Note that the check marks do not replace other active monitoring features available in the Stellar
Cyber platform.

In the Possible Data Sources, the active data sources (with the check marks) are displayed first
and Stellar Cyber data sources have a Stellar Cyber logo. You can search the data sources
using the Search box.

See the following:

Detection Panel for ML Detections

Detection Panel for 3rd Party Detections

Detection Panel for Rule Detections

Detection Panel for Sigma Rules

Detection Panel for ML Detections

When you click a link for an ML type of detection, the panel on the right has an Overview tab
and a Possible Data Sources tab that lists icons of the Possible Data Sources and their count.

Detection Panel for 3rd Party Detections

When you click a link for a 3rd party type of detection, the panel on the right has an Overview
tab and a Possible Data Sources tab that lists icons of the Possible Data Sources and their

count.

Detection Panel for Rule Detections

When you click a link for a rule type of detection (for analytics rules), the panel on the right has
an Overview tab and a Possible Data Sources tab that lists icons of the Possible Data Sources
and their count.

 The Analytics tag differentiates rule detections that are analytical rules.

When you click a link for a rule type of detection (only for Sigma rules), the panel on the right has
an Overview tab, a Rules tab that lists Rules and their count, and a Possible Data Sources tab
that lists icons of the Possible Data Sources and their count.

 The Sigma tag differentiates rule detections that are Sigma rules.

When you click the Rules tab, the panel lists the individual rules.

When you click the Possible Data Sources tab, the panel lists icons of the Possible Data
Sources.

Detection Panel for Sigma Rules

When you click the Rules tab in a Sigma rule type of detection, there is the following information:

A check box to select all rules. If you select all rules, you can change the state on all
rules at the same time to ON, OFF, or SILENT.

To deselect all the rules, check the check box again.

Search rules box in which you can enter a search string, for example, CVE.

Sort, in which you can sort the rules as follows:

A-Z—alphabetic sort, in ascending order

Z-A—alphabetic sort, in descending order

Hits—numeric sort, in descending order (from the highest number of hits to the
lowest)

State—OFF, ON, SILENT

Grade Level—Tier 1, Tier 2, Experimental

Risk Level—Low, Medium, High

Pagination icons at the bottom for next and previous, and first and last pages, if there
are many rules

The Rules tab has the following information for the individual rules in the detection:

check box to select an individual rule

Toggle for ON, OFF, or SILENT

Hits count of the number of alerts triggered

Grade of Tier1, Tier2, or Experimental

description of the individual rule

icon to expand the individual rule (

)

The expanded rule has the following additional information for an individual rule:

Reset hit stats button. When selected, a confirmation warning is displayed:

If the hits are reset, a successful message is displayed:

Rule ID—Stellar Cyber rule ID, such as azure_64

Product—product, such as AWS, Azure, or Windows, or Category, such as
process_creation

Rule Source—rule source, such as SigmaHQ or developed internally by Stellar Cyber

Tactics, Techniques and Procedure—links to https://attack.mitre.org/ for tactics or
techniques

Maturity—maturity status as follows:

Production—for rules that are reliable in a production environment

Stable—for rules that have had one year of use

Test—for rules that have had months of use

Experimental—for new rules

Risk Level—color-coded risk level as follows:

Low—yellow

Medium—orange

High—red

Creation date—date the rule was created

Sigma Rule—Sigma rule, with Copy button

Configuring Customizations for ML Detections

There are three ML detections that offer customizations: Impossible Travel Anomaly, User
Login Location Anomaly, and Successful Login After Brute Force. The detection panel for
those ML detections have a Customization tab containing settings you can customize.

For Impossible Travel Anomaly, you can customize the minimum distance and speed
thresholds and select the frequent location suppression.

For User Login Location Anomaly, you can customize the distance threshold, the behavior for
previously visited locations, and rules for tenant-level location suppression.

For Successful Login After Brute Force, you can customize the thresholds for unique IP
addresses and the length of recent history.

 Before customizing these ML detections, review the factors listed under each Customization

tab to understand the impacts.

See the following:

Customizing Impossible Travel Anomaly

Customizing User Login Location Anomaly

Customizing Successful Login After Brute Force

Customizing Impossible Travel Anomaly

To customize the Impossible Travel Anomaly detection:

1. You can search for impossible and click the link to the detection in the Name column.

2. Click the Customization tab.

3. Use the slider to change the Min distance (Miles). This sets the minimum travel

distance to trigger an alert. It is the minimum distance between two login locations that
could be considered impossible travel. Logins from locations closer than this distance
will not trigger an alert, regardless of the time between them. The default is 100 miles,
which is also the minimum. The maximum is 8000 miles. Higher values (greater than
500 miles) may miss regional threats and may restrict the number of low-distance
anomalies.

4. Use the slider to change the Speed threshold (MPH). This sets the realistic travel

speed (in miles per hour) considered possible. If the calculated speed between the two
logins exceeds this threshold, it may trigger an alert. The default is 600 MPH. The
minimum is 300 MPH. The maximum is 2500 MPH. Lower values flag routine air travel
as suspicious, while higher values may miss threats. Low speeds (less than 600 MPH)
may overload analysts with routine flight alerts. Extremely high speeds (greater than
1,000 MPH) could exclude most travel-based threats.

5. Select how to handle frequent locations with Frequent Location Suppression. The

options are:

Off: Do not suppress alerts based on location history. Allow all alert locations.

Destination Only: This is the default. Suppress if the destination is known.
More aggressive suppression may result in fewer alerts.

Destination & Source: Suppress if both the destination and the source are
frequent locations. Less aggressive suppression may result in more alerts.

6. Select the Attributes for DMS Alert Suppression. Sets how profile-based alert

suppression in the Detection Management System (DMS) interacts with alerts from the

Impossible Travel Anomaly, changing the behavior.

If Alert Suppression is enabled in DMS with a defined interval (default: 24 hours), the
following attributes will rate limit or filter the alerts from this detection:

Unique User: A maximum of one alert per user will be triggered within the
interval set in DMS.

Unique Locations For User: A maximum of one alert per unique pair of
locations per user will be triggered within the interval set in DMS. A pair of
locations means both locations (source/dest) have been seen before. There
may be multiple alerts for a single user.

7. Click Submit. You may be prompted to Review Changes or Save Anyways, for

example:

8. (Optional) Click Restore to Default to put the settings back to the default values.

Customizing User Login Location Anomaly

To customize the User Login Location Anomaly detection:

1. You can search for login location and click the link to the detection in the Name column.

2. Click the Customization tab.

3. Use the slider to change the Distance threshold (Miles). This sets the minimum travel
distance required to generate an alert. If a user logs in from a location farther than this
distance from their last known location, it may generate an alert. The default is 100
miles. The minimum is 50 miles. The maximum is 10000 miles. Lower values flag short-
distance logins, while higher values detect long-distance anomalies. Very low
thresholds (less than 100 miles) may overwhelm analysts with local alerts. High
thresholds (greater than 500 miles) could miss regional threats.

4. Select the Location History behavior:

Allow alerts on known recent locations: Enable alerts for previously visited
locations, if enough time has passed.

Use separate threshold for frequent travelers:Enable this threshold to apply
different alert rules for users who travel often. This helps reduce false positives
for frequent travelers while maintaining stricter rules for stationary users.

Use the slider to change the Location Reset Threshold (Days): This sets the
number of days with no visits before a location is eligible for another alert. This
is the number of days without a visit that must pass before the system can
generate another alert for a known location. This threshold applies to all users
if separate thresholds are disabled and it applies to stationary users if it is
enabled. This helps reduce alert fatigue from repeated logins at the same

location. The default is 90 days. The minimum is 14 days. The maximum is
730 days. Shorter periods make the detection more sensitive to previously
visited locations. Very short periods may incur alerts for known locations. Long
periods risk suppressing alerts for locations that have not been visited in
awhile.

Use the slider to change the Location Reset Threshold for Traveling Users
(Days): Sets the number of days with no visits before a location is eligible for
another alert for traveling users. This is the number of days that should pass
before the system can generate another alert for the same location for
traveling users. This threshold is only active if Use separate threshold for
frequent travelers is enabled. The default is 180 days. The minimum is 14
days. The maximum is 730 days. Shorter periods make the detection more
sensitive to previously visited locations. Very short periods may incur alerts for
known locations and travel hubs. Long periods risk suppressing alerts for
locations that have not been visited in a while.

5. Select the Suppression Rules. When Tenant location alert suppression is enabled,
the detection attempts to prevent alerts from being generated for logins occurring at
locations associated with your organization, for example, office locations.

6. Use the slider to change the New User Training Period (Days): Sets the number of
days for the new user training period, which is a per-key silence period. This is the
period during which the system will not generate alerts while it learns a user's normal
login patterns. This help reduce false positives when setting up the system or
onboarding new users. The default is 14 days. The minimum is 0 days. The maximum is
90 days. If the period is short, immediate alerts for new activity may overwhelm
analysts. If the period is long, the detection of new threats may be delayed.

7. Select the Attributes for DMS Alert Suppression. Sets how profile-based alert

suppression in the Detection Management System (DMS) interacts with alerts from the

User Login Location Anomaly, changing the behavior.

If Alert Suppression is enabled in DMS with a defined interval (default: 24 hours), the
following attributes will rate limit or filter the alerts from this detection:

Unique User: A maximum of one alert per user will be triggered within the
interval set in DMS.

Unique Location For User: A maximum of one alert per location per user will
be triggered within the interval set in DMS.

8. Click Submit. You may be prompted to Review Changes or Save Anyways for

example:

9. (Optional) Click Restore to Default to put the settings back to the default values.

Customizing Successful Login After Brute Force

To customize the Successful Login After Brute Force detection:

1. You can search for login after and click the link to the detection in the Name column.

2. Click the Customization tab.

3. Use the slider to change the IP History Duration (Days). This sets how long an

IP address is remembered as known for each user. Successful logins from IP addresses
not seen within this period are considered new and may trigger an alert if brute force
activity is detected. Logins from IP addresses seen within this window are not flagged.
The default is 30 days. The minimum is 7 days. The maximum is 60 days. Short history
durations (less than 14 days) may flag returning legitimate users. Long history durations
(greater than 30 days) will reduce alert volume but may miss attacks from genuinely
new IP addresses.

4. Use the slider to change the Min Failure IPs (30 min window). This sets the minimum
number of unique IP addresses that must have login failures in the 30-minute window
before a successful login to indicate active brute force and trigger an alert. The default
is 5 unique IP addresses. The minimum is 2. The maximum is 50. Low thresholds (less
than 5) may flag normal failed login attempts. High thresholds (greater than 10) focus
only on aggressive attacks.

5. Use the slider to change the Min Failure IPs (24 hour window). This sets the minimum

number of unique IP addresses that must have login failures in the 24-hour window
before a successful login to indicate distributed brute force and trigger an alert. The
default is 25 unique IP addresses. The minimum is 5. The maximum is 250. Low
thresholds (less than 10) may generate alerts for sporadic login issues. High thresholds
(greater than 100) may only detect sustained, large-scale attacks.

6. Click Submit. You may be prompted to Review Changes or Save Anyways for

example:

7. (Optional) Click Restore to Default to put the settings back to the default values.

Configuring Detection Preferences

You configure Detection Preferences from the top left of the Detection Management page. The
Detection Preferences are the specific detection settings configured for a selected profile. For
example, if the Default Profile is selected, the Detection Preferences you choose will be applied
to the Default Profile.

Use the dropdown menu (click on Default Profile) to select a different profile. For details on
profiles, see Configuring Profiles.

 No matter which profile you select from the dropdown menu, the Detection Management

table displays all the detections.

Click Detection Preferences or the icon (

) to choose the settings for a selected profile.

See the following:

Configuring Alert Suppression

Configuring New Detections and Rules

Configuring Alert Suppression

Alert Suppression is configured per profile.

To minimize excessive alerting, each alert type is triggered only once in a configurable period
(from 1 to 24 hours) for the set of attributes that triggered that specific alert.

To configure Alert Suppression for a profile:

1. To turn Alert Suppression on and off, click the toggle.

2. If Alert Suppression is on, select the Interval Hours from 1 hour to 24 hours. The

default is 24 hours.

3. Click Submit to save the settings.

Alert Suppression Process

This section further explains the alert suppression process summarized in the sentence: To
minimize excessive alerting, each alert type is triggered only once in a configurable period (from
1 to 24 hours) for the set of attributes that triggered that specific alert.

The set of attributes are the detected fields in an alert type. Examples include srcip, dstport,
OrganizationId, tenant_id, and file_path. Refer to the Alert Type Model Summary.

The process is as follows:

The set of attributes reaches the alert threshold.

Stellar Cyber checks if an alert with the same set of attributes has already been
triggered within the past X hours.

If yes, suppress (do not report) the current alert.

If no, report the alert.

For example, if the detection is based on the source IP address and the alert suppression period
is set to 6 hours, then alerts for the same source IP address will only be reported if their
timestamps are more than 6 hours apart.

The following diagram shows that the alerts with similar detected field attributes are suppressed.

Configuring New Detections and Rules

You can configure the preferences for any new detections or rules coming in a future release.
These preferences apply to the selected profile and do not impact existing detections.

To configure New Detections and Rules for a profile:

1. For Rules, you can change the preferences based on the grade:

Tier 1—ON, OFF, or SILENT. The default is ON.

Tier 2—ON, OFF, or SILENT. The default is ON.

Experimental—ON, OFF, or SILENT. The default is SILENT.

2. For ML detections, you can change the preferences to ON, OFF, or SILENT. The default

is ON.

3. For 3rd Party detections, you can change the preferences to ON, OFF, or SILENT. The

default is ON.

4. To set the detections back to the default settings, click Set detections states back to

default.

5. Click Submit to save the settings.

Using the Settings & Profiles Page

) at the top right of the Detection Management

Click Settings & Profiles or the gear icon (
page to open the Detection Settings page.

See the following:

Configuring Profiles

Configuring Tenant Assignment

Configuring Profiles

Profiles support multi-tenancy. They define the behavior of the detection mechanism states ON,
OFF, and SILENT.

You can assign several tenants to one profile, with those tenants sharing the same settings, or
you can create unique profiles for specific tenants. The maximum number of profiles is 30. Each
tenant can only be assigned to one profile.

The Profiles table displays the existing detection profiles and the number of tenants in each
profile. In the table, you can add and delete profiles, as well as change the name of a profile.

Click the Add new button to add a new profile. Enter a name and click Save. Newly created
profiles are based on the Default Profile.

If you hover over the name of a profile, an edit icon is available.

Click the edit icon (

) to change the name of a profile. Type the new name and click Save.

Click the trash icon (

) to delete a profile. You cannot delete the Default Profile.

You can edit profiles, including the Default Profile. See Configuring Detection Preferences.

To assign tenants to a profile, see Configuring Tenant Assignment.

Configuring Tenant Assignment

Click the Tenant Assignment tab to assign tenants to profiles or to see the tenants that are
assigned to a profile. The existing profiles are listed horizontally across the top of the table.

The Tenants table has the following columns:

Tenant Name

Tenant Group

Profile

In the Tenants table, you can:

Click each column heading (Tenant Name, Tenant Group, or Profile) to sort
alphabetically, ascending or descending.

Click the name of a profile next to Filter by profile to filter on that profile. The table
displays the tenants associated with that profile. Click the name of a selected profile to
de-select it or click All to remove filtering.

Use the search boxes, Search by tenant name and Search by tenant group, to

search by tenant name or tenant group. Click the filter icon (
keywords: Starts with, Contains, Not contains, Ends with, Equals, Not equals, and No
Filter.

) to include filtering

Use the dropdown menus on the right side of the Profile column to select a profile. A
tenant can only be assigned to a single profile.

Click one or more checkboxes for Tenant Name. The number of selected tenants is
shown. Use the dropdown menu to apply a profile to the selected tenants.

Creating Tenants and Tenant Groups

Tenants and Tenant Groups are created in the Stellar Cyber platform under System |
 ORGANIZATION MANAGEMENT. See Managing Tenants and Using Tenant Groups.

 A newly created tenant may not immediately appear when associating it with a Detection
Profile. Please allow up to 5 minutes for the tenant to become available on the Detection
Management profile page.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

