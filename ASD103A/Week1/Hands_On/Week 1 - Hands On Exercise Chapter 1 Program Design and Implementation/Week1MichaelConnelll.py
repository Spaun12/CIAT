"""
Author: Michael D. Connell Jr.
Date: 2023-05-22
"""

import statistics

def mean(lst):
    """
    Calculates the mean (average) of a list of numbers.
    It uses the mean function from the statistics library.
    
    :param lst: List of numbers
    :return: Mean of the numbers
    """
    return statistics.mean(lst)

def median(lst):
    """
    Calculates the median (middle value) of a list of numbers.
    If the list is even, it returns the average of the two middle numbers.
    It uses the median function from the statistics library.
    
    :param lst: List of numbers
    :return: Median of the numbers
    """
    return statistics.median(lst)

def mode(lst):
    """
    Calculates the mode (most frequent value) of a list of numbers.
    If there are multiple modes, it will return the first one it encounters.
    It uses the mode function from the statistics library.
    
    :param lst: List of numbers
    :return: Mode of the numbers
    """
    try:
        return statistics.mode(lst)
    except statistics.StatisticsError:
        return "No unique mode found"

def run_program():
    """
    Runs the main program. It asks the user to input a list of numbers,
    calculates the mean, median and mode of the numbers, and then asks the user if they
    want to continue.
    """
    while True:
        numbers = input("Please enter a list of numbers, separated by spaces: ")

        # Attempt to parse the input into a list of integers
        try:
            numbers = list(map(int, numbers.split()))
        except ValueError:
            print("Invalid input. Please enter only numbers separated by spaces.")
            continue

        # Calculate and print the mean, median and mode
        print(f"Mean: {mean(numbers)}")
        print(f"Median: {median(numbers)}")
        print(f"Mode: {mode(numbers)}")

        # Ask the user if they want to continue
        cont = input("Do you want to try again? (yes/no): ")
        if cont.lower() != "yes":
            break

run_program()