Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Creating Saved Scripts

You can create and save scripts to be executed manually from the event display, or automatically
from an automated threat hunting playbook. Scripts are run via SSH.

Stellar Cyber can execute scripts that are one line long. For example, a simple script to:

Block the source IP address:

sudo iptables -I INPUT -s {{_source.srcip}} -p tcp -j DROP

Write device info to a table on the target remote host:

/home/aella/list_eng_info.sh {{_source.engid}} {{_source.engid_name}}

If you have a longer script, you can use the Stellar Cyber scripting feature to call that script on
the target remote host. For example: python /home/aella/IP_table.py

Scripts are usually run on the DP, but you can also run a script on a device sensor (not an agent
sensor). This allows you to run scripts on networks isolated from the DP, such as a remote office
or a customer environment.

The existing scripts are displayed in a System | Saved Objects | Saved Scripts table similar to
the following.

You can:

Click Create to add a new script.

Click

 to edit the script.

Click

 to delete the script.

See the Tables page for details on working with tables.

Adding or Editing a Script

Whether you add or edit a script, a similar dialog box appears. For our example, we are adding a
script:

1. Enter the Name. Each script must have a unique name. This field does not support

multibyte characters or spaces. You cannot edit the name after you submit. We entered
Block-Source-IP-Address.

2. Choose a Tenant Name. We chose All Tenants. You cannot edit the tenant after you

submit.

3. Enter your script. You can edit the script later.

4. Click Submit. The script is saved and added to the table.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

