from datetime import datetime
from typing import List
from pydantic import BaseModel, ConfigDict, UUID4

from src.app.schemas.godsend.category import CategoryGodSend


class GodSendSchema(BaseModel):
    id: UUID4
    name: str
    card_number: str
    country: str
    city_id: str
    address: str

    model_config = ConfigDict(from_attributes=True)
