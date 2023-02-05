#Week4 Discussion Board V2 MichaelConnell

import datetime
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white"]

def get_fortune():
    # Control structure to output a user's fortune randomly
    fortunes = ["You will have good luck and success in your future.",
                "You will have a happy and prosperous future.",
                "You will be surrounded by good friends and positive energy.",
                "You will find prosperity in your career and financial endeavors.",
                "You will have a great future ahead.",
                "You will be blessed with a loving family and good health.",
                "Beware of people who appear friendly, they might not be who they seem.",
                "Be careful of making hasty decisions, they might lead to regret.",
                "Expect challenges and obstacles in your near future."]
    return random.choice(fortunes)

def end_or_continue():
    # Control structure to end or continue the program based on user input
    user_input = input("Do you want to continue running the program? (yes/no)")
    if user_input.lower() == "yes":
        return True
    elif user_input.lower() == "no":
        return False
    else:
        print("Invalid input. Please enter either 'yes' or 'no'.")
        return end_or_continue()

def greet_user():
    # Control structure to greet the user based on the time of day
    current_time = datetime.datetime.now().time()
    if current_time >= datetime.time(6) and current_time < datetime.time(12):
        print("Good morning!")
    elif current_time >= datetime.time(12) and current_time < datetime.time(18):
        print("Good afternoon!")
    else:
        print("Good evening!")

# Main program
while True:
    greet_user()
    print("Valid colors are: ", colors)
    color = input("What is your favorite color? ")
    color = color.lower()
    if color in colors:
        print(get_fortune())
    else:
        print("Invalid color. Please enter a valid color.")

    if not end_or_continue():
        break

