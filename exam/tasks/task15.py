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


stad()