from asyncio import run

from hypercorn.asyncio import serve, Config
from fastapi import FastAPI
from fastapi.routing import APIRoute

from api.auth import login, hour

app = FastAPI(routes=[
    APIRoute('/login', login, methods=['GET']),
    APIRoute('/hour', hour, methods=['GET'])
])

if __name__ == '__main__':
    config = Config()
    config.accesslog = '-'
    config.errorlog = '-'
    run(serve(app, config))  # type: ignore
