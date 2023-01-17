from aiohttp import web


async def handler(request: web.Request):
    print(request.match_info.get("a"))
    return web.Response(text="Hello")


app = web.Application()
app.add_routes(
    [
        web.get("/", handler),
        web.get("/{a}", handler),
     ]
)


if __name__ == '__main__':
    web.run_app(app)
