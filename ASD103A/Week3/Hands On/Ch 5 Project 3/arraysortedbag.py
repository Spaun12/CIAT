"""
Project 5.3
File: arraysortedbag.py
Author: Ken Lambert
"""

from arrays import Array

class ArraySortedBag(object):
    """An array-based sorted bag implementation."""

    # Class variable
    DEFAULT_CAPACITY = 10

    # Constructor
    def __init__(self, sourceCollection = None):
        """Sets the initial state of self, which includes the
        contents of sourceCollection, if it's present."""
        self._items = Array(ArraySortedBag.DEFAULT_CAPACITY)
        self._size = 0
        if sourceCollection:
            for item in sourceCollection:
                self.add(item)

    # Accessor methods
    def isEmpty(self):
        """Returns True if len(self) == 0, or False otherwise."""
        return len(self) == 0
    
    def __len__(self):
        """Returns the number of items in self."""
        return self._size

    def __str__(self):
        """Returns the string representation of self."""
        return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        """Supports iteration over a view of self."""
        cursor = 0
        while True:
            if cursor == len(self):
                raise StopIteration
            yield self._items[cursor]
            cursor += 1

    def __add__(self, other):
        """Returns a new bag containing the contents
        of self and other."""
        result = ArraySortedBag(self)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        """Returns True if self equals other,
        or False otherwise."""
        if self is other: return True
        if type(self) != type(other) or \
           len(self) != len(other):
            return False
        for item in self:
            if not item in other:
                return False
        return True

    def __contains__(self, item):
        """Returns True if item is in self, or False otherwise."""
        left = 0
        right = len(self) - 1
        while left <= right:
            midPoint = (left + right) // 2
            if self._items[midPoint] == item:
                return True
            elif self._items[midPoint] > item:
                right = midPoint - 1
            else:
                left = midPoint + 1
        return False

    # Mutator methods
    def clear(self):
        """Makes self become empty."""
        self._size = 0
        self._items = Array(ArraySortedBag.DEFAULT_CAPACITY)

    def add(self, item):
        """Adds item to self."""
        # Empty or last item, call ArrayBag.add
        if self.isEmpty() or item >= self._items[len(self) - 1]:
            self._items[len(self)] = item
            self._size += 1
        else:
            # Check array memory here and increase it if necessary
            if len(self) == len(self._items):
                temp = Array(2 * len(self))
                for i in range(len(self)):
                    temp[i] = self[i]
                self._items = temp
            # Search for first item >= new item
            targetIndex = 0
            while item > self._items[targetIndex]:
                targetIndex += 1
            # Open a hole for new item
            for i in range(len(self), targetIndex, -1):
                self._items[i] = self._items[i - 1]
            # Insert item and update size
            self._items[targetIndex] = item
            self._size += 1

    def remove(self, item):
        """Precondition: item is in self.
        Raises: KeyError if item in not in self.
        Postcondition: item is removed from self."""
        # Check precondition and raise if necessary
        if not item in self:
            raise KeyError(str(item) + " not in bag")
        # Search for the index of the target item
        targetIndex = 0
        for targetItem in self:
            if targetItem == item:
                break
            targetIndex += 1
        # Shift items to the left of target up by one position
        for i in range(targetIndex, len(self) - 1):
            self._items[i] = self._items[i + 1]
        # Decrement logical size
        self._size -= 1
        # Check array memory here and decrease it if necessary
        if len(self) < len(self._items) // 3 and \
           2 * len(self) >= ArraySortedBag.DEFAULT_CAPACITY:
            temp = Array(len(self._items) // 2)
            for i in range(len(self)):
                temp[i] = self[i]
            self._items = temp
        
        
