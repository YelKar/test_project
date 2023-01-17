import asyncio
import aiohttp
import webbrowser


webbrowser.register(
    "yb",
    None,
    webbrowser.BackgroundBrowser(
        "C:\\Users\\karam\\AppData\\Local\\"
        "Yandex\\YandexBrowser\\Application\\"
        "browser.exe"
    )
)


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [
            asyncio.create_task(req(f"http://192.168.1.{i}", session))
            for i in range(1, 20)
        ]
        results = await asyncio.gather(*tasks)

    for link, resp in results:
        if resp:
            webbrowser.get("yb").open_new(link)


async def req(
        link: str,
        session: aiohttp.ClientSession,
        timeout=aiohttp.ClientTimeout(total=1)
):
    try:
        async with session.get(link, timeout=timeout) as res:
            return link, await res.read()
    except asyncio.exceptions.TimeoutError:
        return link, ""


asyncio.run(main())
