import asyncio
from asyncio import AbstractEventLoop


async def first() -> None:
    current_loop: AbstractEventLoop = asyncio.get_running_loop()
    print(current_loop.time())
    print(id(current_loop))


async def second() -> None:
    print(asyncio.all_tasks())


async def main() -> None:
    await asyncio.gather(first(), second())

if __name__ == '__main__':
    asyncio.run(main())
