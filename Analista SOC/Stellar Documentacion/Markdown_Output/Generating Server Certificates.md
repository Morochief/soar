Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Generating Server Certificates

You can use an SSL certificate to secure communications between clients and the Stellar Cyber
user interface. This topic describes how to generate the Certificate Signing Request (CSR) file
you will need to obtain a certificate for your domain from your service provider. Once you obtain
a certificate using these instructions, you can upload it to Stellar Cyber in the System |
 ORGANIZATION MANAGEMENT | Certificates page and apply it to the DP in the System |
 ORGANIZATION MANAGEMENT | Settings page. The procedure consists of the following main
steps:

1. Generate the CSR file and corresponding private key.

2. Use the CSR to obtain a certificate in PEM format from your service provider.

3. Upload and apply the certificate in Stellar Cyber.

Generating a CSR
You can use the OpenSSL utility to generate a CSR file and private key. To do so, you will need
the following:

Access to a Linux or Windows host that is not in your Stellar Cyber cluster.

The OpenSSL utility installed on the host. You can download OpenSSL from the
following link:

https://wiki.openssl.org/index.php/Binaries 

 Make sure you save the private key file in a safe place. You'll need it when you

upload the certificate to Stellar Cyber in Managing Certificates.

 The CSR and private key must be generated without a password or encryption.

Generating the CSR in Linux

Generate the CSR in Linux by opening a command line session with the host (SSH or local) and
issuing the following command:

openssl req -new -newkey rsa:2048 -nodes -keyout <yourdomain>.key -out
<yourdomain>.csr

This OpenSSL command generates a 2048-bit RSA private key and CSR:

The -nodes argument specifies that the created private key file is not encrypted.

The <yourdomain>.key is the path and filename to your private key file.

The <yourdomain>.csr is the path and filename to the created certificate signing
request.

Generating the CSR in Windows

Generate the CSR in Windows by opening a command prompt window on the host (CMD.exe)
and running the following commands:

1. Change directories to the OpenSSL directory:

cd \OpenSSL-Win32

2. Generate the private key:

openssl genrsa -out private-key.key 2048

3. Generate the CSR:

openssl req -new -key private-key.key -out csr.txt

Using the CSR to Obtain a Certificate from your Service
Provider
Once you've generated the CSR file, you can take the entirety of its text and paste it into the
appropriate field of your service provider's SSL certificate enrollment form. Download the
resulting certificate in PEM format.

The exact instructions vary depending on your service provider. As a convenience, here are the
instructions for GoDaddy .

Uploading and Applying the Certificate in Stellar Cyber
Once you've retrieved the certificate from your service provider, you can use it to secure the
Stellar Cyber user interface as follows:

1. Upload the certificate to Stellar Cyber in System | Saved Objects | Certificates.

2. Apply the certificate to the DP using the CA Certificate entry in the Data Processor

section of System | ORGANIZATION MANAGEMENT | Settings.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

