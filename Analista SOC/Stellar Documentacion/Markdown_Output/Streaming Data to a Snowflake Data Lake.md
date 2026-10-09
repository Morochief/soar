Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Streaming Data to a Snowflake Data Lake

 Snowflake integration is available in SaaS deployments of Stellar Cyber through the Early

Access Program. If you already have a Snowflake account and are interested in integrating
Stellar Cyber with it, contact Stellar Cyber customer support . No additional license is
required.

Snowflake data lakes lets you store, manage, and analyze large volumes of structured and semi-
structured data on multiple cloud platforms such as Amazon Web Services (AWS), Google
Cloud, and Microsoft Entra ID. If you integrate Stellar Cyber with Snowflake, Stellar Cyber will
stream the data it collects and the alerts it generates through a Snowflake Snowpipe to the data
lake in near real-time. Snowflake stores the data it receives from Stellar Cyber in a database
that’s organized into SQL-like tables aligned with the indices in Stellar Cyber: Alerts, Syslog,
Traffic, and so on. You can then use the Snowflake user interface (UI) or third-party applications
like Tableau or Power BI to query and analyze the data.

After the data is sent to Snowflake, you can perform short-term and long-term forensics on it,
doing immediate investigations and analyses of security incidents soon after they occur and
analyzing archived data, logs, and other historical information to uncover patterns, persistent
threats, or previously unnoticed incidents.

While Stellar Cyber excels at collecting and analyzing security data, Snowflake lets you integrate
security data with other data types such as financial, operational, and customer data for broader
analytics. In addition, you can integrate third-party machine-learning tools like DataRobot and
Amazon SageMaker for even more varied analytic options. Finally, while using the long-term
storage, querying, and analytic capabilities that Snowflake offers, you’d still use features for
threat detection and response in Stellar Cyber such as case management and automated threat
hunting.

The Stellar Cyber customer support team will work with you to configure the necessary settings
in Snowflake and generate a public/private key pair for a service account that they’ll use to
create a new database in Snowflake to store data from Stellar Cyber. Your Stellar Cyber Platform
later uses this service account to access the newly created database and send it data.

 The Stellar Cyber database on Snowflake is separate from other databases you already

have there and the user role assigned to the service account only has permission to access
it.

After the setup is complete, Stellar Cyber begins streaming data to the Stellar Cyber database in
Snowflake where it becomes available in near real-time for various types of detections and
analyses made possible not only by their combined capabilities but also by those of other third-
party integrations as well.

Additional External Data Destinations in Stellar Cyber
Refer to External Storage Destinations in On-Premises vs. Managed Deploymentsfor
information on other external destinations available in Stellar Cyber.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

