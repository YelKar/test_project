def task35460():
    print("w x y z")
    for x in range(2):
        for y in range(2):
            for z in range(2):
                for w in range(2):
                    if _task35460(w, x, y, z):
                        print(w, x, y, z)


def _task35460(w, x, y, z):
    return (not ((x or y) <= (z and w))) and (x <= w)


task35460()
