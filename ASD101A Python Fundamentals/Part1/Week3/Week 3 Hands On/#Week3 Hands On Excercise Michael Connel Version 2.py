#Week3 Hands On Excercise Michael Connell version 2
from termcolor import colored
#Does same thing but a bit more pretty
import pyfiglet
# get the input from user
day = int(input("Enter a number in the range of 1 through 7: "))
# list of days 
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# check if the entered number is within the range of 1-7
if day < 1 or day > 7:
    # if not, print the error message
    print(colored(pyfiglet.figlet_format("Error"), "red"))
else:
    # if yes, print the corresponding day
    print(colored(pyfiglet.figlet_format(days[day-1]), "green"))