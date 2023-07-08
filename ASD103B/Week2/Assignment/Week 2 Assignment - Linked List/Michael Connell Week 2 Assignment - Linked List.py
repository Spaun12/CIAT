#Student: Michael Connell
# Date: 2023-07-08
#Version 1
class Node:
    """ 
    This is the story of Node, the superhero of our LinkedList. 
    He has the superpower of holding data and knowing about the next Node.
    I took some strong meds so here we go.
    """
    def __init__(self, data):
        self.data = data
        self.next = None # No knowledge about the next Node yet, such suspense!


class LinkedList:
    """ 
    LinkedList, the city of Nodes! 
    """
    def __init__(self):
        """
        Initializing our city with no superheroes, I mean, Nodes.
        """
        self.head = None 

    def add_node(self, data):
        """
        Our city needs a new superhero, I mean, Node! Let's add it.
        """
        if not self.head:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next # We keep going until we find a lonely Node with no next.
            node.next = Node(data) # We provide company to the lonely Node by adding a new Node. 

    def print_list(self):
        """
        Show me my superheroes, I mean, Nodes!
        """
        node = self.head
        while node:
            print(node.data)
            node = node.next # On to the next one!

    def insert_at_beginning(self, data):
        """
        Special delivery, a new superhero at the city entrance!
        """
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head

    def delete_node(self, target):
        """
        Sad day, we have to say goodbye to one of our superheroes :(
        """
        if self.head is None:
            return
        
        # Oh no! The first superhero is leaving the city!
        if self.head.data == target:
            self.head = self.head.next
            return

        node = self.head
        while node.next:
            if node.next.data == target:
                node.next = node.next.next
                break
            node = node.next

    def search_node(self, target):
        """
        Is our superhero in the city? Let's find out!
        """
        node = self.head
        while node:
            if node.data == target:
                return True # Found our superhero!
            node = node.next
        return False # Looks like our superhero is on a vacation.

# Time to test the might of our city and its superheroes!

# Initialize the city
ll = LinkedList()

# Add some superheroes
ll.add_node("Superman")
ll.add_node("Batman")
ll.add_node("Wonder Woman")

# Print all superheroes in the city
print("Superheroes in the city:")
ll.print_list()

# A new superhero is coming to town!
ll.insert_at_beginning("Spiderman")
print("\nSuperheroes in the city after Spiderman's arrival:")
ll.print_list()

# Is Batman in town?
print("\nIs Batman in town?")
print(ll.search_node("Batman"))  # Should print: True

# Oh no! Batman left the city!
ll.delete_node("Batman")
print("\nSuperheroes in the city after Batman's departure:")
ll.print_list()

# Is Batman still in town?
print("\nIs Batman in town?")
print(ll.search_node("Batman"))  # Should print: False
