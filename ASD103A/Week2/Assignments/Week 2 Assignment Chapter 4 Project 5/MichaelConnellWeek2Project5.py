"""
File: arrays.py
Project 4.5

Adds the __eq__ method. (and further modified the program to allow the user to
compare two arrays. The user can choose to compare the entire arrays or
specific items in the arrays. The program should also allow the user to
create either one or two arrays.)

An Array is a restricted list whose clients can use
only [], len, iter, and str.

To instantiate, use

<variable> = array(<capacity>, <optional fill value>)

The fill value is None by default.

Reuse your solution from Programming Exercise 4.4 as your starter file
"""

#I ended up using the solutions from earlier and experimenting with them. So it has been changed quite a bit.
#I was able to get the program to work, and believe it meets the requirment.
#My goal was to make it more enteractive while still checking the boxes.

class Array:
    # Initializing Array class
    def __init__(self, capacity, fillValue=None):
        # The array starts with a given capacity, all items are None initially
        self._items = list([fillValue]*capacity)
        self._original_capacity = capacity  # Store the original capacity to use when resizing
        self._logicalSize = 0  # Tracks how many items are actually in the array

    # This function allows calling len(Array) to get its physical size (capacity)
    def __len__(self):
        return len(self._items)

    # This function allows converting the Array to a string for display
    def __str__(self):
        return str(self._items[:self._logicalSize])

    # This function allows iterating over the Array with a for loop
    def __iter__(self):
        return iter(self._items[:self._logicalSize])

    # This function returns the logical size of the array (how many items it actually holds)
    def size(self):
        return self._logicalSize

    # This function inserts an item at the given position, shifting other items to the right
    # If the array is full, it replaces the value at the given index
    def insert(self, index, newItem):
        if index >= 0 and index < len(self) and self._logicalSize < len(self):
            for i in range(self._logicalSize, index, -1):
                self._items[i] = self._items[i-1]
            self._items[index] = newItem
            self._logicalSize += 1

    # This function allows comparing two Array objects for equality
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self._items == other._items
        else:
            return False

    # This function removes an item at the given position, shifting other items to the left
    def remove(self, index):
        if index >= 0 and index < self._logicalSize:
            for i in range(index, self._logicalSize - 1):
                self._items[i] = self._items[i+1]
            self._items[self._logicalSize - 1] = None
            self._logicalSize -= 1
            # Shrink the physical size of the array if it's larger than the logical size
            self._items = self._items[:self._logicalSize]
            
    # This function expands the array back to its original size or more
    def expand(self, new_capacity=None):
        if new_capacity is None:
            new_capacity = self._original_capacity
        if new_capacity > len(self):
            self._items.extend([None] * (new_capacity - len(self)))

# This function prompts the user to create an array, entering its size and items
def create_array(array_number):
    capacity = int(input(f"Enter the initial capacity of array {array_number}: "))
    array = Array(capacity)
    for i in range(capacity):
        value = int(input(f"Enter the value for position {i} of array {array_number}: "))
        array.insert(i, value)
    return array

def main():
    # Main loop, continues until the user chooses to exit
    while True:
        print("\\nOptions:")
        print("1 - Create and manipulate arrays")
        print("2 - Exit")
        option = int(input("Enter an option: "))

        if option == 1:
            # Prompt the user to create either 1 or 2 arrays
            array_count = int(input("Enter the number of arrays to create (1 or 2): "))
            array1 = create_array(1)  # Always create at least one array
            array2 = None
            if array_count == 2:
                array2 = create_array(2)  # Optionally create a second array

            while True:
                print("\\nOptions for comparing arrays:")
                print("1 - Compare the entire arrays")
                print("2 - Compare specific items in the arrays")
                print("3 - Start again")
                compare_option = int(input("Enter an option: "))

                if compare_option == 1:
                    # Compare the entire arrays
                    print("Array 1:", array1)
                    if array2 is not None:
                        print("Array 2:", array2)
                        print("The arrays are equal." if array1 == array2 else "The arrays are not equal.")
                    else:
                        print("No second array to compare with.")
                elif compare_option == 2 and array2 is not None:
                    # Compare specific items in the arrays
                    index = int(input("Enter the index of the item to compare: "))
                    if index < len(array1) and index < len(array2):  # Check if the index exists in both arrays
                        print(f"Item in array 1 at position {index}:", array1._items[index])
                        print(f"Item in array 2 at position {index}:", array2._items[index])
                        print("The items are equal" if array1._items[index] == array2._items[index] else "The items are not equal.")
                    else:
                        print("Index is out of range in one or both arrays. Please try again.")
                elif compare_option == 3:
                    # Start again
                    break
                else:
                    print("Invalid option, please try again.")
        elif option == 2:
            # Exit the program
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
