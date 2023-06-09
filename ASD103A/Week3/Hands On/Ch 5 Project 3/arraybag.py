"""
Project 5.3
File: arraybag.py
Author: Ken Lambert (Student Use and Edits by Michael Connell 2023-06-09)
"""

"""Pseudocode for Chapter 5 Project 3:
First: START add METHOD
Second: RECEIVE the item to add
Third: CHECK if the bag (array) is full, i.e. if the size of the bag equals the length of the array
Forth: IF the bag is full:
A) CREATE a new array with double the capacity of the current one
B) COPY all items from the current array to the new array
C) SET the new array as the bag's array
D) ADD the new item to the end of the array
E) INCREMENT the bag's size by 1
Fifth: END add METHOD"""

"""Pseudocode for Chapter 5 Project 4:
First: If the item to be removed is in the bag:
A: Find the item in the array
B: Replace the item with the last item in the array
C: Decrease the size by 1
D: If the size is less than or equal to a quarter of the capacity of the array:
1: Create a new array with half the capacity of the current array (but not less than the default capacity)
2: Copy the elements from the old array to the new array
3: Set the new array as the current array
Second: Else, raise an error indicating the item is not in the bag"""



from arrays import Array

class ArrayBag(object):
    """An array-based bag implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection=None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)
        self.size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0

    def __len__(self):
        """Returns the number of items in self."""
        return self.size

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while cursor < len(self):
            yield self.items[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new bag containing the contents of self and other."""
        result = ArrayBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other, or False otherwise."""
        if self is other: 
            return True
        if type(self) != type(other) or len(self) != len(other):
            return False
        for item in self:
            if self.count(item) != other.count(item):
                return False
        return True

    def count(self, item):
        """Returns the number of instances of item in self."""
        total = 0
        for nextItem in self:
            if nextItem == item:
                total += 1
        return total

    def clear(self):
        """Makes self become empty."""
        self.size = 0
        self.items = Array(ArrayBag.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        # Check if the array is full
        if len(self) == len(self.items):
            # If so, create a new array with double the capacity
            temp = Array(len(self.items) * 2)
            # Copy the items to the new array
            for i in range(len(self)):
                temp[i] = self.items[i]
            # Set the new array as the current array
            self.items = temp
        # Add the new item
        self.items[len(self)] = item
        # Increase the size by 1
        self.size += 1

    def remove(self, item):
        """Removes item from self and resize if necessary."""
        # Check if the item is in the bag
        if item in self.items:
            # Find the item and replace it with the last item
            for i in range(len(self)):
                if self.items[i] == item:
                    self.items[i] = self.items[len(self)-1]
                    break
            # Decrease the size by 1
            self.size -= 1
            # Check if the size is less than or equal to a quarter of the capacity
            if self.size <= len(self.items) // 4:
                # Create a new array with half the capacity (but not less than default)
                new_capacity = max(ArrayBag.DEFAULT_CAPACITY, len(self.items) // 2)
                temp = Array(new_capacity)
                # Copy the items to the new array
                for i in range(self.size):
                    temp[i] = self.items[i]
                # Set the new array as the current array
                self.items = temp
        else:
            # If the item is not in the bag, raise an error
            raise KeyError("Item not in bag")