def task1():
    exp = lambda _w, _x, _y, _z: (_w <= _y) and ((not _y) == _x) and (_x or _z)
    print("w x y z F")
    for w in range(2):
        for x in range(2):
            for y in range(2):
                for z in range(2):
                    if exp(w, x, y, z):
                        print(w, x, y, z, 1)


task1()
