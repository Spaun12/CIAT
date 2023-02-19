#Week3 Assignment Part2 Michael Connell

# Define a dictionary with the key-value pairs
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Loop until the user decides to stop
while True:
    # Ask the user for a key
    key = input("Enter a key ('a', 'b', or 'c'): ")    
    # Check if the key exists in the dictionary
    if key in my_dict:
        # If the key exists, print its value
        print(f"The value of {key} is {my_dict[key]}")
    else:
        # If the key doesn't exist, inform the user
        print(f"{key} is not a valid key.")
    
    # Ask the user if they want to try again
    while True:
        try_again = input("Do you want to try again? (yes/no) ")
        if try_again.lower() in ["yes", "y"]:
            break
        elif try_again.lower() in ["no", "n"]:
            # If the user doesn't want to try again, break out of the loop
            exit()
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")