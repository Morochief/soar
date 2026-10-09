Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Vendor-Related Metadata

When Stellar Cyber ingests data, some of the information is stored in standardized fields
(example: srcip) within the Interflow record. The table below shows a set of the standard fields
that you may find helpful for identifying vendor-specific data in the searches or queries that you
build.

Metadata Field

Purpose

msg_origin.vendor

Vendor associated with the data

Examples

trendmicro

msg_origin.source

Vendor's product name associated with the data

trendmicro_cloudone

msg_origin.category

Overall data category

msg_origin.processor.nam

For connectors, this is the same as msg_origin.source

e

endpoint

trendmicro_cloudone

msg_origin.processor.type For connectors, this is always log_collector

log_collector

msg_class

Sub-category of data applicable to multiple content types from a

vendor

trendmicro_cloudone_compute

rs

View the metadata fields in the JSON tab.

Vendor-Specific Data
In addition to standard metadata fields in the Interflow record, Stellar Cyber dynamically creates
fields to store vendor-specific data.

To learn which fields may be useful for your queries, expand the Interflow details in views such
as the Threat Hunting Documents table. Locate the vendor name and note the fields. Repeat
this with different Interflow rows, since Stellar Cyber does not typically create the fields if the
incoming value is blank.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

