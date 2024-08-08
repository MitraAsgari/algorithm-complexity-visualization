import time
import tracemalloc
import matplotlib.pyplot as plt

def linear_search(arr, target):
    start_time = time.time()
    tracemalloc.start()
    
    for i in range(len(arr)):
        if arr[i] == target:
            break
    
    memory_usage, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.time()
    
    return end_time - start_time, memory_usage

def binary_search(arr, target):
    start_time = time.time()
    tracemalloc.start()
    
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            break
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    memory_usage, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.time()
    
    return end_time - start_time, memory_usage

def plot_complexity():
    sizes = [100, 1000, 5000, 10000]
    times_linear, memories_linear = [], []
    times_binary, memories_binary = [], []
    
    for size in sizes:
        arr = list(range(size))
        target = size - 1
        
        t, m = linear_search(arr.copy(), target)
        times_linear.append(t)
        memories_linear.append(m)
        
        t, m = binary_search(arr.copy(), target)
        times_binary.append(t)
        memories_binary.append(m)
    
    plt.figure(figsize=(14, 7))
    
    plt.subplot(2, 2, 1)
    plt.plot(sizes, times_linear, label='Linear Search', marker='o')
    plt.plot(sizes, times_binary, label='Binary Search', marker='o')
    plt.title('Time Complexity')
    plt.xlabel('Input Size')
    plt.ylabel('Time (s)')
    plt.legend()
    
    plt.subplot(2, 2, 2)
    plt.plot(sizes, memories_linear, label='Linear Search', marker='o')
    plt.plot(sizes, memories_binary, label='Binary Search', marker='o')
    plt.title('Space Complexity')
    plt.xlabel('Input Size')
    plt.ylabel('Memory (Bytes)')
    plt.legend()
    
    plt.show()

if __name__ == "__main__":
    plot_complexity()
