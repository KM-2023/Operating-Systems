# The following code utilizes disabling interrupts to achieve mutual exclusion
import threading

# Represents a simple process
class Process(threading.Thread):
    def __init__(self, name, lock): # Initialize the process with a name and lock
        super(Process, self).__init__() # Here we call the superclass (Process) to initialize the thread
        self.name = name  # Represents an instance of the name of the process
        self.lock = lock  # Represents an instance of the lock set on the process

    def run(self):
        while True:
            with self.lock:  # utilizes the lock to ensure mutual exclusion -> next line
                # to allow one process to execute the critical section at a time.
                print(f"Process {self.name} is running")  # Print the process running


# Define a lock for mutual exclusion
lock = threading.Lock()

# Create processes
process1 = Process("1", lock)
process2 = Process("2", lock)

# Start the processes
process1.start()
process2.start()
