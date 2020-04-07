import pytest
from starlette.testclient import TestClient

from async_rest_api.main import app


@pytest.fixture(scope='module')
def client():
    client = TestClient(app)
    yield client
