from datetime import datetime, timezone, timedelta

from PIL import Image
from aiohttp import request
from fastapi import File
from fastapi.responses import PlainTextResponse, FileResponse

IMAGE = Image.open('image.png')


async def login():
    return PlainTextResponse('vovetta')


async def hour():
    return PlainTextResponse(datetime.now(tz=timezone(timedelta(hours=3))).strftime('%H'))


async def user(user_id):
    async with request('GET', f'https://nd.kodaktor.ru/users/{user_id}') as response:
        return PlainTextResponse((await response.json())['login'])


async def decypher(key: bytes = File(), secret: bytes = File()):
    raise NotImplementedError()


async def make_image(height: int = 200, width: int = 100):
    new_image = IMAGE.resize((width, height))
    new_image.save('response.png', format='PNG')
    return FileResponse('response.png', media_type='image/png')
