import itertools


def task_egkr():
    even = set(range(0, 7, 2))
    odd = set(range(1, 7, 2))
    print(even, odd)
    count = 0
    for n in range(7 ** 5, 7 ** 6):
        lst = list(map(int, svn(n)))
        if lst.count(6) == 1:
            ev = lst[::2]
            od = lst[1::2]
            if even.issuperset(ev) and odd.issuperset(od) or \
                    odd.issuperset(ev) and even.issuperset(od):
                count += 1
    print(count)


def svn(n: int):
    s = ""
    while n:
        s += str(n % 7)
        n //= 7
    return s


def stad():
    pass


