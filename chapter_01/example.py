import time
import asyncio
import functools
from typing import Callable, Any


def async_timer():
    
    def wrapper(function: Callable) -> Callable:
        @functools.wraps(function)
        async def wrapped(*args, **kwargs) -> Any:
            start = time.perf_counter()
            try:
                return await function(*args, **kwargs)
            finally:
                end = time.perf_counter()
                print("procedure", function.__name__, "finished in", end - start, "seconds")
        return wrapped
        
    return wrapper 


async def print_after_delay(message: str, seconds: int):
    await asyncio.sleep(seconds)
    print(message)


@async_timer()
async def first_main():
    await asyncio.gather(
        print_after_delay("message 1", 1),
        print_after_delay("message 2", 2),
        print_after_delay("message 3", 3)
    )


@async_timer()
async def second_main():
    await print_after_delay("message 1", 1)
    await print_after_delay("message 2", 2)
    await print_after_delay("message 3", 3)


@async_timer()
async def third_main():
    
    task1 = asyncio.create_task(print_after_delay("message 1", 1))
    task2 = asyncio.create_task(print_after_delay("message 2", 2))
    task3 = asyncio.create_task(print_after_delay("message 3", 3))
    
    await task1
    await task2
    await task3


if __name__ == '__main__':
    asyncio.run(first_main())
    asyncio.run(second_main())
    asyncio.run(third_main())
