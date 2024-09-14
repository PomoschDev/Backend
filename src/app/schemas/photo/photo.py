from pydantic import BaseModel


class PhotoSchema(BaseModel):
    id: int
    name: str
    url: str
