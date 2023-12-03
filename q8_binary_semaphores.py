import threading
import time

# Shared resource
shared_variable = 0  # Represents the critical section
mutex = threading.Lock()  # Creates a lock to ensure that only one process ca access the critical section at a time

# Note: Process 1 increments the shared variable, while process 2 decrements it
# Function for the Process 1
def process_1():
    global shared_variable
    while True:
        mutex.acquire()  # Process 1 acquired the lock, so the critical section would be exclusive to it
        shared_variable += 1  # Incrementing the shared variable
        print(f"Process 1 incremented shared_variable: {shared_variable}")
        mutex.release()  # Process 1 will release the lock after it finished from the critical section
        time.sleep(1)  # Pause the execution of process 1

# Function for the Process 2
def process_2():
    global shared_variable
    while True:
        mutex.acquire()  # Process 2 acquired the lock, so the critical section would be exclusive to it
        shared_variable -= 1  # Decrementing the shared variable
        print(f"Process 2 decremented shared_variable: {shared_variable}")
        mutex.release()  # Process 2 will release the lock after it finished from the critical section
        time.sleep(1)  # Pause the execution of process 2

# Creating threads for processes
process1_thread = threading.Thread(target=process_1)
process2_thread = threading.Thread(target=process_2)

# Starting threads
process1_thread.start()
process2_thread.start()
