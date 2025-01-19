import time
import asyncio
import concurrent.futures


def work(latency):
    time.sleep(latency)


def sequential(latency, units_count):
    for _ in range(units_count):
        work(latency)


def run_async_io(latency, units_count):
    asyncio.run(async_io_tasks(latency, units_count))


async def async_work(latency):
    await asyncio.sleep(latency)


async def async_io_tasks(latency, units_count):
    tasks = [asyncio.create_task(async_work(latency)) for _ in range(units_count)]
    await asyncio.gather(*tasks)


def run_threads(latency, units_count):
    with concurrent.futures.ThreadPoolExecutor(max_workers=units_count) as executor:
        executor.map(work, [latency] * units_count)


def run_processes(latency, units_count):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        executor.map(work, [latency] * units_count)


if __name__ == '__main__':
    testCases = [(0.1, i) for i in range(1000, 2001, 200)]
    variants = [run_threads, run_async_io]

    for i, t in enumerate(testCases):
        case_latency, execution_units_count = t
        print(f"Parallelism\: {execution_units_count}")

        for j, variant in enumerate(variants):
            start = time.perf_counter()

            variant(case_latency, execution_units_count)

            end = time.perf_counter()
        print()
