from typing import List

from fastapi import APIRouter
from fastapi import HTTPException

from async_rest_api.api import crud
from async_rest_api.api.models import Note
from async_rest_api.api.models import NoteIn


router = APIRouter()


@router.post('/', response_model=Note, status_code=201)
async def create_note(payload: NoteIn):
    note_id = await crud.post(payload)

    response_object = {
        'id': note_id,
        'text': payload.text,
        'completed': payload.completed,
    }
    return response_object


@router.get('/{id}/', response_model=Note)
async def read_note(id: int):
    note = await crud.get(id)
    if not note:
        raise HTTPException(status_code=404, detail='Note not found')
    return note


@router.get('/', response_model=List[Note])
async def read_all_notes():
    return await crud.get_all()


@router.put("/{id}/", response_model=Note)
async def update_note(id: int, payload: NoteIn):
    note = await crud.get(id)
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")

    note_id = await crud.put(id, payload)
    response_object = {
        "id": note_id,
        "text": payload.text,
        "completed": payload.completed,
    }
    return response_object


@router.delete('/{id}/', response_model=Note)
async def delete_note(id: int):
    note = await crud.get(id)
    if not note:
        raise HTTPException(status_code=404, detail='Note not found')
    await crud.delete(id)
    return note
