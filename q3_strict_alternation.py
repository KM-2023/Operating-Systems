
    #   This Program implements the Strict Alternation 
                    
    # - The implementation is done on threads to simulate lock variables solution on processes
    
    # - Strict alternation is an attractive solution against lock variables for several reasons: 
    #       - avoids buisy waiting (alternates between processes), achieves mutual exclusion, fairnness for processes with similar execution time
    
    #   Not attractive when processes have different execution time 
    

# importing libraires
import threading

shared_value = 0   # Shared resource in the critical section of the two processes

turn = 0    # boolean variable to alternative turns between two involved processes

# a function applying strict alternation to process 1's turn
def P1():
    global shared_value, turn     # global variables shared_value and turn
    
    while True:             # infinite loop to check for turns
        while True:
            
            if turn == 0:        # checking if it is process one's turn using the global variable turn
                
                # Crtiical Section
                shared_value += 1        # increasing value just to show critical section altered
                print(f"Process 1 incremented shared_value: {shared_value}")
                
                # Crtiical section exit code , setting turn to be 1 for process 2
                turn = 1    
                break

# a function applying strict alternation to process 2's turn
def P2():
    global shared_value, turn     #globally shared variables
    while True:
        while True:
            if turn == 1:              # checking if it is process 2's turn using the global variable turn
                 # Crtiical Section
                shared_value += 1       # adding 1 to shared_value just to show that critical section has been altered
                print(f"Process 2 incremented shared_value: {shared_value}")
                turn = 0
                break


# Creating threads
p1 = threading.Thread(target=P1)    # p1 will execute P1 function 
p2 = threading.Thread(target=P2)    # p2 will execute P2 function

# Starting threads and their execution
p1.start()
p2.start()

