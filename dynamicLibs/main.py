from module import fibonacci


for i in range(0, 1000):
    fib = fibonacci(i)
    print(fib, end=" ")
    if fib > 1000:
        print("\n", i, fib)
        break
