from datetime import datetime
from typing import List, Optional

from sqlalchemy import (
    UUID,
    Column,
    ForeignKey,
    String,
    Enum as SQLAEnum,
    Integer,
    Boolean,
    DateTime,
    Table,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.models.mixin.mixin import CreationDateMixin, IsActiveMixin
from src.app.schemas.order.collect import Collect
from src.app.schemas.order.dimension import Dimension
from src.app.schemas.order.order import OrderSchema
from src.app.schemas.order.task import Task
from src.database.database_metadata import Base
from src.database.types import UUID_PK

order_photos = Table(
    "order_photos",
    Base.metadata,
    Column("order_id", ForeignKey("order.id"), primary_key=True),
    Column("photo_id", ForeignKey("photo.id"), primary_key=True),
)


class OrderORM(Base, CreationDateMixin, IsActiveMixin):
    __tablename__ = "order"

    id: Mapped[UUID_PK]
    godsend_id: Mapped[UUID] = mapped_column(
        UUID, ForeignKey("god_send.id"), nullable=False
    )
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    task: Mapped[Task] = mapped_column(
        SQLAEnum(Task), nullable=False, default=Task.Money
    )
    order_sum: Mapped[int] = mapped_column(Integer, nullable=False)
    dimension: Mapped[Dimension] = mapped_column(
        SQLAEnum(Dimension), nullable=False, default=Dimension.Rub
    )
    collect_id: Mapped[Collect] = mapped_column(
        SQLAEnum(Collect), nullable=False, default=Collect.One_time
    )
    moderator_id: Mapped[UUID] = mapped_column(ForeignKey("user.id"), nullable=False)
    check: Mapped[Optional[bool]] = mapped_column(Boolean, nullable=True)
    data_check: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    text_check: Mapped[Optional[str]] = mapped_column(String, nullable=True)

    god_send: Mapped["GodSendORM"] = relationship("GodSendORM", back_populates="order")  # type: ignore
    user: Mapped["UserORM"] = relationship("UserORM", back_populates="order")  # type: ignore
    donats: Mapped[List["DonatORM"]] = relationship("DonatORM", back_populates="order")  # type: ignore
    photos = relationship("PhotoORM", secondary=order_photos, back_populates="order")

    def get_schema(self) -> OrderSchema:
        return OrderSchema(
            id=self.id,
            user_id=self.user_id,
            god_send_id=self.god_send_id,
            title=self.title,
            description=self.description,
            task=self.task,
            order_sum=self.order_sum,
            dimension=self.dimension,
        )
