## Desktop Wallpaper Changer Script

These PowerShell scripts automate changing your desktop wallpaper at regular intervals, either by selecting images from a local folder or fetching random images online from Pexels.

**Requirements**

*   Windows PowerShell (version 5.1 or later recommended).
*   Administrator privileges for scheduled task creation.
*   A Pexels API key if using online images from Pexels.

**Usage**

1.  Set-Wallpaper.ps1: Handles the actual changing of the wallpaper.
    Save this script as Set-Wallpaper.ps1.
2.  Schedule-Wallpaper.ps1: Schedules the wallpaper changes at specified intervals.
    Save this script as Schedule-Wallpaper.ps1.
3.  Open a PowerShell console with administrator privileges.
3.  Usage
    For Immediate Wallpaper Change:
    Run Set-Wallpaper.ps1 with the necessary parameters to immediately change the wallpaper.

**Example**

`.\Set-Wallpaper.ps1 -Source <Folder or Pexels> -FolderPath <Local_Folder_Path>`

**To Schedule Wallpaper Changes:**

1.  Open a PowerShell console with administrator privileges.
2.  Execute Schedule-Wallpaper.ps1 with the desired parameters to set up scheduled wallpaper changes.

`.\Schedule-Wallpaper.ps1`

**Immediate Change Using Pexels:**

1. You'll need to edit Set-Wallpaper.ps1 to include your Pexels API key.

`.\Set-Wallpaper.ps1 -Source Pexels -SearchTerm "Nature"`

**Scheduling Wallpaper Changes from a Local Folder:**

After running .\Schedule-Wallpaper.ps1, specify:

Source: Folder
Interval: 60 (for 60 minutes)
Folder Path: "C:\Users\YourName\Pictures\Wallpapers"
Duration: 24 (to run the task for 24 hours)
Notes:

Ensure you have your Pexels API key ready if you choose Pexels as the image source.
Scheduled tasks require administrator privileges to create. Make sure to run the PowerShell console as an administrator.

**Suppressing Command Prompt Pop-Up When Scheduling Wallpaper Changes**
- When using the Schedule-Wallpaper.ps1 script to schedule regular wallpaper changes, you may notice a brief command prompt window popping up each time the wallpaper is changed. This occurs because the scheduled task is configured to run a PowerShell script, which by default, opens a console window.

**Recommendation to Suppress the Pop-Up:**

To prevent the command prompt window from appearing, you can modify the task action in the Schedule-Wallpaper.ps1 script to include the `-WindowStyle` Hidden parameter when invoking PowerShell. This makes the execution window invisible.

**Updated Task Action Example:**

When setting up the scheduled task action within Schedule-Wallpaper.ps1, ensure the action is defined as follows:

```$action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$scriptPath`" -Source $Source -FolderPath `"$FolderPath`""```

This modification ensures that PowerShell executes the script without displaying the command prompt window, providing a seamless experience.

Note: While this approach effectively suppresses the window, it's essential to test your scheduled tasks after making this change to ensure they continue to work as expected in your environment. Some users may require administrative privileges for this change to take effect.

**And Finally Using Third-Party Schedulers for Background Execution**
For users seeking additional features or a more seamless background execution, third-party task schedulers like `System Scheduler or Z-Cron Scheduler` can offer advanced control, including the ability to run tasks without any visible windows. These tools provide a robust alternative to Windows Task Scheduler, with intuitive interfaces for scheduling and managing tasks invisibly.

