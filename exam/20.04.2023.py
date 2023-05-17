"""13054772

1: 20
2: 1101
3:
"""
import math


def task3():
    def r(n: int):
        return (n << 2) + 0b10 * count1(n)

    def count1(n: int):
        c = 0
        while n:
            c += n % 2
            n //= 2
        return c % 2

    i = 0
    while r(i) <= 55:
        i += 1
    print(r(i), r(i-1),)


def task4():
    from turtle import Turtle, tracer, exitonclick

    t = Turtle()
    t.left(90)
    size = 20
    tracer(10)

    for _ in range(6):
        t.forward(7 * size)
        t.right(90)
        t.forward(7 * size)
        t.right(90)

    t.penup()
    for x in range(8):
        for y in range(8):
            t.goto(x * size, y * size)
            t.dot(3)

    exitonclick()


def task5():
    ln = 10
    char = len(f"{26:b}")
    pwd = math.ceil(ln * char / 8)



task5()
