def task3607(n: int):
    if n < 2:
        return 0
    if n == 2:
        return 1
    elif n % 5 == 0 or n % 2 == 0:
        return task3607(n // 5) + task3607(n - 2)
    return 0


def task13471(n: int):
    if n == 24:
        return 0
    if n == 1:
        return 1
    elif (n - 1) % 2 == 0:
        return task13471(n - 1) + task13471((n - 1) // 2)
    elif n:
        return task13471(n - 1)
    return 0


def task5977(n: int):
    if n == 10:
        return 1
    elif n < 10:
        return 0
    elif n > 10:
        return task5977(n - 10) + task5977(n - 1)
    return task5977(n - 1)


print(task5977(33))
