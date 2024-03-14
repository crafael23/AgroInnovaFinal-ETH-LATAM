import threading
import time
import random

# Define the size of the virtual memory and the page size
VIRTUAL_MEMORY_SIZE = 100
PAGE_SIZE = 10

# Define the number of processes to simulate
NUM_PROCESSES = 4

# Define a list to hold the page tables for each process
page_tables = [[] for _ in range(NUM_PROCESSES)]

# Define a lock to synchronize access to the page tables
lock = threading.Lock()


# Define a function to simulate a process
def process(pid):
    # Generate a random number of pages for the process
    num_pages = random.randint(1, 10)
    print(f"Process {pid} has {num_pages} pages")

    # Allocate pages for the process
    for i in range(num_pages):
        # Generate a random page number
        page_num = random.randint(0, VIRTUAL_MEMORY_SIZE // PAGE_SIZE - 1)

        # Acquire the lock to access the page table
        lock.acquire()

        # Check if the page is already allocated
        if page_num in page_tables[pid]:
            print(f"Process {pid} already has page {page_num}")
        else:
            # Allocate the page
            page_tables[pid].append(page_num)
            print(f"Process {pid} allocated page {page_num}")

        # Release the lock
        lock.release()

        # Sleep for a random amount of time to simulate processing
        time.sleep(random.uniform(0.1, 1.0))


# Create threads for each process
threads = []
for i in range(NUM_PROCESSES):
    t = threading.Thread(target=process, args=(i,))
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()
