import math


def task2():  # yzwx
    """((x ∧ ¬y) ≡ (z ∨ ¬w)) → (x ∧ z)"""
    def f():
        return ((x and (not y)) == (z or (not w))) <= (x and z)

    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    if not f():
                        print(y, z, w, x)


def task5():  # 22
    def r(n: int):
        return n * 4 + n % 2 * 3

    for i in range(1000, 0, -1):
        if r(i) < 94:
            print(i)
            break


def task6():  # 40
    from turtle import Turtle, exitonclick, tracer

    t = Turtle()
    t.left(90)
    size = 20
    tracer(10)

    for i in range(5):
        t.forward(7 * size)
        t.right(90)
        t.forward(4 * size)
        t.right(90)

    t.up()
    for x in range(6):
        for y in range(8):
            t.goto(x * size, y * size)
            t.dot(4)
    exitonclick()


def task7():  # 256
    img = 512 * 300
    mx_size = 150 * 2 ** 13
    px = mx_size / img
    print(f"{px} bit/px")
    print(f"{2**px} colors")


def task8():  # 5400
    print(5 * 6 * 6 * 6 * 5)


def task11():  # 150
    char = len(f"{7:b}")
    pwd = char * 15
    print(math.ceil(pwd / 8) * 25)


def task12():
    s = f">{'1' * 26}{'2' * 10}{'3' * 14}"
    while ">1" in s or ">2" in s or ">3" in s:
        s = s.\
            replace(">1", "22>", 1).\
            replace(">2", "2>", 1).\
            replace(">3", "1>", 1)
    print(sum(map(int, s[:-1])))


def task14():  # 119
    from string import digits, ascii_uppercase as letters
    alph = (digits + letters)[1:12]
    mn = 10000000000000
    for x in alph:
        for y in alph:
            r = int(f"{y}AA{x}", 12) + int(f"{x}02{y}", 14)
            if r < mn and r % 80 == 0:
                mn = r
    print(mn // 80)


def task15():  # 24
    def f():
        return (120 % a == 0) and ((x % a != 0) <= ((x % 18 == 0) <= (x % 24 != 0)))

    for a in range(1000000, 0, -1):
        for x in range(1, 10000):
            if not f():
                break
        else:
            print(a)
            break


def task16():  # 256
    def f(n: int):
        if n <= 2:
            return n
        return f(n - 1) * f(n - 2)

    print(f(7))


def task17():
    with open("files/17_22.03.23.txt", "r", encoding="utf-8") as f:
        *nums, = map(int, f)

    mx = 0
    count = 0
    for i, x in enumerate(nums[:-1]):
        for y in nums[i+1:]:
            diff = abs(x - y)
            if diff % 60 == 0 and (x % 15 == 0 or y % 15 == 0):
                count += 1
                mx = max(mx, diff)

    print(count, mx)


def task23():  # 48
    def f(a: int, b: int):
        return a == b or (a < b != 59 and f(a, b // 2) * (b % 2 == 0) + f(a, b - 1))

    print(f(3, 14) * f(14, 62))


task23()
