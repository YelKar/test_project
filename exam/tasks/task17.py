from itertools import pairwise


def stad():
    with open("files/17_stad.txt") as f:
        nums = list(map(int, f))

    rt_mn = min(filter(lambda x_: abs(x_) % 10 == 3, nums)) ** 2

    c = 0
    mx = 0

    for x, y in pairwise(nums):
        if (
            abs(x) % 10 == abs(y) % 10 and
            (x % 3 == 0 or y % 3 == 0) and x % 3 != y % 3 and
            (s_rt := x ** 2 + y ** 2) <= rt_mn
        ):
            c += 1
            mx = max(mx, s_rt)

    print(c, mx)


stad()
