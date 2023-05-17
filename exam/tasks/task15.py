def task9804():
    f = lambda: (x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0))
    for a in range(1000):
        for x in range(1000):
            if not f():
                break
        else:
            print(a)
            break


def task34506():
    def f():
        return (x & 25 != 0) <= ((x & 17 == 0) <= (x & a != 0))

    for a in range(1000):
        for x in range(1000):
            if not f():
                break
        else:
            print(a)
            break


def task34508():
    def f():
        return (x & 29 != 0) <= ((x & 12 == 0) <= (x & a != 0))

    for a in range(1000):
        for x in range(1000):
            if not f():
                break
        else:
            print(a)
            break


def task34517():
    def f():
        return (x & a != 0) <= ((x & 10 == 0) <= (x & 3 != 0))

    for a in range(10000, 0, -1):
        for x in range(10000):
            if not f():
                print(x, a)
                break
        else:
            print(a)
            break


def stad():
    def f():
        return (x & 35 != 0 or x & 22 != 0) <= ((x & 15 == 0) <= (x & A != 0))

    for A in range(1, 1000):
        for x in range(10000):
            if not f():
                break
        else:
            print(A)
            break


def task34510():
    """x&25 ≠ 0 → (x&9 = 0 → x&А ≠ 0)"""
    print(task34510.__doc__)

    def f():
        return eval(
            task34510.
            __doc__.
            replace("→", "<=").
            replace("≠", "!=").
            replace("=", "==")
        )

    for a in range(int(1e10)):
        for x in range(1000):
            if not f():
                break
        else:
            print(a)
            break


def task34509():
    def f():
        return


def task34518():
    def f():
        return (x & A != 0) <= ((x & 36 == 0) <= (x & 6 != 0))

    for A in range(999462, -1, -1):
        flag = True
        for x in range(10000):
            for y in range(10000):
                if not f():
                    flag = False
                    break
            if not flag:
                break
        else:
            print(A)
            break


task34518()
