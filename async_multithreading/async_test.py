from asyncio import *
import asyncio
from colorama import Fore, Style


async def main():
    task1 = create_task(foo1("Hello"))
    task2 = create_task(foo2())
    await task1
    await task2


async def foo1(line: str, **formating):
    print("foo1 started")
    await sleep(5)
    for i in range(1, 11):
        print(
            f"{Style.BRIGHT}{Fore.RED}{i}:", 
            line.format(**formating), 
            end=f"{Style.RESET_ALL} "
        )
        await sleep(1.2)


async def foo2():
    print("foo2 started")
    await sleep(1)
    for x in range(1, 10):
        for y in range(1, 10):
            print(x * y, end=" ")
            await sleep(0.2)
        print()
        await sleep(0.5)


async def foo3():
    print("foo2 started")
    await sleep(1)
    for x in range(1, 10):
        for y in range(1, 10):
            print(x * y, end=" ")
            await sleep(0.2)
        print()
        await sleep(0.5)

run(main())
