#!/bin/bash

# Prompt the user to enter the name of the file to search within
echo "Enter the file name:"
read filename

# Check if the file exists
if test -f "$filename"; then
    # Prompt the user to enter the search text
    echo "Enter the text to search for:"
    read search_text
    
    # Prompt the user to enter the replacement text
    echo "Enter the text to replace with:"
    read replace_text
    
    # Perform the search and replace operation
    sed -i "s/$search_text/$replace_text/g" "$filename"
    
    # Inform the user that the operation is complete
    echo "The text has been replaced."
else
    # Inform the user that the file doesn't exist
    echo "The file $filename does not exist."
fi
