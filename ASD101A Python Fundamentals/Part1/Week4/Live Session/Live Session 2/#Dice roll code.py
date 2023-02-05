#Dice roll code MichaelConnell

import random

while True:
    print(random.randint(1, 6))
    print(random.randint(1, 6))
    again = input("Roll the dice again? (y/n) ")
    if again.lower() != "y":
        break
