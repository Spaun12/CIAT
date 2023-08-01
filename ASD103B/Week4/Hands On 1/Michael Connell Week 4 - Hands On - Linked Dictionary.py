#Michael Connell
#2023-07-19

#Week 4 - Hands On - Linked Dictionary

#Create Node class
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

#Create Linked Dictionary class
class LinkedDict:
    def __init__(self):
        # The head node is the start of the linked list.
        self.head = None
    
    def add(self, key, value):
        # If the list is empty, create a new node as the head node.
        if self.head is None:
            self.head = Node(key, value)
        else:
            # If the list is not empty, we traverse it until we find the key or reach the end of the list.
            current = self.head
            while current is not None:
                # If we find the key, we update the value and return.
                if current.key == key:
                    current.value = value
                    return
                # If we've reached the end of the list, we add a new node and return.
                if current.next is None:
                    current.next = Node(key, value)
                    return
                # Otherwise, we move to the next node and continue the search.
                current = current.next

    def get(self, key):
        # Start at the head node.
        current = self.head
        # Traverse the list until we find the key or reach the end of the list.
        while current is not None:
            if current.key == key:
                return current.value
            current = current.next
        # If we've reached the end of the list without finding the key, we return None.
        return None

    def delete(self, key):
        # If the list is empty, there's nothing to delete.
        if self.head is None:
            return
        # If the head node is the one to delete, we just set the head to the next node.
        if self.head.key == key:
            self.head = self.head.next
            return
        # Otherwise, we need to traverse the list and keep track of the previous node.
        current = self.head
        previous = None
        while current is not None and current.key != key:
            previous = current
            current = current.next
        # If we've reached the end of the list without finding the key, there's nothing to delete.
        if current is None:
            return
        # If we've found the key, we remove the node from the list by making the previous node point to the next node.
        previous.next = current.next

#Last, for the testing code (I actually made the mistake of not have it print a
# message if the test passed, so I added that in for my own sanity.)
# Test cases
linked_dict = LinkedDict()

# Test add
linked_dict.add("key1", "value1")
assert linked_dict.get("key1") == "value1"
print("Test add passed")

# Test update
linked_dict.add("key1", "new_value1")
assert linked_dict.get("key1") == "new_value1"
print("Test update passed")

# Test get
assert linked_dict.get("non_existent_key") == None
print("Test get passed")

# Test delete
linked_dict.delete("key1")
assert linked_dict.get("key1") == None
print("Test delete passed")
  