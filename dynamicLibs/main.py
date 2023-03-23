from functools import cache

import module


@cache
def fib(n: int):
    return n <= 2 or fib(n - 1) + fib(n - 2)


num = 93
print(2 ** 64)
print(fib(num))
print(module.fibonacci(num))
