import time
import tracemalloc
import matplotlib.pyplot as plt

def stack_operations(n):
    start_time = time.time()
    tracemalloc.start()
    
    stack = []
    for i in range(n):
        stack.append(i)
    while stack:
        stack.pop()
    
    memory_usage, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.time()
    
    return end_time - start_time, memory_usage

def queue_operations(n):
    start_time = time.time()
    tracemalloc.start()
    
    queue = []
    for i in range(n):
        queue.append(i)
    while queue:
        queue.pop(0)
    
    memory_usage, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.time()
    
    return end_time - start_time, memory_usage

def plot_complexity():
    sizes = [100, 1000, 5000, 10000]
    times_stack, memories_stack = [], []
    times_queue, memories_queue = [], []
    
    for size in sizes:
        t, m = stack_operations(size)
        times_stack.append(t)
        memories_stack.append(m)
        
        t, m = queue_operations(size)
        times_queue.append(t)
        memories_queue.append(m)
    
    plt.figure(figsize=(14, 7))
    
    plt.subplot(2, 2, 1)
    plt.plot(sizes, times_stack, label='Stack Operations', marker='o')
    plt.plot(sizes, times_queue, label='Queue Operations', marker='o')
    plt.title('Time Complexity')
    plt.xlabel('Input Size')
    plt.ylabel('Time (s)')
    plt.legend()
    
    plt.subplot(2, 2, 2)
    plt.plot(sizes, memories_stack, label='Stack Operations', marker='o')
    plt.plot(sizes, memories_queue, label='Queue Operations', marker='o')
    plt.title('Space Complexity')
    plt.xlabel('Input Size')
    plt.ylabel('Memory (Bytes)')
    plt.legend()
    
    plt.show()

if __name__ == "__main__":
    plot_complexity()
