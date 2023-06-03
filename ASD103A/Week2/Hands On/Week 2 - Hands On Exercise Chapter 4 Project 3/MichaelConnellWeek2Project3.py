"""
File: arrays.py
Project 4.3

Michael Connell
2023-06-03

Adds methods grow and shrink to increase or decrease the capacity
of the array if necessary.

An Array is a restricted list whose clients can use
only [], len, iter, and str.

To instantiate, use

<variable> = array(<capacity>, <optional fill value>)

The fill value is None by default.

Reuse your solution from Programming Exercise 4.2 as your starter file
"""

class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self.items = list()
        self.logicalSize = 0
        # Track the capacity and fill value for adjustments later
        self.capacity = capacity
        self.fillValue = fillValue
        for count in range(capacity):
            self.items.append(fillValue)

    def __len__(self):
        """-> The capacity of the array."""
        return len(self.items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self.items)

    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self.items)

    def size(self):
        """-> The logical size of the array."""
        return self.logicalSize

    def grow(self):
        """Increases the physical size of the array by 1, filling the new cell with the fill value."""
        # Append the fill value to the end of the list, effectively growing the array
        self.items.append(self.fillValue)
        # Increase the logical size of the array by 1
        self.logicalSize += 1

    def shrink(self):
        """Decreases the size of the array by 1."""
        # Check if the new size would be less than the initial capacity
        if len(self.items) - 1 < self.capacity:
            print("Cannot shrink below initial capacity.")
        else:
            self.items.pop()
            self.logicalSize -= 1

def main():
    """Test code for modified Array class."""
    # Ask the user for the capacity of the array and convert it to an integer
    capacity = int(input("Enter initial capacity of the array: "))

    # Initialize an array with the given capacity
    a = Array(capacity)

    while True:
        print("\\nOptions:")
        print("1 - Grow")
        print("2 - Shrink")
        print("3 - Display array")
        print("4 - Exit")

        # Ask the user for an option
        option = int(input("Enter an option: "))

        if option == 1:
            a.grow()
            print("Array grown.")
        elif option == 2:
            a.shrink()
            print("Array shrunk.")
        elif option == 3:
            # Display the array
            print("Physical size:", len(a))
            print("Logical size:", a.size())
            print("Items:", a)
        elif option == 4:
            # Exit the program
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
