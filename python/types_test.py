def __iter__(self):
    return iter(
        set(dir(self)) ^
        set(dir(object()))
    )


obj = type("Obj", (), dict(
    a=7,
    b=45,
    c={
        "a": 1,
        "b": 2
    },
    d={1, 34,6 , 32, 5, 5, 45, 67, 4, 5, 4, 5, 6},
    __iter__=__iter__
))()

for i in obj:
    print(i)
