from turtle import Turtle, exitonclick


def task2():
    print("x y z w")

    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if _task2(w, x, y, z) and x == 0:
                        print(x, y, z, w)


def _task2(w, x, y, z):
    return ((x and y) or (y and z)) == ((x <= w) and (w <= z))


def task5():
    for n in range(1, 10000):
        r = _task5(n)
        if r == 2018:
            print(n, r)
            break


def _task5(n):
    bin_n = bin(n)[2:-1]
    bin_n += "10" if n % 2 else "01"
    return int(bin_n, 2)


def task6():
    size = 20
    t = Turtle()
    t.speed(0)
    t.left(90)

    for _ in range(4):
        t.forward(7 * size)
        t.right(90)
        t.forward(8 * size)
        t.right(90)

    t.penup()
    for x in range(9):
        for y in range(8):
            t.goto(x * size, y * size)
            t.dot(4, "black")

    exitonclick()


def task7():
    size = 12
    x = 2 / 4 / 1.5
    print(size * x)


def task8():
    pass


def task12():
    s = "1" * 39 + "2" * 39

    while "111" in s:
        s = s.replace("111", "2", 1)
        s = s.replace("222", "1", 1)

    print(s)


def task14():
    d = (9 ** 11) * (3 ** 20) - 3 ** 9 - 27
    b = ""

    while d:
        b += str(d % 3)
        d //= 3

    print(b.count("2"))


def task15():
    pass


def _task15(a: int):
    pass


def task16():
    def f(n):
        if n == 0:
            return 0
        if n % 2 == 0:
            return f(n / 2)
        else:
            return 1 + f(n - 1)

    for n in range(10000):
        if f(n) == 12:
            print(n)
            break


def task17():
    with open("17.txt") as f:
        nums = list(map(int, f))

    count = 0
    max_sum = 0

    for ind, i in enumerate(nums[:-1]):
        for j in nums[ind+1:]:
            if (i + j) % 2 != 0 and i * j % 3 == 0:
                count += 1
                max_sum = max(max_sum, i + j)

    print(count, max_sum)


def task24():
    with open("./zadanie24_2.txt") as f:
        curr_len = 0
        max_len = 0
        for let in f.read():
            if let == "R":
                curr_len += 1
            else:
                max_len = max(max_len, curr_len)
                curr_len = 0

        print(max_len)


def task25():
    nums = range(174457, 174505)
    all_divs = []
    for num in nums:
        if len(divs := get_dividers(num)) == 2:
            all_divs.append(divs)

    all_divs.sort(key=lambda x: x[0] * x[1])
    for x, y in all_divs:
        print(f"{x:6}{y:6}")


def get_dividers(n):
    dividers = []
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            dividers.append(i)
    return dividers



