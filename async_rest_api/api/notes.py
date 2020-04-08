from fastapi import APIRouter

from async_rest_api.api import crud
from async_rest_api.api.models import NoteDB
from async_rest_api.api.models import NoteSchema


router = APIRouter()


@router.post('/', response_model=NoteDB, status_code=201)
async def create_note(payload: NoteSchema):
    note_id = await crud.post(payload)

    response_object = {
        'id': note_id,
        'title': payload.title,
        'description': payload.description,
    }
    return response_object
