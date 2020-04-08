import pytest

from async_rest_api.api import crud
from async_rest_api.api.models import NoteSchema
from async_rest_api.db import database


@pytest.mark.asyncio
async def test_crud(monkeypatch):
    test_request_payload = NoteSchema(
        title='something',
        description='something else',
    )

    test_response_payload = {
        'id': 1,
        'title': 'something',
        'description': 'something else',
    }

    async def mock_execute(query):
        return test_response_payload

    monkeypatch.setattr(database, 'execute', mock_execute)

    response = await crud.post(test_request_payload)
    assert test_response_payload == response
