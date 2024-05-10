# tests/test_app.py

from hashlib import sha256

import pytest

from backend.app import create_app


@pytest.fixture
def cli(event_loop, aiohttp_client):
    app = create_app()
    return event_loop.run_until_complete(aiohttp_client(app))


@pytest.mark.asyncio
async def test_hello(cli):
    resp = await cli.get("/")
    assert resp.status == 200
    text = await resp.text()
    assert "Hello, world" in text


@pytest.mark.asyncio
async def test_healthcheck(cli):
    resp = await cli.get("/healthcheck")
    assert resp.status == 200
    text = await resp.text()
    assert text == "{}"


@pytest.mark.asyncio
async def test_hash_from_string_passed(cli):
    payload = {"string": "test"}
    resp = await cli.post("/hash", data=payload)
    text = await resp.text()
    print(f"Text: {text}")
    assert resp.status == 200
    assert sha256(payload["string"].encode()).hexdigest() in text


@pytest.mark.asyncio
async def test_hash_from_string_absent_payload(cli):
    resp = await cli.post("/hash")
    assert resp.status == 400
    text = await resp.text()
    assert "validation_errors" in text


@pytest.mark.asyncio
async def test_hash_from_string_other_key(cli):
    payload = {"foo": "bar"}
    resp = await cli.post("/hash", data=payload)
    assert resp.status == 400
    text = await resp.text()
    assert "validation_errors" in text
