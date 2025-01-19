import multiprocessing


def say_hello(name: str) -> str:
    context = multiprocessing.get_context()
    return f'Hi there, {name}'


if __name__ == "__main__":
    with multiprocessing.Pool() as process_pool:  # A
        hi_jeff = process_pool.apply(say_hello, args=('Jeff',))  # B
        hi_john = process_pool.apply(say_hello, args=('John',))
        print(hi_jeff)
        print(hi_john)

    print(multiprocessing.get_context())
