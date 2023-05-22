"""
File: arrays.py
Project 4.5

Adds the __eq__ method.

An Array is a restricted list whose clients can use
only [], len, iter, and str.

To instantiate, use

<variable> = array(<capacity>, <optional fill value>)

The fill value is None by default.

Reuse your solution from Programming Exercise 4.4 as your starter file
"""

class Array(object):
    """Represents an array."""
	
	# Reuse your solution from Programming Exercise 4.4 as your starter file

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
    for item in range(4):
        a.insert(0, item)
    b = a
    c = Array(5)
    for item in range(4):
        c.insert(0, item)
    print("True:", a == b)
    print("True:", a is b)
    print("True:", a == c)
    print("False:", a is c)
    c.insert(10, 10)
    print("False:", a == c)
    c.pop(c.size() - 1)
    c[2] = 6
    print("False:", a == c)
    d = []
    print("False:", a == d)

if __name__ == "__main__":
    main()
