#Michael Connell
#2023-07-23

#Week 5: Assignment - More on Graph

# The Node class, where we "Take on me... take me on..." Hard to believe this is still a thing.
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.edges = []  # We add an adjacency list to hold the edges

# The Queue class, like a good mullet, business at the front, party at the rear.
class Queue:
    def __init__(self):
        self.front = self.rear = None

    # In queue, we party (add nodes) at the rear.
    def enqueue(self, node):
        if not isinstance(node, Node):
            print("Hey, we only party with nodes here!")
            return
        if self.rear is None:
            self.front = self.rear = node
            return
        self.rear.next = node
        self.rear = node

    # When leaving the party (removing nodes), we exit from the front.
    
    def dequeue(self):
        if not self.is_empty():
            temp = self.front
            self.front = temp.next
            if(self.front == None):
                self.rear = None
            return temp  # Here, we return the node, not just the value
        else:
            return None

    def is_empty(self):
        return self.front is None

# The Stack class, it's like a hot, hot TV, it'll push till you drop.
class Stack:
    def __init__(self):
        self.top = None

    # We push it (add nodes) to the limit.
    def push(self, node):
        if not isinstance(node, Node):
            print("Hold up, that's not a node!")
            return
        node.next = self.top
        self.top = node

    # We pop it (remove nodes) like it's hot.
    def pop(self):
        if self.is_empty():
            return None
        else:
            temp = self.top
            self.top = self.top.next
            return temp

    def is_empty(self):
        return self.top is None

# The Visited class, where we "Been there, done that."
class Visited:
    def __init__(self):
        self.visited = None

    # Here we check if a node has been visited before. If yes, it's a "Deja vu."
    def is_visited(self, node):
        current = self.visited
        while current:
            if current == node:
                return True
            current = current.next
        return False

    # Here we add a node to the visited list. It's like signing a yearbook. I remember those days.
    def add_visited(self, node):
        if not isinstance(node, Node):
            print("We don't sign yearbooks of non-nodes!")
            return
        if self.visited is None:
            self.visited = node
        else:
            current = self.visited
            while current.next:
                current = current.next
            current.next = node

# The LinkedGraph class, it's where the magic happens, like Saturday morning cartoons.
class LinkedGraph:
    def __init__(self):
        self.nodes = None

    # add_node is like adding a new character to your D&D campaign. Never played this game much, but I hear it's fun.
    def add_node(self, value):
        new_node = Node(value)
        if not self.nodes:
            self.nodes = new_node
        else:
            current = self.nodes
            while current.next:
                current = current.next
            current.next = new_node

    # add_edge is making a pact of friendship between two nodes. 
    def add_edge(self, node1, node2):
        n1, n2 = self._get_node(node1), self._get_node(node2)
        if n1 and n2:
            n1.edges.append(n2)  # We append n2 to n1's adjacency list
            n2.edges.append(n1)  # We append n1 to n2's adjacency list
        else:
            print("One or both nodes not found in the graph. Maybe they're out on a coffee break.")

    # _get_node is like a directory assistance, helps you find the node you're looking for. An efficient maximizer.
    def _get_node(self, value):
        current = self.nodes
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    # bfs is like a game of Marco Polo, but for nodes.
    def bfs(self, start_node, target_value):
        start = self._get_node(start_node)
        if not start:
            print("The start node is not in the graph. Probably taking a break.")
            return None
        queue = Queue()
        visited = Visited()
        queue.enqueue(start)
        visited.add_visited(start)  # Marking the start node as visited
        while not queue.is_empty():
            current_node = queue.dequeue()  # Here, we dequeue the node, not the value
            if current_node.value == target_value:
                return current_node
            for node in current_node.edges:  # We now iterate over the adjacency list
                if not visited.is_visited(node):
                    queue.enqueue(node)
                    visited.add_visited(node)  # Marking the node as visited after enqueuing
        return None

    # dfs is like playing a game of hide and seek, it goes deep to seek nodes.
    def dfs(self, start_node, target_value):
        start = self._get_node(start_node)
        if not start:
            print("The start node is not in the graph. Maybe it's playing hide-and-seek.")
            return None
        stack = Stack()
        visited = Visited()
        stack.push(start)
        visited.add_visited(start)  # Marking the start node as visited
        while not stack.is_empty():
            current_node = stack.pop()  # Here, we pop the node, not the value
            if current_node.value == target_value:
                return current_node
            for node in current_node.edges:  # We now iterate over the adjacency list
                if not visited.is_visited(node):
                    stack.push(node)
                    visited.add_visited(node)  # Marking the node as visited after pushing onto the stack
        return None
    
    # add_all_paths is like playing a game of Clue. It finds all the paths to the target node.
    def all_paths(self, start_node, target_value, path=None):
        start = self._get_node(start_node)
        if path is None:
            path = []  # If no path is provided, we start with an empty path.

        path = path + [start.value]  # We append the current node to the path.

        # If we've hit the jackpot (found the target node), we return the current path.
        if start.value == target_value:
            return [path]

        paths = []  # This will hold all the paths we find.
        for node in start.edges:  # We explore all the neighbors of the current node.
            if node.value not in path:  # We only proceed if the node has not been visited.
                newpaths = self.all_paths(node.value, target_value, path)  # Recursive call
                for newpath in newpaths:
                    paths.append(newpath)
        return paths  # Return all the paths we've found.

# Here's where we test it in action.
if __name__ == "__main__":
    graph = LinkedGraph()  # We're on a "Highway to the Danger Zone."

    for i in range(5):  # Adding nodes to the graph like a new season of Friends.
        graph.add_node(i)

    for i in range(4):  # Adding edges to the graph, forming a perfect rock band.
        graph.add_edge(i, i+1)

    start_node = 0
    target_value = 4
    bfs_result = graph.bfs(start_node, target_value)  # Going on a BFS like a search for the Holy Grail.
    dfs_result = graph.dfs(start_node, target_value)  # Going on a DFS like a deep dive.

    # Testing all_paths function like playing a round of Jeopardy.
    start_node = 0
    target_value = 4
    all_paths_result = graph.all_paths(start_node, target_value)
    print(f"All Paths: Found these paths from {start_node} to {target_value}: {all_paths_result}")

    if bfs_result:
        print(f"BFS: Found node with value {bfs_result.value}!")
    else:
        print("BFS: Target node not found. Maybe it's hanging out with Waldo.")

    if dfs_result:
        print(f"DFS: Found node with value {dfs_result.value}!")
    else:
        print("DFS: Target node not found. I bet it's out on a secret mission.")
