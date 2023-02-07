#Week 1 Py2 Hands On Function V1 Michael Connell

import datetime

def HappyBirthday():
    # Get User Input Year and name
    year = int(input("Enter the year of birth: "))
    
    # Get the current year
    current_year = datetime.datetime.now().year
    
    # Check if year is less than 1920
    if year < 1920:
        print("Error, need at least 1920 year value")
        HappyBirthday()
    else:
        # Get User Input for Name
        name = input("Enter the name: ")
        # Calculate the age
        age = current_year - year
        # Print the birthday message
        print("Happy {} Birthday {}!".format(age, name))
        
    try_again = input("Would you like to try again? (yes/no) ")
    if try_again.lower() == "yes":
        HappyBirthday()

HappyBirthday()
