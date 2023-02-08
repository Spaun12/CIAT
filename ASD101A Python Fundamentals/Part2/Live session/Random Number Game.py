#Random Number game
#Create a function that generates a random number between 1 and 100
# and prompts the user for the desired number of guesses. 
# The program will alert the user that their guess was incorrect
# if it is higher than the random number and encourage them 
# to try again if it is lower. When the allotted attempts are used 
# up or the user correctly guesses the number, the game is over.

import random

# Ask the user how many attempts they would like
attempts = int(input("""Welcome to the Random Number Game! 
            How many attempts would you like to guess the number? """))

def guess_game(attempts):
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)

    # Loop for the number of attempts provided by the user
    for i in range(attempts):
        # Ask the user to guess the number
        guess = int(input("Guess the number between 1 and 100: "))

        # Check if the guess is correct
        if guess == number:
            # If the guess is correct, return a message indicating the user has won
            return f"You win! The number was {number}."

        # Check if the guess is too high
        elif guess > number:
            print("Too high, try again.")

        # If the guess is not correct or too high, it must be too low
        else:
            print("Too low, try again.")

    # If the loop has ended, the user has not won, so return a message indicating they lost
    return f"Almost! The number was {number}."

# Start the game and print the result
print(guess_game(attempts))
