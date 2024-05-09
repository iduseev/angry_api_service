import json

from hashlib import sha256

from aiohttp import web


async def handler(request) -> web.Response:
    return web.Response()


routes = web.RouteTableDef()


@routes.get("/")
async def hello(request):
    return web.Response(text="Hello, world")


@routes.get("/healthcheck")
async def healthcheck(request):
    response_obj = {}
    return web.Response(text=json.dumps(response_obj), status=200)


@routes.post("/hash")



# async def hello(request):
#     return web.Response(text="Hello, world!")

# app.add_routes([web.get("/", hello)])

app = web.Application()
app.add_routes(routes)


# todo what is it for???
def init_func(argv):
    app = web.Application()
    app.router.add_get("/", hello)
    return app


if __name__ == "__main__":
    web.run_app(app)
