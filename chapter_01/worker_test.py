import threading
import time

done = False


def worker():
    count = 0
    while not done:
        count += 1
        print(count)
        time.sleep(1)


th = threading.Thread(target=worker, daemon=True)
th.start()

input('Press Enter')
done = True
