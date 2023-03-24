start = 0o10000000000
r = range(start, start * 8)


def f(n: int):
    prev = 0
    c = 0
    while n:
        curr = (n % 8) % 2
        c += (n % 8) % 2
        if prev == curr == 1 or c > 3:
            return False
        prev = curr
        n //= 8
    return c == 3


count = 0

print(start * 8)
for i in r:
    count += f(i)


print(count)
