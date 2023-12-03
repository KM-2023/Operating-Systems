
 #   This code is TSL (Test and Set ) solution

 # TSL is a hardware solution so to simulate it in the code we will assume only one process is in critical section 
 # Similar to lock variable solution, with some more disaadvantages due to the hardware solution
 # Benefit: reduced overhead and improved performance especially if the number of concurrent processes increase
 
import threading    # importing the threading library 

lock = False     # Shared variable that determines if critical section is occupied or not

# Function for process 1
def P1():
    global lock       # global lock variable
    while True:
        while lock:  # busy waiting if lock is true, that is a process is already in the critical section
            pass

        # Critical section, critical section  occupied by this process
        lock = True
        print("Process 1 entered the critical section")

        # setting lock to be false, critical section free
        lock = False

# Function for process 2
def P2():
    global lock   # global lock variable
    while True:
        while lock:  # busy waiting if lock is true, that is a process is already in the critical section
            pass

        # Critical section, critical section  occupied by this process
        lock = True
        print("Process 2 entered the critical section")
        # setting lock to be false, critical section free
        lock = False

# Creating threads
p1 = threading.Thread(target=P1)
p2 = threading.Thread(target=P2)

# Starting threads
p1.start()
p2.start()
