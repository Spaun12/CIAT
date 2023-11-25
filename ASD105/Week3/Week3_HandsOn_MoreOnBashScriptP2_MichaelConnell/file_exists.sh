#!/bin/bash
# Shebang: Tells the system this is a Bash script

echo "Enter a file name:"
# Prompt the user to enter a file name

read filename
# Read the user input and store it in the variable 'filename'

if test -e "$filename"; then
  # Test if the file exists (-e checks for existence)
  echo "The file $filename exists"
  # Output if file exists
else
  echo "The file $filename does not exist"
  # Output if file does not exist
fi
# End of if-else block
