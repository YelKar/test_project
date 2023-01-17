import sys
import time
from threading import Thread, Event


res = ""


def foo():
    for line in sys.stdin:
        if not line.strip():
            break
        print(line.strip())


inputs = Thread(target=foo)
inputs.start()
