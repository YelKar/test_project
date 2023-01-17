import time
from os import system
from threading import Thread


py_thread = Thread(target=lambda: (
    print("| start py |", end=""),
    system("py py.py"),
))

js_thread = Thread(target=lambda: (
    print("| start JS |", end=""),
    system("node js.js"),
))

java_thread = Thread(target=lambda: (
    print("| start Java |", end=""),
    system("java java.java"),
))

system("gcc c.c -o c")
c_thread = Thread(target=lambda: (
    print("| start C |", end=""),
    system(".\c"),
))
c_thread.start()
py_thread.start()
js_thread.start()
java_thread.start()
print(" => Started ALL")
