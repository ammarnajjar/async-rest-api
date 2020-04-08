import json

from async_rest_api.api import crud


def test_create_note(client, monkeypatch):
    test_request_payload = {
        'title': 'something',
        'description': 'something else',
    }
    test_response_payload = {
        'id': 1,
        'title': 'something',
        'description': 'something else',
    }

    async def mock_post(payload):
        return 1

    monkeypatch.setattr(crud, 'post', mock_post)
    response = client.post('/notes/', data=json.dumps(test_request_payload))

    assert 201 == response.status_code
    assert test_response_payload == response.json()


def test_create_note_invalid_json(client):
    response = client.post('/notes/', data=json.dumps({'title': 'somethong'}))
    assert 422 == response.status_code
