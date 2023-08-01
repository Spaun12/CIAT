#Michael D. Connell Jr.
#2023-07-15

#Week 3 - Hands On Exercise - Binary Tree Part I

class Node:
    # Define the structure of the node
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    # Initialize the tree with a root node
    def __init__(self):
        self.root = None

    # Method to add a node to the tree
    def add_node(self, value):
        if self.root is None:  # If tree is empty, set root as the new node
            self.root = Node(value)
        else:
            self._add_node(value, self.root)

    # Helper method for add_node, it's recursive
    def _add_node(self, value, node):
        if value <= node.value:  # If value is less than current node value, go left
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_node(value, node.left)
        else:  # If value is more than current node value, go right
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_node(value, node.right)

    # Method to search a value in the tree
    def search(self, value):
        if self.root is not None:
            return self._search(value, self.root)
        else:
            return False

    # Helper method for search, it's also recursive
    def _search(self, value, node):
        if value == node.value:  # If value is found, return True
            return True
        elif value < node.value and node.left is not None:  # If value is less, go left
            return self._search(value, node.left)
        elif value > node.value and node.right is not None:  # If value is more, go right
            return self._search(value, node.right)
        return False  # Return False if not found

# Test Case 1: Adding and searching for a value in the tree
tree = BinaryTree()
tree.add_node(10)
try:
    assert(tree.search(10) == True)
    print("Test Case 1 Passed") 
except AssertionError:
    print("Test Case 1 Failed")

# Test Case 2: Searching for a value not in the tree
try:
    assert(tree.search(15) == False)
    print("Test Case 2 Passed")
except AssertionError:
    print("Test Case 2 Failed")

# Test Case 3: Adding multiple values and searching
tree.add_node(15)
tree.add_node(5)
tree.add_node(20)
try:
    assert(tree.search(15) == True and tree.search(5) == True and tree.search(20) == True)
    print("Test Case 3 Passed")
except AssertionError:
    print("Test Case 3 Failed")

# Test Case 4: Searching for a value not in the tree should return False
try:
    assert not tree.search(40)
    print("Test Case 4 Passed")
except AssertionError:
    print("Test Case 4 Failed")

# Test Case 5: Intentional fail. We know 100 is not in the tree, so this should return False
try:
    assert(tree.search(100) == True)
    print("Test Case 5 Passed")
except AssertionError:
    print("Test Case 5 Failed")
