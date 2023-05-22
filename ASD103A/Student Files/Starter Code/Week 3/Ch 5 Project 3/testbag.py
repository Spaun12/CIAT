"""
File: testbag.py
Author: Ken Lambert
A tester program for bag implementations.
"""

from arraybag import ArrayBag
from linkedbag import LinkedBag

def test(bagType):
    """Expects a bag type as an argument and runs some tests
    on objects of that type."""
    print("Testing", bagType)
    lyst = list(range(1, 11))
    print("The list of items added is:", lyst)
    b = bagType(lyst)
    print("Expect the bag's string:", b)
    print("Add 5 more items to test increasing the array size:")
    for i in range(11, 16):
        b.add(i)
    print("Expect the bag's string:", b)

test(ArrayBag)
#test(LinkedBag)
