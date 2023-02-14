def task48390():
    result = []

    for x in range(8):
        for y in range(8):
            a = int(f"{x}01{y}4", 9) + int(f"{x}{y}544", 8)
            if a % 89 == 0:
                result.append(a)

    print(min(result) // 89)


task48390()
