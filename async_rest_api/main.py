from fastapi import FastAPI

from async_rest_api.api import notes
from async_rest_api.api import ping
from async_rest_api.db import database
from async_rest_api.db import engine
from async_rest_api.db import metadata

metadata.create_all(engine)
app = FastAPI()


@app.on_event('startup')
async def startup() -> None:
    await database.connect()


@app.on_event('shutdown')
async def shutdown() -> None:
    await database.disconnect()


app.include_router(ping.router)
app.include_router(notes.router, prefix='/notes', tags=['notes'])
