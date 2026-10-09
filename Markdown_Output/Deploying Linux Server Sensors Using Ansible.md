✖
Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!
Deploying Linux Server Sensors Using Ansible
This topic describes how to deploy Linux Server Sensors using an Ansible playbook and
inventory file downloaded from Stellar Cyber. Once customized, you can run the playbook from
your own Ansible administration system..
See the following sections for details:
Downloading Sample Ansible Files
Customizing the Ansible Playbook for Linux Server Sensor Deployment
Sample Ansible Files
Downloading Sample Ansible Files
You can download a sample Ansible playbook and inventory file using the links below. You can
see the contents of the sample playbook and inventory file in Sample Ansible Files.
Contact Stellar Cyber support (support@stellarcyber.ai) for login credentials.
Sample Playbook
curl -O -k -u login:password https://acps.stellarcyber.ai/public/aella-agent-
File
install.yml
Sample Inventory curl -O -k -u login:password https://acps.stellarcyber.ai/public/aella-agent-
File inventory
Customizing the Ansible Playbook for Linux Server
Sensor Deployment
Before running the playbook, use the information in the table below to review and update the
variables in the vars section to match your deployment environment. These values control how
the installer is downloaded, authenticated, and registered with the Stellar Cyber platform.

R
e
Va
q
ria Description Example
ui
ble
re
d
clo Ye acps.stellarcyber.ai
Hostname used to
ud_ s
download the Linux
url
Server Sensor
installer.
Do not change this
variable. It is
preconfigured with the
address of the Stellar
Cyber software
repository
(acps.stellarcyber.ai).
ver Ye 6.6.0
Sensor software
sio s
version to install.
n
This value is used to
construct the installer
download URL. The
playbook downloads
the installer from:
https://<cloud_url>/re
lease/<version>/data
sensor/
tok C Click to see: "eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4R0NNIn0..S_4moX-
SaaS Deployments –
en on NTXCOy2adE7q5Jw.3hSjeblj9dzqrcGduttYHY6adfcs054-
Registration token
dit yclhXS94anVs84TUBNY_dMayEy34o50U9vvrIRKOXrMRXJPs9CElKGIWeHlWLYanyiIXR1phe
used to onboard the
io 1R-
sensor. If this value is
na TeXpKtfJUZ9k7ZuWjzr6wLOprM3EdGgxs4LuOCwAGs4WltGCu5DcHg1ZEWXj5BKC4oQwj37J
provided, the installer
l 5dGxRw4qpAo3cO1_A2hHkVmS3m21it7v9KMefEt1UVJluFzRlRpBCh6BwwuNuPtQ8KjW5Ok
uses token-based
mABwj9rjP03iOW4svlx8AEkJ5jkwG3VzCDaeIL_Ao_fRMdL9tR64AOzuN4f5x_YMVkV_7PjRE6r
authentication and
KSgMQmq83-
adds itself to the Data
2xVvENjdjzyFu2cUSddnOGPgEoK5EaZWo1mlXGhOVwqVkojTyDqb0F7QUvD_mU4Wg5_Si-
Processor encoded in
Rrh3b8fAB-iwbbPUKxQt0AH8-
the token.
HSbDyNJYfecB_1mAHLYaWYzxdtOW7rxVRIyqEYXy6517NlKwaEUw5MSWBZfWMOg0FKCn
You obtain tokens in
H-J-
the System | DATA
YrMgpC1jcDNjukqbs7wUAdmVoXhjQsAILfQHeD_rIlnO0bEEOsYb9fbxVKNAuZyMMpZYgomBJ
SOURCE
u6LKNzKcvvSoPoXShy_2hG0-
MANAGEMENT |
zWQEcpxgcEAPXcncjNOnGnpgVR76uniEis8HfF78CjcFqQl_e2hg9vash8ohYFihif-
Sensors | Sensor
8FPbpFA9lRuhZU8lFk6aKz-Zo1YOunXJVtA.QJ8dSftCckeD8i3tMu9UXw"

R
e
Va
q
ria Description Example
ui
ble
re
d
Installation | Tokens.
Refer to Obtaining a
Token for the
Installation for details.
cm_ C On-Premises 192.168.11.11
ip on Deployments – Stellar
dit Cyber If a token is not
io provided, the installer
na uses the Data
l Processor IP address
specified here for
sensor registration.
ds_ Ye "download_user"
Username used to
use s
authenticate when
rna
downloading the
me
installer from
acps.stellarcyber.ai.
Contact Stellar Cyber
support
(support@stellarcyber.
ai) for login
credentials.
ds_ Ye "download_password"
Password used to
pas s
authenticate when
swo
downloading the
rd
installer from
acps.stellarcyber.ai.
Contact Stellar Cyber
support
(support@stellarcyber.
ai) for login
credentials.
sel Ye true
Determines which
f_c s
installer script is used:
ont
true – The all-
ain in-one installer
(ds_linux_inst

R
e
Va
q
ria Description Example
ui
ble
re
d
all_all_in_one.
sh) is used.
false – The
run-time
installer
(ds_linux_inst
all.sh) is used.
Refer to Choosing an
Installation Script
with the self_contain
Variable for details on
the differences
between the two
scripts. If you are not
sure which installer to
select, use the all-in-
one script (the default).
ins N Directory on the target /tmp
tal o host where the
l_d installer will be
ir downloaded. Set to
/tmp by default.
ten N Associates the sensor "My-Tenant"
ant o with a specific tenant.
_id
pri N Primary aggregator "10.0.1.10"
mar o used by the sensor for
y_a communication with
ggr the Stellar Cyber
ega platform.
tor
sec N Backup aggregator "10.0.1.11"
ond o used if the primary
ary aggregator becomes
_ag unavailable.
gre
gat
or
Choosing an Installation Script with the self_contain Variable
Stellar Cyber provides two different installation scripts for the Linux Server Sensor:

ds_linux_install_all_in_one.sh is an entirely self-contained installation script that
includes the images for all supported target environments. Because of this, it does not
require access to the Internet and can be used in dark sites. However, it is quite large
(on the order of ~700 MB).
ds_linux_install.sh does not bundle images with the script and instead pulls the
correct image from the Stellar Cyber production server at run time. Because of this, it is
much smaller than the all-in-one script (on the order of 10 KB, plus the single 200 MB
image pulled from Stellar Cyber production servers).
The table below provides you with details on the two scripts:
| Name                | Type/Size | Usage | Dark Site Support     | Pros      | Cons     |
| ------------------- | --------- | ----- | --------------------- | --------- | -------- |
| ds_linux_install.sh |           |       | Yes, but only if the  | Script is |          |
|                     | Small     |       |                       |           | Internet |
|                     |           |       | installation image is | small and |          |
access
Installer does not include
|     |     |     | downloaded separately, | only |     |
| --- | --- | --- | ---------------------- | ---- | --- |
required
images and is roughly 10
|     |     |     | copied to the target | downloads |     |
| --- | --- | --- | -------------------- | --------- | --- |
in most
KB. If used without the -
|     |     |     | machine, and pointed to | the one | use |
| --- | --- | --- | ----------------------- | ------- | --- |
p/--package parameter,
|     |     |     | with the -p/--package | image |     |
| --- | --- | --- | --------------------- | ----- | --- |
cases.
the single image pulled
|     |     |     | parameter at run time. | required for |     |
| --- | --- | --- | ---------------------- | ------------ | --- |
from Stellar Cyber
installation.
production servers is
roughly 200 MB.
ds_linux_install_all_in_one.sh Mostly identical. Yes, with no further Supports Script is
Large
|     |     | Obtain credentials | download. | dark site |     |
| --- | --- | ------------------ | --------- | --------- | --- |
large.
Installer includes images
|     |     | from Customer |     | installation |     |
| --- | --- | ------------- | --- | ------------ | --- |
for all supported target
|     |     | Support, download |     | with no |     |
| --- | --- | ----------------- | --- | ------- | --- |
environments and is
|     |     | and execute script |     | further |     |
| --- | --- | ------------------ | --- | ------- | --- |
roughly ~700 MB.
|     |     | with optional |     | downloads. |     |
| --- | --- | ------------- | --- | ---------- | --- |
arguments.
Customizing the Ansible Inventory File
The Ansible inventory file defines the target systems where the Linux Server Sensor will be
installed. The playbook references the target host group, so any hosts included in that group
will receive the deployment.
The inventory file contains the sections shown below:
[hosts_linux]
10.36.29.162
[hosts_linux:vars]
ansible_connection=ssh
ansible_port=22
ansible_user=root
ansible_ssh_pass=mypassword
ansible_become_pass=mypassword
ansible_ssh_common_args='-o UserKnownHostsFile=/dev/null -o
StrictHostKeyChecking=no'
[target:children]
hosts_linux

Host Group Definition (hosts_linux Section)
The hosts_linux group defines the Linux servers where the sensor will be installed. Each entry
represents a target host.
[hosts_linux]
10.36.29.162
To deploy the sensor to additional systems, add their hostnames or IP addresses to this list. For
example:
[hosts_linux]
10.36.29.162
10.36.29.163
10.36.29.164
Connection Variables (hosts_linux:vars Section)
The hosts_linux:vars section defines connection settings used by Ansible when connecting to
the target systems.
Variable Description Example
ansible_connec Connection method used to access the host. ssh
tion
ansible_port SSH port used for the connection. 22
ansible_user User account used to log in to the target system. root
ansible_ssh_pa Password used for SSH authentication. mypassword
ss
ansible_become Password used for privilege escalation when running commands mypassword
_pass with sudo.
ansible_ssh_co Optional SSH arguments. In this example, strict host key -o UserKnownHostsFile=/dev/null -o
mmon_args checking is disabled to simplify initial connections. StrictHostKeyChecking=no
Target Group Mapping (target:children Section)
The playbook installs the Linux Server Sensor on the target host group. The inventory file maps
the hosts_linux group into the target group using the following configuration:
[target:children]
hosts_linux
This structure allows you to organize hosts into logical groups while keeping the playbook
consistent. Any host placed in hosts_linux automatically becomes part of the target group
used by the playbook.
Running the Deployment
Once the inventory file and playbook variables are configured, you can run the deployment:
Run the deployment from an Ansible control node as follows:
ansible-playbook -i aella-agent-inventory aella-agent-install.yml

Ansible will connect to each host defined in the target group and install the Linux Server Sensor
automatically.
 For production deployments, consider using SSH key authentication instead of storing
passwords directly in the inventory file.
Sample Ansible Files
The following files are provided to illustrate how the Ansible files might appear. Refer to
Customizing the Ansible Playbook for Linux Server Sensor Deployment for details on how
to customize the files for your own deployment.
Sample Ansible Playbook File
The playbook file is a YAML-format file similar to the following:
---
- hosts: target
become_method: sudo
become: yes
gather_facts: true
vars:
# Optional token – if set, will use --token; otherwise uses --cm
token: ""
cm_ip: 192.168.11.11
cloud_url: acps.stellarcyber.ai
version: 6.2.0
self_contain: true
ds_username: "user310"
ds_password: "HMTe3dJ3cmAPK"
install_dir: /tmp
# Optional parameters
tenant_id: "" # e.g., "123456"
primary_aggregator: "" # e.g., "10.0.1.10"
secondary_aggregator: "" # e.g., "10.0.1.11"
tasks:
- name: Choose installer script based on self_contain
set_fact:
installer_script: >-
{{ 'ds_linux_install_all_in_one.sh' if (self_contain | bool) else
'ds_linux_install.sh' }}
- name: Announce installation
debug:
msg: >-
Installing Data Sensor Agent (Linux) using {{ installer_script }} — please
wait...
- name: Download installer
ansible.builtin.get_url:
url: "https://{{ cloud_url }}/release/{{ version }}/datasensor/{{
installer_script }}"
dest: "{{ install_dir }}/{{ installer_script }}"
url_username: "{{ ds_username }}"
url_password: "{{ ds_password }}"
force: yes
validate_certs: no
mode: "0755"
# Conditionally choose install flag (token or cm)
- name: Determine installer authentication flag
set_fact:
auth_flag: >-
{% if token is defined and token | trim | length > 0 -%}
--token {{ token | quote }}
{%- else -%}
--cm {{ cm_ip }}
{%- endif %}
- name: Build optional installer flags
set_fact:
optional_flags: >-
{% set flags = [] -%}
{% if tenant_id is defined and tenant_id | trim | length > 0 %}

{% set _ = flags.append('--tenant_id ' ~ tenant_id | quote) %}
{% endif %}
{% if primary_aggregator is defined and primary_aggregator | trim | length
> 0 %}
{% set _ = flags.append('--primary_aggregator ' ~ primary_aggregator |
quote) %}
{% endif %}
S a m p le I n {v%e nift osreyc oFnidlaery_aggregator is defined and secondary_aggregator | trim |
length > 0 %}
{% set _ = flags.append('--secondary_aggregator ' ~ secondary_aggregator
A |s aqmuoptlee )A n%s}ible inventory is shown as follows:
{% endif %}
{{ flags | join(' ') }}
[hosts_linux]
1 0 . 3-6 .n2a9m.e1:6 2Debug optional flags (safe for logs)
debug:
[ h o s t s _ lmisngu:x :v"aOrpst]ional flags passed: {{ optional_flags | default('(none)') }}"
ansible_connection=ssh
a n s i-b lnea_mpeo:r tE=c2h2o installer command
a n s i b ldee_buusge:r=root
a n s i b l e _msssgh:_ p>ass=mypassword
a n s i b l e _ b ebcaosmhe _{p{a sisn=smtyaplals_sdwiorr d}}/{{ installer_script }}
a n s i b l e _ s s-hv_ c{o{m mvoenr_sairogns =}'}-o UserKnownHostsFile=/dev/null -o
S t r i c t H o s t{K{e yaCuhtehc_kfilnagg= n}o}'
{{ optional_flags | default('') }}
[target:children]
h o s t-s _nlaimneu:x Run installer
ansible.builtin.shell: >
bash {{ install_dir }}/{{ installer_script }}
-v {{ version }}
{{ auth_flag }}
{{ optional_flags | default('') }}
args:
warn: false
S te lla r C-yb enr avemresi:on 6D.6i.s0splay post install message © 2026 Stellar Cyber . All rights reserved.
debug:
msg: Support | Contact Us |  
- "Stellar Cyber Linux Agent Sensor installation complete."
- name: Wait a bit for CM to start sending configuration
ansible.builtin.pause:
seconds: 15
prompt: "Pausing 15 seconds to allow CM to register the agent..."
- name: Wait until cm_assigned_name is assigned (not 'unknown')
shell: egrep 'cm_assigned_name *= *' /etc/aella/aos.yaml | awk '{print $4}'
register: device
changed_when: false
retries: 15 # roughly 150 secs (15 * 10s)
delay: 10
until:
- device.stdout is defined
- device.stdout | length > 0
- device.stdout != 'unknown'
- name: Display Agent Assigned Name from CM
debug:
var: device.stdout
- name: Get engid
ansible.builtin.shell: "egrep 'engid *= *' /etc/aella/aos.yaml | awk '{print
$4}'"
register: engid
changed_when: false
- name: Display engid
debug:
var: engid.stdout