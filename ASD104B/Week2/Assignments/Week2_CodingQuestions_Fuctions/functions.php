<?php
//Function1
function concatenateString($number, $string) {
    // Initialize an empty string to store the concatenated result
    $result = "";
    
    // Loop $number times to concatenate the $string that many times
    for ($i = 0; $i < $number; $i++) {
        $result .= $string;
    }
    
    // Return the concatenated string
    return $result;
}

// Example usage:
// This will print the string "I want my MTV" three times
echo "Function 1 output: " . concatenateString(3, "I want my MTV") . "<br>";

//Function2
function countVowels($string) {
    // Define a string containing all the vowels
    $vowels = "aeiouAEIOU";
    
    // Initialize a counter to zero
    $count = 0;

    // Loop through each character in the input string
    for ($i = 0; $i < strlen($string); $i++) {
        // If the character is a vowel, increment the counter
        if (strpos($vowels, $string[$i]) !== false) {
            $count++;
        }
    }
    
    // Return the final count of vowels
    return $count;
}

// Example usage:
// This will print the number of vowels in the phrase "Boots on the ground"
echo "Function 2 output: " . countVowels("Boots on the ground") . "<br>";

//Function3
function squareNumbers($array) {
    // Create a new array to store the squared numbers
    $squaredArray = array();

    // Loop through each number in the input array
    foreach ($array as $number) {
        // Square the number and add it to the new array
        $squaredArray[] = $number * $number;
    }
    
    // Return the new array with squared numbers
    return $squaredArray;
}

// Example usage:
// This will print an array containing the squares of each number in the input array
echo "Function 3 output:<pre>";
print_r(squareNumbers(array(1, 2, 3, 4, 5)));
echo "</pre><br>";

//Function4
function isAlphabetical($string) {
    // Check if the string contains only alphabetical characters using ctype_alpha function
    if (ctype_alpha($string)) {
        return true;
    } else {
        return false;
    }
}

// Example usage:
// This will print true because the input string contains only alphabetical characters
echo "Function 4 output: " . var_export(isAlphabetical("SemperFi"), true) . "<br>";

//Function5
function validateDateFormat($date) {
    // Define a pattern to match the date format "mm/dd/yyyy"
    $pattern = '/^(0[1-9]|1[0-2])\/(0[1-9]|[12][0-9]|3[01])\/(19|20)\d\d$/';
    
    // Check if the input date matches the defined pattern using preg_match function
    if (preg_match($pattern, $date)) {
        // Further validate if the date is a valid calendar date using checkdate function
        list($month, $day, $year) = explode('/', $date);
        if (checkdate((int)$month, (int)$day, (int)$year)) {
            return true;
        }
    }

    // Return false if the date does not match the pattern or is not a valid calendar date
    return false;
}

// Example usage:
// This will print false due to February not having 30 days
echo "Function 5 output: " . var_export(validateDateFormat("02/30/2023"), true) . "<br>";
?>
