# Week 2: Hands On Exercise - File and List Michael Connell

def print_states(states):
    # Print the states in descending order
    print("States in descending order:")
    for i, state in enumerate(reversed(states)):
        print("{:<23}".format(state), end="")
        if (i + 1) % 4 == 0:
            print()
    print("\n")
    # Print the states in ascending order
    print("States in ascending order:")
    for i, state in enumerate(states):
        print("{:<23}".format(state), end="")
        if (i + 1) % 4 == 0:
            print()

# Use a try-except block to handle file handling operations
try:
    # Open the file handle for reading "states.txt"
    with open("states.txt", "r") as file:
        # Read the state names from the file and store them in a list named states
        states = [line.strip() for line in file]
        # Call the function to print the states in both descending and ascending orders
        print_states(states)
except FileNotFoundError:
    # Print an error message if the file is not found
    print("File not found.")