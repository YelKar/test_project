from numba import njit, prange
from colorama import Fore


@njit(fastmath=True, parallel=True)
def foo():
    for i in prange(int(1e10)):
        if i % 1e9 == 0:
            print(f"\x1b[33mpy => {i}\x1b[39m")


foo()
