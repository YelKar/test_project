mt = [[0 for i in range(8)] for _ in range(8)]


def count3(n_: int):
    d = n_ % 3
    c = 0
    while not d and c < 7:
        c += 1
        n_ //= 3
        d = n_ % 3
    return c


with open("files/27-B_stad.txt", "r", encoding="utf-8") as f:
    *nums, = map(int, f.readlines()[1:])


for n in nums:
    mt[n % 8][count3(n)] += 1


print(" ", *(f"{i:6}" for i in range(8)), "  3 ** _")
print(*map(
    lambda x: f"{x[0]} {' '.join(map(lambda x_: f'{x_:6}', x[1]))}",
    enumerate(mt, 0)
), "_ % 8", sep="\n")


for x, y in zip(mt[1:5], mt[4:]):
    for ind, (i, j) in enumerate(zip(x, y)):
        pass
