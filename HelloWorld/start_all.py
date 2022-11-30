import os
import threading
import traceback
from ctypes import CDLL
from colorama import Fore, Style, Back


def compiler(lang, name=None):
    try:
        save_route = f"compiled\\{name or lang}"
        if lang == "c":
            os.system(f"gcc c.c -o {save_route}")
            os.system(f".\\{save_route}")
        elif lang == "cpp":
            os.system(f"gcc cpp.cpp -lstdc++ -o {save_route}")
            os.system(f".\\{save_route}")
        elif lang == "java":
            os.system(f"java Java.java")
        elif lang == "so":
            os.system(f"gcc -shared -o {save_route}.so -fPIC so.c")
            dll = CDLL(f".\\{save_route}.so")
            dll.HelloWorld()
    except:
        print(f"{Fore.BLACK}{Style.BRIGHT}{Back.WHITE} {lang}\n{Fore.RED}{Back.BLACK}",
              traceback.format_exc().strip(),
              f"\n{Style.RESET_ALL}")


if __name__ == '__main__':
    # DLL
    threading.Thread(target=compiler, args=("so",)).start()
    # C++
    threading.Thread(target=compiler, args=("cpp",)).start()
    # Java
    threading.Thread(target=compiler, args=("java",)).start()
    # C
    threading.Thread(target=compiler, args=("c",)).start()
    # python
    os.system("py python.py")
    # javascript
    os.system("node javascript")
    # Windows CMD
    os.system("cmd")
