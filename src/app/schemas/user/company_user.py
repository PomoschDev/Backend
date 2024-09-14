from typing import List
from pydantic import BaseModel, UUID4, ConfigDict


class CompanyUserSchema(BaseModel):
    title: str
    phone: str
    address: str
    site: str
    inn: str
    kpp: str
    okpo: str
    card_number: str

    model_config = ConfigDict(from_attributes=True)
