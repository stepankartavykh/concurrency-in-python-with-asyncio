import time
from multiprocessing import Pool


def say_hello(name: str, sleep_seconds: int) -> str:
    time.sleep(sleep_seconds)
    return f'Hi there, {name}'


if __name__ == "__main__":
    start = time.perf_counter()
    with Pool() as process_pool:
        hi_jeff = process_pool.apply_async(say_hello, args=('Jeff', 5))
        hi_john = process_pool.apply_async(say_hello, args=('John', 1))
        print(hi_jeff.get())
        print(hi_john.get())
    end = time.perf_counter()

    print(end - start)
