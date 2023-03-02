class TestClass(dict):
    __match_args__ = ("",)
    __current_cycle = 0
    __iter = None
    __count = 0
    __len = None

    def __new__(cls, arg, *args, **kwargs):
        instance = super().__new__(cls, *args, **kwargs)
        instance.parameter = arg
        return instance

    def __init__(self, count, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__iter = list(self.items())
        self.__len = len(self.__iter)
        self.__count = count
        print(f"init main class {count=}")

    def __get_name(self):
        for i, j in globals().items():
            if j is self:
                return i

    def __repr__(self):
        result = super().__repr__()\
            .replace('{', '')\
            .replace('}', '')\
            .replace(': ', '=>')
        return f"{self.__get_name()}" \
               f"({result})"

    def __str__(self):
        return f"TestClass > {self.__get_name()}({super().__repr__()})"

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_cycle == self.__count or not self.__len:
            self.__current_cycle = 0
            raise StopIteration

        result = self.__iter[self.__current_cycle % self.__len]
        self.__current_cycle += 1
        return result

    @property
    def par(self):
        return 5

    @par.setter
    def par(self, other):
        print("Set par = {}".format(other))


iterator = TestClass(20, {1: 2, 2: 3, "3": 4})

for key, val in iterator:
    key, val = key.__repr__(), val.__repr__()
    print(f"{key=:<3} {val=:<3}")

print({1: iterator})

print(iterator.par)
iterator.par = 5
