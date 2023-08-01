#Michael Connell
#2023-07-19

#This was very interesting to see in action and 
#begining to understand the usefulness of these data structures.

# 1) Create Node class
class Node:
    def __init__(self, value):
        self.value = value  # node's value
        self.next = None  # pointer to the next node
        self.prev = None  # pointer to the previous node

# 2) Create LinkedSet class with required methods
# includiing: add, remove, contains, union, intersection
class LinkedSet:
    def __init__(self):
        self.head = None  # first node in the set
        self.tail = None  # last node in the set

    # 3a) add method
    def add(self, value):
        # if the set is empty, add the new node
        if self.head is None:
            new_node = Node(value)
            self.head = self.tail = new_node
        # if the value is not in the set, add the new node
        elif not self.contains(value):
            new_node = Node(value)
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    # 3b) remove method
    def remove(self, value):
        current = self.head

        # iterate over the set
        while current is not None:
            # if the node's value matches the target value, remove the node
            if current.value == value:
                if current.prev is not None:
                    current.prev.next = current.next
                if current.next is not None:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
            current = current.next

    # 3c) contains method
    def contains(self, value):
        current = self.head

        # iterate over the set
        while current is not None:
            # if the node's value matches the target value, return True
            if current.value == value:
                return True
            current = current.next

        # if we've gone through the entire set and didn't find the value, return False
        return False

    # 3d) union method
    def union(self, other):
        union_set = LinkedSet()

        current = self.head
        # add all elements from the first set
        while current is not None:
            union_set.add(current.value)
            current = current.next

        current = other.head
        # add all elements from the second set
        while current is not None:
            union_set.add(current.value)
            current = current.next

        return union_set

    # 3e) intersection method
    def intersection(self, other):
        intersection_set = LinkedSet()

        current = self.head
        # add the elements present in both sets
        while current is not None:
            if other.contains(current.value):
                intersection_set.add(current.value)
            current = current.next

        return intersection_set

#Now we test
# create two sets
set1 = LinkedSet()
set2 = LinkedSet()

# add some elements
set1.add(1)
set1.add(2)
set1.add(3)

set2.add(3)
set2.add(4)
set2.add(5)

# remove an element
set1.remove(2)

# check if the sets contain some elements
print("Does set1 contain 1?:", set1.contains(1))  # True
print("Does set1 contain 2?:", set1.contains(2))  # False
print("Does set2 contain 4?:", set2.contains(4))  # True

# find the union of the sets
print("\nUnion of set1 and set2:")
union_set = set1.union(set2)
current = union_set.head
while current is not None:
    print(current.value)  # 1, 3, 4, 5
    current = current.next

# find the intersection of the sets
print("\nIntersection of set1 and set2:")
intersection_set = set1.intersection(set2)
current = intersection_set.head
while current is not None:
    print(current.value)  # 3
    current = current.next