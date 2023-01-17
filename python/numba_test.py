import timeit
from numba import njit, prange


@njit(parallel=True)
def foo(c=int(1e9)):
    res = 0
    for i in prange(c):
        if i % 1e8 == 0:
            print(f"\x1b[33mpy => {i}\x1b[39m")
            res += i
    return res


@njit(parallel=True)
def foo(c=int(1e9)):
    res = 0
    for i in prange(c):
        if i % 1e8 == 0:
            print(f'\x1b[33mpy => {i}\x1b[39m')
            res += i
    return res


print(timeit.timeit(foo, number=1))
