import asyncio
from collections import Counter
from turtle import Turtle, exitonclick


t = Turtle()
size = 35
up = 200

async def dots(step, pos_x=0, pos_y=0):
    await asyncio.sleep(0.01)
    dt = Turtle()
    dt.speed(0)
    dt.penup()
    for x in range(-6, 11):
        for y in range(-1, 16):
            dt.goto(x * step + pos_x, -y * step + pos_y)
            dt.dot(4)
            await asyncio.sleep(0.01)
        # await asyncio.sleep(0.01)


def check(step):
    over = []
    cvs = t.screen.getcanvas()
    for x in range(-10 * step, 20 * step, step):
        for y in range(-10 * step, 20 * step, step):

            # t.goto(x, y)
            over.append(cvs.find_overlapping(x, y, x, y))
        # await asyncio.sleep(0.01)
    print(Counter(over)[(5,)])


async def star():
    t.speed(0)
    t.up()
    t.goto(0, up)
    t.down()
    t.fillcolor("red")

    t.lt(90)
    t.begin_fill()
    for i in range(14):
        t.rt(60)
        await asyncio.sleep(0.01)
        t.fd(2 * size)
        await asyncio.sleep(0.01)
        t.rt(60)
        await asyncio.sleep(0.01)
        t.fd(2 * size)
        await asyncio.sleep(0.01)
        t.rt(270)
        await asyncio.sleep(0.01)

    t.end_fill()


async def main():
    # task_dots = asyncio.create_task(dots(size, pos_y=up))
    task_star = asyncio.create_task(star())

    await task_star
    # await task_dots


asyncio.run(main())
check(size)

exitonclick()