#Funny Joke Code

import random

# List of jokes
jokes = [
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why did the coffee file a police report? It got mugged!",
    "Why did the math book look so sad? Because it had too many problems.",
    "Why don’t scientists trust atoms? Because they make up everything.",
    "Why did the scarecrow win an award? Because he was outstanding in his field."
]

# Initialize a list to keep track of which jokes have been told
told_jokes = []

# Function to ask if the user wants to hear a joke
def ask_for_joke():
    response = input("Would you like to hear a joke? (y/n) ")
    return response.lower() == 'y'

# Function to ask if the user wants to hear another joke
def ask_for_another_joke():
    response = input("Would you like to hear another joke? (y/n) ")
    return response.lower() == 'y'

# Function to tell a random joke
def tell_joke():
    # Check if all jokes have been told
    if len(told_jokes) == len(jokes):
        print("I'm all out of jokes. Have a nice day!")
        return
    
    # Select a random joke from the list that hasn't been told yet
    joke = random.choice([j for j in jokes if j not in told_jokes])
    
    # Add the joke to the list of told jokes
    told_jokes.append(joke)
    
    # Print the joke
    print(joke)
    
    # Ask if the user wants to hear another joke
    if ask_for_another_joke():
        tell_joke()

# Start the app
while ask_for_joke():
    tell_joke()
