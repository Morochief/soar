✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Configuring Data Enrichment
 Administrators for an individual tenant, tenant group, or the root tenant can use this feature
if they have Security Admin, Platform Admin, or Super Admin privileges.
Stellar Cyber uses information from a variety of sources to enrich collected data. The options in
the Enrichment page let you customize the following enrichment types:
DNS Track
Custom Geo
Private IP
Using the Enrichments Table
When you select System | DATA MANAGEMENT | Enrichments, Stellar Cyber displays a table
of the available enrichment options that have been configured for your organization. From this
table, you can Create, Edit, or Delete the enrichments, as well as perform other standard table
functions.
Configuring DNS Track Enrichments
You can use DNS Track to track DNS resolution changes for specified domains. If one of the
tracked domains resolves to a new IP address, Stellar Cyber creates an entry in the Changed
Domains to IP Resolutions table in the Threat Hunting | Threat Hunting Library|
DNS Analysis page.

1. Select System | DATA MANAGEMENT | Enrichments.
The enrichment table appears.
2. Select Create.
3. In the dialog box that appears, set Type to DNS Track.
4. Use the Tenant dropdown to select the tenant for whom this enrichment will apply.
5. Select Next.
6. Specify a domain; for example, yourdomain.com.
7. To add another domain, select the Add icon () and enter it in the new row that
appears. Continue adding as many domains as you need. (Use the  icon to remove
rows.)
8. Select Next.
9. Review the configuration and Submit.
10. To add more domains for DNS tracking later:
a. Select the Edit this row icon on the far right.
b. Select Advanced in the Edit Enrichment dialog that appears and Add more
domains.
c. When done, select Done and then Submit.
Configuring Custom (IP) Geo Enrichments
You can use the IP Geo Enrichment module to configure the geolocation associated with
specified IP addresses manually, overriding the geolocation that Stellar Cyber obtains from
geolocation databases. This is useful in situations where you are seeing false positives for
Impossible Travel and Location Anomaly alerts based on an inaccurate geolocation. This lets
you adjust information if you think that false positives have occurred.
1. Select System | DATA MANAGEMENT | Enrichments.
The enrichment table appears.
2. Select Create.

3. In the dialog box that appears, set Type to Custom Geo.
4. Specify the Tenant that will be allowed to use this enrichment. You can select All
Tenants or a specific individual tenant.
5. Select Next.
6. Set the following options:
(Options with an asterisk are required; others appear in geolocation display information
for the specified IP address.)
IP* – The IP address for which you want to specify a geolocation.
Latitude* – The latitude for the geolocation of this IP address in decimal
degrees format, from -90 to 90.
Longitude* – The longitude for the geolocation of this IP address in decimal
degrees format, from -180 to 180.
Country Name – Select the country for this IP address from the dropdown list.
Country Code (read only) – Set automatically based on the selected
Country Name.
City – Specify the city for this IP address.
Region – Specify the region for this IP address
7. Select Next.
8. Review the configuration and Submit.
9. To add more geolocation configurations later:
a. Select the Edit this row icon on the far right.
b. Select Advanced in the Edit Enrichment dialog that appears and Add more
geolocation configurations.
c. When done, select Done and then Submit.
Configuring Private IP Enrichments
The IP enrichment option lets you specify subnets for which IP addresses should be considered
private and marked accordingly in event record fields. All other addresses (except RFC-1918
addresses) are considered public.
 IP addresses described by RFC-1918 as generally-accepted "private" IP addresses do not
need to be configured. They are automatically designated as private.
 Public IP addresses designated as private in the IP enrichment interface are counted as
assets for licensing purposes.

1. Select System | DATA MANAGEMENT | Enrichments.
The enrichment table appears.
2. Select Create.
3. In the dialog box that appears, set Type to Private IP.
4. (Root tenant) Specify the Tenant that will be allowed to use this enrichment.
You can select All Tenants or a specific individual tenant.
5. Select Next.
6. Enter a standard IPv4 address/subnet; for example, 10.1.1.0/24.
7. To add another subnet, select the Add icon () and enter it in the new row that
appears.
Continue adding as many subnets as you need. (Use the  icon to remove rows.)
8. Select Next.
9. Review the configuration and Submit.
10. To add more private IP subnets later:
a. Select the Edit this row icon on the far right.
b. Select Advanced in the Edit Enrichment dialog that appears and Add more
subnets.
c. When done, select Done and then Submit.
Enrichment Details
The following table lists the metadata fields that Stellar Cyber uses for enrichment, a description
of the field, the source of the information, and the enrichment it is used for.
Enrichment Field Description Source Enrichment
access_mask Permission required to access the object - Windows object
access
access_subject Process or system object that initiated access - Windows object
access
aella_tuples Unique session ID comprising source IP, destination IP and - -
port, and app ID
appid_family Application family DP App ID
appid_name Application name DP App ID
appid_stdport Whether or not the application is using the standard port DP App ID

| Enrichment Field  | Description                          | Source | Enrichment    |
| ----------------- | ------------------------------------ | ------ | ------------- |
| attack_start_date | Timestamp of the start of the attack | -      | -             |
| command           | Command that was run                 | -      | Linux command |
correlation_info The metadata in individual events of a correlation result - -
| detect_date    | When the sensor detected an attack | -   | -   |
| -------------- | ---------------------------------- | --- | --- |
| detect_origin  | Direction of the attack            | -   | -   |
| detection_flag | Detection this record applies to   | -   | -   |
direction Direction of the file transfer, either forward for source to Traffic data File transfer direction
destination, or backward for destination to source
| domain_reputation | Reputation of the domain | -      | -                  |
| ----------------- | ------------------------ | ------ | ------------------ |
| dscp_name         | Readable DSCP value      | Sensor | Network identifier |
| dstmac            | Destination MAC address  | -      | -                  |
dstip_aella_flag How to process the IP address for detections - -
dstip_asn Autonomous System Number (ASN) responsible for the MaxMind
ASN ID
| hostip_asn | IP address |     |     |
| ---------- | ---------- | --- | --- |
remote_ip_asn
srcip_asn
dstip_asn_org Organization name associated with the ASN for the MaxMind
ASN organization
| hostip_asn_org | IP address |     | name |
| -------------- | ---------- | --- | ---- |
remote_ip_asn_org
srcip_asn_org
| dstip_tag | Asset tag associated with the IP address | -   | -   |
| --------- | ---------------------------------------- | --- | --- |
srcip_tag
hostip_tag
| dstip_assetid | Asset ID associated with the IP address | -   | -   |
| ------------- | --------------------------------------- | --- | --- |
srcip_assetid
hostip_assetid
dstip_host Host name associated with the IP address DNS/DHCP Host/domain name
| srcip_host |     |     | correlation |
| ---------- | --- | --- | ----------- |
hostip_host
dstip_geo Geographic location (country, city, etc) associated with the IP MaxMind Geographic location
| srcip_geo | address |     | of the IP address |
| --------- | ------- | --- | ----------------- |
remote_ip_geo
hostip_geo
dstip_geo_point Latitude and longitude associated with the IP address MaxMind Geographic
| srcip_geo_point     |     |     | coordinates of the |
| ------------------- | --- | --- | ------------------ |
| remote_ip_geo_point |     |     | IP address         |
hostip_geo_point
dstip_reputation Reputation associated with the IP address - Reputation
srcip_reputation

Enrichment Field Description Source Enrichment
remote_ip_reputation
hostip_reputation
dstip_reputation_sour Source of the reputation associated with the IP address - Reputation
ce
srcip_reputation_sour
ce
remote_ip_reputation
_source
hostip_reputation_so
urce
dstip_sig_id Signature ID associated with the IP address - -
srcip_sig_id
hostip_sig_id
dstip_type Whether the IP address is public or private - IP type
srcip_type
remote_ip_type
hostip_type
dstip_username Username and user ID associated with the IP address AD Username
srcip_username correlation
remote_ip_username
hostip_username
dstip_usersid
srcip_usersid
remote_ip_usersid
hostip_usersid
dstip_domain_creatio When the domain associated with the IP address was - -
n created
srcip_domain_creatio
n
hostip_domain_creati
on
remote_ip_domain_c
reation
dstip_version The version associated with the IP address, IPv4 or IPv6 - -
srcip_version
hostip_version
engid_device_class Sensor operating system, either Windows or Linux Sensor Sensor information
correlation
engid_gateway Sensor's gateway Sensor Sensor information
correlation
exec_user User that executed the command - Linux command
fidelity Fidelity of an event - -
hostip IP address of the host reporting the event - -

| Enrichment Field | Description       | Source | Enrichment |
| ---------------- | ----------------- | ------ | ---------- |
| icmp_type        | ICMP message type | DP     | ICMP       |
inbytes_total Total inbound bytes in the session so far Sensor Network traffic metric
| is_dga | If a DNS request is DGA | DP  | Suspicious domain |
| ------ | ----------------------- | --- | ----------------- |
identification
| login_result | Result of the login attempt | Sensor | Login |
| ------------ | --------------------------- | ------ | ----- |
| login_type   | Application logged in to    | Sensor | Login |
login_user Username associated with the login attempt Sensor Login
| mac | MAC addresses associated with the host | -   | -   |
| --- | -------------------------------------- | --- | --- |
metadata.is_tunnelin If a DNS session is potentially tunneling DP DNS tunneling
| g   |     |     | correlation |
| --- | --- | --- | ----------- |
metadata.request.do Creation of a domain in the DNS request DP DNS domain creation
main_creation
metadata.request.eff Effective TLD of a domain name DP DNS domain name
| ective_tld |     |     | TLD extraction |
| ---------- | --- | --- | -------------- |
metadata.response.d Creation of a domain in the DNS request DP DNS domain creation
omain_creation
metadata.response.e Effective TLD of a domain name DP DNS domain name
| ffective_tld |     |     | TLD extraction |
| ------------ | --- | --- | -------------- |
metadata._whitelist Whether any metadata field is whitelisted - -
msg_class Whether this record belongs to an endpoint class - -
| msg_origin.source | Vendor'r product     | -      | -                  |
| ----------------- | -------------------- | ------ | ------------------ |
| netid_name        | Name of a network ID | Sensor | Network identifier |
new_dns_record A DNS record that has not been seen before DP DNS records tracking
outbytes_total Total outbound bytes in the session so far Sensor Network traffic metric
parent_child Concatenation of the parent and child process names DP Process correlation
parent_proc_name Name of the parent process DP Process correlation
| process_name | Name of the process  | DP  | Process correlation |
| ------------ | -------------------- | --- | ------------------- |
| proto_name   | Name of the protocol | -   | -                   |
remote_ip IP address of the remote host involved in the event Sensor Windows PowerShell
script
remote_port Port of the remote host involved in the event Sensor Windows PowerShell
script
smb_denied_count Number of times access was denied in a single SMB session DP SMB
smb_username_coun Number of unique usernames used in a single SMB session DP SMB
t
smb_username_set Set of unique usernames used in a single SMB session DP SMB
| srcmac   | MAC address of the source IP address | -             | -                  |
| -------- | ------------------------------------ | ------------- | ------------------ |
| tenantid | ID of the tenant                     | Sensor and DP | Tenant information |
correlation

| Enrichment Field | Description | Source | Enrichment |
| ---------------- | ----------- | ------ | ---------- |
tenant_name Name of the tenant Sensor and DP Tenant information
correlation
totalbytes Total bytes in the session so far Sensor Network traffic metric
totalpackets Total packets since the last session update Sensor Network traffic metric
| url_reputation | Reputation of the URL                    | -   | -   |
| -------------- | ---------------------------------------- | --- | --- |
| username       | Username associated with the application | -   | -   |
vulnerabilities.cve The CVE associated with a plugin or vulnerability Database Security scan
vulnerability
vulnerabilities.descrip Description of a Nessus vulnerability Security scan
Database
| tion |     |     | vulnerability |
| ---- | --- | --- | ------------- |
Stellar Cyber version 6.6.0s © 2026 Stellar Cyber . All rights reserved.
Support   |  Contact Us   |        