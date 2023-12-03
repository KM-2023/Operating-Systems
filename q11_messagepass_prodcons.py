# The following is a code utilizing Message-Passing for the Producer-Consumer Problem:
import threading
import queue
import time

# Shared resource (queue)
buffer_size = 5
shared_buffer = queue.Queue(buffer_size)  # Message passing is implemented in the queue.Queue
# which enables them to communicate by passing messages (data items in this case)

# Function for the Producer
def producer():
    while True:
        data = f"Item-{time.time()}"  # Generates a data item with a unique timestamp as message content
        shared_buffer.put(data)  # Producer adds data to buffer
        print(f"Produced {data}.")  # Print the data that the producer produced
        time.sleep(1)  # Introduce a delay after completion to ensure appropriate synchronization
# Function for the Consumer
def consumer():
    while True:
        data = shared_buffer.get()  # Consume the data produced by the producer
        print(f"Consumed {data}.")  # Print the consumed data
        time.sleep(1)   # Introduce a delay after completion to ensure appropriate synchronization

# Creating threads for producer and consumer
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

# Starting threads
producer_thread.start()
consumer_thread.start()
