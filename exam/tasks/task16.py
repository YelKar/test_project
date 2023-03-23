def stad():
    def f(a, b):
        if a == b == 0:
            return 0
        if a > b:
            return f(a - 1, b) + b
        return f(a, b - 1) + a

    c = 1

    for i in range(1, 1_048_576 // 2 + 1):
        if 1_048_576 % i == 0:
            c += 1
    print(c)


stad()
