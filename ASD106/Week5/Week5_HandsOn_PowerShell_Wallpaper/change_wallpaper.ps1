# .SYNOPSIS
#   A PowerShell script to change the desktop wallpaper at specified intervals.
#
# .DESCRIPTION
#   This script allows users to:
#   - Set the total running time and interval for wallpaper changes.
#   - Select an image source (local folder or online).
#   - Use random wallpaper selection from the specified source.
#
# .PARAMETER TotalTime
#   Specifies the total time in minutes the script should run.
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
#   PowerShell.exe -ExecutionPolicy Bypass -File .\change_wallpaper.ps1

param(
    [int]$TotalTime,
    [int]$Interval,
    [ValidateSet("Local", "Online")]
    [string]$ImageSource,
    [string]$ImagePath
)

# Ask for user input
$TotalTime = Read-Host "Enter the total time (in minutes) for the script to run"
$Interval = Read-Host "Enter the interval (in minutes) between wallpaper changes"
$ImageSource = Read-Host "Enter 'Local' for local folder or 'Online' for online source"
$ImagePath = Read-Host "Enter the path to the image folder or URL for online images"

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
        $SPI_SETDESKWALLPAPER = 0x0014
        $UpdateIniFile = 0x01
        $SendChangeEvent = 0x02
        $flags = $UpdateIniFile -bor $SendChangeEvent # Bitwise OR operation for update flags
        [Win32.Wallpaper]::SystemParametersInfo($SPI_SETDESKWALLPAPER, 0, $Path, $flags)
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
    $startTime = Get-Date
    $endTime = $startTime.AddMinutes($TotalTime) # Dynamic end time based on user input

    while ((Get-Date) -lt $endTime) {
        switch ($ImageSource) {
            "Local" {
                $imageFiles = Get-ChildItem -Path $ImagePath -Include "*.jpg","*.jpeg","*.png" -Recurse
                if ($imageFiles.Count -gt 0) {
                    $randomImage = $imageFiles | Get-Random
                    Set-DesktopWallpaper($randomImage.FullName)
                } else {
                    Write-Error "No images found in the specified folder."
                    break
                }
            }
            "Online" {
                $tempFile = Join-Path $env:TEMP "temp_wallpaper.jpg"
                Invoke-ImageDownload $ImagePath $tempFile
                Set-DesktopWallpaper $tempFile
                Remove-Item $tempFile -Force # Clean up temporary file
            }
        }

        Start-Sleep -Seconds ($Interval * 60) # Dynamic wait time based on user input
    }

    Write-Output "Wallpaper change task has finished."
} catch {
    Write-Error "An error occurred: $_"
}
