from datetime import datetime
from pydantic import BaseModel, ConfigDict, UUID4


class DonatSchema(BaseModel):
    id: int
    user_id: UUID4
    order_id: UUID4
    summa: float
    date_done: datetime

    model_config = ConfigDict(from_attributes=True)
