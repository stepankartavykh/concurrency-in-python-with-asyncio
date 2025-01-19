import os
import threading


def factorial_of_number(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result


def calculate_factorial(n):
    print(f"\nCalculating factorial of {n} in thread {threading.current_thread().name}")
    result = factorial_of_number(n)
    print(os.getpid())
    print(f"Factorial of {n} is {result} in thread {threading.current_thread().name}")


def calc():
    # Factorial of 12
    n = 50

    # Create threads for factorial calculation
    thread1 = threading.Thread(target=calculate_factorial, args=(n,))
    thread2 = threading.Thread(target=calculate_factorial, args=(n,))

    # Start the threads
    thread1.start()
    thread2.start()

    # Wait for the threads to complete
    thread1.join()
    thread2.join()


def main():
    print(factorial_of_number(1000))


if __name__ == '__main__':
    # main()
    calc()
