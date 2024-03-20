# Michael Connell
# 2024/03/05
# Week 5- Hands On PowerShell and Wallpaper

# This script schedules the Set-Wallpaper.ps1 script to run at regular intervals
# Ask for source (Folder or Pexels)
$Source = Read-Host "Enter 'Folder' for local images or 'Pexels' for online images"
# Ask for interval in minutes
$Interval = Read-Host "Enter the interval in minutes at which the wallpaper should change"
# If Folder is chosen, ask for the folder path
$FolderPath = $null
if ($Source -eq "Folder") {
    $FolderPath = Read-Host "Enter the full path to your image folder"
}
# Ask how many hours the task should run
$DurationHours = Read-Host "Enter how many hours the task should run"

# Determine the script path
$scriptPath = "C:\Users\mdcte\OneDrive\Computer learning\CIAT1\CIAT2\ASD106\Week5\Week5_HandsOn_PowerShell_Wallpaper\Set-Wallpaper.ps1" # Ensure this path is correct

# Create Scheduled Task Action
$arguments = "-NoProfile -ExecutionPolicy Bypass -File `"$scriptPath`" -Source $Source"
if ($Source -eq "Folder") {
    $arguments += " -FolderPath `"$FolderPath`""
}
$action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument $arguments

# Calculate the repetition duration in the format expected by Register-ScheduledTask
$repetitionDuration = (New-TimeSpan -Hours $DurationHours)

# Create Trigger
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes $Interval) -RepetitionDuration $repetitionDuration

# Register the scheduled task
$taskName = "DynamicWallpaperChange"
try {
    Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -Force
    Write-Host "Wallpaper change scheduled every $Interval minutes for $DurationHours hours."
}
catch {
    Write-Error "Failed to schedule the task: $_"
}


