from math import inf
from typing import Iterable


def pairwise(it: Iterable):
    it = list(it)
    return zip(it, it[1:])


def stad():
    with open("../files/17_stad.txt", "r", encoding="utf-8") as f:
        nums = list(map(int, f))

    mn = min(filter(lambda _x: abs(_x) % 10 == 3, nums))
    rt_mn = mn ** 2
    print(mn)
    print(rt_mn)
    c = 0
    mx = 0
    for x, y in pairwise(nums):
        s_rt = x ** 2 + y ** 2
        if x % 10 == y % 10 and \
                (x % 3 == 0 or y % 3 == 0) and x % 3 != y % 3 and \
                rt_mn >= s_rt:
            c += 1
            mx = max(mx, s_rt)
    print(c, mx)


def task55813():
    with open("../files/17_55813.txt") as f:
        *nums, = map(int, f)

    def len3(n: int):
        return 100 <= n < 1000

    mn = min(filter(lambda i: len3(i) and i % 10 == 5, nums))

    mn_sm = inf
    c = 0
    for x in zip(nums, nums[1:]):
        *ln, = map(len3, x)
        if any(ln) and not all(ln) and sum(x) % mn == 0:
            c += 1
            mn_sm = min(mn_sm, sum(x))
    print(c, mn_sm)


task55813()
