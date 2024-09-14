from typing import List
from pydantic import BaseModel, UUID4, ConfigDict


class ProductShopSchema(BaseModel):
    id: UUID4
    product_name: str
    price: int
    title: str
    description: str
    quantity: int
    creator_id: UUID4

    model_config = ConfigDict(from_attributes=True)
