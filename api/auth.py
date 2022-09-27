from datetime import datetime, timezone, timedelta

from fastapi.responses import PlainTextResponse


async def login():
    return PlainTextResponse('vovetta')


async def hour():
    return PlainTextResponse(datetime.now(tz=timezone(timedelta(hours=3))).strftime('%H'))
