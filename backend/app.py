import json
import traceback

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
async def hash_from_string(request):
    try:
        string = request.query["string"]
        print(f"Gotten the following string from the request body: {string}")
        response_obj = {"hash_string": sha256(string.encode()).hexdigest()}
        return web.Response(text=json.dumps(response_obj), status=200)

    except Exception as e:
        tb = traceback.format_exc()
        print(f"Could not find a string within the request body! The following exception occurred: {str(e)}")
        response_obj = {"validation_errors": tb}
        return web.Response(text=json.dumps(response_obj), status=400)


app = web.Application()
app.add_routes(routes)


# todo what is it for???
def init_func(argv):
    app = web.Application()
    app.router.add_get("/", hello)
    app.router.add_get("/healthcheck", healthcheck)
    app.router.add_get("/hash", hash_from_string)
    return app


if __name__ == "__main__":
    web.run_app(app)
