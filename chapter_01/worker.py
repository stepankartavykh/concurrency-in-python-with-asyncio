import threading, time


class Worker(threading.Thread):

    def __init__(self, num_thread):
        super().__init__()
        self.num_thread = num_thread

    def run(self):
        print(f'Старт потока №{self.num_thread}')
        time.sleep(1)
        print(f'Завершение работы потока №{self.num_thread}')


for i in range(2):
    th = Worker(i)
    th.start()
    print(th.is_alive())


print(threading.enumerate())