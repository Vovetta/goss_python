from asyncio import run

from hypercorn.asyncio import serve, Config
from fastapi import FastAPI
from fastapi.routing import APIRoute

from api.auth import login, hour, user, decypher, make_image

app = FastAPI(routes=[
    APIRoute('/login', login, methods=['GET']),
    APIRoute('/hour', hour, methods=['GET']),
    APIRoute('/decypher', decypher, methods=['GET', 'POST']),
    APIRoute('/id/{user_id}', user, methods=['GET']),
    APIRoute('/makeimage', make_image, methods=['GET'])
])

if __name__ == '__main__':
    config = Config()
    config.bind = '0.0.0.0:8000'
    config.accesslog = '-'
    config.errorlog = '-'
    run(serve(app, config))  # type: ignore
