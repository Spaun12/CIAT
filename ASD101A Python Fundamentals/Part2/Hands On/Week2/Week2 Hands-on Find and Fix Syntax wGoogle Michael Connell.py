# Week2 Hands-on Find and Fix with Google Michael Connell
import requests
from bs4 import BeautifulSoup
# Define a function that takes a syntax error message as input
def search_for_syntax_error(error_message):
    # Construct a search query by combining the error message with a search for Stack Overflow
    search_query = error_message + " site:stackoverflow.com"
    # Encode the search query as a URL
    search_url = "https://www.google.com/search?q=" + search_query
    # Send a GET request to the search URL
    response = requests.get(search_url)
    # Use BeautifulSoup to parse the HTML response
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Initialize an empty list to store the results
    results = []
    # Find all the `a` elements (links) in the HTML response
    for link in soup.find_all("a"):
        # Get the `href` attribute of the link
        href = link.get("href")
        # Check if the `href` attribute starts with "/url?q="
        if href.startswith("/url?q="):
            # Extract the URL from the `href` attribute
            url = href[7:]
            # Add the URL to the list of results
            results.append(url)
    # Return the list of results
    return results
# Prompt the user to input the error message they are looking for
error_message = input("Enter the syntax error message: ")
# Call the search_for_syntax_error function with the user's input
results = search_for_syntax_error(error_message)
# Print the results in a numbered list
print("Results:")
for i, result in enumerate(results):
    # Print each result on a new line, with a space before the number
    print(f" {i + 1}. {result}")