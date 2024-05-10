# backend/app.py

import json
import traceback

from hashlib import sha256
from typing import List, AnyStr, Optional

from aiohttp import web


routes = web.RouteTableDef()


@routes.get("/")
async def hello(request) -> web.Response:
    """_summary_

    :param request: _description_
    :type request: _type_
    :return: _description_
    :rtype: web.Response
    """
    return web.Response(text="Hello, world")


@routes.get("/healthcheck")
async def healthcheck(request) -> web.Response:
    """_summary_

    :param request: _description_
    :type request: _type_
    :return: _description_
    :rtype: web.Response
    """
    response_obj = {}
    return web.Response(text=json.dumps(response_obj), status=200)


@routes.post("/hash")
async def hash_from_string(request) -> web.Response:
    try:
        data = await request.post()
        string = data.get("string")
        if not string:
            return web.Response(
                text=json.dumps({"validation_errors": "Missing 'string' query parameter"}),
                status=400
            )
        response_obj = {"hash_string": sha256(string.encode()).hexdigest()}
        return web.Response(
            text=json.dumps(response_obj),
            status=200
        )
    except Exception as e:
        tb = traceback.format_exc()
        print(f"Exception occurred: {str(e)}\nTraceback: {tb}")
        response_obj = {"error": tb}
        return web.Response(
            text=json.dumps(response_obj),
            status=400
        )


def create_app(argv: Optional[List[AnyStr]] = None) -> web.Application:
    app = web.Application()
    app.add_routes(routes)
    return app


if __name__ == "__main__":
    app = create_app()
    web.run_app(app)
