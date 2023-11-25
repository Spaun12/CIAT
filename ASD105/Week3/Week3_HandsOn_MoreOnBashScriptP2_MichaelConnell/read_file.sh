#!/bin/bash
# Shebang: Tells the system this is a Bash script

echo "Enter the file name:"
# Prompt the user to enter a file name

read filename
# Read the user input and store it in the variable 'filename'

if test -f "$filename"; then
  # Test if the file exists and is a regular file (-f checks for regular file)
  echo "The contents of $filename are:"
  # Output header
  cat "$filename"
  # Print the contents of the file
else
  echo "The file $filename does not exist"
  # Output if file does not exist
fi
# End of if-else block
