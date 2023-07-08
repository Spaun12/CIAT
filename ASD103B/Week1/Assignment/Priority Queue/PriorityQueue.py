#Michael Connell
#2023-07-01
#Week 1: Assignment - Priority Queue

# Import the heapq module which provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.
import heapq

class PriorityQueue:
    # Here, we define two attributes: queue and index
    # 'queue' is where we store our items with their priorities
    # 'index' is used to differentiate items with the same priority
    def __init__(self):
        self.queue = []  # the queue is initialized as an empty list
        self.index = 0   # the index is initialized as 0

    # The push function adds an item to the queue with a given priority
    # heapq.heappush pushes values onto the heap maintaining the heap invariant
    # By default, heapq creates a min-heap, so we use negative priority to turn it into max-heap
    # Index is used to sort items with the same priority
    def push(self, item, priority):
        heapq.heappush(self.queue, (-priority, self.index, item))
        self.index += 1  # increment the index after adding an item

    # The pop function removes and returns the highest priority item from the queue
    # heapq.heappop pops and returns the smallest item from the heap, maintaining the heap invariant.
    def pop(self):
        return heapq.heappop(self.queue)[-1]  # we return the item, ignoring priority and index

# Now, let's test our PriorityQueue class

# Instantiate the PriorityQueue class
pq = PriorityQueue()

# Use the push method to add some items with different priorities
pq.push("test1", 3)
pq.push("test2", 1)
pq.push("test3", 2)

# Test the pop method and print out the items
# They should be printed in the order of their priorities: "item1", "item3", "item2"
print(pq.pop())
print(pq.pop())
print(pq.pop())
