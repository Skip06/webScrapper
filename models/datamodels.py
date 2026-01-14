from pydantic import BaseModel, Field


class Quotes(BaseModel):
    text:str =  Field(min_length=5)
    author: str
    tags: list[str]

