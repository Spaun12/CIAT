#Lottery Number Generator

import random

def pick_lottery_numbers():
    # Set the number of picks and the range of numbers
    num_picks = 6
    num_range = 69
    power_ball_range = 26

    # Generate a list of random numbers
    numbers = random.sample(range(1, num_range+1), num_picks)

    # Generate a random powerball number
    powerball = random.randint(1, power_ball_range)

    # Sort the numbers in ascending order
    numbers.sort()

    # Return the numbers
    return numbers, powerball

numbers, powerball = pick_lottery_numbers()

print("Your lottery numbers are:", numbers)
print("Your Powerball number is:", powerball)

