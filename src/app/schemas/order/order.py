from typing import List
from pydantic import BaseModel, ConfigDict, UUID4

from src.app.schemas.order.dimension import Dimension
from src.app.schemas.order.task import Task


class OrderSchema(BaseModel):
    id: UUID4
    user_id: UUID4
    god_send_id: UUID4
    title: str
    description: str
    task: Task
    order_sum: int
    dimension: Dimension

    model_config = ConfigDict(from_attributes=True)
