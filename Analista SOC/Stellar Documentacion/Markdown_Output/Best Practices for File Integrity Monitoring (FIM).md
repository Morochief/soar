Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Best Practices for File Integrity Monitoring (FIM)

Stellar Cyber includes a File Integrity Monitoring feature for both Windows Server Sensors and
Linux Server Sensors that lets you keep track of changes to specified files and directories on the
host Server Sensor machine, including file changes, file creations, and file deletions.

This topic provides guidance on using the FIM feature effectively.

Performance Considerations
It's a good idea to focus your FIM settings on specific files and directories to optimize
performance. Adding directories with large numbers of files and subdirectories can have an
adverse affect on performance. Keep an eye on the memory and processor consumption for the
windows agent sensor fim (Windows) or aella_audit (Linux) process and adjust the number
of monitored files and directories as necessary.

Commonly Monitored Files and Directories – Windows
Based on the best practices for file integrity monitoring published by Microsoft , the
FIM Windows feature is preconfigured to monitor the following files and directories for changes,
creations, and deletions:

C:\boot.ini

C:\autoexec.bat

C:\config.sys

C:\Windows\system.ini

C:\Windows\win.ini

C:\Windows\regedit.exe

C:\Windows\explorer.exe

C:\Windows\System32\userinit.exe

C:\Program Files\Microsoft Security Client\msseces.exe

Commonly Monitored Files and Directories – Linux

Based on industry-standard best practices, the FIM Linux feature is preconfigured to monitor the
following directories for changes, creations, and deletions:

/bin

/boot

/etc

/sbin

/usr/bin

/usr/sbin

/usr/local/bin

/usr/local/sbin

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

