#DnD Dice Roller Applican Idea
import random
dice_dict = {
    "d4": 4,
    "d6": 6,
    "d8": 8,
    "d10": 10,
    "d12": 12,
    "d20": 20
}
while True:
    roll_all = input("Would you like to roll all of your dice at once? (y/n) ")
    if roll_all == "y":
        rolls = {}
        for dice_type, sides in dice_dict.items():
            roll = random.randint(1, sides)
            rolls[dice_type] = roll
        print("Rolls:")
        for dice_type, roll in rolls.items():
            print(f"{dice_type} x 1: {roll}")
    else:
        while True:
            try:
                dice = int(input("How many dice? "))
                if dice <= 0:
                    print("You must roll at least one die.")
                    continue
                dice_types = []
                for i in range(dice):
                    while True:
                        dice_type = input(f"Enter the type of dice {i+1}: ")
                        if dice_type not in dice_dict:
                            print("Invalid dice type. Please enter a valid type (e.g. d6).")
                        else:
                            break
                    dice_types.append(dice_type)
                rolls = {}
                for dice_type in dice_types:
                    sides = dice_dict[dice_type]
                    roll = random.randint(1, sides)
                    rolls[dice_type] = roll
                print("Rolls:")
                for dice_type, roll in rolls.items():
                    print(f"{dice_type} x 1: {roll}")
                break
            except ValueError:
                print("Please enter a valid integer.")
    while True:
        play_again = input("Roll again? (y/n) ")
        if play_again == "y":
            break
        elif play_again == "n":
            exit()
        else:
            print("Invalid input. Please enter 'y' or 'n'.")