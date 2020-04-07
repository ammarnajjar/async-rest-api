from fastapi import FastAPI

from async_rest_api.api import ping


app = FastAPI()

app.include_router(ping.router)
