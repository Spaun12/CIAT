#Positive Quote Generator

import requests
import json
import time
import os

# Check if the script is running in a scheduled task
is_scheduled_task = "SystemPropertiesScheduledTasks" in os.environ.get("COMPUTERNAME", "")

# Define a function to get a random quote and ask the user if they want another one
def get_quote():
    # Make a request to the Quotes API
    response = requests.get("https://zenquotes.io/api/random")

    # Parse the JSON response
    data = json.loads(response.text)

    # Extract the quote and author from the data
    quote = data[0]["q"]
    author = data[0]["a"]

    # Print a greeting with the user's name
    print(f"Good morning, Michael! Here's a positive quote for you:\n")

    # Print the quote and author
    print(f"{quote}\n- {author}")

    # Ask the user if they want another quote, unless the script is running in a scheduled task
    if not is_scheduled_task:
        while True:
            answer = input("Would you like another quote? (Y/N): ").lower()
            if answer == "y":
                print("\n")
                time.sleep(1)
                get_quote()
            elif answer == "n":
                break
            else:
                print("Invalid input. Please enter Y or N.")

# Call the function to start the program
get_quote()