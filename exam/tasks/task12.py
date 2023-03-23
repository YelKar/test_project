from itertools import permutations


def egkr():
    s = "8" * 120
    while "888" in s or "2222" in s:
        if "2222" in s:
            s = s.replace("2222", "88", 1)
        else:
            s = s.replace("888", "22", 1)

    print(s, s.count("8"))


def stad():
    def f(s: str):
        while "00" not in s:
            if "011" in s:
                s = s.replace("011", "101", 1)
            else:
                s = s\
                    .replace("01", "40", 1)\
                    .replace("02", "20", 1)\
                    .replace("0222", "1401", 1)
        return s

    print(f(""))


stad()
