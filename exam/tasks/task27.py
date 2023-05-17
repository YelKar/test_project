def stad():
    with open("../files/27-A_stad.txt", "r", encoding="utf-8") as f:
        nums = list(map(int, f))

    print("start")
    c = 0
    for i, x in enumerate(nums[:-18]):
        for y in nums[i+18:]:
            if (x + y) % 8 == 0 and x * y % 2187 == 0:
                c += 1
        print(c)

    print(c)


def task38604():
    for let in "AB":
        with open(f"../files/27_{let}_38604.txt") as f:
            _, *nums = map(int, f)

        a = []
        sm = 0
        for x in nums:
            sm += x
            a.append(sm % 43)

        mx = (0,)

        for i in range(43):
            if i not in a:
                continue
            r = nums[a.index(i) + 1:-a[::-1].index(i)]
            mx = max(
                mx,
                (sum(r), sum(r) % 43, len(r))
            )

        print(mx)


def task27424():
    with open("../files/27-B_27424.txt") as f:
        _, *nums = map(lambda line: sorted(map(int, line.split()),), f)

    sm = 0
    diff = 1000000
    for mn, mx in nums:
        sm += mx
        diff = (mx - mn) % 3 and min(diff, mx - mn) or diff

    print(f"{sm = }  {sm % 3 = }  {diff % 3 = }  {sm - diff = }")


def task27889():
    with open("../files/27-B_27889.txt") as f:
        _, *nums = map(lambda x: sorted(map(int, x.split())), f)

    sm = 0
    diff = 100000000
    for mn, mx in nums:
        sm += mn
        diff = (mx - mn) % 3 and min(mx - mn, diff) or diff

    print(f"{sm=}  {sm % 3 = }")


def task48475():
    with open("../files/27-B_48475.txt") as f:
        _, *nums = map(int, f)

    c = 0
    for i, x in enumerate(nums[:-1]):
        for y in nums[i+1:]:
            c += not ((x + y) % 3 or x * y % 4096)

    print(c)





task48475()
