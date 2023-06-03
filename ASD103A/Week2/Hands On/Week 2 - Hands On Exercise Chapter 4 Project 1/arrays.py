"""
File: arrays.py
Project 4.1

Michael D. Connell Jr.
06/03/2023


Adds a logical size attribute and a size method.


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
        self.logicalSize = 0  # Instance variable tracking logical size of the array
        for count in range(capacity):
            self.items.append(fillValue)

    def size(self):
        """-> The logical size of the array."""
        return self.logicalSize

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
        """Subscript operator for access at index."""
        return self.items[index]

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index.
        Increase logical size if a None value is being replaced."""
        if self.items[index] is None and newItem is not None:
            self.logicalSize += 1  # Increase logical size when a new item is added
        self.items[index] = newItem


def main():
    """Test code for modified Array class."""
    a = Array(10)
    print("Physical size:", len(a))
    print("Logical size:", a.size())
    print("Items:", a)

if __name__ == "__main__":
    main()

