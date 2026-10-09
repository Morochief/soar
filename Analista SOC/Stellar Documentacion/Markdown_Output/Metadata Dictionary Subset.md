✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Metadata Dictionary Subset
Stellar Cyber monitors your network to collect and respond to data reported from multiple
sources such as network packets, endpoint telemetry, cloud logs, and threat intelligence feeds.
Each type of data is handled differently before being populated into a standardized set of fields
referred to as metadata. Where applicable, and based on your configuration and the type of
content, the data may be de-duplicated, normalized, and enriched as it passes through sensors
and the data processor, on its way to becoming part of an Interflow record.
The following tables list the metadata dictionary field names in the Stellar Cyber Interflow record,
their description, and data type.
You can use these fields as part of your searches or queries that you build, along with vendor
specific fields and values.
Alerts
Click here for table of Alert field names
| Field Name | Description | Data Type |
| ---------- | ----------- | --------- |
_id2 Elasticsearch ID of the earlier of two login records string
_index2 Elasticsearch index of the earlier of two login records string
accumulated_anoma Score value of TRW model, showing the degree of abnormal activities integer
lous_failures
actual Real value input for machine learning (ML) to process integer
| actual_range | Actual login time range | string |
| ------------ | ----------------------- | ------ |
string
| anomaly_id | Elasticsearch ID of the data that caused the anomaly |     |
| ---------- | ---------------------------------------------------- | --- |
integer
| days_silent    | Time intervals between latest two appearances |        |
| -------------- | --------------------------------------------- | ------ |
| detected_field | Identification field of the detection         | string |
list
| detected_fields | Identification field of the detection |     |
| --------------- | ------------------------------------- | --- |

| Field Name | Description | Data Type |
| ---------- | ----------- | --------- |
string
| detected_value | Identification field's value of the detection |     |
| -------------- | --------------------------------------------- | --- |
detected_values Identification field's value of the detection list
integer
| detector_index | Detector index in ML detections |     |
| -------------- | ------------------------------- | --- |
distance_deviation Distance deviation between two login geo locations float
integer
diversity Metric of a parent node's unique child nodes, the higher value, the more unique child
nodes it has
end_bucket_time End timestamp of the data that caused the anomaly, combines with start_bucket_time to timestamp
form a time range of data
| event_name | Event name for the job | string |
| ---------- | ---------------------- | ------ |
event_score Event score, combination of severity, fidelity, and threat_score float
| event_status | Current status of a given event record | string |
| ------------ | -------------------------------------- | ------ |
event_summary Namespace for summarized data points from records contributing to an alert object
fidelity How confident that machine learning thinks the attack is happening float
last_login_time Login time of the earlier of two login records timestamp
login_failure_rate Rate of login failures per minutes in a fixed period float
| num_failed     | Number of fail in current bucket    | integer |
| -------------- | ----------------------------------- | ------- |
| num_successful | Number of success in current bucket | integer |
orig_id Elasticsearch ID of the data that caused the anomaly string
string
| orig_index | Elasticsearch index of the data that caused the anomaly |     |
| ---------- | ------------------------------------------------------- | --- |
float
percent_failed Fail percentage = num_fail / (num_failed + num_successful)
possible_breached_i List of source IP addresses that have suspicious activities list
ps
| query_count | Number of DNS queries in a tunnel       | integer |
| ----------- | --------------------------------------- | ------- |
| severity    | How serious is the event when it occurs | integer |
object
| srcip_geo2 | Geo location of the earlier of two login records |     |
| ---------- | ------------------------------------------------ | --- |

| Field Name | Description | Data Type |
| ---------- | ----------- | --------- |
integer
stability Update frequency of a parent node's number of child nodes, the higher value, the lower
frequency
start_bucket_time Start timestamp of the data that caused the anomaly timestamp
| stellar.alert_time | Time the anomaly was detected | timestamp |
| ------------------ | ----------------------------- | --------- |
float
| stellar.confidence | Prediction output from the SVM classifier |     |
| ------------------ | ----------------------------------------- | --- |
stellar.detection_time Original write_time - new write_time from pipeline, indicating the total time from the timestamp
Original Records being written to ES to the time of alert creation
stellar_index_id Indicates the Stellar Cyber index from which the alert was generated. Can be used string
together with the stellar_uuid to identify an alert uniquely.
stellar.nearest_geo Previous login location nearest to the alerted login location object
stellar.nearest_geo_i Count and frequency of logins from the nearest login location object
nfo
stellar.rule_id Identifier of the rule triggering an alert string
float
| stellar.threshold | Threshold used for detection |     |
| ----------------- | ---------------------------- | --- |
stellar_uuid Universally unique identifier for the alert, assigned by Stellar. Can be used together with string
the stellar_index_id to identify an alert uniquely.
suspicious_ips List of suspicious IP addresses that could do credential stuffing to a cloud service list
float
| time_deviation | Time deviation between two login times   |       |
| -------------- | ---------------------------------------- | ----- |
| total_entropy  | Total entropy of DNS queries in a tunnel | float |
float
| travel_speed | Travel speed between two login locations |     |
| ------------ | ---------------------------------------- | --- |
integer
| typical       | Typical value that machine learning calculated |        |
| ------------- | ---------------------------------------------- | ------ |
| typical_range | Typical login time range                       | string |
float
unknown_users_rate Rate of unknown login usernames per minutes in a fixed period
float
unknown_users_to_l Ratio of unknown usernames in login failures in a fixed period
ogin_failures
object
xdr_event XDR kill chain info of each alert, such as kill chain stage, tactic, technique, and so on
Traffic

Click here for table of Traffic field names
Data
| Field Name | Description |     |
| ---------- | ----------- | --- |
Type
| action | Action to be taken | string |
| ------ | ------------------ | ------ |
aella_tuples Concatenated field of srcip+dstip+dstport+appid string
appid ID of an application (>3,000 apps) identified by DPI engine long
appid_family Name of the application family to which the application belongs string
appid_name Name of an application (>3,000 apps) identified by DPI engine string
appid_stdport Indicates if application is using the standard port string
list
| appid_tags  | Tags of the application     |          |
| ----------- | --------------------------- | -------- |
| direction   | Direction of maltrace event | string   |
| domain_list | List of domain              | list_of_ |
string
domain_reputation Encoded string of a list of domain reputation separated by commas string
string
dscp_name Name describing the commonly used DSCP values in RFC 2475
| dstip | Destination IP address of the session | ip  |
| ----- | ------------------------------------- | --- |
dstip_aella_flag Flag to indicate how the IP address will be processed in following pipeline integer
dstip_domain_creation Creation time of the domains associated with the IP address date
dstip_geo Geo location information for the destination IP address object
dstip_geo_point Geo point of the destination IP address string
string
dstip_host Hostname or DNS name for the destination IP address
| dstip_sig_id | Signature ID concatenated with dstip | string |
| ------------ | ------------------------------------ | ------ |
string
dstip_tag Asset tag associated with the destination IP address
string
| dstip_type | Type of the destination IP address |     |
| ---------- | ---------------------------------- | --- |
dstip_username Username associated with the destination IP address string
string
dstip_usersid User ID associated with the destination IP address, for windows, windows SID is used
string
dstip_version Indicates if the destination IP address is IPv4 or IPv6
| dstmac | Destination MAC address | string |
| ------ | ----------------------- | ------ |

Data
| Field Name | Description |     |
| ---------- | ----------- | --- |
Type
| dstport    | Layer 4 destination port         | integer |
| ---------- | -------------------------------- | ------- |
| duration   | Session duration in milliseconds | integer |
| end_reason | Reason the session ended         | integer |
| hostip     | IP address the endpoint is using | ip      |
hostip_assetid Asset ID associated with the IP address string
hostip_domain_creation Creation time of the domains associated with the IP address date
hostip_geo Geo location information for the host IP address object
| hostip_geo_point  | Geo point of the host IP address | string |
| ----------------- | -------------------------------- | ------ |
| hostip_host       | Host name of the host IP address | string |
| hostip_reputation | Reputation of the IP address     | string |
hostip_reputation_source Source of the reputation data string
| hostip_sig_id | Signature ID concatenated with hostip    | string |
| ------------- | ---------------------------------------- | ------ |
| hostip_tag    | Asset tag associated with the IP address | string |
| hostip_type   | Type of the host IP address              | string |
hostip_username Username associated with the IP address string
hostip_usersid User ID associated with the IP address, for windows, windows SID is used string
hostip_version Indicates if the IP address is IPv4 or IPv6 string
| icmp_type      | ICMP message type     | string  |
| -------------- | --------------------- | ------- |
| in_bytes_delta | Same as inbytes_delta | integer |
| in_bytes_total | Same as inbytes_total | integer |
Incoming traffic rate, which is in_bytes_delta / <stats update time interval> float
in_rate
integer
inbytes_delta Number of bytes received by client from the server since last update time
inbytes_total Number of bytes received by client from the server during the whole session integer

Data
| Field Name | Description |     |
| ---------- | ----------- | --- |
Type
inpkts_delta Number of packets received by client from the server since last update time integer
integer
inpkts_total Number of packets received by client from the server during the whole session
mac List of MAC addresses associated with the host, also from scan result list
string
| netid_name      | Name of a network ID   |         |
| --------------- | ---------------------- | ------- |
| out_bytes_delta | Same as outbytes_delta | integer |
| out_bytes_total | Same as outbytes_total | integer |
float
out_rate Outgoing traffic rate, which is out_bytes_delta / <stats update time interval>
integer
outbytes_delta Number of bytes sent to the server by client since last update time
outbytes_total Number of bytes sent by client to the server during the whole session integer
integer
outpkts_delta Number of packets sent to the server by client since last update time
integer
outpkts_total Number of packets sent to the server by client during the whole session
remote_ip IP address of the remote entity involved in an event ip
date
remote_ip_domain_creation Creation time of the domains associated with the IP address
remote_ip_geo Geo location information for the remote IP address object
remote_ip_geo_point Geo point of the remote IP address string
string
| remote_ip_reputation | Reputation of the remote IP address |     |
| -------------------- | ----------------------------------- | --- |
remote_ip_reputation_source Source of the reputation data string
string
| remote_ip_type | Type of the remote IP address |     |
| -------------- | ----------------------------- | --- |
string
| remote_ip_username | Username associated with the remote IP address |     |
| ------------------ | ---------------------------------------------- | --- |
remote_ip_usersid User ID associated with the IP address, for windows, windows SID is used string
string
| remote_ip_version | Indicates if the IP address is IPv4 or IPv6 |     |
| ----------------- | ------------------------------------------- | --- |
integer
| remote_port | Port of a remote entity involved in an event |     |
| ----------- | -------------------------------------------- | --- |
| srcip       | Source IP address of the session             | ip  |

Data
| Field Name | Description |     |
| ---------- | ----------- | --- |
Type
srcip_assetid Asset ID associated with the source IP address string
date
srcip_domain_creation Creation time of the domains associated with the source IP address
srcip_geo Geo location information for the source IP address object
string
| srcip_geo_point | Geo point of the source IP address |     |
| --------------- | ---------------------------------- | --- |
object
| srcip_geo2 | Geo location of the earlier of two login records |     |
| ---------- | ------------------------------------------------ | --- |
srcip_host Hostname or DNS name for the source IP address string
string
srcip_reputation Reputation of the source IP address identified by Threat Intelligence
string
| srcip_reputation_source | Source of the reputation data        |        |
| ----------------------- | ------------------------------------ | ------ |
| srcip_sig_id            | Signature ID concatenated with srcip | string |
string
| srcip_tag | Asset tag associated with the source IP address |     |
| --------- | ----------------------------------------------- | --- |
string
| srcip_type | Type of the source IP address |     |
| ---------- | ----------------------------- | --- |
srcip_username Username associated with the source IP address string
string
srcip_usersid User ID associated with the source IP address, for windows, windows SID is used
srcip_version Indicates if the source IP address is IPv4 or IPv6 string
| srcmac | Source MAC address | string |
| ------ | ------------------ | ------ |
integer
| srcport | Layer 4 source port          |        |
| ------- | ---------------------------- | ------ |
| state   | Current state of the session | string |
list
suspicious_ips List of suspicious IP addresses that could do credential stuffing to a cloud service
integer
| tos | Type of Service (ToS) value in IP header |     |
| --- | ---------------------------------------- | --- |
float
| total_entropy | Total entropy of DNS queries in a tunnel |     |
| ------------- | ---------------------------------------- | --- |
integer
totalbytes Number of total bytes received and sent by client for the whole session
integer
totalpackets Number of total packets received and sent by client for the whole session
Vulnerabilities

Click here for table of Vulnerability field names
| Field Name      | Description                                  | Data Type      |
| --------------- | -------------------------------------------- | -------------- |
| info            | Host IP and MAC addresses for asset tracking | object         |
| scan_end        | Timestamp of when the security scan ends     | date           |
| scan_start      | Timestamp of when the security scan starts   | date           |
| vuln_count      | Count of vulnerabilities                     | integer        |
| vulnerabilities | List of vulnerabilities                      | list_of_object |
| vulnerability   | Vulnerability information                    | object         |
Assets
Click here for table of Asset field names
| Field Name | Description | Index Data Type |
| ---------- | ----------- | --------------- |
data_sources Integrations that discover or report the asset Assets array
desc Description (likely unused or used by the end user) Assets string
device_class Host and OS related info from a vulnerability scanner Assets string
device_desc Host and OS related info from a vulnerability scanner Assets string
engid ID of the sensor that discovers the asset Assets string
| engid_name | Name of sensor                  | Assets string |
| ---------- | ------------------------------- | ------------- |
| geoip      | Geo location                    | Assets string |
| geo_point  | Coordinates of the Geo location | Assets string |
| hostname   | Hostname of asset               | Assets array  |
| id         | Asset ID                        | Assets string |
| ip         | IP address                      | Assets array  |
iphistory List of IP addresses previously used by the current asset Assets object (ip, time)
last_seen Last time the asset is reported or updated Assets timestamp
locid Location of the data sensor if the location is assigned by the user from the GUI Assets string
| mac             | MAC address                | Assets string  |
| --------------- | -------------------------- | -------------- |
| name            | Name of the asset          | Assets string  |
| os              | OS-related info            | Assets string  |
| os_version      | OS-related info            | Assets string  |
| reputation      | IP reputation of the asset | Assets string  |
| risk_score      | Asset risk score           | Assets integer |
| risk_score_hist | Asset risk score history   | Assets array   |
start_time Timestamp the current asset was first reported Assets timestamp
state State of the asset: new, approved, unapproved Assets string
| subtype     | Asset type: router, server, client | Assets string |
| ----------- | ---------------------------------- | ------------- |
| tag         | Asset tag                          | Assets string |
| tenantid    | Tenant ID                          | Assets string |
| tenant_name | Tenant name                        | Assets string |

| Field Name | Description | Index Data Type |
| ---------- | ----------- | --------------- |
timestamp Last_seen of the asset, used as timestamp in daily snapshot in ES Assets timestamp
| user_sid | Usersid in asset or user tracking | Assets string |
| -------- | --------------------------------- | ------------- |
vendor Vendor of the asset, calculated from the MAC address Assets string
vuln_score Vulnerability score, calculated from vulnerabilities reported on the asset Assets integer
Users
Click here for table of User field names
Inde
| Field Name | Description | Data Type |
| ---------- | ----------- | --------- |
x
data_source Integrations that discover or report the user User array
| s   |     | s   |
| --- | --- | --- |
desc Description (likely unused or used by the end user) User string
s
| engid | ID of the sensor that discovers the user | User string |
| ----- | ---------------------------------------- | ----------- |
s
last_seen Last time the asset is reported or updated User timestamp
s
last_seen_sr Last time the asset is reported or updated with the data source from which it is User object
| cs  | reported or updated | s {"azure_ad": } |
| --- | ------------------- | ---------------- |
last_updated Last time the asset is reported or updated User timestamp
s
| name | User name | User string |
| ---- | --------- | ----------- |
s
name_srcs User name with the data source from which the name is reported User ojbect
s {"azure_ad":}
| profile | User profile from the data source | User object |
| ------- | --------------------------------- | ----------- |
s
| risk_score | User risk score | User integer |
| ---------- | --------------- | ------------ |
s
| risk_score_hi | User risk score history | User array |
| ------------- | ----------------------- | ---------- |
| st            |                         | s          |
search_key Combination of username, sid, and other info for search optimization User string
s
| sid | User Sid | User array |
| --- | -------- | ---------- |
s
| tag | User tag | User string |
| --- | -------- | ----------- |
s
tag_srcs User tag with the data source on which the tag is applied User object
s {"azure_ad":}

Inde
| Field Name | Description | Data Type |
| ---------- | ----------- | --------- |
x
| tenantid | Tenant ID | User string |
| -------- | --------- | ----------- |
s
| tenant_name | Tenant name | User string |
| ----------- | ----------- | ----------- |
s
timestamp Last_seen of the asset, used as timestamp in daily snapshot in ES User timestamp
s
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        