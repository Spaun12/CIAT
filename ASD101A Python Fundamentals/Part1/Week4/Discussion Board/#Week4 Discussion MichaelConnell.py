#Week4 Discussion MichaelConnell

import datetime

def get_fortune(color):
    # Control structure to output a user's fortune based on their favorite color
    if color == "red":
        return "You will have good luck and success in your future."
    elif color == "orange":
        return "You will have a happy and prosperous future."
    elif color == "yellow":
        return "You will be surrounded by good friends and positive energy."
    elif color == "green":
        return "You will find prosperity in your career and financial endeavors."
    elif color == "blue":
        return "You will have good luck and success in your future."
    elif color == "purple":
        return "You will have a happy and prosperous future."
    else:
        return "Invalid color. Please enter a valid color."

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
greet_user()
color = input("What is your favorite color? ")
print(get_fortune(color))
if end_or_continue():
    # continue running the program
    pass
else:
    # end the program
    pass
