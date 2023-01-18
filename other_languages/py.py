from decimal import Decimal
from functools import cache
from c import load
from timeit import timeit


@cache
def fib_cache(n):
    return n <= 2 or fib_cache(n - 1) + fib_cache(n - 2)


def fib(n):
    return n <= 2 or fib(n - 1) + fib(n - 2)

c = load("c.c")
c.fib_cache = c.fib
c.fib_cache = cache(fib_cache)

funcs = {
    "C + cache": c.fib_cache,
    "Python + cache": fib_cache,
    "C": c.fib,
    "Python": fib,
}

num = 38

for name, foo in funcs.items():
    time_sum = 0
    times = []
    for _ in range(10):
        if time_sum < 20:
            curr = Decimal(timeit(lambda: foo(num), number=1))
            times.append(curr)
            time_sum += curr

    print(
        f"{name}:",
        *times,
        f"Среднее время выполнения: {time_sum / len(times)}",
        sep="\n\t"
    )



