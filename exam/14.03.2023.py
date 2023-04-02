"""
Вариант № 12747781
"""
from math import ceil


def task1():
    def f():
        return (z and y) or ((x <= z) == (y <= w))

    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    if not f():
                        print(w, z, y, x,)


def task2():
    # ((x → y) ≡ (z → w)) ∨ (x ∧ w)
    def f():
        return ((x <= y) == (z <= w)) or (x and w)

    c = 0
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    if not f():
                        if c != 2:
                            print(z, y, x, w,)
                        c += 1


def task3():
    def r(n: int):
        sec = n // 10 % 10
        a = [n // 100 * sec, n % 10 * sec]
        return "".join(
            map(
                str,
                sorted(a)
            )
        )

    for i in range(1000, 99, -1):
        if r(i) == "621":
            print(i)
            break


def task4():
    from turtle import Turtle, exitonclick, tracer

    t = Turtle()
    t.left(90)
    size = 25
    tracer(10)
    for _ in range(4):
        t.forward(12 * size)
        t.right(90)
    t.right(30)
    for _ in range(3):
        t.forward(8 * size)
        t.right(60)
        t.forward(8 * size)
        t.right(120)

    t.up()
    for x in range(13):
        for y in range(13):
            t.goto(x * size, y * size)
            t.dot(3)

    exitonclick()


def task5():
    u = 5 * 13
    p = 7 * 2
    s = ceil((u + p) / 8)
    print(32 - s)


def task6():
    s = "1" * 98
    while "1111" in s:
        s = s.replace("1111", "22", 1).replace("222", "1", 1)
    print(s)


def task7():
    for x in range(10):
        res = int(f"95{x}2", 11) + int(f"{x}458", 12)
        if res % 136 == 0:
            print(res / 136)


def task8():
    with open("tasks/files/17_37344.txt", "r", encoding="utf-8") as f:
        nums = list(map(int, f))

    c = 0
    mx = 0
    for i, x in enumerate(nums[:-1]):
        for y in nums[i+1:]:
            if x * y % 10 == 0:
                c += 1
                mx = max(mx, x + y)

    print(c, mx)


task5()
