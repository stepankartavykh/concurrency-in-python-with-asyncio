import random
import threading
import time
from threading import Thread

state = {}


def task(ident: int):
    while True:
        time.sleep(1)
        state[random.randint(1, 10)] = random.randint(1, 100)
        print(threading.current_thread().name, state)


if __name__ == '__main__':
    threads = [
        Thread(target=task, args=(1,)),
        Thread(target=task, args=(1,))
    ]
    for th in threads:
        th.start()
