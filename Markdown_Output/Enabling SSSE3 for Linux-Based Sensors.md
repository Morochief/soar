Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Enabling SSSE3 for Linux-Based Sensors

In order to guarantee the performance of your virtual modular sensors, you must ensure that
SSSE3 is enabled for their processors. Refer to the procedure below.

 Virtual modular sensors installed on Linux hosts must have SSSE3 enabled for their

processors in order to operate correctly.
SSSE3 is typically supported/enabled for most vCPUs, but may not be for certain legacy
AMD vCPUs. See below for instructions on enabling SSSE3.

To enable SSSE3 for a virtual machine:

1. Start the virtual shell (virsh)

2. Type the following command to edit the virtual machine's settings:

edit <virtual_machine_name>

3. Locate the <cpu> section. It should appear similar to the following:

<cpu mode='custom' match='exact' check='partial'>

    <model fallback='allow'>SandyBridge</model>

......

 </cpu>

4. Add the following line to the <cpu> section:

<feature policy='require' name='ssse3'/>

When you are done, the <cpu> section should appear similar to the following:

<cpu mode='custom' match='exact' check='partial'>

    <model fallback='allow'>SandyBridge</model>

    <feature policy='require' name='ssse3'/>

...........

  </cpu>

5. Save changes to the virtual machine and exist virsh.

6. Run the following command:

virsh define /etc/libvirt/qemu/<virtual_machine_name>.xml

 Each virtual machine has a configuration .xml file. Typically, these files are stored

under /etc/libvirt/qemu, but the location may be different for your system.

7. Stop and start the virtual machine in virsh.

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

