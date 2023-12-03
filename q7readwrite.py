
  #  This program is Semaphores implementation for Reader-Writer Problem  

import threading
import time

# resources that are shared
shared_data = ["Hello"]    
readers_count = 0      # number of concurent readers in critical section
readers_count_lock = threading.Lock()   # lock variable that protects readers_count
data_lock = threading.Lock()    # lock variable that protects the data accessed by writers and readers
write_lock = threading.Semaphore(1)    # sempahor python implementation, here we have s = 1 thus, we have a binary semaphor upto two writers can access it but only one at a time

# function that simualates reader
def reader(reader_id):
    global readers_count      # readers_count global variable
    
    # critical section entry code: reader is entering into the critical section
    with readers_count_lock:   # lock variable to access reader's count 
        readers_count += 1     # increasing the number of readers
        
        # this block acquires the write_lock , that is writer cannot write to the shared data when the first reader enters
        # in other words no writer can write when there is a readers in the critical section
        if readers_count == 1:
            write_lock.acquire()  # First reader acquires write lock
            

    print(f"Reader {reader_id} is reading data: {shared_data}")    # displaying data read by a reader

    # critical section exit code: reader is exisitng the critical section
    with readers_count_lock:
        readers_count -= 1
        if readers_count == 0:
            write_lock.release()     # Last reader releases write lock, which means writers can write as there is no lock (restriction) on the critical section

# function that simualates reader
def writer(writer_id):
    global shared_data
    # critical section entry code: the write_lock is to ensure that only one writer writes to the critical section locking(prevening) all other writers
    with write_lock:
        data_lock.acquire()  # Acquire data lock for writing (locking it)
        
        # Simulating data update
        shared_data.append(writer_id)
        print(f"Writer {writer_id} is writing data: {shared_data}")  # a text to show case that a writer is in the critical section
        
    # critical section exit code
        data_lock.release()  # Release data lock after writing

# Creating threads for readers and writers
reader_processes = []     
writer_processes = []

# 5 iterations to create thread for 5 readers, and invoke the reader classs
for i in range(5):
    reader_processes.append(threading.Thread(target=reader, args=(i,)))
    
# 2 iterations to create thread for 2 writers, and invoke the writer class (that's why binary semaphor was used above)
for i in range(2):
    writer_processes.append(threading.Thread(target=writer, args=(i,)))

# Starting threads
for thread in reader_processes + writer_processes:
    thread.start()

# Waiting for all threads to complete
for thread in reader_processes + writer_processes:
    thread.join()
