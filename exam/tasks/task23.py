def task3607(n: int):
    if n < 2:
        return 0
    if n == 2:
        return 1
    elif n % 5 == 0 or n % 2 == 0:
        return task3607(n // 5) + task3607(n - 2)
    return 0


print(task3607(50))
