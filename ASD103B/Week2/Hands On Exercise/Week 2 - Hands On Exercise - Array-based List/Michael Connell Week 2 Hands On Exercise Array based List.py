#Styudent: Michael Connell
# Date: 2023-07-07

class Array:
    # Initialization method with default size of 10
    def __init__(self, size=10):
        self.array = [None] * size  # Initialize array with None
        self.size = size  # Store the size of the array
        self.count = 0  # Counter for the number of elements in the array

    # Method to add an element to the array and increase count
    def add_element(self, element):
        # If the array is full, we double its size
        if self.count == self.size:
            print("This array is too small! Need to double the size... Because why not? :D")
            new_array = [None] * self.size * 2  # Create new array with doubled size
            # Copy elements from the old array to the new one
            for i in range(self.count):
                new_array[i] = self.array[i]
            self.array = new_array  # Make new array the array of the class
            self.size *= 2  # Update the size of the array
        # Add new element and increase count
        self.array[self.count] = element
        self.count += 1

    # Method to get an element at a specific index from the array and return it
    def get_element(self, index):
        # Check if index is within the range of existing elements
        if index >= self.count or index < 0:
            raise IndexError("Sorry, but it seems like you're trying to access a parallel universe. Index out of range!")
        return self.array[index]

    # Method to remove an element at a specific index from the array and shift remaining elements to the left
    def remove_element(self, index):
        # Check if index is within the range of existing elements
        if index >= self.count or index < 0:
            raise IndexError("Sorry, but it seems like you're trying to remove something from a parallel universe. Index out of range!")
        # Shift elements to the left from the index to remove
        for i in range(index, self.count - 1):
            self.array[i] = self.array[i + 1]
        self.count -= 1  # Decrease count of elements

    # Method to print the elements in the array in a creative way
    def print_array(self):
        print("Here is your array! Isn't it gorgeous?")
        for i in range(self.count):
            print(self.array[i], end=' ')
        print()

# Create an instance of the Array class 
arr = Array()

# Infinite loop for user interaction which can be exited by the user
while True:
    # Prompt the user for their choice of operation
    print("\nWhat would you like to do? You can 'add' an element, 'get' an element, 'remove' an element, 'print' array, or 'quit'")
    # Convert input to lower case to ensure case-insensitive comparison
    choice = input("Enter your choice: ").lower()

    # Perform the operation according to the user's choice 
    if choice == 'add':
        try:
            # Ask for integer input and try to convert it
            element = int(input("Enter the integer element you would like to add: "))
            arr.add_element(element)
        except ValueError:  # Handle case where input is not an integer
            print("Oops! That was no valid number. Try again...")
    elif choice == 'get':
        try:
            # Ask for integer input for index and try to convert it
            index = int(input("Enter the index of the element you would like to get: "))
            print(arr.get_element(index))
        except ValueError:  # Handle case where input is not an integer
            print("Oops! That was no valid number. Try again...")
        except IndexError as e:  # Handle case where index is out of range
            print(e)
    elif choice == 'remove':
        try:
            # Ask for integer input for index and try to convert it
            index = int(input("Enter the index of the element you would like to remove: "))
            arr.remove_element(index)
        except ValueError:  # Handle case where input is not an integer
            print("Oops! That was no valid number. Try again...")
        except IndexError as e:  # Handle case where index is out of range
            print(e)
    elif choice == 'print':
        arr.print_array()
    elif choice == 'quit':
        print("Array-O, Array-O, wherefore art thou Array-O? Thanks for playing!")
        break
    else:
        print("I didn't quite catch that. Can you please try again?")