# Michael Connell
# Date: 2023-05-24  
# Week 1 - Chapter 2 Assignment - Program Design and Implementation

# Importing required libraries
from random import randint

def play_game():
    # Welcome the user to the game
    print("\nWelcome to the Square and Filter game!\n")

    # Ask the user to guess if the number of even squares will be over or under 5
    print("We will generate a list of 10 random numbers, square them, and then filter only the even squares.")
    user_guess = input("Do you think the number of even squares will be over or under 5? Please enter 'over' or 'under': ")

    # Create a list of 10 random numbers between 1 and 100
    original_list = [randint(1, 100) for _ in range(10)]

    # Use the map function to square each number in the list
    squared_list = list(map(lambda x: x**2, original_list))

    # Use the filter function to select only the even numbers from the squared list
    filtered_list = list(filter(lambda x: x % 2 == 0, squared_list))

    # Check the user's guess and provide the result
    if (len(filtered_list) > 5 and user_guess == 'over') or (len(filtered_list) <= 5 and user_guess == 'under'):
        print("\nCongratulations! Your guess was correct!")
    else:
        print("\nSorry, your guess was not correct.")

    # Print the original list of numbers, the squared list, and the filtered list
    print(f"\nOriginal list: {original_list}")
    print(f"Squared list: {squared_list}")
    print(f"Filtered list: {filtered_list}")

# Start the game
play_again = 'yes'
while play_again.lower() == 'yes':
    play_game()
    play_again = input("\nWould you like to play again? (yes/no): ")

print("\nThanks for playing! Have a nice day.")