Reading: Exemplar: Manage files with Linux
commands

Activity overview
In this lab activity, you’ll use Linux commands to modify a directory structure and the files it contains.

You’ll also use the nano text editor to add text to a file.

You previously learned that directories help you organize subdirectories and files in Linux. As a security
analyst, creating, removing, and editing directories and files are core tasks you’ll need to perform to
help you to manage data.

When data is well organized, you can more easily detect issues and keep data safe.

With that in mind, you’re now ready to practice what you've learned.

This exemplar is a walkthrough of the previous Qwiklab activity, including detailed instructions and
solutions. You may use this exemplar if you were unable to complete the lab and/or you need extra
guidance in competing lab tasks. You may also refer to this exemplar to prepare for the graded quiz in
this module.

Scenario
In this scenario, you need to ensure that the /home/analyst directory is properly organized.

You have to make a few changes to the /home/analyst directory and the files it contains.

You also have to edit a file to record the changes or updates you make to the directory.

When you start, the /home/analyst directory contains the following subdirectories and files:

home
└── analyst
           ├── notes
           │       ├── Q3patches.txt
           │       └── tempnotes.txt
           ├── reports
           │       ├── Q1patches.txt
           │       └── Q2patches.txt

          └── temp

You need to modify the /home/analyst directory to the following directory and file structure:

home
└── analyst
          ├── logs
          ├── notes
          │       └── tasks.txt
          └── reports
                     ├── Q1patches.txt
                     └── Q2patches.txt
                     └── Q3patches.txt

Here’s how you’ll do this: First, you’ll create a new subdirectory called logs in the /home/analyst
directory. Next, you’ll remove the temp subdirectory. Then, you’ll move the Q3patches.txt file to the
reports subdirectory and delete the tempnotes.txt file. Finally, you’ll create a new .txt file called
tasks in the notes subdirectory and add a note to the file describing the tasks you've performed.

You’ll need to use the commands learned in the video lesson to complete these steps.

This might sound like quite a number of tasks to perform, but you’ll be guided on how to do this.

Task 1. Create a new directory
First, you must create a dedicated subdirectory called logs, which will be used to store all future log
files.

1. Create a new subdirectory called logs in the /home/analyst directory.

The command to complete this step:

mkdir logs

2. List the contents of the /home/analyst directory to confirm that you’ve successfully created the
new logs subdirectory.

The command to complete this step:

ls

The output should list the original three directories and the new logs subdirectory:

logs notes reports temp

Task 2. Remove a directory
Next, you must remove the temp directory, as you’ll no longer be placing items in it.

1. Remove the /home/analyst/temp directory.

The command to complete this step:

rmdir temp

2. List the contents of the /home/analyst directory to confirm that you have removed the temp
subdirectory.

The command to complete this step:

ls

The temp directory should no longer be listed:

logs notes reports

Task 3. Move a file
The Q3patches.txt file contains notes taken on third-quarter patches and is now in the correct
reporting format.

You must move the  Q3patches.txt file from the notes directory to the reports directory.

1. Navigate to the /home/analyst/notes directory.

The command to complete this step:

cd /home/analyst/notes

The previous command used the absolute path, you could use the relative path as follows:

cd notes

2. Move the Q3patches.txt file from the /home/analyst/notes directory to the
/home/analyst/reports directory.

The command to complete this step:

mv Q3patches.txt /home/analyst/reports/

3. List the contents of the /home/analyst/reports directory to confirm that you have moved the file
successfully.

The command to complete this step:

ls /home/analyst/reports

When you list the contents of the reports directory, it should show that three quarterly report files are
now in the reports directory:

Q1patches.txt Q2patches.txt Q3patches.txt

Task 4. Remove a file
Next, you must delete an unused file called tempnotes.txt from the /home/analyst/notes directory.

Remove the tempnotes.txt file from the /home/analyst/notes directory.

The command to complete this step:

rm tempnotes.txt

2. List the contents of the /home/analyst/notes directory to confirm that you’ve removed the file
successfully.

The command to complete this step:

ls

Task 5. Create a new file
Now, you must create a file named tasks.txt in the /home/analyst/notes directory that you’ll use to
document completed tasks.

1. Use the touch command to create an empty file called tasks.txt in the /home/analyst/notes
directory.

The command to complete this step:

touch tasks.txt

2. List the contents of the /home/analyst/notes directory to confirm that you have created a new file.

The command to complete this step:

ls

A file called tasks.txt should now exist in the notes directory:

tasks.txt

Task 6. Edit a file
Finally, you must use the nano text editor to edit the tasks.txt file and add a note describing the tasks
you’ve completed.

1. Using the nano text editor, open the tasks.txt file that is located in the /home/analyst/notes
directory.

The command to complete this step:

nano tasks.txt

Note: This action changes the shell from the normal Bash interface to the nano text editor interface.

2. Copy and paste the following text into the text input area of the nano editor:

 Completed tasks
  1. Managed file structure in /home/analyst

3. Press CTRL+X to exit the nano text editor.

This triggers a prompt asking Save modified bufferer?

4. Press Y to confirm that you want to save the new data to your file. (Answering "no" will discard
changes.)

5. Press ENTER to confirm that File Name to Write is tasks.txt.

Note: The recommended sequence of commands for saving a file with the nano text editor is to use
CTRL+O to tell nano to save the file and then use CTRL+X to exit immediately.

In this web-based lab environment, the CTRL+O command is intercepted by your web browser and is
interpreted as a request to save the web page. The sequence used here is a commonly used
alternative that achieves the same end result.

6. Use the clear command to clear the Bash shell window and remove any traces of the nano text input
area.

The command to complete this step:

Note: Most Bash shells typically handle the screen cleanup after you exit nano. In this lab environment,
nano sometimes leaves some text clutter around the edges of the screen that the clear command
cleans up for you.

7. Display the contents of the tasks.txt file to confirm that it contains the updated task details.

cat tasks.txt

This file should now contain the contents of the tasks.txt file that you added and saved in previous
steps:

Completed tasks
  1. Managed file structure in /home/analyst

Conclusion
Great work!

You now have practical experience in using basic Linux Bash shell commands to

●  create and remove directories,
●  copy, move, and remove files, and
●  edit files with the nano text editor.

You’re well on your way to managing directories and files in a Linux environment!

