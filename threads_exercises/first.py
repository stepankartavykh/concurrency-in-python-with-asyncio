from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Thread, current_thread
import time
import urllib.request


def print_thread_names(time_to_sleep: int) -> int:
    print("Current thread name:", current_thread().name)
    time.sleep(time_to_sleep)
    # int('qwe')
    value = time_to_sleep ** 10
    print(f'thread {current_thread().name} finished working')
    return value


def run_using_thread_pool_executor():
    with ThreadPoolExecutor() as executor:
        params = [i for i in range(7)]
        futures = [executor.submit(print_thread_names, param) for param in params]
        return_values = [future.result() for future in futures]
        return return_values


def simple_run():
    threads = []
    for i in range(7):
        thread = Thread(target=print_thread_names, args=(i,), name=f"{i}-program-thread")
        threads.append(thread)
        thread.run()

    for thread in threads:
        thread.join()


URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://nonexistant-subdomain.python.org/']


def load_url(url, timeout):
    with urllib.request.urlopen(url, timeout=timeout) as conn:
        return conn.read()


def loader():
    with ThreadPoolExecutor(max_workers=5) as executor:
        future_to_url = {executor.submit(load_url, url, 3): url for url in URLS}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%r generated an exception: %s' % (url, exc))
            else:
                print('%r page is %d bytes' % (url, len(data)))


if __name__ == '__main__':
    loader()