import dis
from typing import Callable


def print_function_bytecode(function: Callable):
    print(dis.dis(function))


