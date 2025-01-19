import random
import threading


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)


def merge(left, right):
    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    while i < len(left):
        merged.append(left[i])
        i += 1

    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged


def multi_threaded_merge_sort(arr, num_threads):
    if num_threads <= 1:
        return merge_sort(arr)
    size = len(arr) // num_threads
    sublists = [arr[i:i + size] for i in range(0, len(arr), size)]
    threads = []
    sorted_sublists = []
    for sublist in sublists:
        thread = threading.Thread(target=lambda sublist: sorted_sublists.append(merge_sort(sublist)), args=(sublist,))
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()
    merged = sorted_sublists[0]
    for sublist in sorted_sublists[1:]:
        merged = merge(merged, sublist)
    return merged


def multi_threaded_sort(numbers):
    num_threads = 2
    # print("Original List:", numbers)
    sorted_list = multi_threaded_merge_sort(numbers, num_threads)
    # print("Sorted list:", sorted_list)


def ordinary_sort(numbers):
    sorted(numbers)


input_list = [random.randint(1, 10000) for _ in range(10 ** 1)]


if __name__ == '__main__':
    # multi_threaded_sort(input_list)
    # ordinary_sort(input_list)
    import timeit

    print(timeit.timeit("multi_threaded_sort(input_list)", setup="from __main__ import multi_threaded_sort, input_list"))
