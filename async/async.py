import asyncio
import time
import threading
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import multiprocessing
import os

# ---------------------------------------------
# 1. Basic async with asyncio
# ---------------------------------------------
async def say_hello_async():
    print("Start async hello")
    await asyncio.sleep(1)
    print("End async hello")

# ---------------------------------------------
# 2. Running multiple async tasks
# ---------------------------------------------
async def run_multiple_async():
    await asyncio.gather(say_hello_async(), say_hello_async())

# ---------------------------------------------
# 3. Async with I/O simulation
# ---------------------------------------------
async def simulate_io(task_id):
    print(f"Task {task_id} starting I/O")
    await asyncio.sleep(2)
    print(f"Task {task_id} completed I/O")

async def run_io_tasks():
    tasks = [simulate_io(i) for i in range(5)]
    await asyncio.gather(*tasks)

# ---------------------------------------------
# 4. Threading example
# ---------------------------------------------
def thread_task(name):
    print(f"Thread {name} starting")
    time.sleep(2)
    print(f"Thread {name} done")

def run_threading():
    threads = [threading.Thread(target=thread_task, args=(i,)) for i in range(3)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

# ---------------------------------------------
# 5. Using ThreadPoolExecutor
# ---------------------------------------------
def blocking_io(task_id):
    print(f"Blocking I/O {task_id} started")
    time.sleep(2)
    print(f"Blocking I/O {task_id} finished")

def run_thread_pool():
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(blocking_io, range(5))

# ---------------------------------------------
# 6. Using ProcessPoolExecutor (multi-core)
# ---------------------------------------------
def cpu_bound_task(n):
    print(f"CPU task {n} starting on PID {os.getpid()}")
    count = 0
    for i in range(10**8):
        count += i * i // (i + 1)
    print(f"CPU task {n} done")
    return count

def run_process_pool():
    print("CPU cores available:", os.cpu_count())
    print("Logical CPU cores:", multiprocessing.cpu_count())
    with ProcessPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(cpu_bound_task, range(4)))
    print("CPU-bound results:", results)

# ---------------------------------------------
# 7. Entry point to run all
# ---------------------------------------------
if __name__ == "__main__":
    # print("--- Async Hello ---")
    # asyncio.run(say_hello_async())

    # print("\n--- Multiple Async Tasks ---")
    # asyncio.run(run_multiple_async())

    # print("\n--- Async I/O Tasks ---")
    # asyncio.run(run_io_tasks())

    # print("\n--- Threading ---")
    # run_threading()

    # print("\n--- ThreadPoolExecutor ---")
    # run_thread_pool()

    print("\n--- ProcessPoolExecutor ---")
    run_process_pool()
