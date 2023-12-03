# The following code represents an implementation for the Producer-Consumer Problem

import threading
import queue
import time

# Shared resource (queue)
BUFFER_SIZE = 5 # The size of our buffer
buffer = queue.Queue(BUFFER_SIZE)

# Locks and conditions for synchronization
lock = threading.Lock()  # Lock here is used for the synchronization between the producer and consumer
not_empty = threading.Condition(lock)  # Concerns the consumer
not_full = threading.Condition(lock)   # Concerns the producer


# Function for the producer
def producer():
    global buffer
    while True:
        not_full.acquire()  # It will keep acquiring to fill the buffer
        while buffer.full():  # It will stop adding items when the buffer is full
            print("Buffer is full. Producer is waiting.")
            not_full.wait()  # Wait until the consumer consumes items

        # Produce an item and add it to the buffer
        item = f"Item-{time.time()}"  # generates a timestamp representing the current time in seconds
        buffer.put(item)  # The producer will add an item to the buffer until it is full
        print(f"Produced {item}.")
        not_empty.notify()  # Notify consumer that buffer is not empty
        not_full.release()  # It will release the condition that it is not full since it completed adding items
        time.sleep(1)  # Producer sleeps for 1 second

# Function for the Consumer
def consumer():
    global buffer
    while True:
        not_empty.acquire()  # It will keep consuming till it empties the buffer
        while buffer.empty():  # It will keep consuming items until the buffer is empty
            print("Buffer is empty. Consumer is waiting.")
            not_empty.wait()  # Wait until the buffer is not empty

        # Consume an item from the buffer
        item = buffer.get()
        print(f"Consumed {item}.")
        not_full.notify()  # Notify producer that buffer is not full
        not_empty.release()  # It will release the condition that it is not empty since it completed consuming items
        time.sleep(1)  # Consumer sleeps for 1 second

# Creating threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Starting threads
producer_thread.start()
consumer_thread.start()

