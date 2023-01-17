from threading import Thread, Event
import keyboard as keyboard


def foo():
    while not e.is_set():
        keyboard.write("Hello")
        keyboard.wait("c")


e = Event()
th = Thread(target=foo)
th.start()
