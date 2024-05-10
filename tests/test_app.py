# tests/test_app.py

from hashlib import sha256

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
async def test_hash_from_string_passed(cli):
    """
    Testing functionality of hash_from_string() function
    when expected request body with the field "string"
    is passed.
    Asserts that properly calculated hash is in the response body
    and the status code is 200.

    :param cli: instance of aiohttp app test client
    :type cli: aiohttp.test_utils.TestClient
    """
    payload = {"string": "test"}
    resp = await cli.post("/hash", data=payload)
    assert resp.status == 200
    text = await resp.text()
    assert sha256(payload["string"].encode()).hexdigest() in text


@pytest.mark.asyncio
async def test_hash_from_string_absent_payload(cli):
    """
    Testing functionality of hash_from_string() function
    when no request body passed.
    Asserts that "validation_errors" field exists in the response body
    and the status code is 400.

    :param cli: instance of aiohttp app test client
    :type cli: aiohttp.test_utils.TestClient
    """
    resp = await cli.post("/hash")
    assert resp.status == 400
    text = await resp.text()
    assert "validation_errors" in text


@pytest.mark.asyncio
async def test_hash_from_string_other_key(cli):
    """
    Testing functionality of hash_from_string() function
    when the request body contains field(s) other from "string".
    Asserts that "validation_errors" field exists in the response body
    and the status code is 400.

    :param cli: instance of aiohttp app test client
    :type cli: aiohttp.test_utils.TestClient
    """
    payload = {"foo": "bar"}
    resp = await cli.post("/hash", data=payload)
    assert resp.status == 400
    text = await resp.text()
    assert "validation_errors" in text
