import sys
import threading
import time


def worker(number):
    n = number + 1
    print(f'Запуск потока №{n}')
    time.sleep(2)
    print(f'Поток №{n} выполнился.')


thread = threading.Thread(target=worker, args=(11,))
thread.start()
print(threading.enumerate())
print('Потоки запущены, основной поток программы так же выполняется')
for _ in range(10):
    print('time between launching ...')
    time.sleep(1)

main_thread = threading.main_thread()

for t in threading.enumerate():
    if t is main_thread:
        continue
    print(f'Ожидание выполнения потока {t.name}')
    t.join()

print('Основной поток программы после ожидания продолжает работу')
