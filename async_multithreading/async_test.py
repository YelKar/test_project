from asyncio import create_task, sleep, run
from random import random

from colorama import Fore, Style


async def main():
    task1 = create_task(foo1("Hello {name}", name="foo1"))
    task2 = create_task(foo2())
    task3 = create_task(foo3())
    await task1
    await task2
    await task3


async def foo1(line: str, **formating):
    print("foo1 started")
    await sleep(5)
    for i in range(1, 11):
        print(
            f"{Style.BRIGHT}{Fore.RED}{i}:", 
            line.format(**formating), 
            end=f"{Style.RESET_ALL}\n"
        )
        await sleep(1.2)


async def foo2():
    print("foo2 started")
    await sleep(1)
    for x in range(1, 10):
        for y in range(1, 10):
            print(f"{Fore.GREEN}foo2: {x*y} => {x=} | {y=}{Fore.RESET}")
            await sleep(0.2)


async def foo3():
    print("foo3 started")
    await sleep(1)
    for x in range(1, 9):
        for y in range(1, 3):
            for z in range(1, 15):
                print(f"{Fore.LIGHTBLUE_EX}foo3: {x*y*z} => {x=} | {y=} | {z=}{Fore.RESET}")
                await sleep(0.1 * random())


run(main())
