def stad():
    with open("files/27-A_stad.txt", "r", encoding="utf-8") as f:
        nums = list(map(int, f))

    print("start")
    c = 0
    for i, x in enumerate(nums[:-18]):
        for y in nums[i+18:]:
            if (x + y) % 8 == 0 and x * y % 2187 == 0:
                c += 1
        print(c)

    print(c)


stad()
