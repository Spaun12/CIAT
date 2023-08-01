#Michael Connell
#2023-07-15

#Week 3 - Hands On Exercise - Binary Tree Part II

class Node:
    # Each node has a value, and pointers to its left and right children
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        # Root node is created when a BinaryTree object is instantiated
        self.root = Node(root)

    def insert(self, new_val):
        # Check if the input is an integer
        if not isinstance(new_val, int):
            raise TypeError("Only integer values can be inserted into the tree")

        # Use helper method to find the correct spot in the tree
        self.insert_helper(self.root, new_val)

    def insert_helper(self, current, new_val):
        # Insert to the right if new value is greater than current node's value
        if current.value < new_val:
            if current.right:
                self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val)
        else:
            # Otherwise, insert to the left
            if current.left:
                self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val)

    # Pre-order traversal: root, left, right
    def preorder(self, start, traversal):
        if start:
            traversal += (str(start.value) + '-')
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal

    # In-order traversal: left, root, right
    def inorder(self, start, traversal):
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += (str(start.value) + '-')
            traversal = self.inorder(start.right, traversal)
        return traversal

    # Post-order traversal: left, right, root
    def postorder(self, start, traversal):
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += (str(start.value) + '-')
        return traversal
    
    # Set up tree
tree = BinaryTree(4)
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

try:
    # This should now raise a TypeError as expected
    tree.insert('six')
except TypeError as e:
    print(e)

# Test preorder
# Should be 4-2-1-3-5
print(tree.preorder(tree.root, ''))

# Test in order
# Should be 1-2-3-4-5
print(tree.inorder(tree.root, ''))

# Test post order
# Should be 1-3-2-5-4
print(tree.postorder(tree.root, ''))
