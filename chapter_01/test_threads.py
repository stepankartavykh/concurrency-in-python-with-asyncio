import threading
import time


def i_thread(i):
    print(f'{i}-thread:: Hello from i-th {threading.current_thread()}! with name {threading.current_thread().name}')
    for _ in range(3):
        print(f'{i}-thread:: wait in thread {i}...')
        print(f'{i}-thread:: active threads count = {threading.active_count()}')
        time.sleep(0.2)
        # threading.current_thread().join()


def main():
    print(f'Python is currently running {threading.active_count()} thread(s)')
    print(f'The current thread is {threading.current_thread().name}')
    first_thread = threading.Thread(target=i_thread, args=(1,))
    second_thread = threading.Thread(target=i_thread, args=(2,))

    all_threads = [first_thread, second_thread]
    [th.start() for th in all_threads]


if __name__ == '__main__':
    main()
    print('=' * 20, 'END', '=' * 20, f'active threads count = {threading.active_count()}')
