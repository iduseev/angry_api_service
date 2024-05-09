# tests/test_app.py

import asyncio

import pytest

from aiohttp import web

from backend.app import hello, healthcheck, hash_from_string


@pytest.mark.asyncio
async def test_hello(aiohttp_client, event_loop):
    app = web.Application()
    app.router.add_get('/', hello)
    client = await aiohttp_client(app)
    resp = await client.get('/')
    assert resp.status == 200
    text = await resp.text()
    assert 'Hello, world' in text


# TODO complete tests for the rest endpoints
