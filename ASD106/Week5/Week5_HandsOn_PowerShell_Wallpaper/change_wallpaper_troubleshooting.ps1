# .SYNOPSIS
#   A PowerShell script to change the desktop wallpaper at specified intervals.
#
# .DESCRIPTION
#   This script allows you to:
#   - Set the wallpaper change interval.
#   - Select an image source (local folder or online).
#   - Use random wallpaper selection from a folder.
#   - Schedule the wallpaper change task.
#
# .PARAMETER Interval
#   Specifies the interval for changing the wallpaper (in minutes).
#
# .PARAMETER ImageSource
#   Determines the source of wallpaper images. Can be "Local" or "Online".
#
# .PARAMETER ImagePath
#   Specify the path to the folder containing images if Local.
#   Specify a URL where images can be downloaded if Online.
#
# .EXAMPLE
#   .\change-wallpaper.ps1 -Interval 30 -ImageSource Local -ImagePath "C:\Users\YourName\Pictures\Wallpapers"
#
# .NOTES
#   - Requires administrator privileges to create a scheduled task.

param(
    [Parameter(Mandatory = $true, HelpMessage = "Interval in minutes")]
    [int]$Interval,

    [Parameter(Mandatory = $true, HelpMessage = "Image source (Local or Online)")]
    [ValidateSet("Local", "Online")]
    [string]$ImageSource,

    [Parameter(Mandatory = $true, HelpMessage = "Path to image folder or URL")]
    [string]$ImagePath
)

# Function to set the desktop wallpaper
function Set-DesktopWallpaper($Path) {
    Add-Type -TypeDefinition @"
    using System;
    using System.Runtime.InteropServices;
    public class Wallpaper {
        [DllImport("user32.dll", CharSet = CharSet.Auto)]
        public static extern int SystemParametersInfo(int uAction, int uParam, string lpvParam, int fuWinIni);
    }
"@ -Name "Wallpaper" -Namespace Win32

    try {
        [Win32.Wallpaper]::SystemParametersInfo(0x0014, 0, $Path, 0x0001 | 0x0002) 
    } catch {
        Write-Error "Failed to set wallpaper. Error: $_"
    }
}

# Function to download an image from the web
function Invoke-ImageDownload($url, $destinationPath) {
    try {
        Invoke-WebRequest -Uri $url -OutFile $destinationPath
    } catch {
        Write-Error "Failed to download image. Error: $_"
    }
}

# Main script execution
try {
    # Validate image source and obtain image
    switch ($ImageSource) {
        "Local" {
            $imageFiles = Get-ChildItem -Path $ImagePath -Filter *.jpg,*.jpeg,*.png
            if ($imageFiles) {
                $randomImage = $imageFiles | Get-Random
                Set-DesktopWallpaper($randomImage.FullName)
            } else {
                Write-Error "No images found in the specified folder."
            }
        }
        "Online" {
            # Download a random image from an online source
            $tempFile = Join-Path $env:TEMP "temp_wallpaper.jpg"
            Invoke-ImageDownload $ImagePath $tempFile  # Corrected function call
            Set-DesktopWallpaper $tempFile
            Remove-Item $tempFile -Force # Clean up temporary file
        }
    }

    # Schedule the wallpaper change task
    $taskName = "Change Desktop Wallpaper"
    $action = New-ScheduledTaskAction -Execute "PowerShell.exe" -Argument "-File `"$PSScriptRoot\change-wallpaper.ps1`" -Interval $Interval -ImageSource $ImageSource -ImagePath `"$ImagePath`""
    $trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionDuration (New-TimeSpan -Days 365) -RepetitionInterval (New-TimeSpan -Minutes $Interval)
    Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger -RunLevel Highest | Out-Null

    Write-Output "Wallpaper change task scheduled successfully."
} catch {
    Write-Error "An error occurred: $_"
}