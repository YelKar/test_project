def task_demo():
    with open("../files/26_Демо_2021.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        s, n = map(int, lines.pop(0).split())
        *nums, = map(int, lines)
    nums.sort()
    nums: list
    sum_ = 0
    i = 0
    for i, n in enumerate(nums):
        sum_ += n
        if sum_ > s:
            sum_ -= n + nums[i - 1]
            break
    max_pos = s - sum_
    print(i, list(filter(lambda x: x < max_pos, nums[i:]))[-1] + sum_)


def task_dosrok():
    with open("../files/Задание_26_C3D450.txt") as f:
        *pairs, = list(f)


task_demo()
