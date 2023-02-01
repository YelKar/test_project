from turtle import Turtle, done


t = Turtle()
t.onclick(lambda *_: exit())
t.up()
t.goto(-20, 220)
t.shape("turtle")
t.fillcolor("green")
t.rt(90)
t.shapesize(3)
t.pensize(4)
t.write("Quit", move=False, align="left", font=("Arial", 20, "normal"))

t.goto(0, 200)


def set_goto(self):
    def goto(_x, _y):
        Turtle.goto(self, _x, -_y)
    return goto


t = Turtle()
t.goto = set_goto(t)
t.screen.tracer(10)
size = 25
up = 200

t.speed(0)
t.fillcolor("red")

t.begin_fill()
t.lt(90)
for i in range(12):
    t.rt(60)
    t.fd(2 * size)
    t.rt(60)
    t.fd(2 * size)
    t.rt(270)

t.end_fill()

t.up()
cvs = t.screen.getcanvas()
c = 0
for x in range(-5, 10):
    for y in range(-15, 2):
        pos = x * size, -y * size
        overlap = cvs.find_overlapping(*pos, *pos)
        t.goto(pos[0], pos[1])
        if len(overlap) == 1 and overlap[0] == 5:
            c += 1
        if len(overlap) > 1:
            print(overlap)
        t.dot(3, "yellow" if (9,) == overlap else "black")

print(c)
done()
