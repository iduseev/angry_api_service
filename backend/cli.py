#backend/cli.py

# TODO should I add shebang here?

import click

from aiohttp import web

from app import create_app


@click.command()
@click.version_option("0.1.0", prog_name="angry_api_service")
@click.option("--host", default="127.0.0.1", help="IP address used as host")
@click.option("--port", default=8080, help="Port number")
def run_server(host: str, port: int):
    app = create_app()
    web.run_app(app=app, host=host, port=port)


if __name__ == "__main__":
    run_server()
