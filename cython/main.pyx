def task5():
    print(r(17))
    nums = set()
    for num in range(15_432_098, 1_000_000_000):
        res = r(num)
        if not res <= 1_987_654_321:
            break
        nums.add(res)

    print(len(nums))

cdef extern from "module.c":
    int _cfib(int n)

def r(n: int):
    if n % 1000000 == 0:
        print(f"{n:_}")
    n = (n * 2) + is_odd(n)
    n = (n * 2) + is_odd(n)
    n = (n * 2) + is_odd(n)
    return n

def cfib(int n):
    return _cfib(n)

def is_odd(n: int):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s % 2






task5()