#Student: Michael D. Connell Jr.
#Date: 2023-07-01
#queue_implementation

""" Queue Class Implementation:

The Queue class has three main methods: enqueue, dequeue, and size. 

The enqueue method adds an item to the end of the queue. 
This is done using the append method of a list, which adds an item to the end of the list.

The dequeue method removes the first item from the queue and returns it. 
This is done by checking if the queue is not empty and then using the pop method of a list with an index of 0,
which removes and returns the first item in the list.

The size method returns the size of the queue. 
This is done using the len function on the queue, which returns the number of items in the list.

The main function creates a Queue object, 
adds some items to the queue, checks the size of the queue, 
removes items from the queue, and checks the size again to verify the correct operation of the Queue class. """

class Queue:
    # This function initializes the queue as an empty list
    def __init__(self):
        self.queue = []

    # This adds an item to the end of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # This removes the first item from the queue if the queue is not empty and returns it
    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    # This returns the size of the queue
    def size(self):
        return len(self.queue)

def main():
    # Instantiate an object of Queue class
    queue = Queue()

    # Add some items to the queue
    queue.enqueue("First Cool Beat")
    queue.enqueue("Second Cool Beat")
    queue.enqueue("Third Cool Beat")
    print(f"Size of queue after enqueue: {queue.size()}")

    # Dequeue and print them out
    while queue.size() > 0:
        print(queue.dequeue())

    print(f"Size of queue after dequeue: {queue.size()}")

if __name__ == "__main__":
    main()

