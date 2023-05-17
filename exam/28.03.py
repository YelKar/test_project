"""
№12867305
"""


def task1():
    def f():
        """((x ≡ ¬y) → (y ∧ ¬z)) ∨ (z ∧ ¬w)"""
        return ((x == (not y)) <= (y and (not z))) or (z and not w)

    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if not f():
                        print(w, z, x, y)


def task3():
    def r(n_: int):
        return n_ - int(bin(n_)[3:], 2)

    print(len({r(i) for i in range(100, 3_001)}))


def task4():
    from turtle import Turtle, tracer, exitonclick

    t = Turtle()
    tracer(10)
    size = 20
    t.left(90)
    for i in range(4):
        t.forward(9 * size)
        t.right(90)
        t.forward(7 * size)
        t.right(90)
    t.penup()
    for x in range(8):
        for y in range(10):
            t.goto(x * size, y * size)
            t.dot(3)
    exitonclick()



task4()
