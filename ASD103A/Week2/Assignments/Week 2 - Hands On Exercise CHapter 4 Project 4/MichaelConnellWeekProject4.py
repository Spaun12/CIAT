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

class Array:
    def __init__(self, capacity, fillValue=None):
        """
        Initialize an Array with given capacity. All positions are initially filled with fillValue.
        logicalSize is initialized to 0, since the Array initially contains no actual elements.
        """
        self._items = [fillValue for _ in range(capacity)]
        self._logicalSize = 0

    def __len__(self):
        """
        Return the physical size of the Array, which is the total number of positions it has, filled or not.
        """
        return len(self._items)

    def __str__(self):
        """
        Return a string representation of the Array.
        """
        return str(self._items)

    def __iter__(self):
        """
        Return an iterator that can be used to traverse the elements of the Array.
        """
        return iter(self._items)

    def size(self):
        """
        Return the logical size of the Array, which is the number of filled positions.
        """
        return self._logicalSize

    def insert(self, index, newItem):
        """
        Insert a new item at a given position in the Array.
        If the Array is not full, the item is inserted at the given index and all items to its right are shifted one position to the right.
        If the Array is full, an error message is displayed.
        """
        if index >= 0 and index < len(self) and self._logicalSize < len(self):
            for i in range(self._logicalSize, index, -1):
                self._items[i] = self._items[i-1]
            self._items[index] = newItem
            self._logicalSize += 1
        else:
            raise IndexError("Array subscript out of range")

    def pop(self, index):
        """
        Remove an item at a given position in the Array.
        The item at the given index is removed and all items to its right are shifted one position to the left.
        The last position in the Array is filled with None.
        """
        if index >= 0 and index < self._logicalSize:
            item = self._items[index]
            for i in range(index, self._logicalSize - 1):
                self._items[i] = self._items[i+1]
            self._items[self._logicalSize - 1] = None
            self._logicalSize -= 1
            return item
        else:
            raise IndexError("Array subscript out of range")

def main():
    capacity = int(input("Enter initial capacity of the array: "))
    a = Array(capacity)

    while True:
        print("\nOptions:")
        print("1 - Insert item")
        print("2 - Pop item")
        print("3 - Display array")
        print("4 - Exit")

        option = int(input("Enter an option: "))

        try:
            if option == 1:
                index = int(input("Enter the index to insert at: "))
                value = int(input("Enter the value to insert: "))
                a.insert(index, value)
                print("Item inserted.")
            elif option == 2:
                index = int(input("Enter the index to pop from: "))
                value = a.pop(index)
                print("Popped item:", value)
            elif option == 3:
                print("Physical size:", len(a))
                print("Logical size:", a.size())
                print("Items:", a)
            elif option == 4:
                break
            else:
                print("Invalid option, please try again.")
        except IndexError as e:
            print(e)
            continue_prompt = input("Would you like to try another option? (Y/N): ")
            if continue_prompt.lower() != 'y':
                break

if __name__ == "__main__":
    main()
