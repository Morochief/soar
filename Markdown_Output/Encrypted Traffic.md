Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Encrypted Traffic

Stellar Cyber does not directly decrypt traffic but can handle it in multiple ways:

Deploy agents behind proxies
Detect applications
Partner with third-party decryption

Deploying Agents Behind Proxies

Stellar Cyber sensors don't need to decrypt traffic when you deploy them behind your proxy
server. The traffic is already decrypted by the proxy server when it gets to the sensor, and the
sensor can add user and process context to the traffic.

Detecting Encrypted Applications

If you cannot deploy the sensor behind the proxy servers or you are not using proxy servers,
Stellar Cyber sensors can still identify encrypted applications by analyzing the encrypted traffic
patterns and TLS/SSL handshaking.

The sensor extracts useful metadata, such as the server certificate, IP addresses, domain
names, session duration, and byte counts from the packet header and TLS/SSL handshaking.
The IP addresses are enriched with geo location, threat intelligence, host name, user name, and
more, to create rich context for alerts and actions. Our machine learning based network traffic
analysis and user behavior analysis apply to the encrypted traffic with the extracted metadata
and enriched context. In addition, Stellar Cyber uses JA3 and JA4 TLS fingerprinting to identify
malware communicating over encrypted traffic:

JA3 fingerprinting creates a hash derived from fields in the TLS Client Hello message,
allowing security systems to identify and group SSL/TLS clients based on handshake
characteristics rather than relying solely on IP addresses.

JA4 fingerprinting extends the JA3 approach with improved handling of modern TLS
features and support for fingerprinting from both client and server perspectives,
enabling more reliable identification of encrypted sessions.

Stellar Cyber supports both fingerprinting methods.

Partnering with Third-Party Decryption Tools

Stellar Cyber sensors work with many third-party decryption tools, such as F5 SSL Orchestration
and Gigamon VAF, taking the decrypted traffic and analyzing it.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

