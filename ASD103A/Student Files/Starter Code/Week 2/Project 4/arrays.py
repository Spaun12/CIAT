"""
File: arrays.py
Project 4.4

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
	
	# Reuse your solution from Programming Exercise 4.3 as your starter file

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

def main():
    """Test code for modified Array class."""
    a = Array(5)
    print ("Physical size:", len(a))
    print ("Logical size:", a.size())
    print ("Items:", a)
    for item in range(4):
        a.insert(0, item)
    print ("Items:", a)
    a.insert(1, 77)
    print ("Items:", a)
    a.insert(10, 10)
    print ("Items:", a)
    print(a.pop(3))
    print ("Items:", a)
    for count in range(5):
        print(a.pop(0), end = " ")
    print ()

if __name__ == "__main__":
    main()
