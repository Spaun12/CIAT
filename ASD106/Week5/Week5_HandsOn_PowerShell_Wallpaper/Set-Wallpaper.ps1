# Michael Connell
# 2024/03/05
# Week 5- Hands On PowerShell and Wallpaper

# This script sets the desktop wallpaper to a random image from a specified folder or from the Pexels API
# It also includes a function to set the wallpaper using the SystemParametersInfo Win32 API
# The Get-RandomImage function retrieves a random PNG image from the specified folder
# The Get-PexelsImage function retrieves a random image from the Pexels API based on a search term
# The Set-Wallpaper function sets the desktop wallpaper using the SystemParametersInfo Win32 API
# The main script logic determines the source of the wallpaper (Folder or Pexels) and calls the appropriate function to retrieve the image
# The retrieved image path is then passed to the Set-Wallpaper function to set the desktop wallpaper

# Define script parameters for source selection and optional folder path
param(
    [Parameter(Mandatory = $true)]
    [ValidateSet("Folder", "Pexels")]
    [string]$Source,

    [string]$FolderPath = "C:\Test"
)

# Function to set the desktop wallpaper
function Set-Wallpaper {
    param([string]$ImagePath)
    
    $code = @"
using System;
using System.Runtime.InteropServices;

public static class Wallpaper {
    [DllImport("user32.dll", CharSet = CharSet.Auto)]
    public static extern int SystemParametersInfo(int uAction, int uParam, string lpvParam, int fuWinIni);
}
"@

    Add-Type -TypeDefinition $code -Language CSharp

    $SPI_SETDESKWALLPAPER = 0x0014
    $SPIF_UPDATEINIFILE = 0x01
    $SPIF_SENDCHANGE = 0x02
    $flags = $SPIF_UPDATEINIFILE -bor $SPIF_SENDCHANGE

    [Wallpaper]::SystemParametersInfo($SPI_SETDESKWALLPAPER, 0, $ImagePath, $flags) | Out-Null
}

# Function to retrieve a random image from a specified folder
function Get-RandomImage {
    param([string]$FolderPath)
    
    # Retrieves all PNG files from the folder path
    $images = Get-ChildItem -Path $FolderPath -Include "*.png" -Recurse -File
    if ($images -eq $null -or $images.Count -eq 0) {
        throw "No PNG images found in the specified folder path: $FolderPath"
    }
    
    # Selects a random image from the array of images
    $randomImage = Get-Random -InputObject $images

    return $randomImage.FullName
}

# Function to retrieve a random image from the Pexels API this was a really fun api to use. So many high quality pictures.
function Get-PexelsImage {
    param([string]$SearchTerm)
    
    $apiKey = "utg7Xo5bLpRVaenpl7rjqxyqTFCtszEPE3TOnopECzsNW6pFiUNCrE8G" # Make sure to replace with your personal Pexels API key
    $baseUrl = "https://api.pexels.com/v1/search?query=$SearchTerm&per_page=80"
    
    $headers = @{ "Authorization" = $apiKey }
    $response = Invoke-RestMethod -Method Get -Uri $baseUrl -Headers $headers
    $randomImage = $response.photos | Get-Random
    $downloadUrl = $randomImage.src.original

    $fileName = "pexels_wallpaper_" + (Get-Date -Format "yyyyMMddHHmmss") + ".jpg"
    $tempPath = Join-Path -Path $env:TEMP -ChildPath $fileName
    Invoke-WebRequest -Uri $downloadUrl -OutFile $tempPath
    
    return $tempPath
}

# Main script logic to determine the source of the wallpaper and retrieve the image
if ($Source -eq "Folder") {
    $imagePath = Get-RandomImage -FolderPath $FolderPath
} elseif ($Source -eq "Pexels") {
    $searchQuery = "nature"
    $imagePath = Get-PexelsImage -SearchTerm $searchQuery
} else {
    Write-Error "Invalid source option. Choose 'Folder' or 'Pexels'"
    return
}

# Execute the Set-Wallpaper function to set the desktop wallpaper
Set-Wallpaper -ImagePath $imagePath
