Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Converting Sensor Storage to Use Encryption in
AWS

This topic describes how to convert the storage volume for a sensor deployed in AWS from
unencrypted to encrypted. You do this by taking a snapshot of your sensor's unencrypted storage
volume, creating a copy of it, reconfiguring the copy to use encryption, and then replacing the
existing storage volume with the encrypted volume you just created. Use the following
procedure:

1. Log in to the AWS EC2 Console and navigate to Instances.

2. Click the Instance ID for the sensor instance whose storage you want to encrypt.

3. Click on the Storage tab and then click the instance's Volume ID.

The Elastic Block Store | Volumes page appears.

4. Click the Volume ID in the list.

5. Select Create snapshot from the Actions dropdown.

6. Supply a description for your snapshot and click Create snapshot to save it to the list.

7. Once the snapshot has been created, select its entry in the Snapshots list and choose

Copy snapshot from the Actions dropdown.

8. Check the Encrypt this snapshot option in the Copy snapshot dialog box.

The new snapshot appears in the list with an entry of Encrypted in the Encryption
column.

9. Select the entry for your encrypted snapshot and choose Create volume from

snapshot from the Actions dropdown :

10. Note that the Encrypt this volume option is checked in the dialog box that appears and

click Create volume.

The new encrypted volume appears in the Volumes list.

11. Navigate to the Instances list, select the entry for your sensor, and choose Stop

instance from the Instance state dropdown.

12. Return to the Volumes list, select the entry for the unencrypted volume currently in use,
and choose Detach volume from the Actions dropdown. Then, click Detach on the
confirmation prompt that appears.

13. Return to the Instances list, click the entry for your sensor, and select the Storage tab.

Notice that the Block devices list shows no attached block devices.

14. Return to the Volumes list, select the entry for the encrypted volume, and choose

Attach volume from the Actions dropdown.

15. The Attach Volume dialog box appears. Use the Instance dropdown to select the

sensor instance where you want to attach the encrypted volume. Ensure that Device
name is set to /dev/sda1 and click Attach volume.

16. Return to the Instances list, select the entry for the sensor with the new encrypted
volume, and select Start instance from the Instance state dropdown to start it.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

