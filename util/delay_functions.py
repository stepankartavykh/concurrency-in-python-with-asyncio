import asyncio


async def delay(delay_seconds: float, task_identifier: str = None) -> float:
    if task_identifier:
        print(f'{task_identifier} sleeping for {delay_seconds} second(s)')
    else:
        print(f'sleeping for {delay_seconds} second(s)')
    await asyncio.sleep(delay_seconds)
    if task_identifier:
        print(f'{task_identifier} finished sleeping for {delay_seconds} second(s)')
    else:
        print(f'finished sleeping for {delay_seconds} second(s)')
    return delay_seconds
