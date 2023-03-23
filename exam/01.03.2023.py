def task2():
    def f():
        return ((not y) <= (z == w)) and ((z <= x) == w)

    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    a = w, x, y, z
                    if f() and not all(a) and a != (0, 0, 1, 1):
                        print(z, w, y, x)


task2()
