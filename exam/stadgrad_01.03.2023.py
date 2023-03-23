"""
1: _
2: yxwz
3: _
4: 11
5:
6: 48
"""
from numba import njit, prange


def task2():  # yxwz
    def f():
        return ((x <= y) or (z <= w)) and ((z == y) <= (w == x))

    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    a = w, x, y, z
                    if not f() and a not in ((1, 0, 0, 0), (1, 0, 1, 1)):
                        print(y, x, w, z)


@njit(parallel=True)
def task5():
    def f(): ...
    print(r(17))
    nums = set()
    for num in range(15_432_098, 1_000_000_000):
        res = r(num)
        if not res <= 1_987_654_321:
            break
        nums.add(res)
    print(len(nums))


def r(n: int):
    if n % 1000000 == 0:
        print(f"{n:_}")
    n = (n * 2) + is_odd(n)
    n = (n * 2) + is_odd(n)
    n = (n * 2) + is_odd(n)
    return n


def is_odd(n: int):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s % 2


def task6():
    from turtle import Turtle, tracer, exitonclick

    tracer(10)

    t = Turtle()
    t.lt(90)
    size = 20

    for i in range(3):
        t.fd(7 * size)
        t.rt(90)
    t.fd(10 * size)

    for i in range(5):
        t.lt(90)
        t.fd(6 * size)

    t.up()
    for x in range(-5 * size, 9 * size, size):
        for y in range(-6 * size, 8 * size, size):
            t.goto(x, y)
            t.dot(4)

    exitonclick()


task5()
