import os
import time
import multiprocessing
from multiprocessing import Process


def count(count_to: int) -> int:
    print(os.getpid())
    start = time.time()
    counter = 0
    while counter < count_to:
        counter = counter + 1
    end = time.time()
    print(f'Finished counting to {count_to} in {end-start}')
    return counter


if __name__ == "__main__":
    print(multiprocessing.cpu_count())
    start_time = time.time()

    first_process = Process(target=count, args=(50000000,))
    second_process = Process(target=count, args=(2000000,))
    third_process = Process(target=count, args=(2000000,))

    first_process.start()
    print('1')
    second_process.start()
    print('2')
    third_process.start()

    first_process.join()
    second_process.join()
    third_process.join()

    end_time = time.time()
    print(f'Completed in {end_time-start_time}')
