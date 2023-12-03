# This is a code implementation of condition variables

import threading
import time

# Condition variable
condition = threading.Condition() # allows threads to wait for notifications based on certain conditions.

# Shared resource
shared_resource = [] # This would be used for all the threads

# Function for the First Process
def process_1():
    global shared_resource
    with condition: # Process 1 acquired the condition lock
        print("Process 1 is waiting...")
        condition.wait()  # Process 1 will remain in waiting state -> check next line
        # until process 3 notifies it using "condition.notify_all()"
        print(f"Process 1 resumed. Shared Resource: {shared_resource}") # Process 3 gave it the signal to resume

# Function for the Second Process
def process_2():
    global shared_resource
    with condition:  # Process 2 acquired the condition lock
        print("Process 2 is waiting...")
        condition.wait()  # Process 2 will remain in waiting state -> check next line
        # until process 3 notifies it using "condition.notify_all()"
        print(f"Process 2 resumed. Shared Resource: {shared_resource}") # Process 3 gave it the signal to resume

# Function for the Third Process (Signaling)
def process_3():
    global shared_resource
    time.sleep(2)  # To give enough time for processes 1 and 2 to initialize
    with condition:  # Process 3 acquired the condition lock
        shared_resource.append("Data 1")  # It will modify data in the critical section
        print("Process 3 added data to shared resource.")
        condition.notify_all()  # It will notify process 1 and 2 to resume

# Creating threads for processes
process1_thread = threading.Thread(target=process_1)
process2_thread = threading.Thread(target=process_2)
process3_thread = threading.Thread(target=process_3)

# Starting threads
process1_thread.start()
process2_thread.start()
process3_thread.start()
