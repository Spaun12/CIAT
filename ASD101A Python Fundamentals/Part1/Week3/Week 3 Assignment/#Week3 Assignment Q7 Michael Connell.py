#Week3 Assignment Q7 Michael Connell

#First we import the modules we need for pizzazz
from termcolor import colored
import pyfiglet

#Then we ask the user for the number of points
points = int(input("Enter the number of points: "))

#Then we check if the number is in the range of 9-52
if points not in range(9,52):
    #If it is not in the range we print the error message
    print(colored(pyfiglet.figlet_format("Invalid points"), "red"))
    #If it is in the range we print the valid message
else:
    print(colored(pyfiglet.figlet_format("Valid points"), "green"))
