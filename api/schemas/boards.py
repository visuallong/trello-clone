from pydantic import BaseModel
from fastapi import Query

class CreateBoard(BaseModel):
    name: str = Query(max_length=255)