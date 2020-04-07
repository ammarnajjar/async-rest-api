import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient

from async_rest_api.api.ping import router


@pytest.fixture(scope='session')
def app():
    _app = FastAPI()
    _app.include_router(router)
    yield _app


@pytest.fixture(scope='session')
def client(app):
    _client = TestClient(app)
    yield _client
