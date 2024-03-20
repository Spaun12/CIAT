# Michael Connell
# Week 4 - Hands On User-defined functions in PowerShell
# 2024/03/02

# Function: GreetUser
function GreetUser($UserName) {
    Write-Host "Hey there, $UserName!"
    }
    
    # Function: GetSum
    function GetSum($Number1, $Number2) {
        return $Number1 + $Number2
    }
    
    # Function: IsEven
    function IsEven($Number) {
        if ($Number % 2 -eq 0) {
            return "Even"
        } 
        else { return "Odd" }
    }
    
    # Main execution loop - This will keep the script running until the user chooses to exit
while ($true) {
    # Get user's name
    $Name = Read-Host "Alright, player, what should I call you?"

    # Call GreetUser function
    GreetUser $Name

    # Get two numbers with try-again feature
    $gotValidNumbers = $false
    while (-not $gotValidNumbers) {
        $Num1 = Read-Host "Enter the first number"
        $Num2 = Read-Host "Enter the second number"

        try {
            # Convert inputs to integers
            $Num1 = [int]$Num1
            $Num2 = [int]$Num2
            $gotValidNumbers = $true # Success! Exit loop
        } catch {
            Write-Host "Oops! Please enter valid numbers."
        }
    }

    # Call GetSum function
    $Result = GetSum $Num1 $Num2
    Write-Host "The sum is: $Result"

    # Initialize wrong sum attempts
    $wrongSumAttempts = 0
    
    # Get a number for even/odd check with try-again feature and sum validation
    $gotValidNumber = $false
    while (-not $gotValidNumber) { 
        $CheckNum = Read-Host "Enter the sum given to see if it's even or odd"
        try {
            $CheckNum = [int]$CheckNum
            if ($CheckNum -ne $Result) { 
                $wrongSumAttempts += 1 

                if ($wrongSumAttempts -eq 1) {
                    Write-Host "Whoa, does not compute! That's not the right sum. Try again!"
                } else {
                    Write-Host "Woah, you're seriously messing with my program, player! It's like, totally fried!"
                    break # End the script
                }
            } else {
                $gotValidNumber = $true 
            }
        } catch {
            Write-Host "Oops! Please enter a valid number."
        }
    } 

    # Call IsEven function (only if they didn't destroy the program)
    if ($wrongSumAttempts -lt 2) {
        $EvenOdd = IsEven $CheckNum
        Write-Host "The number is: $EvenOdd" 
    }

    # Ask if the user wants to try again 
    $tryAgain = Read-Host "Would you like to try again, $Name? (Y/N)"
    if ($tryAgain.ToLower() -ne "y") {
        break  
    }
}

    
