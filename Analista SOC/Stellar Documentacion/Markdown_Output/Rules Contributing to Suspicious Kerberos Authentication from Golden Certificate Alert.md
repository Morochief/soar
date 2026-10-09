Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Rules Contributing to Suspicious Kerberos
Authentication from Golden Certificate Alert

The following rules are used to identify suspicious Kerberos certificate-based authentication
activity potentially resulting from Golden Certificate in Active Directory. Any one or more of these
will trigger the Suspicious Kerberos Authentication from Golden Certificate Alert. Details for each
rule can be viewed by clicking the More Details link in the description.

Title

Description

Suspicious Active Directory
Kerberos Certificate Authentication

A Golden Certificate is a persistence technique that expands upon an AD CS compromise.
If malicious actors obtain administrative access to a CA, they can extract a CA certificate
and private key. Once obtained, these can be used to forge valid certificates for client
authentication to impersonate any other user object in the domain. This rule detects
unusual certificate usage by monitoring certificate-based authentication.

More details

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

