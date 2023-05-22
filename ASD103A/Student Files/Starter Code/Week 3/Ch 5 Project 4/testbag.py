"""
File: testbag.py
Author: Ken Lambert
A tester program for bag implementations.
"""

from arraybag import ArrayBag

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

def testResize():
    """Tests the resizing of an array-based bag,
    when space is wasted."""
    bag = ArrayBag(range(100))
    print("Added 100 items, length of bag =", len(bag))
    print("Expect 160 as length of array =", len(bag.items))
    print(bag)
    for item in range(76):
        bag.remove(item)
    print("Removed 76 items, expect 24 as length of bag:", len(bag))
    print("Expect 80 as length of array =", len(bag.items))
    for item in range(76, 100):
        bag.remove(item)
    print("Removed remaining items, length of bag =", len(bag))
    print("Expect 10 as length of array =", len(bag.items))

testResize()
