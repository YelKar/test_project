from typing import Iterable


def pairwise(it: Iterable):
    it = list(it)
    return zip(it, it[1:])


def stad():
    with open("files/17_stad.txt", "r", encoding="utf-8") as f:
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


stad()
