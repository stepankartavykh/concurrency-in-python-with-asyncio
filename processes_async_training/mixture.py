import os
import time
from multiprocessing import current_process, Pool, cpu_count
from threading import current_thread

import urllib.request


def make_request(num):
    pid = os.getpid()
    thread_name = current_thread().name
    process_name = current_process().name
    print(f"{pid} - {process_name} - {thread_name}")
    with urllib.request.urlopen("https://httpbin.org/ip", timeout=5) as conn:
        return conn.read()


async def make_request_async(num, client):
    pid = os.getpid()
    thread_name = current_thread().name
    process_name = current_process().name
    print(f"{pid} - {process_name} - {thread_name}")

    await client.get("https://httpbin.org/ip")


def get_prime_numbers(num):
    pid = os.getpid()
    thread_name = current_thread().name
    process_name = current_process().name
    print(f"{pid} - {process_name} - {thread_name}")

    numbers = []

    prime = [True for i in range(num + 1)]
    p = 2

    while p * p <= num:
        if prime[p]:
            for i in range(p * 2, num + 1, p):
                prime[i] = False
        p += 1

    prime[0] = False
    prime[1] = False

    for p in range(num + 1):
        if prime[p]:
            numbers.append(p)

    return numbers


def main():
    with Pool(cpu_count() - 1) as p:
        p.starmap(get_prime_numbers, zip(range(1000, 16000)))
        p.close()
        p.join()


if __name__ == "__main__":
    start_time = time.perf_counter()

    main()

    end_time = time.perf_counter()
    print(f"Elapsed run time: {end_time - start_time} seconds.")