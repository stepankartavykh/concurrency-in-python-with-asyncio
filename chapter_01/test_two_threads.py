import threading
import time

collected_data = []


def data_collection_thread():
    global collected_data
    while True:
        data = input("Enter data (or 'exit' to quit): ")
        if data.lower() == 'exit':
            break
        collected_data.append(data)


def print_thread():
    global collected_data
    while True:
        print("Printing messages...")
        time.sleep(2)
        if collected_data:
            print("Collected data:", collected_data)
            collected_data = []


data_thread = threading.Thread(target=data_collection_thread)
print_thread = threading.Thread(target=print_thread)

data_thread.start()
data_thread.join()
print_thread.start()


print_thread.join()

print("Program finished.")
