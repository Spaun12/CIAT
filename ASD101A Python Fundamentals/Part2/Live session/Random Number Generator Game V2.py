#Random Number Generator Game V2b

import random

# Ask the user how many attempts they would like
attempts = int(input("How many attempts would you like to guess the number? "))

def guess_game(attempts):
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    
    # Counter to keep track of the number of guesses
    guesses = 0
    
    # Loop until the user runs out of attempts or correctly guesses the number
    while guesses < attempts:
        # Ask the user to guess the number
        guess = int(input("Guess the number between 1 and 100: "))
        guesses += 1

        # Check if the guess is correct
        if guess == number:
            return f"You win! The number was {number}."

        # Check if the guess is too high or low
        elif guess > number:
            if guesses < attempts - 1:
                print("Too high, try again.")
            else:
                print("Too high.")
        else:
            if guesses < attempts - 1:
                print("Too low, try again.")
            else:
                print("Too low.")

    return f"You lost! The number was {number}."

print(guess_game(attempts))

