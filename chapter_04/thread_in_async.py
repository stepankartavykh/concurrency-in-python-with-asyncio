import asyncio
import threading


async def first():
    print(threading.current_thread())
    await asyncio.sleep(1)


async def second():
    print(threading.current_thread())
    await asyncio.sleep(3)


async def main():
    t1 = asyncio.create_task(first())
    t2 = asyncio.create_task(second())
    await t1
    await t2


if __name__ == '__main__':
    asyncio.run(main())
