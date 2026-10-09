Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Windows to Identify Who Deleted
Files

If you configure the following settings on a Windows file server with a Windows Server Sensor,
Stellar Cyber can quickly identify any users who make unauthorized file and folder deletions:

Enable object access auditing

Set audit rules that log the identity of anyone who deletes specific files and folders on
the server

This integration works with a Windows Server Sensor. The only configuration for the sensor
profile is to make sure that event_id=4663 is enabled, which it is by default in all predefined
Windows Server Sensor templates.

 If you just want to audit which files and folders are added, changed, or deleted but not who
does it, enable FIM in the Windows sensor profile and specify file paths to audit there. You
don't have to configure anything extra in Windows, but you also won’t be able to see who
made the additions, changes, or deletions. For information, see Configuring Standard
Sensor Profiles .

Follow these steps to set up Windows file servers and find the identity of anyone who deletes an
audited file or folder:

1. Log in to a Windows file server that has files and folders that you want to monitor and

enable object access auditing.

On the Windows file server, open the Local Security Policy management
console (secpol.msc).

Navigate to Advanced Audit Policy Configuration | Object Access.

Enable Audit File System and configure it to audit successful and failed
attempts.

2. Set audit rules for specific files and folders of interest to log who deletes them.

Right-click or tap and hold the file or folder you want to audit, and select
Properties.

On the Security tab, select Advanced.

On the Auditing tab and select Add.

Select the principal (for example, Everyone), and choose to audit Delete and
Delete Subfolders and Files operations.

3. To see who deleted a file or folder, query for event_id = 4663 and

event.old.action contains “deleted”.

Also, if a Windows file server administrator knows what was deleted, they can tell you
the file path and file name and you can query for it; for example:

file_path = C:\\Users\\jsmith\\Downloads\\important-doc.txt

 Although single backslashes appear in file paths in the UI, double backslashes
appear in file paths in JSON records. Therefore, when including a file path in a
query, use double backslashes.

Then view the subject user ID and subject user name in the JSON section of the event
record details in the Stellar Cyber Platform UI:

“file_path”: “C:\\Users\\jsmith\\Downloads\\important-doc.txt”,

“event”: {

   “old”: {

      “extension”: “.txt”,

      “subjectUserSid”: “S-1-5-21-2282635044-1084901748-1986453373”,

      “driver_letter”: “C”,

      “type”: “File”,

      “subjectUserName”: “jsmith”,

   },

   “action”: [

      “deleted”

   ],

   “type”: [

      “Delete”

   ]

},

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

