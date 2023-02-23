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
# Prompt the user to roll all of their dice at once, or individually
roll_all = input("Would you like to roll all of your dice at once? (y/n) ")
if roll_all == "y":
    # If the user selects "y", roll all the dice
    rolls = []
    for dice_type, sides in dice_dict.items():
        roll = random.randint(1, sides)
        rolls.append(roll)
    # Print the resulting rolls to the user
    print(f"Rolls: {rolls}")
else:
    # If the user selects "n", prompt for the number and type of dice, and generate rolls for each die individually using a for loop
    dice = int(input("How many dice? "))
    if dice <= 0:
        print("You must roll at least one die.")
        quit()
    dice_type = input("Enter the type of dice you want to roll (e.g. d6): ")
    try:
        sides = dice_dict[dice_type]
    except KeyError:
        print("Invalid dice type. Please enter a valid type (e.g. d6).")
        quit()
    rolls = []
    for i in range(dice):
        face = random.randint(1, sides)
        rolls.append(face)
    # Print the resulting rolls to the user
    print(f"Rolls: {rolls}")
