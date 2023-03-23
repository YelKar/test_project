import timeit
from ctypes import cdll


lib = cdll.LoadLibrary("./test.so")
print(timeit.timeit(lib.main, number=1))
