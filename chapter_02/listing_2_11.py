import asyncio
from asyncio import CancelledError
from util import delay


async def add_test_tasks_creation():
    tasks = [asyncio.create_task(delay(1 + 0.0001 * i) for i in range(10000))]

    while not any([task.done() for task in tasks]):
        await asyncio.sleep(1)


async def main():
    long_task = asyncio.create_task(delay(10))

    seconds_elapsed = 0

    while not long_task.done():
        print('Task not finished, checking again in a second.')
        await asyncio.sleep(1)
        seconds_elapsed = seconds_elapsed + 1
        if seconds_elapsed == 5:
            long_task.cancel()

    try:
        await long_task
    except CancelledError:
        print('Our task was cancelled')


asyncio.run(main())
asyncio.run(add_test_tasks_creation())
