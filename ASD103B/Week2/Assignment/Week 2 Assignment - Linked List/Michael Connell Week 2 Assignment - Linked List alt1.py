#Student: Michael Connell
# Date: 2023-07-08
#Version 2
class Node:
    """
    The story of 'Node', the superhero of our LinkedList.
    """
    def __init__(self, data):
        self.data = data
        self.next = None  # No knowledge about the next Node yet, such suspense!


class LinkedList:
    """
    LinkedList, the city of Nodes!
    """
    def __init__(self):
        """
        Requirement 1: Initializing our city with no superheroes, I mean, Nodes.
        """
        self.head = None  # Requirement 1: __init__ method

    def add_node(self, data):
        """
        Requirement 2: Our city needs a new superhero/Node! Let's add them.
        """
        if not self.head:  # If our city is empty,
            self.head = Node(data)  # The new superhero is the head
        else:
            node = self.head
            while node.next:  # Traverse to the end of the city
                node = node.next
            node.next = Node(data)  # Add our new superhero  # Requirement 2: add_node method

    def print_list(self):
        """
        Requirement 3: Show me my superheroes/Nodes!
        """
        node = self.head
        while node:  # Traverse through the city
            print(node.data)  # Print superhero's name
            node = node.next  # Move to next superhero  # Requirement 3: print_list method

    def insert_at_beginning(self, data):
        """
        Requirement 4: Special delivery, a new superhero/Node at the city entrance!
        """
        new_head = Node(data)  # Create our new superhero
        new_head.next = self.head  # Link new superhero to the current head
        self.head = new_head  # Make new superhero the head  # Requirement 4: insert_at_beginning method

    def delete_node(self, target):
        """
        Requirement 5: Sad day, we have to say goodbye to one of our Nodes/superheroes :(
        """
        if self.head is None:  # If the city is empty,
            return  # No superheroes to say goodbye to
        if self.head.data == target:  # If head superhero is leaving the city,
            self.head = self.head.next  # Just skip it  # Requirement 5: delete_node method
            return
        node = self.head
        while node.next:  # Traverse the city
            if node.next.data == target:  # If next superhero's name matches target
                node.next = node.next.next  # Skip the superhero with target name
                break
            node = node.next

    def search_node(self, target):
        """
        Requirement 6: Is our superhero/Node in the city? Let's send up the signal to!
        """
        node = self.head
        while node:  # Traverse the city
            if node.data == target:  # If we find target superhero
                return True  # Superhero found!
            node = node.next  # Move on to next superhero
        return False  # Superhero not found  # Requirement 6: search_node method

def superhero_linked_list_game():
    """
    Welcome to the Superhero Node Game! Let's manage our superhero city.
    """
    ll = LinkedList()  # Initialize an empty linked list (Requirement 1: __init__ method)

    while True:
        print("\n1. Add a superhero")  # Requirement 2: add_node method
        print("2. Add a superhero at the beginning")  # Requirement 4: insert_at_beginning method
        print("3. Remove a superhero")  # Requirement 5: delete_node method
        print("4. Search for a superhero")  # Requirement 6: search_node method
        print("5. Display all superheroes")  # Requirement 3: print_list method
        print("6. Exit game")

        choice = input("\nChoose an option: ")

        if choice == "1":
            superhero = input("\nWho's the new superhero? ")
            ll.add_node(superhero)  # Requirement 2: add_node method
        elif choice == "2":
            superhero = input("\nWho's the new superhero at the entrance? ")
            ll.insert_at_beginning(superhero)  # Requirement 4: insert_at_beginning method
        elif choice == "3":
            superhero = input("\nWho's leaving the city? ")
            ll.delete_node(superhero)  # Requirement 5: delete_node method
        elif choice == "4":
            superhero = input("\nWho are you looking for? ")
            if ll.search_node(superhero):  # Requirement 6: search_node method
                print(f"{superhero} is in town!")
            else:
                print(f"{superhero} is not in town.")
        elif choice == "5":
            print("\nSuperheroes in town:")
            ll.print_list()  # Requirement 3: print_list method
        elif choice == "6":
            print("\nThanks for playing the Node superhero game!")
            break
        else:
            print("\nInvalid choice. Please choose a valid option.") 
        
if __name__ == "__main__":
    superhero_linked_list_game()
