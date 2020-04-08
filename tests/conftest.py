import pytest
from fastapi import FastAPI
from starlette.testclient import TestClient

from async_rest_api.api.notes import router as notes_router
from async_rest_api.api.ping import router as ping_router


@pytest.fixture(scope='session')
def app():
    _app = FastAPI()
    _app.include_router(ping_router)
    _app.include_router(notes_router, prefix='/notes', tags=['notes'])
    yield _app


@pytest.fixture(scope='session')
def client(app):
    _client = TestClient(app)
    yield _client
