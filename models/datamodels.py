from pydantic import BaseModel, Field


class Quotes(BaseModel):
    text: Field(min_length=5)
    author: str
    tags: list[str]

