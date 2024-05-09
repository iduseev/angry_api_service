#backend/app.py

import json
import traceback

from hashlib import sha256

from aiohttp import web


async def handler(request) -> web.Response:
    return web.Response()


routes = web.RouteTableDef()


@routes.get("/")
async def hello(request) -> web.Response:
    return web.Response(text="Hello, world")


@routes.get("/healthcheck")
async def healthcheck(request) -> web.Response:
    response_obj = {}
    return web.Response(text=json.dumps(response_obj), status=200)


@routes.post("/hash")
async def hash_from_string(request) -> web.Response:
    try:
        string = request.query["string"]
        if not string:
            return web.Response(
                text=json.dumps({"validation_errors": "Missing 'string' query parameter"}),
                status=400
            )
        print(f"Gotten the following string from the request body: {string}")
        response_obj = {"hash_string": sha256(string.encode()).hexdigest()}
        return web.Response(
            text=json.dumps(response_obj),
            status=200
        )

    except Exception as e:
        tb = traceback.format_exc()
        print(f"Exception occurred: {str(e)}")
        response_obj = {"error": tb}
        return web.Response(
            text=json.dumps(response_obj),
            status=400
        )


def create_app() -> web.Application:
    app = web.Application()
    app.add_routes(routes)
    return app


# todo what is it for???
def init_func(argv) -> web.Application:
    app = web.Application()
    app.router.add_get("/", hello)
    app.router.add_get("/healthcheck", healthcheck)
    app.router.add_post("/hash", hash_from_string)
    return app


if __name__ == "__main__":
    app = create_app()
    web.run_app(app)
