"""
5_1: 233024691 time=2580
5_2: 233024691 time=52s
5_3: 233024691 time=?
"""
import timeit
from numba import prange, njit


def task5():
    task5_3()
    # print(f"time(task5_2) => {timeit.timeit(task5_2, number=1)}s")
    # print(f"time(task5_1) => {timeit.timeit(task5_1, number=1)}s")


def task5_1():
    start, stop = 123456789, 1987654321
    count = 0
    n = 15_000_000

    while (res := r(n)) <= stop:
        n += 1
        count += res >= start
        if n % 1_000_000 == 0:
            print("N=%d\tR=%d" % (n, res))

    print("\nN=%d => R=%d\nresult=%d" % (n, r(n), count))


def r(n: int):
    n = (n * 2) + is_odd(n)
    n = (n * 2) + is_odd(n)
    n = (n * 2) + is_odd(n)
    return n


def is_odd(n: int):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s % 2


def task5_2():
    from ctypes import cdll
    lib_name = "stadgrad_01.03.2023"

    # import os
    # os.system(f"gcc -shared -o {lib_name}.so -fPIC {lib_name}.c")

    lib = cdll.LoadLibrary(f"./{lib_name}.so")
    lib.task5()


@njit(parallel=True)
def task5_3():
    start, stop = 123_456_789, 1987654321
    count = 0
    for n in prange(15_000_000, 2_000_000_000):
        if n % 100_000_000 == 0:
            print(n, count)
        for i in range(3):
            a = n
            s = 0
            while a:
                s += a % 10
                a //= 10
            s %= 2
            n = (n * 2) + s

        count += stop >= n >= start

    print(f"result={count}")






task5()
