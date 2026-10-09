Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Using the Detection Tab in the Case Details
View

The Detection tab is the default display for the Case Detail view – it's what you see when you
first open the Detail view of a case. From here, you can get a high-level summary of the case,
including a breakdown of what Stellar Cyber has seen and why it is scoring the case the way it
is. You can also see a summary of the XDR Kill Chain stages involved, and a table of Associated
Alerts.

The figure below illustrates key features of the Detection tab:

Case Score Breakdown lists the XDR Kill Chain stages with associated alerts, as well
as the observables involved in the case (internal or external hosts, as well as URLs,
files, users, services, processes, and sensor status alerts).

 If AI Case Analysis is enabled in your version of the Stellar Cyber Platform, the
Case Score Breakdown is replaced by a Case Summary with a high-level
narrative of the case.

Automated Case Summary in the Detection Tab
When AI Case Analysis is enabled in Global Settings, you can run AI Case Analysis to accelerate
investigations with AI-generated narratives, insights, and suggested incident responses in the
Detection, Analysis, and Response tabs in the Case Detail view.

After running AI Case Analysis on a case, the Detection tab in the Case Detail view replaces the
Case Score Breakdown with a new, AI-generated Case Summary, as shown in the figure
below:

The Case Summary provides a high-level narrative of the case to help you quickly understand
the nature of the incident without reviewing every individual alert. This can reduce triage time by
giving you a fast, reliable entry point into an investigation.

The Case Summary includes the following information:

Overview – A concise explanation of the triggering activity and its immediate impact.

Key Insights – Highlights of the most important findings, such as compromised
accounts, suspicious reconnaissance, or exploit attempts.

Impact – A description of potential business and operational consequences, such as
data loss or compromised accounts.

Recommended Next Steps – A short list of high-level actions, such as forensic review
or account audits.

 You can use the one-click copy button at the base of the Case Summary to copy all four of

these sections for easy pasting elsewhere.

Next Steps with AI Case Analysis

For deeper case analysis, see the Hypothesis, Timeline, and Observables panels in
the Analysis tab.

For next steps and actionable response guidance for the case, see the Response tab.

Using the Associated Alerts Table
The Detection tab also provides the Associated Alerts table, a sortable table of all alerts
associated with the case.

In addition to standard Stellar Cyber table functionality for searching, sorting, exporting, and
column management, the Associated Alerts table lets you perform the following useful tasks for
a case:

Remove any alert in the table from an case by clicking its Delete button
Alternatively, you can bulk delete multiple alerts by selecting their entries in the table
and then clicking the Remove Alerts button. Regardless of the technique you choose,
Stellar Cyber asks you to confirm your choice before deleting the alert(s).

.

Note the following:

Deleting an alert from a case might change its score as Stellar Cyber
reevaluates the case in light of the new suite of associated alerts.

After you remove all alerts from a case, Stellar Cyber asks if you want to set
the case status to Cancelled, as shown below:

 You can also remove alerts from a case without deleting them by selecting their

check boxes in the table and then using the drop-down at the top of the table to set
their Event Status to either Ignored or Closed. This way, you can remove an alert
from a case without losing visibility of its previous existence.

Apply Quick Filters to the Associated Alerts table to focus the list on just those alerts
matching a selected Kill Chain stage. Remove a Quick Filter either by applying a
different one or using the Clear All button that appears when a Quick Filter is applied,

as illustrated below.

Select the More Info button for any alert in the Alerts table to see its associated Event
Details, including the supporting Interflow data. From here, you can find a Cases list
that shows other cases associated with an alert in descending order by score up to a
maximum of five. You can then drill into another related case detail display or use the
View All link at the top of the list to see a filtered tab showing only those cases
associated with the selected alert.

Cascade any alert open using the > button at the far left of the Alerts table to see its
associated Interflow data.

Add comments to one or more alerts by selecting their entries in the table and then
using the Add a Comment button.

Add the InSyncs column to the display to get more information about cases that are
synchronized with an associated ServiceNow installation using an InSync. You can
hover your mouse over the NOW icon in the InSyncs column and see the following
information on the synchronization for the case:

The name of the InSync performing the synchronization between Stellar Cyber
and the third-party application (ServiceNow in this release).

The status of the InSync (Synced, Paused, or Error).

The ticket number for the synchronized case in ServiceNow.

The last time the case was synchronized, expressed in the time zone of your
browser.

Use the Bulk Edit options to change information for multiple alerts simultaneously:

1. Select the check boxes for one or more alerts to enable the Bulk Edit controls.

You can change Status, Event Tags, or Assignee.

2. Select the field you want to edit.

3. Use the adjacent Bulk Edit drop-down to set the new value.

The available values change depending on which field you are editing.

Export the contents of the Associated Alerts table to a CSV file using the Export CSV
button.

 You can also export the case as a whole using the Export button in the Case

Identification panel at the top of the display
and a CSV file of the case.

. This technique exports both a PDF

Applying Display Filters to the Associated Alerts Table

The Associated Alerts table supports standard display filtering capabilities:

1. Select the vertical Filters button at the left of the table to see the available display

filters. For example:

2. You can filter by any combination of the listed criteria. If a particular criterion you expect

to see is not listed, use the Add new filter feature to see all available criteria.

Display filters apply to all table entries, not just those that are currently visible (for
example, if a table contains multiple pages of entries, the filter applies to all pages, not
just the currently visible page).

Display filters that are currently applied are displayed with a distinctive filter icon in their
entry. In addition, the currently displayed filters are summarized at the top of the table,
as shown below.

You can remove filter criteria individually by clicking the close icon ("x) in their entries at
the top of the table, or remove all filters with the Clear All button.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

