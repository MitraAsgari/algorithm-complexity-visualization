import time
import tracemalloc
import matplotlib.pyplot as plt

def bubble_sort(arr):
    start_time = time.time()
    tracemalloc.start()
    
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    memory_usage, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.time()
    
    return end_time - start_time, memory_usage

# استفاده از داده‌های نمونه و رسم نمودار
def plot_complexity():
    sizes = [100, 1000, 5000, 10000]
    times = []
    memories = []
    
    for size in sizes:
        arr = list(range(size, 0, -1))
        t, m = bubble_sort(arr)
        times.append(t)
        memories.append(m)
    
    plt.figure(figsize=(10, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(sizes, times, marker='o')
    plt.title('Time Complexity')
    plt.xlabel('Input Size')
    plt.ylabel('Time (s)')
    
    plt.subplot(1, 2, 2)
    plt.plot(sizes, memories, marker='o')
    plt.title('Space Complexity')
    plt.xlabel('Input Size')
    plt.ylabel('Memory (Bytes)')

    plt.tight_layout()
    plt.show()

plot_complexity()
