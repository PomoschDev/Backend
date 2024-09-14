from datetime import datetime
from pydantic import BaseModel, UUID4


class ProductBasketSchema(BaseModel):
    id: UUID4
    product_id: UUID4
    user_id: UUID4
    quantity: int
    total_price: int
    created_at: datetime
    updated_at: datetime
