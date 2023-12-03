# The following code attempts to implement Peterson's solution for mutual exclusion

# Note flag[0] = True for process_0, and flag[1] = True for process_1

import threading
import time

shared_value = 0  # This represents the shared resource

# Flags to indicate if a thread wants to enter the critical section
flag = [False, False]  # It is either 1 or 0

# Variable to indicate whose turn it is to enter the critical section
turn = 0  # Turn = 0 for process 0, Turn = 1 for process 1

# Function for Thread 0
def process_0():
    global shared_value, flag, turn  # The variables involved, shared value is critical section
    while True:
        flag[0] = True  # Process 0 wants to enter the critical section (It sets the flag to True)
        turn = 1  # It is process 1's turn currently
        while flag[1] and turn == 1: # Wait for process 1 to finish
            pass

        # Critical section
        shared_value += 1  # Here we indicate that the process modified the critical section
        print(f"Process 0 incremented shared_value: {shared_value}")
        
        flag[0] = False  # Here the flag indicates that process 0 is done
        # Non-critical section
        time.sleep(1)  # Now it will wait for process 1 to finish

# Function for Thread 1
def process_1():
    global shared_value, flag, turn # The variables involved, shared value is critical section
    while True:
        flag[1] = True # Process 1 wants to enter the critical section (It sets the flag to True)
        turn = 0  # It is process 0's turn currently
        while flag[0] and turn == 0:  # Wait for process 0 to finish
            pass

        # Critical section
        shared_value += 1
        print(f"Process 1 incremented shared_value: {shared_value}")
        
        flag[1] = False  # Here the flag indicates that process 1 is done
        # Non-critical section
        time.sleep(1)  # Now it will wait for process 0 to finish

# Creating threads
p0 = threading.Thread(target=process_0)
p1 = threading.Thread(target=process_1)

# Starting threads
p0.start()
p1.start()
