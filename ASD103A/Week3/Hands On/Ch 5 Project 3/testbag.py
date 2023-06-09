"""
File: testbag.py
Author: Ken Lambert (Edited by Michael Connell 2023-06-09)
A tester program for bag implementations.
"""

# Import the ArrayBag class from arraybag.py file.
# We don't need to import LinkedBag, so we can comment it out.
from arraybag import ArrayBag
from linkedbag import LinkedBag

def test(bagType):
    """Expects a bag type as an argument and runs some tests
    on objects of that type."""
    print("Testing", bagType)
    lyst = list(range(1, 11))  # This creates a list of integers from 1 to 10.
    print("The list of items added is:", lyst)  # Print the created list.
    
    # Create a new bag object using the list, which tests the __init__ and add methods.
    b = bagType(lyst)
    print("Expect the bag's string:", b)  # Print the string representation of the bag.
    
    # Testing the add method specifically with the automatic resizing functionality.
    print("Add 5 more items to test increasing the array size:")
    for i in range(11, 16):  # Add numbers 11 to 15 to the bag.
        b.add(i)  # This also tests the automatic resizing of the array in the add method.
    print("Expect the bag's string:", b)  # Print the updated bag.
    
    # Testing the remove method specifically with the automatic resizing functionality.
    print("Remove 5 items to test decreasing the array size:")
    for i in range(11, 16):  # Remove numbers 11 to 15 from the bag.
        b.remove(i)  # This also tests the automatic resizing of the array in the remove method.
    print("Expect the bag's string:", b)  # Print the updated bag.

# Call the test function with the ArrayBag class.
# We don't need to test the LinkedBag, so we can comment it out.
test(ArrayBag)
# test(LinkedBag)

