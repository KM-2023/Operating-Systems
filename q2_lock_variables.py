

    #   This Program implements the Lock variables solution for Inter-Process Communication
                    
    # - The implementation is done on threads to simulate lock variables solution on processes
    
 
# importing required libraries                   
import threading
import time

# Shared resources
shared_var_1 = 0        # variable for process 1 manipulated in critical section of Process 1
shared_var_2 = 0       # variable for process 2 manipulated in critical section of process 2

# Locks for each shared variable
lock_1 = threading.Lock()      # lock object to serve as lock variable for process 1
lock_2 = threading.Lock()       # lock objects to serve as lock variable for process 1


# a function to update shared_var_1 (for process 1)
def modify_shared_var_1():
    global shared_var_1       # to make sure the variable is not out of scope of this class, as it is a global variable 
       
    while True: 
        # this with statement acquires the lock to this critical section  | and locks the critical section | with releases critical section lock after it finishes executing
        with lock_1:
            
            # incrementing p1's critical section to demonstrate that only p1 is accsing this section
            shared_var_1 += 1
            print(f"Process 1 modified shared_var_1: {shared_var_1}\n")
            
            # suspending a process/thread for 1 second to to prevent excessive CPU/other resources consumption
            time.sleep(1)

# a function to update shared_var_2 (for process 2)
def modify_shared_var_2():
    global shared_var_2
    while True:
                
        # this 'with' statement acquires the lock to this critical section  | and locks the critical section | with releases critical section lock after it finishes executing
        with lock_2:
            
            # incrementing p2's critical section to demonstrate that only p2 is accsing this section
            shared_var_2 += 1
            print(f"Process 2 modified shared_var_2: {shared_var_2} \n")
            time.sleep(1)

# Creating threads / which are equivalent to processes 

thread1 = threading.Thread(target=modify_shared_var_1)    # target indicates the function we want our thread to execute
thread2 = threading.Thread(target=modify_shared_var_2)    # thread 2 to execute process 2's critical section

# starting the threads | 
thread1.start()
thread2.start()
