"""
File: arrays.py
Project 4.2

Michael Connell
2023-06-03
 
Adds a precondition on __getitem__ and __setitem__
and raises an exception if it is not satisfied.

An Array is a restricted list whose clients can use
only [], len, iter, and str.

To instantiate, use

<variable> = array(<capacity>, <optional fill value>)

The fill value is None by default.
"""

class Array(object):
    """Represents an array."""

    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        self.items = list()
        self.logicalSize = 0
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

    def __getitem__(self, index):
        """Subscript operator for access at index.
        Precondition: 0 <= index < size()"""
        # Check precondition: 0 <= index < size()
        if not(0 <= index < self.size()):
            raise IndexError("Array index out of range")
        return self.items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index.
        Precondition: 0 <= index < capacity"""
        # Check if index is within range of capacity
        if not(0 <= index < len(self.items)):  
            raise IndexError("Array index out of range")
        # If adding a new item
        if self.items[index] is None and newItem is not None:  
            self.logicalSize += 1
        # If removing an item
        elif self.items[index] is not None and newItem is None:  
            self.logicalSize -= 1
        # Set the new item at the given index
        self.items[index] = newItem

    def size(self):
        """-> The number of items in the array."""
        return self.logicalSize


def main():
    """Test code for modified Array class."""

    # Ask the user for the capacity of the array and convert it to an integer
    capacity = int(input("Enter capacity of the array: "))

    # Initialize an array with the given capacity
    a = Array(capacity)

    # Loop through each index in the array
    for i in range(capacity):
        # Ask the user for an item to add at the current index
        item = input(f"Enter item for index {i}: ")

        # Add the item at the current index in the array
        a[i] = item

    # After all items are added, print the physical size of the array
    print("Physical size:", len(a))

    # Print the logical size of the array
    print("Logical size:", a.size())

    # Print all items in the array
    print("Items:", a)

    # Ask the user for an index to retrieve an item from
    index_to_retrieve = int(input("Enter index of item to retrieve: "))

    # Check if the index is within the valid range
    if 0 <= index_to_retrieve < a.size():
        # If it is, retrieve and print the item at that index
        print("Retrieved item:", a[index_to_retrieve])
    else:
        # If it is not, print an error message
        print("Invalid index")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
