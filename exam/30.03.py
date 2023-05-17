"""
1: ДАЕВГБЖИ
2: xzyw
3: 11111000
"""


def task2():
    """
    F1 = (x → y) ≡ (w ∨ ¬z)
    F2 = (x → y) ∧ (¬w ≡ z)
    :return:
    """

    def f1():
        return (x <= y) == (w or not z)

    def f2():
        return (x <= y) and ((not w) == z)

    print("  x  z  y  w f1 f2")

    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    if (not f1() and sum((w, x, y, z)) <= 1) or \
                            (f1() and not f2() and z and (y or w) and y != w):
                        print(f"{x:3}{z:3}{y:3}{w:3}{f1():3}{f2():3}")


def task4():
    def r(n_: int):
        odds, evens = count(n_)
        n_ *= 2
        n_ += odds > evens or odds == evens and ...

    def count(n_: int):
        a = [0, 0]
        while n_:
            a[n_ % 2] += 1
            n_ //= 10
        return a

    print(count(123))


task4()
