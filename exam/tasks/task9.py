from collections import Counter


with open("files/09.csv", encoding="utf-8") as f:
    rows = list(map(lambda x: list(map(int, x.split())), f))


for nums in rows:
    count = Counter(nums)
    if 0 < list(count.values()).count(1) < 6:
        s = 0
        c = 0
        for k, v in count.items():
            if v == 1:
                s += k
                c += 1

        print(s, c)
