#Python2 Week 1 Assignment1 Part 2 Michael Connell
#Write your own function, named Quizzer

import random

def Quizzer():
    # Generate 2 random integers between 1-10 (inclusive)
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    
    # Calculate the product of the two numbers
    product = num1 * num2
    
    # Print the math problem to the screen
    print(f"{num1} * {num2} = ?")
    
    # Ask the user what the product is
    answer = int(input("What is the product of the two numbers?: "))
    
    # Return True if the answer is correct, False otherwise
    if answer == product:
        return True
    else:
        return False

# Main program to call the Quizzer function
if __name__ == '__main__':
    success = Quizzer()
    if success:
        print("Good job!")
    else:
        print("Better luck next time.")
