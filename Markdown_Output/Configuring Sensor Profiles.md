Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Configuring Sensor Profiles

 You must have Root scope to use this feature.

Instead of configuring each sensor individually, you can configure sensor profiles to centralize
settings. When you add a new sensor, you simply apply the profile to the sensor. Similarly, when
you need to change a sensor configuration, you can change the profile instead of changing each
sensor.

You can create as many profiles as you need. You can even clone an existing profile if you want
to make small changes to an existing profile before applying it to other sensors.

 Each sensor profile names a specific receiver. Although there is a default receiver, you

should set up receivers before entering new profiles. See the Receivers configuration page
for more information.

Sensor Profile List
Select the System | DATA SOURCE MANAGEMENT | Sensors | Sensor Profiles option to
display the Sensor Profile Configuration table listing the existing sensor profiles.

Each row represents a sensor profile. You can:

Click Create to create a new sensor profile.

Click

 to edit the sensor profile.

Click

 to delete the sensor profile.

 If you try to delete a sensor profile that is associated with a token, Stellar Cyber
alerts you with a confirmation prompt informing you that all associated tokens will
also be deleted.

Check one or more profile's boxes and use the Clone button to create copies of them
for editing.

See the Tables page for more information on working with tables.

About the Default Sensor Profiles

When your organization is initially provisioned by Stellar Cyber, it includes the following default
sensor profiles:

Default – Applied to Server Sensors when they first register with Stellar Cyber.

Default_modular – Applied to Modular Sensors when they first register with Stellar
Cyber.

Keep in mind the following:

The Platform Admin for your organization can edit the settings for the default sensor
profiles.

You can create as many sensor profiles as you like to tailor settings as necessary.

You can change the profile applied to a sensor.

The default Modular Sensor profile created for your organization has Network Traffic,
Sandbox, and IDS enabled. If you create a new Modular Sensor profile, however, those
options are not enabled by default and must be enabled.

Stellar Cyber occasionally makes changes to the Default and Default_modular sensor
profiles. Any changes are indicated in the Release Notes for your release. Adjustments
you have made to existing profiles are treated differently depending on whether they are
saved to the Default profiles or to a new profile:

Stellar Cyber keeps track of changes you have made to the settings in your
own sensor profiles and preserves those changes.

Other settings in your profiles may still be updated by Stellar Cyber if they
were in the previous Default profile but have now been changed by Stellar
Cyber.

Example: You create a new Standard Sensor profile and add some custom
Event IDs to Windows | Microsoft Windows Sysmon. Stellar Cyber will not
change these settings when migrating existing profile settings to a new set of
values.

Example 2: You create a new Modular Sensor profile but have not made any
changes to the rule sets in IDS | Signature. If we add new rule sets to our
default Modular Sensor profile, those new sets are automatically added to both
your new Modular Sensor profile and the Default_modular profile.

If you save changes to the Default or Default_modular profiles, those
changes are now considered to be default and not edited by a user. Because

of this, they may be changed by Stellar Cyber when new changes to the
Default or Default_modular templates are released.

Cloning Sensor Profiles

You can clone sensor profiles by checking their boxes in the Sensor Profiles list and clicking the
Clone Selected Profile button. By default, cloned sensor profiles are given the same name as
the source profile plus a timestamp indicating the time when the profile was cloned – for
example, if you clone Pluto, it might become Pluto (Tue Jun 21 2022 13:12:24).

The system handles clone names differently depending on whether you selected a single sensor
profile for the clone or multiple:

If you clone a single sensor profile, you can supply your own name for the cloned profile
in the dialog box that appears. For example, in the illustration below, we've cloned the
Default_modular sensor profile and given it the custom name of Pluto:

If you elect to clone multiple sensor profiles, you cannot customize the names for the
clones and must accept the defaults instead. For example:

 Keep in mind that Sensor Profile names cannot be changed once the profile is created.

Because of this, if you want to customize the names of your cloned sensor profiles, make
sure to clone them one at a time rather than using the bulk clone feature.

Adding or Editing Sensor Profiles
When you create a new sensor profile you can:

Add a new standard sensor profile
Add a new modular sensor profile

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

