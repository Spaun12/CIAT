#!/bin/bash
# Shebang: Tells the system this is a Bash script

echo "Enter a directory name:"
# Prompt the user to enter a directory name

read dirname
# Read the user input and store it in the variable 'dirname'

if test -d "$dirname"; then
  # Test if the directory exists (-d checks for directory)
  echo "The directory $dirname already exists"
  # Output if directory exists
else
  mkdir "$dirname"
  # Create new directory
  echo "The directory $dirname has been created"
  # Output if directory has been created
fi
# End of if-else block
