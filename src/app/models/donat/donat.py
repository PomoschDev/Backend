from datetime import datetime
from src.app.models.mixin.mixin import CreationDateMixin, IsActiveMixin
from src.app.schemas.donat.donat import DonatSchema
from src.database.database_metadata import Base
from sqlalchemy import Float, Integer, String, DateTime, ForeignKey, UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship


class DonatORM(Base, CreationDateMixin, IsActiveMixin):
    __tablename__ = "donat"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("user.id"), nullable=False)
    order_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("order.id"), nullable=False)
    summa: Mapped[float] = mapped_column(Float, nullable=False)
    date_done: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    user: Mapped["UserORM"] = relationship("UserORM", back_populates="donat")  # type: ignore
    order: Mapped["OrderORM"] = relationship("OrderORM", back_populates="donat")  # type: ignore

    def get_schema(self):
        return DonatSchema(
            id=self.id,
            user_id=self.user_id,
            order_id=self.order_id,
            summa=self.summa,
            date_done=self.date_done,
        )
