# Michael Connell Week2 Coding Assignment Multi-threading
# Date: 2023-10-23

# Step1: Import required modules
import threading
from time import sleep

# Step2: Define a custom class that extends Thread
class MyThread(threading.Thread):
    # Constructor
    def __init__(self, name, num):
        # Call the constructor of the superclass
        super().__init__()
        # Set the name and num attributes
        self.name = name
        self.num = num
        # Set the finished attribute to False
        self.finished = False

    # Main thread method
    def run(self):
        # Loop from num to 0
        for i in range(self.num, 0, -1):
            # Print the countdown
            print(f"{self.name}: Countdown {i}")
            # Sleep for one second
            sleep(1)
        # Set the finished attribute to True
        self.finished = True

    # Additional method to check if thread has finished
    def is_finished(self):
        return self.finished

# Step3: Create five instances of the MyThread class
threads = [
    MyThread("Thread 1", 5),
    MyThread("Thread 2", 4),
    MyThread("Thread 3", 3),
    MyThread("Thread 4", 2),
    MyThread("Thread 5", 1),
]

# Step4: Start the threads
for thread in threads:
    thread.start()

# Step5: Wait for all threads to finish before continuing
for thread in threads:
    thread.join()

# Step6: Check if each thread has finished
for thread in threads:
    print(f"{thread.name} has finished: {thread.is_finished()}")

# Step7: Print a message to indicate that the program has finished
print("Program finished.")
