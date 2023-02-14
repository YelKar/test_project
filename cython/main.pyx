from functools import cache

def fib(n: int):
    return int(n < 2) or fib(n - 1) + fib(n - 2)


def fib2(int n):
    return int(n < 2) or fib(n - 1) + fib(n - 2)


@cache
def cache_fib(int n):
    return int(n < 2) or cache_fib(n - 1) + cache_fib(n - 2)