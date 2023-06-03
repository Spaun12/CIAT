"""
File: arrays.py
Project 4.4
Michael Connell
2023-06-03

Adds methods insert and remove to insert or remove an item
at a given position in the array.

An Array is a restricted list whose clients can use
only [], len, iter, and str.

To instantiate, use

<variable> = array(<capacity>, <optional fill value>)

The fill value is None by default.

Reuse your solution from Programming Exercise 4.3 as your starter file
"""

class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self.items = [fillValue]*capacity
        self.capacity = capacity
        self.fillValue = fillValue

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

    def insert(self, index, value):
        """Inserts an item at the given index, replacing the None value if available."""
        if index >= self.capacity:
            print("Index out of range. Item is not inserted.")
        elif self.items[index] == None:
            self.items[index] = value
            print("Item inserted.")
        else:
            print("Item already exists at this index. Please choose another index.")

    def pop(self, index):
        """Removes and returns the item at the given index, adjusting the length of the array if necessary."""
        if 0 <= index < self.capacity and self.items[index] != None:
            value = self.items[index]
            self.items[index] = self.fillValue
            return value
        else:
            print("Cannot pop from this index.")

def main():
    """Test code for modified Array class."""
    #Ask the user for the capacity of the array and convert it to an integer
    capacity = int(input("Enter initial capacity of the array: "))

    #Initialize an array with the given capacity
    a = Array(capacity)

    while True:
        print("\nOptions:")
        print("1 - Insert item")
        print("2 - Pop item")
        print("3 - Display array")
        print("4 - Exit")

        #Ask the user for an option
        option = int(input("Enter an option: "))

        if option == 1:
            index = int(input("Enter the index to insert at: "))
            value = int(input("Enter the value to insert: "))
            a.insert(index, value)
        elif option == 2:
            index = int(input("Enter the index to pop from: "))
            value = a.pop(index)
            if value != None:
                print("Popped item:", value)
        elif option == 3:
            #Display the array
            print("Physical size:", len(a))
            print("Logical size:", a.size())
            print("Items:", a)
        elif option == 4:
            #Exit the program
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()