import pytest
from starlette.testclient import TestClient

from async_rest_api.main import app


@pytest.fixture(scope='session')
def client():
    _client = TestClient(app)
    yield _client
