import pytest

from async_rest_api.api import crud
from async_rest_api.api.models import NoteIn
from async_rest_api.db import database


@pytest.mark.asyncio
async def test_crud(monkeypatch):
    test_request_payload = NoteIn(
        text='something',
        completed=True,
    )

    test_response_payload = {
        'id': 1,
        'text': 'something',
        'completed': True,
    }

    async def mock_execute(query):
        return test_response_payload

    monkeypatch.setattr(database, 'execute', mock_execute)

    response = await crud.post(test_request_payload)
    assert test_response_payload == response
