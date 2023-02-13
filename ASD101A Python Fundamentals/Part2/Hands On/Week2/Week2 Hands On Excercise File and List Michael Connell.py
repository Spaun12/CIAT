# Week 2: Hands On Exercise - File and List Michael Connell

# Define a function to print the states in both descending and ascending order
def print_states(states):
    # Print header for the states in descending order
    print("States in descending order:")
    # Loop through the list of states in reverse order and print each state
    for state in reversed(states):
        print(state)
    # Print header for the states in ascending order
    print("States in ascending order:")
    # Loop through the list of states in normal order and print each state
    for state in states:
        print(state)

# Use a try/except block to handle any errors when opening the file
try:
    # Open the file "states.txt" for reading
    with open("states.txt", "r") as file:
        # Read the contents of the file and create a list of state names
        states = [line.strip().split(".")[1].strip() for line in file]
        # Call the function to print the states
        print_states(states)
# If the file is not found, print an error message
except FileNotFoundError:
    print("File not found.")
