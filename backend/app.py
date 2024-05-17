# backend/app.py

import json
import traceback

from hashlib import sha256
from typing import List, AnyStr, Optional

from aiohttp import web


routes = web.RouteTableDef()


@routes.get("/")
async def hello(request) -> web.Response:
    """
    Returns a greeting message to check API workability.

    :param request: HTTP request object
    :type request: aiohttp.web.Request
    :return: HTTP response object
    :rtype: web.Response
    """
    return web.Response(text="Hello, world")


@routes.get("/healthcheck")
async def healthcheck(request) -> web.Response:
    """
    Returns an empty JSON and status code = 200
    for each request

    :param request: HTTP request object
    :type request: aiohttp.web.Request
    :return: HTTP response object
    :rtype: web.Response
    """
    response_obj = {}
    return web.Response(text=json.dumps(response_obj), status=200)


@routes.post("/hash")
async def hash_from_string(request) -> web.Response:
    """
    Endpoint checks if "string" field is provided within the request body.
    If "string" field is provided - calculates a hash of the given value
    using algorithm sha256.
    Returns JSON {"hash_string": <calculated hash>} and status code = 200.
    Otherwise returns JSON {"validation errors": <error description>} and
    status code = 400.
    If encountered an unexpected exception, returns JSON with exception
    traceback and status code 400.

    :param request: HTTP request object
    :type request: aiohttp.web.Request
    :return: HTTP response object
    :rtype: web.Response
    """
    try:
        data = await request.post()
        string = data.get("string")
        if not string:
            return web.Response(
                text=json.dumps(
                    {"validation_errors": "Missing 'string' query parameter"}
                ),
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
    """
    Creates an instance of web application and registers routes.
    Allows passing optional arguments via CLI such as desired host or port.

    :param argv: list of arguments passed in CLI for running
                the web-app (host, port), defaults to None
    :type argv: Optional[List[AnyStr]], optional
    :return: aiohttp application object
    :rtype: web.Application
    """
    app = web.Application()
    app.add_routes(routes)
    return app


if __name__ == "__main__":
    app = create_app()
    web.run_app(app)
