#!/bin/bash
# Program 2 - I/O (Input and Output)
# This script takes a user input and prints it back.

while true; do  # Infinite loop to allow retries
  # Prompt the user for input
  echo "Greetings, User! What is your name?"

  # Read the input
  read name

  # Error handling: Check if the name is empty
  if [[ -z "$name" ]]; then
    echo "Ah, a silent type, huh? Would you like to try again? (y/n)"
    read retry
    if [[ "$retry" == "n" ]]; then
      echo "Alright, exit stage left!"
      exit 1
    else
      echo "Take two! Action!"
      continue
    fi
  fi

  # Print the input back and exit the loop
  echo "Salutations, $name! Welcome to the Matrix."
  break
done

