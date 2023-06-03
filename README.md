
# checkoraimopod
Used in conjuction with the Windows Task Scheduler, this application checks whether the oraimo FreePods 3 TWS True Wireless Stereo Earbuds is available and sends notification to the windows desktop.

# Requirements
You need to install python on your windows computer.
Link: https://www.python.org/downloads/

# Note:
-  This application is specific to the oraimo FreePods 3 TWS True Wireless Stereo Earbuds. However, feel free to download and edit code for other products.
-  You will need to manually schedule a task on your windows machine to run the script. (Steps are given below)


# Steps to schedule task to run script on windows
NOTE: Be careful not to touch anything you do not understand
-  Click on the windows icon and search "Task Scheduler"
-  On the left pane, Select the "Task Scheduler Library"
-  Click on "Create Task" on the right pane
-  On the dialog box that appears, Enter the Name (Any name of your choice) and description
-  Check the "Run whether user is logged on or not"
-  Select the "Triggers" tab and set up the timing to run the script
-  At the "Actions" tab set Action to "Start a program" and select the location of python installation on your computer in the Program/script field.
-  (optional) You can specify the name of the python script in the "Add arguments" field and the location of the script in the "Start in" field.

Enjoy!
