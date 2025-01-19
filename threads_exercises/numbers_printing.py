import sys
import threading
import time


def inner_task():
    print(f'inner task of thread {threading.current_thread().name}')
    time.sleep(4)


def print_even_numbers():
    print("List of even numbers:")
    for i in range(30, 51, 2):
        print(i, end=" ")
    new_threads = []
    for _ in range(50):
        new_threads.append(threading.Thread(target=inner_task))
        new_threads[-1].start()
        new_threads[-1].join()


def print_odd_numbers():
    sys.exit(1)
    print("\nList of odd numbers:")
    for i in range(31, 51, 2):
        print(i, end=" ")
    time.sleep(5)


print(threading.enumerate())
even_thread = threading.Thread(target=print_even_numbers)
odd_thread = threading.Thread(target=print_odd_numbers)
even_thread.start()
odd_thread.start()
even_thread.join()
odd_thread.join()
print(threading.enumerate())
