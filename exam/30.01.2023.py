import math
import re
from collections import Counter
from itertools import pairwise
from turtle import Turtle, exitonclick


def task7():
    f = 4
    size = 12
    print(size / f * 2 / 1.5)


def task11():
    char = 7
    users = 100
    size = 2400

    pwd_size = math.ceil(len(bin(char)[2:]) * 25 / 8)
    pwds_size = pwd_size * users
    print((size - pwds_size) / users)


def task12():
    s = "1" * 80
    while "11111" in s:
        s = s.replace("111", "2", 1).replace("222", "1", 1)
    print(s)


def task15():
    f = lambda a, x, y: (y + 2 * x != 48) or (a < x) or (a < y)
    for a in range(1000, -1, -1):
        flag = False
        for x in range(100):
            for y in range(100):
                if not f(a, x, y):
                    flag = True
                    break
        if not flag:
            print(a)
            break


def task16():
    print(_task16(30))


def _task16(n: int):
    return n < 2 or _task16(n - 1) + n


def task5():
    for i in range(10000):
        if _task5(i) == "1215":
            print(i)
            break


def _task5(n: int):
    res_list = sorted(map(lambda x: int(x[0]) + int(x[1]), pairwise(str(n))))[1:]
    return "".join(map(str, res_list))


def task6():
    t = Turtle()
    t.speed(0)
    size = 35
    up = 200
    t.up()
    t.goto(0, up)
    t.down()

    t.lt(90)

    for i in range(14):
        t.rt(60)
        t.fd(2 * size)
        t.rt(60)
        t.fd(2 * size)
        t.rt(270)
    t.up()

    for x in range(-6, 11):
        for y in range(-1, 16):
            t.goto(x * size, -y * size + up)
            t.dot(4)

    exitonclick()


def task14():
    arr = []
    for x in range(8):
        for y in range(8):
            n = _task14(x, y)
            if n % 117 == 0:
                arr.append(n)
    print(min(arr) / 117)


def _task14(x, y):
    return int(f"{y}04{x}5", 11) + int(f"253{x}{y}", 8)


def task17():
    with open("17 (3).txt") as f:
        nums = list(map(int, f.readlines()))

    c = 0
    ms = 0

    for i, x in enumerate(nums[:-1]):
        for y in nums[i+1:]:
            if (x + y) % 9 == 0:
                c += 1
                ms = max(ms, x + y)

    print(c, ms)


def task24():
    with open("24.txt") as f:
        let = f.read().strip()
    res = re.findall(r"A\w", let)
    print(sorted(Counter(res).items(), key=lambda x: x[1]))


def task25():
    r = range(110203, 110246)
    for i in r:
        divs = list(
                filter(
                    lambda x: x % 2 == 0, dividers(i)
                )
            )
        if len(divs) == 4:
            print(*divs)


def dividers(n: int):
    divs = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            divs.append(i)
    return divs + [n]


task25()
