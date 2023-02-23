#DnD Dice Roller Applican Idea
# Import the random module to generate random numbers
import random
# Define a dictionary mapping dice types (e.g. "d6") to the number of sides on the dice
dice_dict = {
    "d4": 4,
    "d6": 6,
    "d8": 8,
    "d10": 10,
    "d12": 12,
    "d20": 20
}
# Keep rolling until the user chooses to quit
while True:
    # Prompt the user to roll all of their dice at once, or individually
    roll_all = input("Would you like to roll all of your dice at once? (y/n) ")
    if roll_all == "y":
        # If the user selects "y", roll all the dice
        rolls = {}
        for dice_type, sides in dice_dict.items():
            roll = random.randint(1, sides)
            rolls[dice_type] = roll
        # Print the resulting rolls to the user
        print("Rolls:")
        for dice_type, roll in rolls.items():
            print(f"{dice_type} x 1: {roll}")
    else:
        # If the user selects "n", prompt for the number and type of dice, and generate rolls for each die individually using a for loop
        dice = int(input("How many dice? "))
        if dice <= 0:
            print("You must roll at least one die.")
            continue
        dice_types = []
        for i in range(dice):
            dice_type = input(f"Enter the type of dice {i+1}: ")
            if dice_type not in dice_dict:
                print("Invalid dice type. Please enter a valid type (e.g. d6).")
                break
            dice_types.append(dice_type)
        else:
            rolls = {}
            for dice_type in dice_types:
                sides = dice_dict[dice_type]
                roll = random.randint(1, sides)
                rolls[dice_type] = roll
            # Print the resulting rolls to the user
            print("Rolls:")
            for dice_type, roll in rolls.items():
                print(f"{dice_type} x 1: {roll}")
            continue
    # Ask the user if they want to try again
    play_again = input("Roll again? (y/n) ")
    if play_again == "n":
        break