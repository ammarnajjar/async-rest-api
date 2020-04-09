from async_rest_api.api.models import NoteIn
from async_rest_api.db import database
from async_rest_api.db import notes


async def post(payload: NoteIn):
    query = notes.insert().values(
        text=payload.text,
        completed=payload.completed,
    )
    return await database.execute(query=query)


async def get(id: int):
    query = notes.select().where(id == notes.c.id)
    return await database.fetch_one(query=query)


async def get_all():
    query = notes.select()
    return await database.fetch_all(query=query)


async def put(id: int, payload: NoteIn):
    query = (
        notes
        .update()
        .where(id == notes.c.id)
        .values(text=payload.text, completed=payload.completed)
        .returning(notes.c.id)
    )
    return await database.execute(query=query)


async def delete(id: int):
    query = notes.delete().where(id == notes.c.id)
    return await database.execute(query=query)
