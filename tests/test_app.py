# tests/test_app.py

from hashlib import sha256
from typing import AnyStr, Dict

import pytest

from backend.app import create_app


@pytest.fixture
def cli(event_loop, aiohttp_client):
    """
    Fixture that creates an app test client

    :param event_loop: An event loop instance
    :type event_loop: asyncio.AbstractEventLoop
    :param aiohttp_client: fixture factory that creates TestClient for
                            access to tested server
    :type aiohttp_client: pytest_aiohttp.aiohttp_client
    :return: instance of an aiohttp test client
    :rtype: aiohttp.test_utils.TestClient
    """
    app = create_app()
    return event_loop.run_until_complete(aiohttp_client(app))


@pytest.mark.asyncio
async def test_hello(cli):
    """
    Testing functionality of hello() function

    :param cli: instance of aiohttp app test client
    :type cli: aiohttp.test_utils.TestClient
    """
    resp = await cli.get("/")
    assert resp.status == 200
    text = await resp.text()
    assert "Hello, world" in text


@pytest.mark.asyncio
async def test_healthcheck(cli):
    """
    Testing functionality of healthcheck() function

    :param cli: instance of aiohttp app test client
    :type cli: aiohttp.test_utils.TestClient
    """
    resp = await cli.get("/healthcheck")
    assert resp.status == 200
    text = await resp.text()
    assert text == "{}"


@pytest.mark.asyncio
@pytest.mark.parametrize("payload, expected_status_code, expected_string_in_response", [
    ({"string": "test"}, 200, sha256("test".encode()).hexdigest()),
    ({}, 400, "validation_errors"),
    ({"foo": "bar"}, 400, "validation_errors"),
])
async def test_hash_from_string(
    cli,
    payload: Dict,
    expected_status_code: int,
    expected_string_in_response: AnyStr
):
    """
    Testing functionality of hash_from_string() function
    when one of the following occurs:
    - expected request body with the field "string" is passed
    - no request body passed
    - the request body contains field(s) other from "string"

    Asserts that expected string exists within the response body
    and the status code is as expected.

    :param cli: instance of aiohttp app test client
    :type cli: aiohttp.test_utils.TestClient
    :param payload: data that is sent in a request
    :type payload: Dict
    :param expected_status_code: status code to be in the response headers
    :type expected_status_code: int
    :param expected_string_in_response: string to be in the response body
    :type expected_string_in_response: AnyStr

    """
    resp = await cli.post("/hash", data=payload)
    assert resp.status == expected_status_code
    text = await resp.text()
    assert expected_string_in_response in text
