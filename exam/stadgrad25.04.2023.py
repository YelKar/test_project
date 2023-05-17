import math
import re
from itertools import product
from string import digits


def task2_n():  # yzxw
    """yzxw"""

    def f1():
        return int((x or not y) <= (w == z))

    def f2():
        return int((x or not y) == (z <= w))

    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    arr = (y, z, x, w, f1(), f2())
                    if (
                            (arr.count(0) >= 5 or
                             (not arr[-2]) and arr.count(0) >= 1 and arr.count(1) >= 2) and arr[1]
                            or sum(arr[:4]) <= 1 and not arr[-1] and not arr[1]
                    ):
                        print(*arr)


def task5_p():  # 432098
    def append(n_: int, i_: int):
        if n_ % i_ == 0:
            return (n_ << 3) + i_
        return (n_ << 1) + 1

    def r(n_: int):
        n_ = append(n_, 5)
        n_ = append(n_, 7)
        return n_

    for n in range(1000000, -1, -1):
        if r(n) < 1_728_404:
            return f"{n = } | {r(n) = }"


def task6_n():
    """400 ** 0.5 - 3 = 17"""
    from turtle import Turtle, exitonclick, tracer

    tracer(10)

    t = Turtle()
    t.lt(90)
    a = int(400 ** 0.5 - 3)

    size = 20
    for _ in range(5):
        t.forward(a * size)
        t.right(90)
        t.forward(3 * size)

    t.penup()
    for x in range(a + 3 + 1):
        for y in range(-3, a + 1):
            t.goto(x * size, y * size)
            t.dot(3)
    exitonclick()


def task7_p():
    img = 640 * 480
    clr = 16
    img_s = 12
    img2 = 1280 * 960
    clr2 = 24

    size = img * clr
    size2 = img2 * clr2

    speed = size * img_s
    speed2 = speed * 2
    return speed2 / size2


def task8_p():
    from itertools import permutations

    i = 266
    return "".join(list(permutations(sorted("ВИКТОР")))[i - 1])


def task11_p():
    alpha = 10 + 26
    ln = 13
    code = math.ceil(len(f"{alpha:b}") * ln / 8)

    all_obj_size = 2 * 2 ** 20
    obj = 16384
    size = all_obj_size / obj

    els = len(f"{500:b}") * 60
    desc = math.ceil(els / 8)

    return size - code - desc


def task14_p():
    from string import ascii_uppercase as upper, digits

    let = digits + upper

    for p in range(5, 37):
        for x in let[:p]:
            for y in let[:p]:
                if int("12", p) * int("34", p) == int(f"{x}{y}2", p):
                    return int(f"{y}{x}", p)


def task16_p():
    def f(n_: int):
        return n_ * (n_ > 1e6) or n_ + f(2 * n_)

    def g(n_: int):
        return f(n_) / n_

    a = g(1000)
    c = 0
    for i in range(1, 10000):
        c += g(i) == a
    return c


def task17_p():
    with open("files/stadgrad_25.04.2023/17.txt") as f:
        *nums, = map(int, f)

    mn = min(filter(lambda x_: 100 <= x_ < 1000 and x_ % 10 == 5, nums))

    def four_sign(x_):
        return 10 ** 3 <= x_ < 10 ** 4

    def any_n_all(*els):
        return any(els) and not all(els)

    c = 0
    mx = 0
    for x, y in zip(nums, nums[1:]):
        if (x ** 2 + y ** 2) % mn == 0 and any_n_all(*map(four_sign, (x, y))):
            c += 1
            mx = max(mx, x ** 2 + y ** 2)
    return f"{c} {mx}"


def task23_p():
    def f(a: int, b: int):
        return a <= b != 11 and b != 15 and \
               (
                       a == b or
                       f(a, b - 1) + f(a, b - 3)
                       + (b % 2 == 0) * f(a, b // 2)
               )

    return f(2, 8) * f(8, 20)


def task25():
    """

    :return:
    """
    mask = re.compile(r"1\d7602\d*0")

    for i in range(10):
        for j in product("0123456789", repeat=5):
            print(''.join(j))
            n = f"1{i}7602{''.join(j)}0"
            if int(n) > 10**10:
                break
            if mask.fullmatch(n) and int(n) % 4891 == 0:
                print(n)


def task26_p():
    with open("files/stadgrad_25.04.2023/26.txt") as f:
        _, *lines = f.readlines()
        *cars, = sorted(
            map(
                lambda x: (int(x[0]), int(x[1]), str(x[2])),
                map(lambda x: x.split(), lines)
            )
        )

    a: list[int] = []
    b: list[int] = []

    a_count = 0
    skip = 0
    for start, dur, c_type in cars:
        t = start + dur
        *a, = filter(lambda x: x > start, a)
        *b, = filter(lambda x: x > start, b)
        if c_type == "A" and len(a) < 80:
            a.append(t)
            a_count += 1
        elif len(b) < 20:
            b.append(t)
            a_count += c_type == "A"
        else:
            skip += 1

    return f"{a_count=} {skip=}"


def _task27():
    with open("files/stadgrad_25.04.2023/27-A.txt") as f:
        _, *nums = map(int, f)

    mtx = [[0] * 9 for _ in range(9)]

    for i, n in enumerate(nums):
        mtx[i % 9][n % 9] += 1

    space = 3

    print(end="  ")
    for i in range(9):
        print(f"{i:_>{space}}", end="")
    print()

    for i, row in enumerate(mtx):
        print(i, end="|")
        for num in row:
            print(f"{num:>{space}}", end="")
        print()

    res = 0
    used = set()

    for comb in product(range(9), repeat=4):
        i1, j1, i2, j2 = comb
        if (i1 + i2) % 9 == abs(j1 - j2) and comb not in used:
            res += mtx[j1][i1] * mtx[j2][i2]
            used.add((*comb[2:], *comb[:2]))
    print(res, res % 10 ** 6)


for k, v in filter(lambda x: x[0].startswith("task"), dict(globals()).items()):
    print(k, end=": ")
    if k.endswith("_p"):
        print(v())
    elif k.endswith("_n"):
        print(v.__doc__)
    else:
        print()
        v()
