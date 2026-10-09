Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring NXLog for HostIP Field

For NXLog, some configuration is needed to create the HostIP field from the Hostname field.
This configuration in NXLog enables the collection of the host or source IP address when
Windows events are ingested from NXLog.

 The NXLog version must be 5.5 or later.

To configure NXLog:

1. Import Extension Modules
2. Configure NXLog
3. Refer to the Sample NXLog Configuration File
4. Refer to the Alert Types Received

Import Extension Modules
To import two extension modules, Resolver (xm_resolver) and Syslog (xm_syslog), you can refer
to the following NXLog documentation:

https://docs.nxlog.co/refman/current/xm/resolver.html 

https://docs.nxlog.co/refman/current/xm/syslog.html 

Then import the extension modules:

Configuring NXLog
For rewriting and modifying logs, you can refer to the following NXLog documentation:
https://docs.nxlog.co/userguide/configure/rewriting.html .

To configure NXLog to create the HostIP field:

1. In the input module, configure the listening host:

Use parse_syslog(). Parse the $raw_event field as either BSD Syslog (RFC
3164) or IETF Syslog (RFC 5424) format.

If there is more than one instance of xm_syslog, reference the module
instance with INSTANCENAME->parse_syslog(), otherwise use
parse_syslog().

2. In the output module, create the HostIP from the Hostname and rewrite HostIP to get

the output:

Use ipaddr name_to_ipaddr(string name) to change the value of
Hostname to the value of HostIP.

The HostIP is added to the raw_event field to display the output.

Sample NXLog Configuration File

Panic Soft

define INSTALLDIR C:\Program Files\nxlog

#ModuleDir %INSTALLDIR%\modules

#CacheDir  %INSTALLDIR%\data

#SpoolDir  %INSTALLDIR%\data

define CERTDIR %INSTALLDIR%\cert

define CONFDIR %INSTALLDIR%\conf\nxlog.d

# Note that these two lines define constants only; the log file location

# is ultimately set by the `LogFile` directive (see below). The

# `MYLOGFILE` define is also used to rotate the log file automatically

# (see the `_fileop` block).

define LOGDIR %INSTALLDIR%\data

define MYLOGFILE %LOGDIR%\nxlog.log

# If you are not using NXLog Manager, disable the `include` line

# and enable LogLevel and LogFile.

include %CONFDIR%\*.conf

#LogLevel    INFO

#LogFile     %MYLOGFILE%

<Extension _syslog>

    Module  xm_syslog

</Extension>

# This block rotates `%MYLOGFILE%` on a schedule. Note that if `LogFile`

# is changed in managed.conf via NXLog Manager, rotation of the new

# file should also be configured there.

<Extension _fileop>

    Module  xm_fileop

    # Check the size of our log file hourly, rotate if larger than 5MB

    <Schedule>

        Every   1 hour

        <Exec>

            if ( file_exists('%MYLOGFILE%') and

                 (file_size('%MYLOGFILE%') >= 5M) )

            {

                 file_cycle('%MYLOGFILE%', 8);

            }

        </Exec>

    </Schedule>

    # Rotate our log file every week on Sunday at midnight

    <Schedule>

        When    @weekly

        Exec    if file_exists('%MYLOGFILE%') file_cycle('%MYLOGFILE%', 8);

    </Schedule>

</Extension>

<Extension syslog>

  Module    xm_syslog

</Extension>

<Extension _json>

  Module    xm_json

</Extension>

<Extension xml>

    Module      xm_xml

</Extension>

<Extension _resolver>

    Module      xm_resolver

</Extension>

<Input in_eventlog>

# For windows 2008/vista/7/8/2012/2012R2/2016 and latter use the following:

  Module      im_msvistalog

  ReadFromLast TRUE

  SavePos     TRUE

  Query     <QueryList> \

[System[(EventID=1100)]]</Select> \

[System[(EventID=4768)]]</Select> \

[System[(EventID=4769)]]</Select> \

[System[(EventID=4771)]]</Select> \

[System[(EventID=4616)]]</Select> \

[System[(EventID=4104)]]</Select> \

   <Query Id="0"> \

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

                                                          <Select Path="Security">*

[System[(EventID=4624)]]</Select> \

[System[(EventID=4625)]]</Select> \

[System[(EventID=4634)]]</Select> \

[System[(EventID=4647)]]</Select> \

[System[(EventID=4648)]]</Select> \

[System[(EventID=4656)]]</Select> \

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

                                                          <Select Path="Security">*

[System[(EventID=4688)]]</Select> \

[System[(EventID=4719)]]</Select> \

[System[(EventID=4720)]]</Select> \

[System[(EventID=4722)]]</Select> \

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

[System[(EventID=4723)]]</Select> \

[System[(EventID=4724)]]</Select> \

[System[(EventID=4725)]]</Select> \

[System[(EventID=4726)]]</Select> \

[System[(EventID=4727)]]</Select> \

[System[(EventID=4728)]]</Select> \

[System[(EventID=4729)]]</Select> \

[System[(EventID=4730)]]</Select> \

[System[(EventID=4731)]]</Select> \

[System[(EventID=4732)]]</Select> \

[System[(EventID=4733)]]</Select> \

[System[(EventID=4734)]]</Select> \

[System[(EventID=4735)]]</Select> \

[System[(EventID=4737)]]</Select> \

[System[(EventID=4738)]]</Select> \

[System[(EventID=4739)]]</Select> \

[System[(EventID=4740)]]</Select> \

[System[(EventID=4741)]]</Select> \

[System[(EventID=4742)]]</Select> \

[System[(EventID=4743)]]</Select> \

[System[(EventID=4744)]]</Select> \

[System[(EventID=4745)]]</Select> \

[System[(EventID=4748)]]</Select> \

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

[System[(EventID=4749)]]</Select> \

[System[(EventID=4750)]]</Select> \

[System[(EventID=4753)]]</Select> \

[System[(EventID=4754)]]</Select> \

[System[(EventID=4755)]]</Select> \

[System[(EventID=4756)]]</Select> \

[System[(EventID=4758)]]</Select> \

[System[(EventID=4759)]]</Select> \

[System[(EventID=4760)]]</Select> \

[System[(EventID=4763)]]</Select> \

[System[(EventID=4764)]]</Select> \

[System[(EventID=4767)]]</Select> \

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

                                                          <Select Path="Security">*

[System[(EventID=4776)]]</Select> \

[System[(EventID=4778)]]</Select> \

[System[(EventID=4783)]]</Select> \

[System[(EventID=4800)]]</Select> \

[System[(EventID=4801)]]</Select> \

[System[(EventID=7036)]]</Select> \

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="Security">*

  <Select Path="System">*

                                                          <Select Path="Setup">*

[System[(EventID=1)]]</Select> \

Path="Application">*[System[(EventID=18454)]]</Select> \

  <Select

  <Select

Path="Application">*[System[(EventID=18456)]]</Select> \

      </QueryList>

   </Query> \

</Input>

<Input tcp>

    Module      im_tcp

    ListenAddr  10.xx.xx.xx

    <Exec>

        syslog->parse_syslog();

    </Exec>

</Input>

<Output out_eventlog>

  Module      om_udp

  Host        10.xx.xx.xx:5601

  <Exec>

        if $raw_event =~ s/^(\S+)//

        {

  $HostIP = $Hostname;

          $HostIP = name_to_ipaddr($Hostname);

          if not defined $Hostname $HostIP= $Hostname;

           $raw_event = $HostIP + $raw_event;

        }

    to_json();

   </Exec>

</Output>

<Route eventlog>

  Path      in_eventlog, tcp => out_eventlog

</Route>

Alert Types Received
Data from NXlog will undergo an identical process of normalization and enrichment. This ensures
that it will provide the same level of alert coverage as our existing Windows sensor.

The following alert types are received when using this NXLog configuration:

Abnormal Parent / Child Process
Backup Catalogs Deleted by Ransomware
Bad Reputation Login
Command Anomaly
Encoded PowerShell
External Account Login Failure Anomaly

External Brute-Forced Successful User Login
External Credential Stuffing
External Password Spraying
External RDP BlueKeep
External RDP Suspicious Outbound
External User Login Failure Anomaly
Hydra Password Guessing Hack Tool
Impossible Travel Anomaly
Internal Account Login Failure Anomaly
Internal Brute-Forced Successful User Login
Internal Credential Stuffing
Internal Password Spraying
Internal RDP BlueKeep
Internal RDP Suspicious Outbound
Internal User Login Failure Anomaly
Login Time Anomaly
Malware on Disk
Mimikatz Credential Dump
Mimikatz DCSync
Password Cracking with Hashcat
Password Spraying Attempts Using Dsacls
Potentially Malicious Windows Event
PowerShell Remote Access
Process Anomaly
RDP Port Opening
RDP Registry Modification
RDP Reverse Tunnel
RDP Session Hijacking
RDP Settings Hijacking
RDP Suspicious Logon
RDP Suspicious Logon Attempt
Scanner Reputation Anomaly
Sensitive Windows Active Directory Attribute Modification
Sensitive Windows Network Share File or Folder Accessed
SMB Impacket Lateralization
SMB Specific Service Installation
SMB Suspicious Copy
Suspicious Access Attempt to Windows Object
Suspicious Activity Related to Security-Enabled Group
Suspicious Connection to Another Process
Suspicious Handle Request to Sensitive Object
Suspicious Powershell Script
Suspicious Process Creation Commandline
Suspicious Windows Active Directory Operation
Suspicious Windows Logon Event
Suspicious Windows Process Creation

Suspicious Windows Service Installation
Uncommon Process Anomaly
User Asset Access Anomaly
User Login Location Anomaly
User Process Usage Anomaly
Volume Shadow Copy Deletion via VssAdmin
Volume Shadow Copy Deletion via WMIC

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

