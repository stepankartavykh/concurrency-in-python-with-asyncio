import threading
import time


stack = []


def input_data(n):
    global stack
    d = input()
    stack.append(d)
    time.sleep(n)


def print_to_console():
    global stack
    for _ in range(3):
        print('qwe')
        print(stack)
        time.sleep(3)


input_thread = threading.Thread(target=input_data, args=(1,))
monitoring_thread = threading.Thread(target=print_to_console)

threads = [input_thread, monitoring_thread]
[th.start() for th in threads]

