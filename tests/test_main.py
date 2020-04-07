import pytest
from starlette.testclient import TestClient

from async_rest_api.main import app


@pytest.fixture(scope='module')
def client():
    client = TestClient(app)
    yield client


def test_ping(client):
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.json() == {'ping': 'pong'}
