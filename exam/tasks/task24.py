import re
import os
from collections import Counter


def task_egkr():
    with open("files/24.txt", "r", encoding="utf-8") as f:
        letters = f.read().strip()

    variants = [
        "BAB",
        "BAC",
        "CAB",
        "CAC"
    ]

    gen = task_egkr_iter(len(letters))

    mx = count = 0

    for i in gen():
        if letters[i:i+3] in variants:
            count += 3
            gen.three()
        else:
            mx = max(mx, count)
            count = 0
    print(mx)


def task_egkr_iter(*args):
    r = range(*args).__iter__()

    def gen():
        for _i in r:
            yield _i

    def three():
        try:
            for i in range(2):
                next(r)
        except StopIteration:
            pass

    gen.three = three

    return gen


def task27688():
    exp = re.compile(r"Z+")
    with open("files/24_27688.txt") as f:
        print(max(map(lambda x: x.end() - x.start(), re.finditer(exp, f.read().strip()))))


def task27690():
    with open("files/24_27690.txt") as f:
        let = f.read().strip()

    c = 1
    mx = 0

    for x, y in zip(let, let[1:]):
        if x != y:
            c += 1
        else:
            mx = max(mx, c)
            c = 1

    print(mx)


def task27699():
    exp = re.compile(r"(LDR)+(LD|L)?")
    with open("files/24_27699.txt") as f:
        let = f.read().strip()

    all_found = re.finditer(exp, let)

    print(max(map(
        lambda x: x.end() - x.start(),
        all_found
    )))


def task29672():
    with open("files/24_29672.txt") as f:
        lines = f.readlines()

    c = 0
    for line in lines:
        if line.count("E") > line.count("A"):
            c += 1

    print(c)


def task33494():
    exp = re.compile(r"E\w")
    
    with open("files/24_33494.txt") as f:
        found = re.finditer(exp, f.read())

    print(Counter(
        map(
            lambda x: x.group(),
            found
        )
    ))


def task33526():
    with open("files/24_33526.txt") as f:
        let = f.read().strip()

    counter = {}
    for x, y, z, in zip(let, let[1:], let[2:]):
        if x == z:
            counter[y] = counter.get(y, 0) + 1

    print(sorted(
        counter.items(),
        key=lambda el: el[1],
        reverse=True
    ))


def task33769():
    with open("files/24_33769.txt") as f:
        let = f.read().strip()

    count = []

    for x, y, z, in zip(let, let[1:], let[2:]):
        if x == y:
            count.append(z)

    print(Counter(count))


task33769()
