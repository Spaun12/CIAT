#Week2 Hands On Trouble Shoot Syntax using Doc Library Michael Connell
import requests

# Prompt the user to input the API URL
api_url = input("Enter the API URL: ")

# Try to make a GET request to the API URL
try:
    response = requests.get(api_url)
    # If the response is successful (status code 200), extract the JSON content
    if response.status_code == 200:
        try:
            content = response.json()
        except AttributeError as e:
            # If an AttributeError occurs, check the documentation for the correct syntax
            print("An error occurred:", e)
            print("Checking the documentation for the correct syntax...")
            content = response.content.decode()
            print("The correct syntax is: content = response.content.decode()")
        print(content)
    else:
        # If the response is not successful (status code other than 200), raise an error
        response.raise_for_status()
except Exception as e:
    # If an error occurs, print the error message
    print(f"An error occurred: {e}")

