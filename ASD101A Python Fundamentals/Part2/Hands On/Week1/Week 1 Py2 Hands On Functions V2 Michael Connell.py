#Week 1 Py2 Hands On Functions Michael Connell

import datetime

def HappyBirthday():
    # Get User Input for Name and Date of Birth
    name = input("Enter your name: ")
    dob = input("Enter your date of birth in the format 'YYYY-MM-DD': ")

    # Get the year of birth and check if it is less than 1920
    year = int(dob.split("-")[0])
    if year < 1920:
        print("Error, need at least 1920 year value")
        dob = input("Enter a valid date of birth in the format 'YYYY-MM-DD': ")
        year = int(dob.split("-")[0])

    # Get the current year and calculate the age
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month
    current_day = datetime.datetime.now().day
    month = int(dob.split("-")[1])
    day = int(dob.split("-")[2])
    age = current_year - year
    if (month, day) > (current_month, current_day):
        age -= 1

    # Print the birthday message
    print("Happy {} Birthday {}!".format(age, name))
    
    try_again = input("Would you like to try again? (yes/no) ")
    if try_again.lower() == "yes":
        HappyBirthday()

HappyBirthday()