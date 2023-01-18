import ctypes
import os


def load(src: str) -> ctypes.CDLL:
    command = "gcc -shared -o {so} -fPIC {c}"
    library_format = ".so"
    cache_dir = ".\\__cache__\\"
    if not os.path.exists(cache_dir):
        os.mkdir(cache_dir)
    path = cache_dir + ".".join(src.split(".")[:-1]) + library_format
    os.system(
        command.format(
            c=src,
            so=path
        )
    )
    return ctypes.CDLL(path)


if __name__ == '__main__':
    c = load("c.c")
    c.main()
    c.foo()
