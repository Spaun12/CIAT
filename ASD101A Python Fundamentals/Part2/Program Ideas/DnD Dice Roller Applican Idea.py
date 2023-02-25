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
    while True:
        roll_all = input("Welcome to the Ultimate DnD dice roller! Would you like to roll all of your dice at once? (y/n) ")
        if roll_all.lower() == "y":
            # If the user selects "y", roll all the dice
            rolls = {}
            for dice_type, sides in dice_dict.items():
                roll = random.randint(1, sides)
                rolls[dice_type] = roll
            # Print the resulting rolls to the user
            print("Rolls:")
            for dice_type, roll in rolls.items():
                print(f"{dice_type} x 1: {roll}")
            break
        elif roll_all.lower() == "n":
            # If the user selects "n", prompt for the number and type of dice,
            # and generate rolls for each die individually using a for loop
            dice = int(input("How many dice? "))
            if dice <= 0:
                print("You must roll at least one die.")
                continue
            dice_types = []
            for i in range(dice):
                while True:
                    dice_type = input(f"Enter the type of dice *dice type: d4, d6, d8, d10, d12, d20 {i+1}: ")
                    if dice_type in dice_dict:
                        dice_types.append(dice_type)
                        break
                    print("Invalid dice type. Please enter a valid type (e.g. d6).")
            rolls = {}
            for dice_type in dice_types:
                sides = dice_dict[dice_type]
                roll = random.randint(1, sides)
                rolls[dice_type] = roll
            # Print the resulting rolls to the user
            print("Rolls:")
            for dice_type, roll in rolls.items():
                print(f"{dice_type} x 1: {roll}")
            break
        else:
            print("Invalid input. Please enter 'y' or 'n'.")
    # Ask the user if they want to try again
    while True:
        play_again = input("Roll again? (y/n) ")
        if play_again.lower() == "y":
            break
        elif play_again.lower() == "n":
            quit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")