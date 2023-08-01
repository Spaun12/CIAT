#Michael Connell
#2023-07-15

#Week 3: Assignment - More on Binary Tree
#I didn't realize they needed to be put together. But here it is. This was a great week. I learned a lot. I am looking forward to next week.

class Node:
    #Each node has a value, and pointers to its left and right children.
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    #Binary tree structure with methods for insertion, search, and deletion.
    def __init__(self, root_val):
        #Root node is created when a BinaryTree object is instantiated.
        self.root = Node(root_val)

    def add_node(self, value):
        #Add a node to the binary tree.
        if not isinstance(value, int):
            raise ValueError("Only integer values can be inserted into the tree")
        self._add_node(value, self.root)

    def _add_node(self, value, node):
        #Recursively find the spot to insert the new node.
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_node(value, node.left)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_node(value, node.right)

    def find_min(self, node=None):
        #Returns the node with the minimum value in the tree or subtree.
        if node is None:
            node = self.root
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_max(self):
        #Returns the node with the maximum value in the tree.
        current = self.root
        while current.right is not None:
            current = current.right
        return current

    def delete(self, value):
        #Delete a node with the specified value from the tree.
        self.root = self._delete_node(self.root, value)

    def _delete_node(self, root, value):
        #Recursively find the node to delete and remove it from the tree.
        if root is None:
            return root

        if value < root.value:
            root.left = self._delete_node(root.left, value)
        elif value > root.value:
            root.right = self._delete_node(root.right, value)
        else:
            # Node with only one child or no child
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children: Get the inorder successor
            temp = self.find_min(root.right)
            root.value = temp.value
            # Delete the inorder successor
            root.right = self._delete_node(root.right, temp.value)

        return root

    def search(self, value):
        #Search for a value in the binary tree.
        return self._search(value, self.root)

    def _search(self, value, node):
        #Recursively check nodes until the value is found or all nodes are checked.
        if node is None or node.value == value:
            return node is not None
        if value < node.value:
            return self._search(value, node.left)
        else:
            return self._search(value, node.right)

    def height(self, node=None):
        """Return the height of the tree or subtree."""
        if node is None:
            return 0
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

    
    def insert(self, value):
    #Add a node to the binary tree.
        self._add_node(value, self.root)


# Instantiate a BinaryTree with root node 10
bt = BinaryTree(10)

# Insert some nodes
bt.insert(5)
bt.insert(15)
bt.insert(2)
bt.insert(7)
bt.insert(12)
bt.insert(20)

# Test search method
print(bt.search(15))  # should print True
print(bt.search(8))  # should print False

# Test find_min and find_max methods
print(bt.find_min().value)  # should print 2
print(bt.find_max().value)  # should print 20

# Test delete method
bt.delete(15)  # delete node with value 15
print(bt.search(15))  # should print False now

# Test height method
print(bt.height())  # should print 3

# Test error condition: inserting a string
try:
    bt.add_node("hello")  # should raise ValueError
except ValueError as e:
    print(f"An error occurred: {str(e)}")
