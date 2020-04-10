from pydantic import BaseModel
from pydantic import Field


class NoteIn(BaseModel):
    text: str = Field(..., min_length=3, max_length=50)
    completed: bool


class Note(NoteIn):
    id: int
