import os
import time
import urllib.request
from concurrent.futures import ThreadPoolExecutor, wait, ProcessPoolExecutor
from threading import current_thread
from multiprocessing import current_process, cpu_count

from processes_async_training.mixture import get_prime_numbers


def make_request(num):
    pid = os.getpid()
    thread_name = current_thread().name
    process_name = current_process().name
    print(f"{pid} - {process_name} - {thread_name}")
    with urllib.request.urlopen("https://httpbin.org/ip", timeout=5) as conn:
        return conn.read()


def main_thread_executor():
    futures = []

    with ThreadPoolExecutor() as executor:
        for num in range(1, 101):
            futures.append(executor.submit(make_request, num))

    wait(futures)


def main_process_executor():
    futures = []

    with ProcessPoolExecutor(cpu_count() - 1) as executor:
        for num in range(1000, 16000):
            futures.append(executor.submit(get_prime_numbers, num))

    wait(futures)


if __name__ == "__main__":
    start_time = time.perf_counter()

    main_process_executor()

    end_time = time.perf_counter()
    print(f"Elapsed run time: {end_time - start_time} seconds.")