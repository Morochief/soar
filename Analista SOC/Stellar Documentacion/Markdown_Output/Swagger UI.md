Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Stellar Cyber API Reference

 6.6.0  OAS 3.1

This page lets you explore the different public APIs available for the Stellar Cyber Open XDR platform.

Stellar Cyber performs end-to-end threat detection and response, combining multiple capabilities – NG-

SIEM, NDR, TIP, IDS, SOAR, and UEBA – into a single user experience. Note: Entries in the reference

with a line through them still exist in the product but are deprecated (for example, the /cases API has

replaced the /incidents API, which is now deprecated).

Authorization Instructions:

1. If you don't already have an API key or token, get one from the user interface:

Scoped Key – Use the Create API Key button in the API Keys tab of the Edit User

and User Profile dialog boxes.

All-Access Token – Super Admins with root Scope can use the Generate Token

button in the API Access section of the Edit User dialog box.

2. Click the Authorize button on this page.

3. Log in differently depending on the credentials you're using:

Scoped Key – Use the api key (http, Bearer) option. Enter your API key in the

Value field and click Authorize.

All-Access Token – Use the basic (http, Basic) option. Enter the email address

tied to your account in the Username field and the token in the Password field,

then click Authorize.

⚠ Note: If you normally log in with a username, you must enter the

email address instead. Usernames will not work in the basic options.

4. Open the /access_token endpoint, click Try it out, and then Execute.

5. Copy only the green JWT token from the response.

💡 Tip: Don't use the Copy button — it copies the full response body. Select just
the green JWT token (inside quotation marks).

6. Click the Authorize button again.

7. Paste the copied JWT token into the jwt (http, Bearer) field and click Authorize.

🔁 Token Expiration: JWT tokens expire 10 minutes after creation. If you experience authorization
failures, repeat these steps to generate a new one.

Access Token

POST
POST

/access_token

AI Agent - Alert Management

GETGET

/ai/alerts/detail

AI Agent - Case Management

GETGET

/ai/cases/detail

Alert Types

GETGET

/alert_types

Alert Watcher

GETGET

/alert_watchers

PATCH
PATCH

/alert_watchers/{id}

POST
POST

/alert_watchers/export

POST
POST

/alert_watchers/import

POST
POST

/alert_watchers/import

/preflight

Auth

POST
POST

/reset_user

Auto Triage Management

PUTPUT

/auto_triage_management/{id}

AutoTriage Alert

/autotriage/v1/alert

POST
POST

/{stellar_uuid}/feedback/key-

findings/{finding_uuid}

/autotriage/v1/alert

POST
POST

/{stellar_uuid}/feedback

/summary

/autotriage/v1/alert

POST
POST

/{stellar_uuid}/feedback

/verdict

GETGET

/autotriage/v1/alert

/{stellar_uuid}/summary

POST
POST

/autotriage/v1/alert/feedback

/verdicts/batch

AutoTriage Case

GETGET

/autotriage/v1/case/{id}

/activities

POST
POST

/autotriage/v1/case/{id}

/feedback/summary

/autotriage/v1/case/{id}

/summary

/autotriage/v1/case/feedback

/verdicts/batch

GETGET

POST
POST

Case

GETGET

/cases

POST
POST

/cases

GETGET

/cases/{id}

PUTPUT

/cases/{id}

GETGET

/cases/{id}/activities

GETGET

/cases/{id}/activity/score

GETGET

/cases/{id}/alerts

POST
POST

/cases/{id}/alerts

PUTPUT

/cases/{id}/alerts{action}

GETGET

/cases/{id}/comments

POST
POST

/cases/{id}/comments

PUTPUT

/cases/{id}/comments

/{commentId}

DELETE
DELETE

/cases/{id}/comments

/{commentId}

GETGET

/cases/{id}/details

GETGET

/cases/{id}/observables

GETGET

/cases/{id}/scores

GETGET

/cases/{id}/summary

GETGET

/cases/{id}/updates

GETGET

/cases/assignees

GETGET

/cases/health

POST
POST

/cases/insyncs/alert

POST
POST

/cases/insyncs/case

GETGET

/cases/minmax

GETGET

/cases/tags

Connector

DELETE
DELETE

/connectors

POST
POST

/connectors

PUTPUT

/connectors

GETGET

/connectors

GETGET

/connectors/{id}

PUTPUT

/connectors/{id}/check-point

GETGET

/connectors/{id}/check-point

DELETE
DELETE

/connectors/{id}/check-point

Custom Log Parser

POST
POST

/custom_log_parsers

GETGET

/custom_log_parsers

PUTPUT

/custom_log_parsers/{name}

DELETE
DELETE

/custom_log_parsers/{name}

GETGET

/custom_log_parsers/parsers

Custom Response Action

GETGET

/custom_response_actions

GETGET

/custom_response_actions/email

GETGET

/custom_response_actions

/endpoint

/custom_response_actions

PUTPUT

/endpoint/{action_type}

/{action_id}/revert

POST
POST

/custom_response_actions

/endpoint/bitdefender

POST
POST

/custom_response_actions

/endpoint/crowdstrike

POST
POST

/custom_response_actions

/endpoint/cybereason

POST
POST

/custom_response_actions

/endpoint/cylance

POST
POST

/custom_response_actions

/endpoint/cynet

POST
POST

/custom_response_actions

/endpoint/deep_instinct

POST
POST

POST
POST

/custom_response_actions

/endpoint/forescout

/custom_response_actions

/endpoint/microsoft_defender

/custom_response_actions

POST
POST

/endpoint

/palo_alto_networks_cortex

POST
POST

/custom_response_actions

/endpoint/sentinelone

POST
POST

/custom_response_actions

/endpoint/sonicwallcc

POST
POST

/custom_response_actions

/endpoint/sophos

POST
POST

/custom_response_actions

/endpoint/vmware_carbonblack

POST
POST

/custom_response_actions

/entra_id/{action_type}

/custom_response_actions

PUTPUT

/entra_id/{action_type}

/{action_id}/revert

GETGET

/custom_response_actions

/firewall

POST
POST

/custom_response_actions

/firewall/{action_type}

/custom_response_actions

PUTPUT

/firewall/{action_type}

/{action_id}/revert

GETGET

/custom_response_actions/idp

POST
POST

/custom_response_actions/idp

/{action_type}

/custom_response_actions/idp

PUTPUT

/{action_type}/{action_id}

/revert

GETGET

GETGET

GETGET

GETGET

/custom_response_actions/idp

/active_directory

/custom_response_actions/idp

/entra_id

/custom_response_actions

/run_script

/custom_response_actions

/security_switch

POST
POST

/custom_response_actions

/security_switch/{action_type}

/custom_response_actions

PUTPUT

/security_switch/{action_type}

/{action_id}/revert

POST
POST

GETGET

/custom_response_actions

/webhook

/custom_response_actions

/webhook

Custom Response Action (Deprecated)

GETGET/custom_response_actionGETGET/custom_response_action/active_directoryPOSTPOST/custom_response_action/active_directoryPUTPUT/custom_response_action/active_directory/{connector_id}/revertGETGET/custom_response_action/emailGETGET/custom_response_action/endpointPOSTPOST/custom_response_action/endpointGETGET/custom_response_action/entra_idPOSTPOST/custom_response_action/entra_idPUTPUT/custom_response_action/entra_id/{connector_id}/revertGETGET/custom_response_action/firewallPOSTPOST/custom_response_action/firewallPUTPUT/custom_response_action/firewall/{connector_id}/revertGETGET/custom_response_action/run_scriptGETGET/custom_response_action/security_switchPOSTPOST/custom_response_action/security_switchCustom Security Event

GETGET

/custom_security_events

POST
POST

/custom_security_events/_bulk

Data Sensor

GETGET

/data_sensors

GETGET

/data_sensors/{sensor_id}

DELETE
DELETE

/data_sensors/{sensor_id}

POST
POST

POST
POST

POST
POST

POST
POST

/data_sensors/{sensor_id}

/assign

/data_sensors/{sensor_id}

/authorize

/data_sensors/{sensor_id}

/deauthorize

/data_sensors/{sensor_id}

/upgrade

GETGET

/data_sensors/sensor_profiles

GETGET

/data_sensors/upgrade_versions

Detection Management

PUTPUT/custom_response_action/security_switch/{connector_id}/revertGETGET/custom_response_action/webhookGETGET

/detections

GETGET

/detections/profiles

DR Profile

GETGET

/dr_profiles

POST
POST

/dr_profiles

GETGET

/dr_profiles/{name}

PUTPUT

/dr_profiles/{name}

DELETE
DELETE

/dr_profiles/{name}

Entity Usage

GETGET

GETGET

/entity_usages/daily_count

/{scope}

/entity_usages/entity_list

/{scope}

HyperAutomation Alert

GETGET

GETGET

/hyperautomation/v1/alert

/{correlation_id}/findings

/hyperautomation/v1/alert

/{correlation_id}/summary

Incident

GETGET/incidentsPOSTPOST/incidentsIngestion Stats

GETGET

/ingestion-stats/connector

GETGET

/ingestion-stats/log-source

GETGET

/ingestion-stats/log-type

GETGET

/ingestion-stats/sensor

Log Filter

GETGET

/log_filters

POST
POST

/log_filters

GETGET

/log_filters/{id}

PUTPUT

/log_filters/{id}

DELETE
DELETE

/log_filters/{id}

Log Forward Filter

GETGET/incidents/{id}/observablesGETGET/logfwd_filtersPOSTPOST/logfwd_filtersGETGET/logfwd_filters/{id}Lookup

GETGET

/lookups

POST
POST

/lookups

GETGET

/lookups/{id}

PUTPUT

/lookups/{id}

DELETE
DELETE

/lookups/{id}

Phone Home

GETGET

/phonehomes

Privilege Profile

GETGET

/privilege_profiles/_names

Query

GETGET

/queries

POST
POST

/queries

POST
POST

/queries/_batch

PUTPUT/logfwd_filters/{id}DELETEDELETE/logfwd_filters/{id}GETGET

/queries/{id}

PUTPUT

/queries/{id}

DELETE
DELETE

/queries/{id}

POST
POST

/queries/export

POST
POST

/queries/import

POST
POST

/queries/import/preflight

Report Config

GETGET

/report-configs

POST
POST

/report-configs

DELETE
DELETE

/report-configs/{id}

Rule

GETGET

/rules

GETGET

/rules/{id}

DELETE
DELETE

/rules/{id}

GETGET

/rules/connector-monitoring

POSTPOST/rules/connector-monitoringGETGET

POST
POST

PUTPUT

POST
POST

PUTPUT

GETGET

GETGET

/rules/connector-monitoring

/{type}

/rules/connector-monitoring

/no-data

/rules/connector-monitoring

/no-data/{id}

/rules/connector-monitoring

/status-change

/rules/connector-monitoring

/status-change/{id}

/rules/device-sensor-

monitoring

/rules/device-sensor-

monitoring/{type}

POST
POST

/rules/device-sensor-

monitoring/feedback

PUTPUT

/rules/device-sensor-

monitoring/feedback/{id}

POST
POST

/rules/device-sensor-

monitoring/ingestion

PUTPUT

/rules/device-sensor-

monitoring/ingestion/{id}

POST
POST

/rules/device-sensor-

monitoring/no-data

PUTPUT

/rules/device-sensor-

monitoring/no-data/{id}

POST
POST

/rules/device-sensor-

monitoring/no-heartbeat

PUTPUT

/rules/device-sensor-

monitoring/no-heartbeat/{id}

POST
POST

/rules/device-sensor-

monitoring/status-change

PUTPUT

/rules/device-sensor-

monitoring/status-change/{id}

GETGET

/rules/license-enforcement

GETGET

POST
POST

/rules/license-enforcement

/{type}

/rules/license-enforcement

/license-in-undesirable-state

/rules/license-enforcement

PUTPUT

/license-in-undesirable-state

/{id}

POST
POST

/rules/license-enforcement

/license-limit-exceeded

PUTPUT

/rules/license-enforcement

/license-limit-exceeded/{id}

GETGET

/rules/license-usage

GETGET

/rules/license-usage/{type}

POST
POST

/rules/license-usage/asset-

threshold-exceeded

PUTPUT

/rules/license-usage/asset-

threshold-exceeded/{id}

POST
POST

/rules/license-usage

/ingestion-threshold-exceeded

/rules/license-usage

PUTPUT

/ingestion-threshold-exceeded

/{id}

GETGET

GETGET

/rules/server-sensor-

monitoring

/rules/server-sensor-

monitoring/{type}

POST
POST

/rules/server-sensor-

monitoring/no-data

PUTPUT

/rules/server-sensor-

monitoring/no-data/{id}

POST
POST

/rules/server-sensor-

monitoring/no-heartbeat

PUTPUT

/rules/server-sensor-

monitoring/no-heartbeat/{id}

POST
POST

/rules/server-sensor-

monitoring/status-change

PUTPUT

/rules/server-sensor-

monitoring/status-change/{id}

Security Event

POST
POST

/insert_ser

POST
POST

/insert_ser_bulk

POST
POST

/security_events/{index}/{id}

PUTPUT

PUTPUT

/security_events/{index}/{id}

/comments

/security_events/{index}/{id}

/status

PATCH
PATCH

/security_events/{index}/{id}

/tags

POST
POST

/security_events/{index}/{id}

/tags/delete

POST
POST

/upsert_ser_bulk

Security Event Filter

GETGET

/security_event_filters

POST
POST

/security_event_filters

PUTPUT

/security_event_filters/{id}

DELETE
DELETE

/security_event_filters/{id}

DELETEDELETE/security_events/{index}/{id}/tagsPOSTPOST/update_serSensor Image

GETGET

/sensor-images

GETGET

/sensor-images/download

/{version}/{image}

Storage Usage

GETGET

/storage-usages

GETGET

/storage-usages

/daily_and_monthly

Tenant

GETGET

/tenants

POST
POST

/tenants

GETGET

/tenants/{cust_id}/logo

DELETE
DELETE

/tenants/{id}

GETGET

/tenants/{id}

PUTPUT

/tenants/{id}

PATCH
PATCH

/tenants/{id}

GETGET

/tenants/{id}/delete_check

Tenant Group

GETGET

/tenant_groups

POST
POST

/tenant_groups

GETGET

/tenant_groups/{id}

PUTPUT

/tenant_groups/{id}

PATCH
PATCH

/tenant_groups/{id}

DELETE
DELETE

/tenant_groups/{id}

User

GETGET

/users

POST
POST

/users

GETGET

/users/{id}

PUTPUT

/users/{id}

PATCH
PATCH

/users/{id}

DELETE
DELETE

/users/{id}

GETGET

/users/homepage_options

GETGET/tenant_groups/{id}/logoUser Activity

GETGET

/user_activities

5.5.0

GETGET/custom_response_actionGETGET/custom_response_action/active_directoryPOSTPOST/custom_response_action/active_directoryPUTPUT/custom_response_action/active_directory/{connector_id}/revertGETGET/custom_response_action/emailGETGET/custom_response_action/endpointPOSTPOST/custom_response_action/endpointGETGET/custom_response_action/entra_idPOSTPOST/custom_response_action/entra_idPUTPUT/custom_response_action/entra_id/{connector_id}/revertGETGET/custom_response_action/firewallPOSTPOST/custom_response_action/firewallPUTPUT/custom_response_action/firewall/{connector_id}/revertGETGET

/queries

POST
POST

/queries

POST
POST

/queries/_batch

GETGET

/queries/{id}

PUTPUT

/queries/{id}

DELETE
DELETE

/queries/{id}

GETGET

/storage-usages

/daily_and_monthly

6.0.0

PUTPUT

/auto_triage_management/{id}

6.1.0

GETGET/custom_response_action/run_scriptGETGET/custom_response_action/security_switchPOSTPOST/custom_response_action/security_switchPUTPUT/custom_response_action/security_switch/{connector_id}/revertGETGET/custom_response_action/webhookPOST
POST

POST
POST

POST
POST

POST
POST

/data_sensors/{sensor_id}

/assign

/data_sensors/{sensor_id}

/authorize

/data_sensors/{sensor_id}

/deauthorize

/data_sensors/{sensor_id}

/upgrade

GETGET

/data_sensors/sensor_profiles

GETGET

/data_sensors/upgrade_versions

GETGET

/entity_usages/daily_count

/{scope}

6.2.0

/autotriage/v1/alert

POST
POST

/{stellar_uuid}/feedback/key-

findings/{finding_uuid}

/autotriage/v1/alert

POST
POST

/{stellar_uuid}/feedback

/summary

/autotriage/v1/alert

POST
POST

/{stellar_uuid}/feedback

/verdict

GETGET

/autotriage/v1/alert

/{stellar_uuid}/summary

POSTPOST/rules/connector-monitoringPOST
POST

GETGET

/autotriage/v1/alert/feedback

/verdicts/batch

/autotriage/v1/case/{id}

/activities

POST
POST

/autotriage/v1/case/{id}

/feedback/summary

GETGET

POST
POST

/autotriage/v1/case/{id}

/summary

/autotriage/v1/case/feedback

/verdicts/batch

GETGET

/custom_response_actions

GETGET

/custom_response_actions/email

GETGET

/custom_response_actions

/endpoint

/custom_response_actions

PUTPUT

/endpoint/{action_type}

/{action_id}/revert

POST
POST

/custom_response_actions

/endpoint/bitdefender

POST
POST

/custom_response_actions

/endpoint/crowdstrike

POST
POST

/custom_response_actions

/endpoint/cybereason

POST
POST

/custom_response_actions

/endpoint/cylance

POST
POST

/custom_response_actions

/endpoint/cynet

POST
POST

/custom_response_actions

/endpoint/deep_instinct

POST
POST

/custom_response_actions

/endpoint/forescout

POST
POST

/custom_response_actions

/endpoint/microsoft_defender

/custom_response_actions

POST
POST

/endpoint

/palo_alto_networks_cortex

POST
POST

/custom_response_actions

/endpoint/sentinelone

POST
POST

/custom_response_actions

/endpoint/sonicwallcc

POST
POST

/custom_response_actions

/endpoint/sophos

POST
POST

/custom_response_actions

/endpoint/vmware_carbonblack

POST
POST

/custom_response_actions

/entra_id/{action_type}

/custom_response_actions

PUTPUT

/entra_id/{action_type}

/{action_id}/revert

GETGET

/custom_response_actions

/firewall

POST
POST

/custom_response_actions

/firewall/{action_type}

/custom_response_actions

PUTPUT

/firewall/{action_type}

/{action_id}/revert

GETGET

/custom_response_actions/idp

POST
POST

/custom_response_actions/idp

/{action_type}

/custom_response_actions/idp

PUTPUT

/{action_type}/{action_id}

/revert

GETGET

GETGET

GETGET

GETGET

/custom_response_actions/idp

/active_directory

/custom_response_actions/idp

/entra_id

/custom_response_actions

/run_script

/custom_response_actions

/security_switch

POST
POST

/custom_response_actions

/security_switch/{action_type}

/custom_response_actions

PUTPUT

/security_switch/{action_type}

/{action_id}/revert

POST
POST

GETGET

/custom_response_actions

/webhook

/custom_response_actions

/webhook

GETGET

/detections

GETGET

/detections/profiles

/hyperautomation/v1/alert

/{correlation_id}/findings

/hyperautomation/v1/alert

/{correlation_id}/summary

GETGET

GETGET

6.3.0

GETGET

/ai/alerts/detail

GETGET

/ai/cases/detail

6.4.0

GETGET

/rules

GETGET

/rules/{id}

POST
POST

POST
POST

/rules/connector-monitoring

/no-data

/rules/connector-monitoring

/status-change

POST
POST

/rules/device-sensor-

monitoring/feedback

POST
POST

/rules/device-sensor-

monitoring/ingestion

POST
POST

/rules/device-sensor-

monitoring/no-data

POST
POST

/rules/device-sensor-

monitoring/no-heartbeat

POST
POST

/rules/device-sensor-

monitoring/status-change

POST
POST

/rules/server-sensor-

monitoring/no-data

POST
POST

/rules/server-sensor-

monitoring/no-heartbeat

POST
POST

/rules/server-sensor-

monitoring/status-change

6.5.0

POST
POST

/alert_watchers/export

POST
POST

/alert_watchers/import

POST
POST

/alert_watchers/import

/preflight

POST
POST

/queries/export

POST
POST

/queries/import

POST
POST

/queries/import/preflight

DELETE
DELETE

/rules/{id}

GETGET

/rules/connector-monitoring

GETGET

/rules/connector-monitoring

/{type}

PUTPUT

PUTPUT

GETGET

GETGET

PUTPUT

PUTPUT

PUTPUT

PUTPUT

PUTPUT

GETGET

GETGET

PUTPUT

PUTPUT

PUTPUT

/rules/connector-monitoring

/no-data/{id}

/rules/connector-monitoring

/status-change/{id}

/rules/device-sensor-

monitoring

/rules/device-sensor-

monitoring/{type}

/rules/device-sensor-

monitoring/feedback/{id}

/rules/device-sensor-

monitoring/ingestion/{id}

/rules/device-sensor-

monitoring/no-data/{id}

/rules/device-sensor-

monitoring/no-heartbeat/{id}

/rules/device-sensor-

monitoring/status-change/{id}

/rules/server-sensor-

monitoring

/rules/server-sensor-

monitoring/{type}

/rules/server-sensor-

monitoring/no-data/{id}

/rules/server-sensor-

monitoring/no-heartbeat/{id}

/rules/server-sensor-

monitoring/status-change/{id}

6.6.0

GETGET

/rules/license-enforcement

GETGET

/rules/license-enforcement

/{type}

POST
POST

/rules/license-enforcement

/license-in-undesirable-state

/rules/license-enforcement

PUTPUT

/license-in-undesirable-state

/{id}

POST
POST

/rules/license-enforcement

/license-limit-exceeded

PUTPUT

/rules/license-enforcement

/license-limit-exceeded/{id}

GETGET

/rules/license-usage

GETGET

/rules/license-usage/{type}

POST
POST

/rules/license-usage/asset-

threshold-exceeded

PUTPUT

/rules/license-usage/asset-

threshold-exceeded/{id}

POST
POST

/rules/license-usage

/ingestion-threshold-exceeded

/rules/license-usage

PUTPUT

/ingestion-threshold-exceeded

/{id}

Schemas

Record_string.number_

Expand all object

UserScope

Expand all string

User

Expand all object

UsersResponse

Expand all object

UserResponse

Expand all object

UserForExternalCreateRequest

Expand all object

Pick_UserCore.Exclude_keyofUserCore.name-or-email__

Expand all object

UserForExternalUpdateRequest

Expand all object

UserForExternalPatchRequest

Expand all object

HomepageOption

Expand all object

HomepageOptionsResponse

Expand all object

InsertSerBulkResponse

Expand all object

EventStatusType

Expand all string

InsertSerRequest

Expand all object

InsertSerBulkRequest

Expand all object

UpdateSerResponse any

EventTag

Expand all object

EventStatus

Expand all string

UpdateSerRequest

Expand all object

ESRefreshOption

Expand all string

TenantGroup

Expand all object

CreateTenantGroupRequest

Expand all object

UpdateTenantGroupRequest

Expand all object

GetTenantGroupLogoResponse

Expand all object

TenantPurgeCheckResponse

Expand all object

AUTH_SSO_SAML

Expand all string

AUTH_SYS_DEFAULT

Expand all string

AUTH_LOCAL

Expand all string

AuthenticationMethodType

Expand all (any | any | any)

Tenant

Expand all object

TenantRequestWithId

Expand all object

TenantRequest

Expand all object

GetTenantLogoResponse

Expand all object

StorageUsage

Expand all object

StorageUsageByTime

Expand all object

StorageUsagesResponse

Expand all object

StorageUsageAggregationQuery

Expand all string

MonthlyAndDailyUsageByTenant

Expand all object

StorageUsagesByTenantResponse

Expand all object

SensorImageEntry

Expand all object

SensorImagesInfo

Expand all object

SensorImagesInfoResponse

Expand all object

UnifiedFilterType

Expand all string

QueryGroup

Expand all object

QueryConditionBase

Expand all object

StringOperator

Expand all string

ExistsOperator

Expand all string

ExistsQueryCondition

Expand all object

LookupOperator

Expand all string

LookupQueryCondition

Expand all object

StringQueryCondition

Expand all (any & object & (object | object | any | any))

SingleNumberOperator

Expand all string

MultiNumberOperator

Expand all string

NumberQueryCondition

Expand all (any & object & (object | object | object |

any | any))

DateQueryCondition

Expand all (any & object & (object | object | object | any |

any))

IpOperator

Expand all string

IpQueryCondition

Expand all (any & object & (object | any | any))

BooleanOperator

Expand all string

BooleanQueryCondition

Expand all (any & object & (object | any))

QueryCondition

Expand all (any | any | any | any | any)

QueryStringCondition

Expand all object

AnyFunction

Expand all object

AllFunction

Expand all object

CountFunction

Expand all (object & (object | object | object))

MaxFunction

Expand all (object & (object | object | object))

MinFunction

Expand all (object & (object | object | object))

SumFunction

Expand all (object & (object | object | object))

AvgFunction

Expand all (object & (object | object | object))

CardinalityFunction

Expand all (object & (object | object | object))

AggregationFunction

Expand all (any | any | any | any | any | any | any | any)

AggregationCondition

Expand all (any & object)

RelativeRange

Expand all object

AbsoluteRange

Expand all object

UnifiedFilterTimeRange

Expand all (any | any)

Record_string.any_

Expand all object

UnifiedFilterMetadata

Expand all object

AlertFilter

Expand all object

SecurityEventFiltersResponse

Expand all object

SecurityEventFilterResponse

Expand all object

AlertFilterPeriod

Expand all string

AlertFilterCustomTimeRange

Expand all object

Record_string.unknown_

Expand all object

SecurityEventFilterFormData

Expand all object

SecurityEventResponse

Expand all object

SecurityEventRequest

Expand all object

UpdateAddTagsRequest

Expand all object

UpdateDeleteTagsRequest

Expand all object

UpdateStatusRequest

Expand all object

UpdateCommentsRequest

Expand all object

MonitoringRuleCreateResponse

Expand all object

ExternalEmailNotificationConfig

Expand all object

ExternalSlackNotificationConfig

Expand all object

ExternalCreateConnectorMonitoringRuleFormData

Expand all object

IntervalUnitType

Expand all (object | object | object)

EmailNotificationConfig

Expand all object

SlackNotificationConfig

Expand all object

CreateConnectorMonitoringRuleNoDataForm

Expand all object

FieldTypeExcludedTenants

Expand all object

FieldTypeConnectorTypes

Expand all object

ExternalCreateConnectorMonitoringRuleNoDataFormData

Expand all (any &

any & any)

MonitoringRuleUpdateResponse

Expand all object

UpdateConnectorMonitoringRuleNoDataForm

Expand all object

ExternalUpdateConnectorMonitoringRuleNoDataFormData

Expand all (any &

any & any)

CreateConnectorMonitoringRuleStatusChangeForm

Expand all object

ExternalCreateConnectorMonitoringRuleStatusChangeFormData

Expand all

(any & any & any)

UpdateConnectorMonitoringRuleStatusChangeForm

Expand all object

ExternalUpdateConnectorMonitoringRuleStatusChangeFormData

Expand all

(any & any & any)

CreateDeviceSensorMonitoringRuleFeedbackForm

Expand all object

ExternalCreateDeviceSensorMonitoringRuleFeedbackFormData

Expand all

any

UpdateDeviceSensorMonitoringRuleFeedbackForm

Expand all object

ExternalUpdateDeviceSensorMonitoringRuleFeedbackFormData

Expand all

any

CreateDeviceSensorMonitoringRuleIngestionForm

Expand all object

ExternalCreateDeviceSensorMonitoringRuleIngestionFormData

Expand all

any

UpdateDeviceSensorMonitoringRuleIngestionForm

Expand all object

ExternalUpdateDeviceSensorMonitoringRuleIngestionFormData

Expand all

any

CreateDeviceSensorMonitoringRuleNoDataForm

Expand all object

ExternalCreateDeviceSensorMonitoringRuleNoDataFormData

Expand all

(any & any)

UpdateDeviceSensorMonitoringRuleNoDataForm

Expand all object

ExternalUpdateDeviceSensorMonitoringRuleNoDataFormData

Expand all

(any & any)

CreateDeviceSensorMonitoringRuleNoHeartbeatForm

Expand all object

ExternalCreateDeviceSensorMonitoringRuleNoHeartbeatFormData

Expand all any

UpdateDeviceSensorMonitoringRuleNoHeartbeatForm

Expand all object

ExternalUpdateDeviceSensorMonitoringRuleNoHeartbeatFormData

Expand all any

CreateDeviceSensorMonitoringRuleStatusChangeForm

Expand all object

ExternalCreateDeviceSensorMonitoringRuleStatusChangeFormData

Expand all (any & any)

UpdateDeviceSensorMonitoringRuleStatusChangeForm

Expand all object

ExternalUpdateDeviceSensorMonitoringRuleStatusChangeFormData

Expand all (any & any)

ScheduleDayType

Expand all string

ScheduleTimeType

Expand all string

MuteSchedule

Expand all object

CreateServerSensorMonitoringRuleNoDataForm

Expand all object

ExternalCreateServerSensorMonitoringRuleNoDataFormData

Expand all

(any & any)

UpdateServerSensorMonitoringRuleNoDataForm

Expand all object

ExternalUpdateServerSensorMonitoringRuleNoDataFormData

Expand all

(any & any)

CreateServerSensorMonitoringRuleNoHeartbeatForm

Expand all object

ExternalCreateServerSensorMonitoringRuleNoHeartbeatFormData

Expand all any

UpdateServerSensorMonitoringRuleNoHeartbeatForm

Expand all object

ExternalUpdateServerSensorMonitoringRuleNoHeartbeatFormData

Expand all any

CreateServerSensorMonitoringRuleStatusChangeForm

Expand all object

ExternalCreateServerSensorMonitoringRuleStatusChangeFormData

Expand all (any & any)

UpdateServerSensorMonitoringRuleStatusChangeForm

Expand all object

ExternalUpdateServerSensorMonitoringRuleStatusChangeFormData

Expand all (any & any)

CreateLicenseInUndesirableStateRuleForm

Expand all object

ExternalCreateLicenseInUndesirableStateRuleFormData

Expand all any

UpdateLicenseInUndesirableStateRuleForm

Expand all object

ExternalUpdateLicenseInUndesirableStateRuleFormData

Expand all any

CreateLicenseLimitExceededRuleForm

Expand all object

ExternalCreateLicenseLimitExceededRuleFormData

Expand all any

UpdateLicenseLimitExceededRuleForm

Expand all object

ExternalUpdateLicenseLimitExceededRuleFormData

Expand all any

CreateLicenseUsageAssetThresholdExceededForm

Expand all object

FieldTypeMonitoredTenants

Expand all object

ExternalCreateLicenseUsageAssetThresholdExceededFormData

Expand all

(any & any)

UpdateLicenseUsageAssetThresholdExceededForm

Expand all object

ExternalUpdateLicenseUsageAssetThresholdExceededFormData

Expand all

(any & any)

CreateLicenseUsageIngestionThresholdExceededForm

Expand all object

ExternalCreateLicenseUsageIngestionThresholdExceededFormData

Expand all (any & any)

UpdateLicenseUsageIngestionThresholdExceededForm

Expand all object

ExternalUpdateLicenseUsageIngestionThresholdExceededFormData

Expand all (any & any)

RuleScope

Expand all string

RuleEventMuteMode

Expand all string

RuleEventMute

Expand all object

RuleRuleCheckMode

Expand all string

RuleVisibility

Expand all string

RuleCheckParamsFieldOption

Expand all object

RuleCheckParamsField

Expand all object

RuleCheckParamsMode

Expand all object

RuleCheckLicenseUsageMode

Expand all string

RuleCheckLicenseUsage

Expand all object

RuleCheckSensorMonitoringMode

Expand all string

RuleCheckSensorMonitoring

Expand all object

RuleCheckConnectorMonitoringMode

Expand all string

RuleCheckConnectorMonitoring

Expand all object

RuleCheckLogSourceMonitoringMode

Expand all string

RuleCheckLogSourceMonitoring

Expand all object

RuleCheckCaseManagementMode

Expand all string

RuleCheckCaseManagement

Expand all object

RuleCheckParams

Expand all object

RuleCheck

Expand all object

RuleActionType

Expand all string

RuleActionEmail

Expand all object

RuleActionSlack

Expand all object

RuleActionWebhook

Expand all object

RuleActionParams

Expand all object

RuleActionBody

Expand all object

RuleAction

Expand all object

RuleState

Expand all string

RuleStatus

Expand all string

RuleDeploymentMode

Expand all string

RuleExecuteResult

Expand all object

RuleResultEvent

Expand all object

RuleResult

Expand all object

RuleReference

Expand all object

RulePurpose

Expand all string

RuleContentConfig

Expand all object

Rule

Expand all object

RulesResp

Expand all object

RuleConnectorMonitoringType

Expand all string

RuleDeviceSensorMonitoringType

Expand all string

RuleLicenseEnforcementType

Expand all string

RuleLicenseUsageType

Expand all string

RuleServerSensorMonitoringType

Expand all string

RuleResp

Expand all object

ReportProgressStatus

Expand all string

ReportConfigJobStatus

Expand all object

ReportConfigAvailabilityAllowed

Expand all object

ReportConfigAvailabilityDeniedReason

Expand all object

ReportConfigAvailability

Expand all object

ReportConfigPageOrientation

Expand all string

ReportFrequency

Expand all string

ReportConfig

Expand all object

ReportConfigV2

Expand all object

ReportConfigsResponse

Expand all object

ReportConfigResponse

Expand all object

ReportConfigReportTimeRange

Expand all string

ReportConfigReportTimeRangeRelative

Expand all string

ReportConfigReportTableSize

Expand all string

ReportConfigReportWeekDay

Expand all string

ReportConfigMonthDay

Expand all string

ReportConfigMonthDayV2

Expand all string

ReportNthDayOfMonthOptions

Expand all string

ReportNthWeekOfMonthOption

Expand all string

ReportConfigDaily

Expand all object

ReportConfigWeekly

Expand all object

ReportConfigMonthly

Expand all object

ReportConfigFrequency

Expand all (any | any | any)

ReportConfigFormData

Expand all (object & any)

ReportConfigV2FormData

Expand all (object & any)

Aggregation

Expand all object

Expressions

Expand all object

QuerySort

Expand all object

QueryMetadata

Expand all (any & object)

Query

Expand all object

QueriesResponse

Expand all object

QueryResponse

Expand all object

QueryFormData

Expand all object

BatchCreateQueryResponse

Expand all object

BatchCreateQueryFormData

Expand all object

Partial_QueryFormData_

Expand all object

ExportSourceDTO

Expand all object

ExportConfigurationDTO

Expand all object

ExportMetadataDTO

Expand all object

ObjectMetadataDTO

Expand all object

SerializedObjectDTO_query_

Expand all object

SerializedObjectDTO

Expand all object

DependencyNodeDTO_string_

Expand all object

DependencyType

Expand all string

DependencyEdgeDTO_DependencyType_

Expand all object

DependencyGraphDTO_string.DependencyType_

Expand all object

ExportPackageDTO_query.DependencyType_

Expand all object

QueryExportPackageDTO

Expand all any

ExportRequest_query_

Expand all object

QueryExportRequest

Expand all any

ImportValidationError

Expand all object

ImportValidationWarning

Expand all object

ConflictType

Expand all string

ConflictResolutionStrategy

Expand all string

ConflictDTO

Expand all object

PreflightSummary

Expand all object

ImportPreflightResponse

Expand all object

ImportPreflightRequest_query.DependencyType_

Expand all object

QueryImportPreflightRequest

Expand all any

ObjectImportResultDTO

Expand all object

ImportExecuteResponse

Expand all object

ConflictResolutionDTO

Expand all object

Record_string.ConflictResolutionDTO_

Expand all object

ImportExecuteRequest_query.DependencyType_

Expand all object

QueryImportExecuteRequest

Expand all any

PrivilegeProfileName

Expand all object

PhoneHome

Expand all object

PhoneHomeResponse

Expand all object

Record_string.string-Array_

Expand all object

LookupTypeString

Expand all string

LookupTypeValuePairString

Expand all object

LookupTypeNumber

Expand all string

LookupTypeValuePairNumber

Expand all object

Lookup

Expand all (object & (any | any))

LookupsResponse

Expand all object

LookupResponse

Expand all object

LookupFormData

Expand all (object & (any | any))

LogfwdFilter

Expand all object

LogfwdFiltersResponse

Expand all object

LogfwdFilterResponse

Expand all object

LogfwdFilterFormData

Expand all object

InsertSerResponse

Expand all object

Ingestion

Expand all object

IngestionsResponse

Expand all object

ExternalIncident

Expand all object

IncidentsResponse_ExternalIncident_

Expand all object

EditIncidentRequest

Expand all object

File

Expand all object

Process

Expand all object

Host

Expand all object

UserInfo

Expand all object

Registry

Expand all object

Sensor

Expand all object

Service

Expand all object

Url

Expand all object

IObservableData

Expand all object

IGObservableData

Expand all any

EntityUsageTenantCountResponse

Expand all object

EntityUsageGroupCountResponse

Expand all object

EntityUsageAllCountResponse

Expand all object

EntityUsageDailyCountResponse

Expand all (array<any> | array<any> |

array<any>)

EntityUsageDailyCountScopeType

Expand all string

EntityUsageTenantListResponseExternal

Expand all object

EntityUsageGroupListResponse

Expand all object

EntityUsageEntityListResponseExternal

Expand all (array<any> | array<any>)

EntityUsageEntityListScopeType

Expand all string

DRProfile

Expand all object

CreateDRProfileRequest

Expand all object

UpdateDRProfileRequest

Expand all object

ProfileSettings

Expand all object

DetectionProfile

Expand all object

ProfileListResponse

Expand all object

DataSourceSimple

Expand all object

DetectionRuleV2Setting

Expand all object

DetectionRuleV2Stat

Expand all object

RuleQuery

Expand all object

LogSource

Expand all object

Tactic

Expand all object

Technique

Expand all object

TTP

Expand all object

DetectionRuleV2

Expand all object

Datafeed

Expand all object

DetectionAlertType

Expand all object

DetectionSetting

Expand all object

DetectionStat

Expand all object

DetectionV2WithDataSourcesAndRules

Expand all object

DetectionListResponseV2WithDataSources

Expand all object

DataSensor

Expand all object

DataSensorsResponse

Expand all object

SifterPolicy

Expand all object

SensorUpgradeRequest

Expand all object

Device

Expand all object

SensorAuthorizationResponse

Expand all object

AuthorizeLicensesRequestBody

Expand all object

DeauthorizeLicensesRequestBody

Expand all object

CustomSecurityEventAction

Expand all object

CustSecEventKeyFields

Expand all object

CustomSecurityEvent

Expand all object

RefinedCustomSecurityEvent

Expand all any

CustomSecurityEventsResponse

Expand all object

CustSecEventCreateBulkResponse

Expand all object

CustSecEventCreateData

Expand all object

CustSecEventCreateBulkRequest

Expand all object

CustomResponseAction

Expand all object

ActiveDirectoryActionType

Expand all string

Duration

Expand all (object | object | object | string)

DurationField

Expand all object

CreateActiveDirectoryActionRequest

Expand all object

RevertActiveDirectoryActionRequest

Expand all object

FirewallActionType

Expand all string

CIDR string

CreateFirewallActionRequest

Expand all object

RevertFirewallActionRequest

Expand all object

EntraIdActionType

Expand all string

CreateEntraIdActionRequest

Expand all object

RevertEntraIdActionRequest

Expand all object

SecuritySwitchActionType

Expand all string

CreateSecuritySwitchActionRequest

Expand all object

RevertSecuritySwitchActionRequest

Expand all object

CreateWebhookActionRequest

Expand all object

CreateEndpointActionForCrowdStrike

Expand all object

MacAddress string matches ^(?:[0-9a-fA-F]{2}[:-]){5}[0-9a-fA-F]
{2}$

CreateEndpointActionRequestForCylance

Expand all object

CreateEndpointActionForForescout

Expand all object

CreateEndpointActionForCybereason

Expand all object

CreateEndpointActionForCynet

Expand all object

CreateEndpointActionForSonicwallcc

Expand all object

CreateEndpointActionForDeepInstinct

Expand all object

CreateEndpointActionForBitdefender

Expand all object

CreateEndpointActionForSophos

Expand all object

CreateEndpointActionForMicrosoftDefender

Expand all object

CreateEndpointActionForVmwareCarbonblack

Expand all object

CreateEndpointActionForSentinelone

Expand all object

CreateEndpointActionForPaloAltoNetworksCortex

Expand all object

EndpointActionType

Expand all string

RevertEndpointActionRequest

Expand all object

CreateCustomResponseActionEndpointRequest

Expand all object

FirewallActionRequest

Expand all object

BlockIpRequest

Expand all object

BlockIpFirewallActionRequest

Expand all (any & any)

UnblockIpRequest

Expand all object

UnblockIpFirewallActionRequest

Expand all (any & any)

CreateBlockIpFirewallActionRequest

Expand all (any | any)

Pick_FirewallActionRequest.Exclude_keyofFirewallActionRequest.connecto
r_id__

Expand all object

Omit_FirewallActionRequest.connector_id_

Expand all any

RevertFirewallRequest

Expand all any

SecuritySwitchActionRequest

Expand all object

BlockIpSecuritySwitchActionRequest

Expand all (any & any)

UnblockIpSecuritySwitchActionRequest

Expand all (any & any)

CreateBlockIpSecuritySwitchActionRequest

Expand all (any | any)

RevertSecuritySwitchRequest

Expand all object

CreateDisableUserSaasActionRequest

Expand all object

RevertSaasRequest

Expand all object

CreateDisableUserActiveDirectoryActionRequest

Expand all object

RevertActiveDirectoryRequest

Expand all object

CustomLogParser

Expand all object

CustomLogParserCreateResponse

Expand all object

CustomLogParserUpdateResponse

Expand all object

CustomLogParserForListParsersResult

Expand all object

CustomLogParserListParsersResponse

Expand all object

CustomLogParserForListResult

Expand all object

CustomLogParserListResponse

Expand all object

ConnectorCheckPoint

Expand all object

UpdateConnectorCheckPointRequest

Expand all object

Category

Expand all string

Connector

Expand all object

CreateConnectorRequest

Expand all object

UpdateConnectorRequest

Expand all object

ConnectorsResponse

Expand all object

CaseHealthStatus

Expand all string

CaseHealth

Expand all object

InSyncStatus.Synced

Expand all string

InSyncStatus.Paused

Expand all string

InSyncStatus.Error

Expand all string

InSyncStatus.Removed

Expand all string

InSyncStatusType

Expand all (any | any | any | any)

InSyncLink

Expand all object

CaseStatus

Expand all string

CaseResolution

Expand all string

CaseSeverity

Expand all string

Case

Expand all object

Partial_CaseDetails_

Expand all object

CaseObservablesValue

Expand all object

CaseSummary

Expand all object

FormattedCase

Expand all (any & any & object)

CasesResponse_FormattedCase_

Expand all object

CaseAlert

Expand all object

ExternalCreateCaseResponseData

Expand all object

ExternalCreateCaseRequest

Expand all object

ExternalUpdateCaseRequest

Expand all object

InSyncActions.Synced

Expand all string

InSyncActions.Paused

Expand all string

InSyncActions.Error

Expand all string

InSyncActivityAction

Expand all (any | any | any)

CaseActivityAction

Expand all (any | string)

CaseActivityField

Expand all string

CaseActivity

Expand all object

CaseScoreActivity

Expand all object

ESCaseAlerts

Expand all object

AddCaseAlertsRequest

Expand all object

DeleteCaseAlertsRequest

Expand all object

CaseComment

Expand all object

AddCaseCommentRequest

Expand all object

UpdateCaseCommentRequest

Expand all object

CaseInsyncServiceNowSyncRequest

Expand all object

AlertInsyncServiceNowSyncRequest

Expand all object

AutoTriageFeatureType

Expand all string

AutoTriageStatus

Expand all object

AutoTriageConf

Expand all object

AutoTriageManagement

Expand all object

AutoTriageManagementResponse

Expand all object

AutoTriageManagementUpdateOnboardingForm

Expand all object

ResetUserResponse any

ResetUserRequest

Expand all object

SerializedObjectDTO_ath_rule_

Expand all object

ExportPackageDTO_ath_rule.DependencyType_

Expand all object

AthRuleExportPackageDTO

Expand all any

ExportRequest_ath_rule_

Expand all object

AthRuleExportRequest

Expand all any

ImportPreflightRequest_ath_rule.DependencyType_

Expand all object

AthRuleImportPreflightRequest

Expand all any

ImportExecuteRequest_ath_rule.DependencyType_

Expand all object

AthRuleImportExecuteRequest

Expand all any

AlertWatcher

Expand all object

AlertWatchersResponse

Expand all object

AlertWatcherResponse

Expand all object

AlertWatcherScope

Expand all object

AlertType

Expand all object

AlertTypeResponse

Expand all object

AccessTokenResponse

Expand all object

VerdictType

Expand all string

VerdictFeedback

Expand all object

SummaryFeedback

Expand all object

KeyFindingsFeedback

Expand all object

FeedbackInfo

Expand all object

CaseTriageResponse

Expand all object

CaseDetailError

Expand all object

AICaseDetailSections

Expand all string

AICaseDetailResponse

Expand all object

ElasticsearchAlertDocument

Expand all object

AutoTriageInfoVerdictEnum

Expand all string

AutoTriageInfoStatusEnum

Expand all string

AutoTriageInfoMitigationStatusEnum

Expand all string

GeneratedAutoTriageInfo

Expand all object

AutoTriageInfo

Expand all any

MitreTactic

Expand all object

MitreTechnique

Expand all object

GeneratedMitreAttack

Expand all object

MitreAttack

Expand all any

ObservableTag

Expand all string

SecurityFindingTag

Expand all string

KeyFinding

Expand all object

TriageDetails

Expand all object

GeneratedEnhancedSummaryInfo

Expand all object

EnhancedSummaryInfo

Expand all any

AlertAISummary

Expand all object

AlertSourceError

Expand all object

AlertDetailResponse

Expand all object

AlertSummaryResponse

Expand all object

AlertErrorResponse

Expand all object

FeedbackSuccessResponse

Expand all object

ErrorResponse

Expand all object

VerdictFeedbackRequest

Expand all object

SummaryFeedbackRequest

Expand all object

KeyFindingFeedbackRequest

Expand all object

VerdictInfo

Expand all object

BatchVerdictResponse

Expand all object

BatchVerdictRequest

Expand all object

StructuredSummaryV1

Expand all object

AICaseTriageV2

Expand all object

CaseSummaryResponse

Expand all object

CaseTriageActivity

Expand all object

CaseVerdictInfo

Expand all object

BatchCaseVerdictResponse

Expand all object

BatchCaseVerdictRequest

Expand all object

HyperAutomationSummaryResponse

Expand all object

HyperAutomationErrorResponse

Expand all object

HyperAutomationSecurityFinding

Expand all object

HyperAutomationFindingsResponse

Expand all object

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

