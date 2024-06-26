import asyncio
import random
import threading


def some_cpu_bound_task():
    sum(i ** 2 for i in range(100000))


async def first_simple_task():
    print(threading.active_count())
    print('first_simple_task')
    await asyncio.sleep(1)


async def second_simple_task():
    print('second_simple_task')
    await asyncio.sleep(1)


async def start_async_processing() -> None:
    links = set()
    print(threading.active_count())

    async def run_process() -> None:
        await first_simple_task()
        some_cpu_bound_task()
        await second_simple_task()
        random_links = [random.randint(1, 100) for _ in range(10)]
        for link in random_links:
            if link not in links:
                links.add(link)
                await run_process()

    await run_process()


if __name__ == '__main__':
    print(threading.active_count())
    current_thread = threading.current_thread()
    print(current_thread.name)
    asyncio.run(start_async_processing())
