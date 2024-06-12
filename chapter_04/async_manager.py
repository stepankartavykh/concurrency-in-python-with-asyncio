import asyncio


class AsyncManager:
    def __init__(self, param):
        self.param = param

    async def __aenter__(self):
        print('start __aenter__')

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print('exit')


async def main():
    async with AsyncManager('test') as async_manager:
        await asyncio.sleep(1)
        int('qwe')
        print('test')


if __name__ == '__main__':
    asyncio.run(main())
