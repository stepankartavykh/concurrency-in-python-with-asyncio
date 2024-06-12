import threading
from threading import Thread, Event
from time import sleep, time


event = Event()


def modify_variable(var):
    print(threading.enumerate())
    while True:
        for i in range(len(var)):
            var[i] += 1
        if event.is_set():
            break
        # sleep(.5)
    print('Stop printing')


my_var = [1, 2, 3]
t = Thread(target=modify_variable, args=(my_var, ))
print(threading.enumerate())
t.start()
print(threading.enumerate())
t0 = time()
while time() - t0 < 5:
    print(my_var)
    sleep(1)
event.set()
t.join()
print(my_var)
