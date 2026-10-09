Stellar Cyber 6.6.0s is now live! Discover all the updates in the release notes!

✖

Cloning Windows Server Sensor VMs

This topic describes how clone a virtual machine with the Windows Server Sensor installed so
that it can be reused elsewhere in your virtual environment.

The Challenge
Windows Server Sensors are uniquely identified by an Engine ID. No two Server Sensors can
share the same Engine ID. Cloning a VM with the Windows Server Sensor installed results in two
Server Sensors with the same Engine ID.

The Solution
You can get around this issue by resetting Engine IDs on individual VMs as you clone them.
However, this can be tedious when you are creating multiple clones from a single VM.

As an improved solution, you can create a VM that can be used as a clone template by deleting
the Windows Registry keys that contain the Engine ID. Then you can shut down the VM, clone it
multiple times, and restart both the source and the clones. Both the source Server Sensor and
each of the clones receive new, unique Engine IDs when they are restarted.

DP Settings Retained

You will have to reapply a token used to authorize and configure the Server Sensors. Once you
have done so, the clones will automatically register themselves with the DP from which you
obtained the token.

The Procedure
The following procedure describes how to clone a VM with the Windows Server Sensor installed:

1. On the Windows Server Sensor host, navigate to

C:\ProgramData\StellarCyber\Windows Agent Sensor\config and open the
aos.yaml file in a text editor.

2. Make the following changes in the aos.yaml file:

Set engid = 0000000000000000

Set registered = 0

3. Navigate to C:\ProgramData\StellarCyber\Windows Agent Sensor\config and

delete ds_token, if it exists.

4. Shut down the host VM so that it can be cloned.

5. Clone the VM.

6. Start the cloned and source VMs.

7. Reapply the token used to authorize and configure the cloned Server Sensors.

 You can reapply a token from the command line using aella_cli_win.exe with the

following syntax:
C:\Program Files\Aella\bins\aella_cli_win.exe set token string
<token>

Stellar Cyber version 6.6.0s

© 2026 Stellar Cyber . All rights reserved.

Support   |  Contact Us   |        

