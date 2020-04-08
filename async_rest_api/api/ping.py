from typing import Dict

from fastapi import APIRouter


router = APIRouter()


@router.get('/ping')
async def pong() -> Dict[str, str]:
    return {'ping': 'pong'}
