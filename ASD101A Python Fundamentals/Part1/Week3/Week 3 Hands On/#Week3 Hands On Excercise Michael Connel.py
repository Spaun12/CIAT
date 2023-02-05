#Week3 Hands On Excercise Michael Connell
#Write a program that asks the user for a number in the range of 1 through 7. 
# The pro-gram should display the corresponding day of the week, where 1 = Monday, 2 = Tuesday, 
# 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday. The program should 
# display an error message if the user enters a number that is outside the range of 1 through 7.

# I decided to combine boolean logic and lists to solve this problem along with 
# the if/else statement

# get the input from user
day = int(input("Enter a number in the range of 1 through 7: "))
# list of days 
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# check if the entered number is within the range of 1-7
if day < 1 or day > 7:
    # if not, print the error message
    print("Error: Enter a number in the range of 1 through 7")
else:
    # if yes, print the corresponding day
    print(days[day-1])
