WildFire Analysis Report
WildFire Analysis Report 1
1 File Information 2
2 Static Analysis 2
2.1. Suspicious File Properties 2
3 Dynamic Analysis 3
3.1. VM1 (Windows 7 x64 SP1, Adobe Reader 11, Flash 11, Office 2010) 3
3.1.1. Behavioral Summary 3
3.1.2. Network Activity 3
3.1.3. Host Activity 3
Process Activity 3
Process Name - sample.exe 3
Event Timeline 3
3.2. VM2 (Windows 10 x64, Flash 22, Adobe Reader 11, Office 2019) 3
3.2.1. Behavioral Summary 3
3.2.2. Network Activity 4
3.2.3. Host Activity 4
Process Activity 4
Process Name - sample.exe 4
Event Timeline 4
3.3. VM3 (Advanced WildFire: Windows 7 x64 SP1, Adobe Reader 11, Flash 11, Office 2010) 5
3.3.1. Behavioral Summary 5
3.3.2. Network Activity 5
3.3.3. Host Activity 5
Process Activity 5
Process Name - kmeeeDGjMEXNMxQSNO.exe 5
Event Timeline 5
1/5

1 File Information
File Type PE
File Signer
SHA-256 0e0c385c6f44bdbbc4f1f3891c45bb1e9f73e6bad743d5e9f17e1ae119967737
SHA-1 8f1b60cf3cbfc849c23318d28464bba45acc9f52
MD5 4f065ac8e18f8acb8cfcd9a8c728e11a
File Size 2836480bytes
First Seen Timestamp 2022-05-10 06:15:40 UTC
Verdict MMaallwwaarree
Antivirus Coverage VirusTotal Information
2 Static Analysis
2.1. Suspicious File Properties
This sample was not found to contain any high-risk content during a pre-screening
analysis of the sample.
Contains an unusual entry point
The entry point of a PE file is the starting address for execution. An unusually located entry point may
indicate a packed or obfuscated file.
Contains sections with size discrepancies
Sections with a large discrepancy between raw and virtual sizes may indicate a packed or obfuscated PE file.
Contains an invalid checksum
The PE file checksum is required for drivers, boot-time DLLs, and other DLLs loaded into secure system
processes. Malware often ignores this value or sets it to zero.
Contains a TLS section
Thread-local storage (TLS) is normally used to manage data in multithreaded applications. However, it can
also allow execution of code outside of the expected entry point of a PE file.
Contains non-standard section names
Standard section names are defined by the compiler. Non-standard section names may indicate a packed or
obfuscated PE file.
Contains sections with zero size
Sections with zero size indicate a packed or obfuscated PE file.
2/5

3 Dynamic Analysis
3.1. VM1 (Windows 7 x64 SP1, Adobe Reader 11, Flash 11, Office
2010)
3.1.1. Behavioral Summary
This sample was found to be benign on this virtual machine.
Behavior Severity
Program has shown a message box.
The program has shown a message box.
Created or modified a file
Legitimate software creates or modifies files to preserve data across system restarts. Malware may create or modify files
to deliver malicious payloads or maintain persistence on a system.
Sample tries to retrieve information about logical processors and related
hardware.
Sample tries to retrieve information about logical processors and related hardware.
The sample shows limited activities during analysis.
A sample may not be able to generate much behaviors by design or because of its dependency on user input or system
environment, which could means it is trying to evade the dynamic analysis.
The idle time between two API events are too long.
The idle time between two API events are too long.
3.1.2. Network Activity
No network data available.
3.1.3. Host Activity
Process Activity
Process Name - sample.exe
(command: C:\Users\Administrator\sample.exe)
Event Timeline
1 Created Process C:\Users\Administrator\sample.exe
3.2. VM2 (Windows 10 x64, Flash 22, Adobe Reader 11, Office 2019)
3.2.1. Behavioral Summary
This sample was found to be malware on this virtual machine.
Behavior Severity
3/5

Program has shown a message box.
The program has shown a message box.
Created or modified a file in the Windows system folder
The Windows system folder contains configuration files and executables that control the underlying functions of the
system. Malware often modifies the contents of this folder to manipulate the system, establish persistence, and avoid
detection.
Created or modified a file
Legitimate software creates or modifies files to preserve data across system restarts. Malware may create or modify files
to deliver malicious payloads or maintain persistence on a system.
Identify System domain DNS controller
Identify System domain DNS controller on an endpoint using nslookup LDAP query. This command is being abused by
malware to gather information on the domain controller of the targeted or compromised host.
Sample tries to retrieve information about logical processors and related
hardware.
Sample tries to retrieve information about logical processors and related hardware.
The sample shows limited activities during analysis.
A sample may not be able to generate much behaviors by design or because of its dependency on user input or system
environment, which could means it is trying to evade the dynamic analysis.
Sample removed system files.
Sample removed system files.
3.2.2. Network Activity
DNS Queries
| Domain Name                  | Query Type | DNS Response           |
| ---------------------------- | ---------- | ---------------------- |
| g2.akamai.net                | NS         | n1g2.akamai.net        |
| g2.akamai.net                | NS         | n4g2.akamai.net        |
| g2.akamai.net                | NS         | n2g2.akamai.net        |
| centralus.cloudapp.azure.com | NS         | ns2-201.azure-dns.net  |
| g2.akamai.net                | NS         | n0g2.akamai.net        |
| g2.akamai.net                | NS         | n3g2.akamai.net        |
| g2.akamai.net                | NS         | n6g2.akamai.net        |
| centralus.cloudapp.azure.com | NS         | ns4-201.azure-dns.info |
| g2.akamai.net                | NS         | n5g2.akamai.net        |
| centralus.cloudapp.azure.com | NS         | ns1-201.azure-dns.com  |
| centralus.cloudapp.azure.com | NS         | ns3-201.azure-dns.org  |
| g2.akamai.net                | NS         | n7g2.akamai.net        |
3.2.3. Host Activity
Process Activity
Process Name - sample.exe
(command: C:\Users\Administrator\sample.exe)
Created Mutexes
Mutex Name
Local\SessionImmersiveColorMutex
Event Timeline
4/5

1 Created Process C:\Users\Administrator\sample.exe
2 Created mutex Local\SessionImmersiveColorMutex
3.3. VM3 (Advanced WildFire: Windows 7 x64 SP1, Adobe Reader 11,
Flash 11, Office 2010)
3.3.1. Behavioral Summary
This sample was found to be benign on this virtual machine.
Behavior Severity
Program has shown a message box.
The program has shown a message box.
Sample tries to retrieve information about logical processors and related
hardware.
Sample tries to retrieve information about logical processors and related hardware.
Used SSL
SSL is a certificate-based cryptographic protocol for secure communication over the Internet. Malware often
communicates over SSL to hide its traffic from network security systems, like most firewalls and IPSes, that do not offer
SSL decryption.
Generic API were found in memory stack.
Generic API were found in memory stack.
Checked system language settings
Microsoft Windows has language locale settings stored in the registry. Malware often checks these language settings if it
wants to target a certain geographic region or avoid executing in a specific region.
Identify System domain DNS controller
Identify System domain DNS controller on an endpoint using nslookup LDAP query. This command is being abused by
malware to gather information on the domain controller of the targeted or compromised host.
Generic API were found in memory executable.
Generic API were found in memory executable.
Permission of a memory page has been made writeable.
Permission of a memory page has been made writeable.
Process API were found in memory executable.
Process API were found in memory executable.
3.3.2. Network Activity
No network data available.
3.3.3. Host Activity
Process Activity
Process Name - kmeeeDGjMEXNMxQSNO.exe
(command: C:\Users\Administrator\kmeeeDGjMEXNMxQSNO.exe )
Event Timeline
No timeline data available.
5/5