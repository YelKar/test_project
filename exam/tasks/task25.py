import timeit


def task27850():
    def is_prime(n: int):
        for num in range(2, n // 2 + 1):
            if n % num == 0:
                return False
        return True

    for i, num in enumerate(range(245_690, 245_757), 1):
        if is_prime(num):
            print(i, num)


def egkr():
    import re

    exp = re.compile(r"^2\d1\d*67$")

    def f1():
        for i in range(20167, 10 ** 7 + 1):
            if i % 159 == 0 and re.match(exp, str(i)):
                print(i, i // 159)

    def f2():
        for i in range(20167 + 26, 10 ** 7 + 1, 159):
            if i % 159 == 0 and re.match(exp, str(i)):
                print(i, i // 159)

    print(f"variant 1 => {timeit.timeit(f1, number=1)}")
    print(f"variant 2 => {timeit.timeit(f2, number=1)}")


def task27851():
    r = range(210_235, 210_301)

    def dividers(n: int):
        for _i in range(2, n // 2 + 1):
            if n % _i == 0:
                yield _i

    for i in r:
        divs = list(dividers(i))
        if len(divs) == 4:
            print(*divs)


def task29673():
    r = range(123_456_789, 223_456_789)

    def dividers(n: int):
        c = 0
        res = []
        for _i in range(2, n // 2 + 1):
            if n % _i == 0:
                c += 1
                res.append(_i)
            if c > 3:
                return False
        return res

    for i in r:
        divs = dividers(i)
        if not divs:
            continue
        if len(divs) == 3:
            print(i, max(divs))


def task27855():
    r = range(95_632, 95_701)

    def dividers(_n: int):
        for i in range(2, _n + 1):
            if i % 2 == 0 and _n % i == 0:
                yield i

    for n in r:
        divs = list(dividers(n))
        if len(divs) == 6:
            print(divs)


task27855()
