import asyncio
import threading
from asyncio import Lock
from util import delay


async def a():
    print('Coroutine a waiting to acquire the lock')
    async with lock:
        print('Coroutine a is in the critical section')
        await delay(2, "-a- CORO:")
    print('Coroutine a released the lock')


async def b():
    print('Coroutine b waiting to acquire the lock')
    async with lock:
        print('Coroutine b is in the critical section')
        await delay(2, "-b- CORO:")
    print('Coroutine b released the lock')


lock = Lock()
policy = asyncio.get_event_loop_policy()
print(policy)


async def main():
    await asyncio.gather(a(), b())


if __name__ == '__main__':
    asyncio.run(main())
