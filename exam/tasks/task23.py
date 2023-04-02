def task3607(n: int):
    if n < 2:
        return 0
    if n == 2:
        return 1
    elif n % 5 == 0 or n % 2 == 0:
        return task3607(n // 5) + task3607(n - 2)
    return 0


def task13471(n: int):
    if n == 24:
        return 0
    if n == 1:
        return 1
    elif (n - 1) % 2 == 0:
        return task13471(n - 1) + task13471((n - 1) // 2)
    elif n:
        return task13471(n - 1)
    return 0


def task5977(n: int):
    if n == 10:
        return 1
    elif n < 10:
        return 0
    elif n > 10:
        return task5977(n - 10) + task5977(n - 1)
    return task5977(n - 1)


def task6241():
    def f(a: int, b: int):
        if a == b:
            return 1
        if a > b:
            return 0
        return f(a, b - 1) + f(a, b - 3)

    print(f(17, 30))


def task18801():
    def f(a: int, b: int):
        if a == b:
            return 1
        if a > b:
            return 0
        return \
            f(a, b // 3) * (b % 3 == 0) \
            + f(a, b - 1) \
            + f(a, b - 2)

    print(f(2, 9) * f(9, 11) * f(11, 12))


def task16825():
    def f(a: int, b: int):
        if a == b:
            return 1
        if a > b or b in (6, 12):
            return 0
        return f(a, b - 1) + f(a, b - 3) + \
            f(a, b // 2) * (b % 2 == 0)

    print(f(3, 16))


def task_stad():
    def f(a, b, mul=False):
        if a == b:
            return 1
        if a > b:
            return 0
        return (
            (
                f(a, b // 3, True) * (b % 3 == 0)
                + f(a, b // 2, True) * (b % 2 == 0)
            ) * (not mul)
            + f(a, b - 1, mul)
            + f(a, b - 2, mul)
        )

    print(f(1, 11) - f(1, 11, True))


for name, func in list(
        filter(
            lambda x: x[0].startswith("task"),
            globals().items()
        )
):
    if not func.__annotations__:
        print(f"{name} => ", end="")
        func()
