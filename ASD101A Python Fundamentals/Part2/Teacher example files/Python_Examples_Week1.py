# Example of a function
def Area(x=2, y=3):
    areaTri = 0.5*x*y
    return areaTri

PI = 3.1415

def AreaCirc(r):
    area_circ = PI*r*r
    return area_circ

# Example of a function call
areaC = AreaCirc(4)
print(areaC)

# ------------------------------------------------------------------
import random

number = random.randint(1,100)
print(number)

def Guess_Number(num):
    testNum = int(input("Please try and guess the number: "))
    print("psst ... the number is", num)
    if testNum == number:
        print("You got it. Winner winner chicken dinner")
    else:
        print("Sorry, no dice")


Guess_Number(number)

# -------------------------------------------------------------------
import math

def Areas(x):
    areaSquare =  x*x
    areaCirc = math.pi*x*x
    sqrtValue = math.sqrt(x)
    return areaSquare, areaCirc, sqrtValue

x,y,z = Areas(9)
print(x)
print(y)
print(z)

# ----------------- Example of Import Statements ----------------------
import math
from math import pi
from math import *

# ---------------------------------------------------------------------
# This function converts temperature in celsius to fahrenheit
def cel2fahr(cel):
    fahr = cel*9/5 + 32
    return fahr

def fahr2cel(fahr):
    cel = (fahr-32)*5/9
    return cel

# Example of a function calling another set of functions
def fahr2cel2fahr(fahr):
    celsius = fahr2cel(fahr)
    fahrenheit = cel2fahr(celsius)
    print("The original value in fahrenhiet is", fahrenheit, "degrees")
    return fahrenheit
    
degrees = fahr2cel2fahr(82)
print(degrees)

#fahrenheit = cel2fahr(32)
#print('The value of the temperature in fahrenheit is', fahrenheit, "degrees.")    
        
#celsius = fahr2cel(95)
#print('The value of the temperature in celsius is', celsius, "degrees.")  

# -----------------------------------------------------------------------------
# Create a function that asks a user to enter the value of three sides and output
# whether the result is an equilateral triangle:

def Equalateral():
    side1 = int(input("Please enter the first side of your triangle: "))
    side2 = int(input("Please enter the second side of your triangle: "))
    side3 = int(input("Please enter the third side of your triangle: "))
    if side1 == side2 & side1 == side3:
        print("This is an equalateral triangle")
    else:
        print("This is not an equalateral triangle")

Equalateral()

# -------------------------------------------------------------------------------
# Create a function that creates a random number from 1 to 100 and asks the user
# how many attempts he/she would like to guess the number.
# if the number guesses is greater than the random number, the program will let
# the user know that their number was too high, otherwise it will inform then it
# is too low.
# The game ends when the number of attempts is reached or the user guesses the
# correct number.
import random

def Guessing_Game():
    maxNum = 100
    randNum = random.randint(1, maxNum + 1)

    print("Welcome to the guessing game.\n Please select a number from 1 to 100.")
    guesses = int(input("How many tries would like to attempts? "))
    
    counter = 0

    while counter < guesses:
        userGuess = int(input("Please enter your number: "))
        if userGuess == randNum:
            print("Congrats! You've won!")
            break
        elif userGuess > randNum:
            print("Your number is too high, please try again.")
        elif userGuess < randNum:
            print("Your number is too low, please try again.")
        else:
            print("You did not enter a number, please try again.")

        counter = counter + 1
        if counter == guesses:
            print("Sorry, your ran out of attempts")

Guessing_Game()