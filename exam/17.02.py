# 12533003


def task1():
    def f():
        return ((x <= y) or (y == w)) and ((x or z) == w)

    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    s = sum((x, y, z, w))
                    if f() and s != 0 and s != 4:
                        print(z, y, x, w)


def task2():
    def f():
        return (w <= x) and ((y <= z) == (x <= y))

    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    s = sum((x, y, z, w))
                    if f() and s != 0 and s != 4:
                        print(x, z, y, w)


def task3():
    def f(n: int):
        b: str = bin(n)
        b += str(b.count("1") % 2)
        b += str(b.count("1") % 2)
        return int(b, 2)

    for n in range(1, 100):
        if f(n) > 77:
            print(n)
            break


def task4():
    def f(n: int):
        s = str(n)
        l = list(map(int, s))
        return "".join(
            map(str, sorted([l[0] * l[1], l[1] * l[2]], reverse=True))
        )

    for i in range(100, 1000):
        if f(i) == "123":
            print(i)
            break


def task5():
    s = "1" * 82

    while "11111" in s or "888" in s:
        if "11111" in s:
            s = s.replace("11111", "88", 1)
        elif "888" in s:
            s = s.replace("888", "8", 1)

    print(s)


def task6():
    s = "1" * 80

    while "11111" in s:
        s = s.replace("111", "2", 1).replace("222", "1", 1)
    print(s)


def task7():
    k = 43
    with open("tasks/files/27_B.txt") as f:
        n, *nums = list(map(int, f))
        print(n)

    mx_sum = 0
    mx_len = 0
    count = 0
    curr_sum = 0

    for i in nums:
        if curr_sum % 43 != 0:
            if curr_sum - i > mx_sum:
                 mx_sum = curr_sum - i
                 mx_len = count - 1
            count = 0
            curr_sum = 0
        else:
            count += 1
            curr_sum += i

    print(mx_len)


task7()
