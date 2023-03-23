from itertools import permutations


class PCB:
    def __init__(self, s: str):
        self.top, self.right, self.bottom, self.left = s

    def __repr__(self):
        return f"{self.top}{self.right}{self.bottom}{self.left}"


pcbs1 = [
    "1211", "1211", "1121", "1121",
    "2121", "2212", "2211", "1221", "1112"
]
pcbs1 = list(map(PCB, pcbs1))

pcbs2 = [
    "3121", "1332", "1211", "3133", "3232",
    "2121", "3321", "2313", "3323"
]
pcbs2 = list(map(PCB, pcbs2))


def chunk(_l: list):
    return [_l[:3], _l[3:6], _l[6:]]


def check(_l: list):
    # vertical
    for x, y, z in zip(*_l):
        x: PCB
        y: PCB
        z: PCB
        if x.bottom != y.top or y.bottom != z.top:
            return False

    # horizont
    for x, y, z in _l:
        if x.right != y.left or y.right != z.left:
            return False
    return True


print("Задание 1")
for i in list(permutations(pcbs1)):
    i = chunk(i)
    if check(i):
        print(*i, sep="\n", end="\n\n")
        break

print("Задание 2")
for i in list(permutations(pcbs2)):
    i = chunk(i)
    if check(i):
        print(*i, sep="\n", end="\n\n")
        break
