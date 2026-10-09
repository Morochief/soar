Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Reputation Definitions

Reputation is an attribute of an IP address, host, domain, or URL.Stellar Cyber uses feeds from
several threat intelligence providers (such as ET Pro, PhishTank, OpenPhish, abuse.ch, and
others) as well as network traffic analysis to assign reputations. These reputations are visible in
the Interflow as srcip_reputation and dstip_reputation, and in the event tables under the
Source Reputation and Dest Reputation columns.

Following are the reputations in use, and their definitions.

Reputatio

n

Definition

Activex

ActiveX attacks and vulnerabilities.

Abused

Rogue TLD and GTLD activity that might be of interest. Limited to registrars who cannot or will not police their

TLD

domains, and TLDs that lack accountability or are free. For example, ICANN cannot claim .su back from the Soviet

Union, as that country no longer exists.

Attack

Indicates the results of a successful attack. For example, LMHost file download, certain banners, Metasploit

Response

Meterpreter kill command detected.

Bitcoin

Bitcoin clients running in the Bitcoin P2P network. This can help identify the rogue use of computing resources in

Bitcoin mining operations.

Blackhole A known black hole, this category often overlaps with CnC.

Bot, Botcc Clear indications of unwanted or criminal code on the host, or a host checking in to a command and control server.

Botcc

Same as Botcc, but grouped by destination port.

Portgroupe

d

Brute

Authentication brute forcing, such as SSH, IMAP, and VNC.

Forcer

Chat,

Chat activity, such as IRC, Jabber, Google Talk, MSN, AIM, ICQ, Baidu, or GaduGadu. Correlate this with CnC to

ChatServer

identify networks used for CnC.

CIArmy

IP rules for blocking from Collective Intelligence  .

CnC

Domains and IPs that are command & control for known Trojans. This reputation is for criminal command & control;

spyware and user tracking domains are classified in SpywareCnC.

Reputatio

n

Definition

Compromi

Known compromised hosts, updated daily.

sed

Current

Currently active campaigns expected to be short-lived, such as fraud related to a current natural disaster.

Events

DDoS

Source of DDoS traffic.

Attacker

DDoSTarg

Target of DDoS traffic, or commands to launch attacks.

et

Decoder-

Normalization events related to decoding.

events

DNS

DOS

DNS attacks and vulnerabilities, which can include DNS tunneling.

Inbound Denial of Service activity, as well as outbound indications.

DriveBySrc Sites used by an exploit kit like Neosploit or Blackhole, where HTML injection is used to redirect a browser to sites

that deliver an exploit by java or some other method.

Drop

From the Spamhaus   Don't Route Or Peer list, updated daily. A site where stolen data or credentials are being

pushed. Excludes droppers being served or other .exe movement.

Dshield

DShield   top attackers, updated daily.

DynDNS

A dynamic DNS entry or request host, or a domain using DynDNS.

EXE_Sour

Serving an executable file. Can indicate CnC.

ce

Exploit

Exploits not covered by other, specific categories.

FakeAV

Fake anti-spyware and anti-virus sites. Often overlaps with CnC.

Files

FTP

Example rules for Suricata file handling and extraction.

DNS attacks and vulnerabilities. Also logs basic activity, such as logins.

Games

Popular online games, such as Starcraft and WoW. Not malicious, just not necessarily appropriate.

Good

Does not have a reputation.

HTTP-

Logging of HTTP events, typically not malicious.

Events

ICMP

ICMP attacks and vulnerabilities. Typically not malicious.

ICMP_info Logging of ICMP events, typically not malicious.

IMAP

IMAP identification, attacks, and vulnerabilities. Also logs basic activity.

Inappropria

Pornography. Not malicious, but not appropriate.

te

IPCheck

IP address and geolocation checking services. These public services can be abused by malware or DynDNS.

Malware

Malware and spyware tracking with no obvious criminal intent. Not criminal, but certainly undesired.

Misc

Miscellaneous things not covered in other categories.

Mobile

Mobile malware and spyware tracking with no obvious criminal intent. Not criminal, but certainly undesired.

Malware

Netbios

NetBIOS identification, attacks, and vulnerabilities. Also logs basic activity.

Reputatio

n

Definition

OnlineGam

Gaming sites that install a client to report or track user activity. Not necessarily criminal, but possibly of interest. This

ing

P2P

is different from outright spyware.

Clients and sources of file sharing, including Bittorrent, Gnutella, Kazaa, LimeWire, and Qvod. Not malicious, just

not necessarily appropriate.

P2PCnC

P2P used as a CnC mechanism. Separated from P2P used for file sharing.

Parking

A parked domain or domain parking server.

Policy

Applications often disallowed by company or organization policy, such as DropBox, Google Apps, eBay, Facebook.

POP3

POP3 identification, attacks, and vulnerabilities. Also logs basic activity.

Proxy

Proxy endpoint for protocols such as HTTP, STUN, and SOCKS.

Remote

Remote access services such as Kaseya, GoToMyPC, and Citrix.

Access

Service

RPC

RPC identification, attacks, and vulnerabilities. Also logs basic activity.

SCADA

SCADA attacks and vulnerabilities. Also logs basic activity.

SCADA_sp

Snort Digital Bond based SCADA preprocessor.

ecial

SCAN,

Vulnerability scanning, open relay scanning, network and service reconnaissance, or other scanning activity.

Scanner

SelfSigned

Self-signed or invalid SSL certificates, which can be suspicious.

SSL

Shellcode Remote shell access to a machine on a local network.

SMTP

SMTP attacks and vulnerabilities. Also logs basic activity.

SMTP-

SMTP operational logging.

events

SNMP

SNMP attacks and vulnerabilities. Also logs basic activity.

Spam

Blacklisted spam sources.

SpywareC

Servers and domains serving or tracking user activity. Not criminal, but could be of interest. Generally toolbars,

nC

SQL

rogue gaming, free screensavers, and such.

SQL attacks and vulnerabilities. Also logs basic activity.

Steam-

TCP streaming events.

events

TELNET

Telnet attacks and vulnerabilities. Also logs basic activity.

TFTP

TFTP attacks and vulnerabilities. Also logs basic activity.

TLS-

TLS events and anomalies.

Events

TOR,

Tor exit nodes and participants in the network.

TorNode

Trojan

Clearly malicious software. Could be in transit, active, infecting, attacking, updating, or in any other state.

Reputatio

n

Definition

Undesirabl

Hacking tool forums, metasploit updates, and such. Not criminal, but of interest.

e

User

User agent identification and detection.

Agents

Utility

VOIP

VPN

Known good services, such as Google search front ends, Bing, and others.

VoIP attacks and vulnerabilities.

VPN concentrator. This is a potential anonymizing service.

Web Client Web client attacks and vulnerabilities.

Web

Server

Web server attacks and vulnerabilities.

Web

Specific web applications.

Specific

Apps

WORM

Indications of a worm in the network.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

