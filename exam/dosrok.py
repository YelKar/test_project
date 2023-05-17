"""
task1: 10
task18: 2226 902
"""
import time
import timeit
from threading import Thread


def task5_p():
    def r(n_: int):
        if n_ % 3 == 0:
            n_ = int(bin(n_) + bin(n_ % 0b1000)[2:], 2)
        else:
            n_ = int(bin(n_) + bin(n_ % 3 * 3)[2:], 2)
        return n_

    for n in range(1000):
        if r(n) >= 76:
            return n


def task16_p():
    def f(n: int):
        if n >= 2025:
            return n
        return n + f(n + 2)

    return f(2022) - f(2023)


def task17_p():
    def two_sign(n_: int) -> bool:
        return 10 <= n_ < 100

    with open("files/Inf_ege2023/1_17.txt") as f:
        _, *nums = map(int, f)

    mx = max(filter(two_sign, nums))
    c = 0
    mx_sm = 0

    for x, y in zip(nums, nums[1:]):
        if two_sign(x) != two_sign(y) and (x + y) % mx == 0:
            c += 1
            mx_sm = max(mx_sm, x + y)

    return f"{c} {mx_sm}"


def task22_p():
    with open("files/Inf_ege2023/1_22.csv", encoding="utf-8") as f:
        nums = []
        for row in f.readlines()[1:]:
            id_, t, req = row.split("\t")
            nums.append((int(id_), int(t), tuple(filter(None, map(int, req.split(";"))))))

    threads = []

    for id_, t, req in nums:
        threads.append(t + max((0, *(threads[i - 1] for i in req))))

    return max(threads)


def task22_2_p():
    diff = 40

    def main():
        with open("files/Inf_ege2023/1_22.csv") as f:
            plan = []
            for row in f.readlines()[1:]:
                id_, duration, req = row.split("\t")
                plan.append((int(id_), int(duration), tuple(filter(None, map(int, req.split(";"))))))

        threads: list[Thread] = []

        def thread(dur, *requires, p_id):
            for r in requires:
                threads[r - 1].join()
            time.sleep(dur / diff)

        for id_, t, req in plan:
            threads.append(Thread(target=thread, args=(t, *req), kwargs={"p_id": id_}))
            threads[id_ - 1].start()

        for th in threads:
            th.join()

    return round(timeit.timeit(main, number=1) * diff)


def task23_p():
    def f(a: int, b: int):
        return (
                a == b or a < b != 15
                and f(a, b - 1)
                + f(a, b // 2) * (b % 2 == 0)
                + f(a, b // 3) * (b % 3 == 0)
        )

    return f(1, 11) * f(11, 25)


def task24_p():
    with open("files/Inf_ege2023/1_24.txt") as f:
        s = f.read().strip()

    prev = False
    a = "ABC"
    c = 1
    mx = 0

    for let in s:
        if let in a and prev:
            mx = max(mx, c)
            c = 1
        else:
            c += 1
        prev = let in a

    return mx


def task25_g():
    import re

    mask = re.compile(r"12\d\d1\d*56")
    yield "\n"
    for x in range(10):
        for y in range(10):
            for z in ("", *range(100)):
                i = f"12{x}{y}1{z}56"
                if int(i) > 10 ** 8:
                    break
                if mask.fullmatch(i) and int(i) % 317 == 0:
                    yield f"\t{int(i)} {int(i) // 317}\n"


def task26_p():
    with open("files/Inf_ege2023/1_26.txt") as f:
        (k,), (_,), *passengers = map(lambda x: tuple(map(int, x.split())), f)
        passengers.sort()

    cells = [0] * k

    ok = 0
    empty = None
    for start, end in passengers:
        empty = None
        for i, cell in enumerate(cells):
            if cell < start:
                cells[i] = cell = 0
            if not cell:
                empty = i
                break

        if empty is not None:
            ok += 1
            cells[empty] = end

    return f"{ok} {empty + 1}"


def task27_g():
    def fn(k: int, _, *nums: int):
        nums = sorted(enumerate(nums), key=lambda x: x[1], reverse=True)

        for i, (a, x) in enumerate(nums):
            for b, y in nums[i + 1:]:
                if abs(a - b) >= k:
                    return x + y

    for let in "AB":
        with open(f"files/Inf_ege2023/1_27_{let}.txt") as f:
            yield f"{fn(*map(int, f))} "
    yield "\n"


print("Without code:", *__doc__.strip().split("\n"), sep="\n\t")

for name, func in filter(lambda x: x[0].startswith("task"), dict(globals()).items()):
    print(name, end=" ==> ")
    if name.endswith("_p"):
        print(func())
    elif name.endswith("_n"):
        print(func.__doc__)
    elif name.endswith("_g"):
        for res in func():
            print(res, end="")
    else:
        print()
        func()
