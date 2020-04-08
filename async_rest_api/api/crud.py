from async_rest_api.api.models import NoteSchema
from async_rest_api.db import database
from async_rest_api.db import notes


async def post(payload: NoteSchema):
    query = notes.insert().values(
        title=payload.title,
        description=payload.description,
    )
    return await database.execute(query=query)
