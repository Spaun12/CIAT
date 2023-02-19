#Week 3 Assignment Part 1 Michael Connell
def reverse_string():
    while True:
        # Prompt the user to enter a string to reverse
        string = input("Welcome to reverse a string! Please enter a statement to see the results: ")
        # Use slicing to reverse the string
        reversed_string = string[::-1]
        # Display the reversed string
        print("Reversed string:", reversed_string)

        # Ask if the user wants to try again
        again = input("Would you like to try again? (y/n) ")
        # If the user does not want to try again, exit the function and display a message
        if again.lower() != "y":
            print("Thank you for playing the reverse string game!")
            break
reverse_string()  # Call the function to start the game