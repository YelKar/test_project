def task33188():
    def f(n: int):
        if n == 0:
            return 0
        if n % 3 == 0:
            return n + f(n - 3)
        return n + f(n - (n % 3))

    print(f(22))


def task4558():
    def f(n: int):
        return n == 1 or f(n - 1) * n

    print(f(5))


def task38591():
    def f(n: int):
        if n == 1:
            return 1
        if n % 2 == 0:
            return n + f(n - 1)
        return 2 * f(n - 2)

    print(f(26))


def task4644():
    def f(n: int):
        return n == 1 or f(n - 1) * f(n - 1) - f(n - 1) * n + 2 * n

    print(f(4))


for name, func in list(
    filter(
        lambda x: x[0].startswith("task"),
        globals().items()
    )
):
    print(f"{name} => ", end="")
    func()
