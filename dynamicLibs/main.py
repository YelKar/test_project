from ctypes import cdll


lib = cdll.LoadLibrary("./main.so")

lib.main()
