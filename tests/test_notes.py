import json

import pytest

from async_rest_api.api import crud
from async_rest_api.api.models import NoteIn


@pytest.fixture
def mock_note_request():
    return {
        'text': 'something',
        'completed': True,
    }


@pytest.fixture
def mock_note_response():
    return {
        'id': 1,
        'text': 'something',
        'completed': True,
    }


@pytest.fixture
def mock_updated_note_response():
    return {
        'id': 1,
        'text': 'someone',
        'completed': False,
    }


@pytest.fixture
def mock_all_notes_response():
    return [
        {
            'id': 1,
            'text': 'something',
            'completed': True,
        },
        {
            'id': 2,
            'text': 'something second',
            'completed': False,
        },
    ]


def test_create_note(
    client,
    mock_note_request,
    mock_note_response,
    monkeypatch,
):

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, 'post', mock_post)
    response = client.post('/notes/', data=json.dumps(mock_note_request))

    assert 201 == response.status_code
    assert mock_note_response == response.json()


def test_create_note_invalid_json(client):
    response = client.post('/notes/', data=json.dumps({'text': 'somethong'}))
    assert 422 == response.status_code


def test_read_note(
    client,
    mock_note_response,
    monkeypatch,
):

    async def mock_get(id: int):
        return mock_note_response

    monkeypatch.setattr(crud, 'get', mock_get)
    response = client.get('/notes/1')

    assert 200 == response.status_code
    assert mock_note_response == response.json()


def test_read_note_incorrect_id(client, monkeypatch):

    async def mock_get(id: int):
        return None

    monkeypatch.setattr(crud, 'get', mock_get)
    response = client.get('/notes/999')

    assert 404 == response.status_code
    assert 'Note not found' == response.json()['detail']


def test_read_all_notes(
    client,
    mock_all_notes_response,
    monkeypatch,
):

    async def mock_get_all():
        return mock_all_notes_response

    monkeypatch.setattr(crud, 'get_all', mock_get_all)
    response = client.get('/notes/')

    assert 200 == response.status_code
    assert mock_all_notes_response == response.json()


def test_update_note(
    client,
    mock_updated_note_response,
    monkeypatch,
):

    async def mock_get(id: int):
        return True

    async def mock_put(id: int, payload: NoteIn):
        return 1

    monkeypatch.setattr(crud, 'get', mock_get)
    monkeypatch.setattr(crud, 'put', mock_put)

    response = client.put(
        '/notes/1/',
        data=json.dumps(mock_updated_note_response),
    )

    assert 200 == response.status_code
    assert mock_updated_note_response == response.json()


@pytest.mark.parametrize(
    'id, payload, status_code',
    [
        (1, {}, 422),
        (1, {'text': 'foo'}, 422),
        (999, {'text': 'foo', 'completed': True}, 404),
    ],
)
def test_invalid_update_note(
    client,
    monkeypatch,
    id,
    payload,
    status_code,
):

    async def mock_get(id: int):
        return None

    monkeypatch.setattr(crud, 'get', mock_get)
    response = client.put(
        f'/notes/{id}/',
        data=json.dumps(payload),
    )

    assert status_code == response.status_code


def test_delete_note(client, monkeypatch, mock_note_response):

    async def mock_get(id: int):
        return mock_note_response

    async def mock_delete(id: int):
        return mock_note_response

    monkeypatch.setattr(crud, 'get', mock_get)
    monkeypatch.setattr(crud, 'delete', mock_delete)

    response = client.delete('/notes/1/')

    assert 200 == response.status_code
    assert mock_note_response == response.json()


def test_delete_note_does_not_exists(client, monkeypatch):

    async def mock_get(id: int):
        return None

    monkeypatch.setattr(crud, 'get', mock_get)
    response = client.delete('/notes/999/')

    assert 404 == response.status_code
    assert 'Note not found' == response.json()['detail']
