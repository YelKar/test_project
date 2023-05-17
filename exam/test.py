n = int(input())
c = 0
while n:
    c += 100 <= n < 1000 and n % 4 == 0
    n = int(input() or input())
print(c)
