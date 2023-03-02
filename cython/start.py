import timeit
from functools import cache
from threading import Thread, enumerate as enum, Event
from typing import Callable
from inspect import signature

import main


n = 40

print(main.cfib(n))
print(main.fib(n))
# main.main()

#
#
# def fib(n: int):
#     return int(n < 2) or fib(n - 1) + fib(n - 2)
#
#
# @cache
# def cache_fib(n: int):
#     return int(n < 2) or cache_fib(n - 1) + cache_fib(n - 2)
#
#
# num = 350
#
#
# funcs = {
#     # "Python": fib,
#     # "Cython": main.fib,
#     # "Cython2": main.fib2,
#     "Cython + cache": main.cache_fib,
#     "Python + cache": cache_fib,
# }
#
#
# def time_all(functions: dict[str, Callable], *args, number: int = 1):
#     threads: list[Thread] = []
#     start = Event()
#     for name, f in functions.items():
#         threads.append(Thread(target=time_one(f, name, number=number, until=start), args=args))
#
#     for thread in threads:
#         thread.start()
#     print(enum())
#     start.set()
#
#
# def time_one(
#         func: Callable,
#         name: str | None = None,
#         number: int = 1,
#         until: Event | None = None
# ):
#     res = None
#
#     def d(*args):
#         if until is not None:
#             until.wait()
#
#         def call():
#             nonlocal res
#             res = func(*args)
#             return res
#         ans = timeit.timeit(call, number=number) / number
#         try:
#             sign = signature(func)
#         except ValueError:
#             sign = ()
#         print(f"{name or func.__name__}{sign} => {args} => {res} | {ans}")
#
#     return d
#
#
# time_all(funcs, num, number=40)
