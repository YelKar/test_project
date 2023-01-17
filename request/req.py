import aiohttp
import webbrowser
import asyncio


webbrowser.register(
    "yb",
    None,
    webbrowser.BackgroundBrowser(
        "C:\\Users\\karam\\"
        "AppData\\Local\\"
        "Yandex\\YandexBrowser\\Application\\"
        "browser.exe"
    )
)


async def main():
    async with aiohttp.ClientSession() as session:
        pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'
        async with session.get(pokemon_url) as resp:
            pokemon = await resp.json()
            print(pokemon['name'])


asyncio.run(main())
