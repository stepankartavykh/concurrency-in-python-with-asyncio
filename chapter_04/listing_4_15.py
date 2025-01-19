import aiohttp
import asyncio
from aiohttp import ClientSession
from util import async_timed


async def fetch_status(session: ClientSession,
                       url: str,
                       delay: int = 0) -> int:
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status


async def main():
    async with aiohttp.ClientSession() as session:
        url = 'http://1gvp01.int.aorti.tech/goz-sg/distribution-plan-analysis?planVariantId=5001&startDate=2024-08-29&endDate=2024-09-05'
        fetchers = [asyncio.create_task(fetch_status(session, url)) for _ in range(100)]

        await asyncio.gather(*fetchers)


asyncio.run(main())
