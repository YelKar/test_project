def task47405():
    from turtle import Turtle, exitonclick

    t = Turtle()
    t.lt(90)
    size = 30
    t.fillcolor("red")
    t.begin_fill()
    for _ in range(4):
        t.fd(9 * size)
        t.rt(90)
    t.end_fill()
    t.fillcolor("green")
    t.begin_fill()
    for _ in range(3):
        t.fd(9 * size)
        t.rt(120)
    t.end_fill()

    t.up()
    cvs = t.screen.getcanvas()
    count = 0
    for x in range(10):
        for y in range(10):
            _x, _y = x * size, y * size

            s = cvs.find_overlapping(_x, -_y, _x, -_y)
            print(s)
            t.goto(_x, _y)
            if s == (5,):
                t.color("yellow")
                count += 1
            else:
                t.color("black")
            t.dot(4)
    print(count)

    exitonclick()


def task47309():
    from turtle import Turtle, exitonclick

    t = Turtle()
    size = 30
    t.begin_fill()
    for i in range(2):
        t.fd(8 * size)
        t.rt(150)
        t.fd(8 * size)
        t.rt(30)
    t.end_fill()

    t.up()
    for x in range(-10 * size, 10 * size, size):
        for y in range(-5 * size, 5 * size, size):
            t.goto(x, y)
            t.dot(3, "red")


task47309()
