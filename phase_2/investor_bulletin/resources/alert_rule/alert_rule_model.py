""" Alert Rule Model """
from sqlalchemy import Column, DateTime, Integer, String, Float, UniqueConstraint, func
from db.models.model_base import Base


# Ideally this should be linked with the user.
class AlertRule(Base):
    __tablename__ = "alert-rule"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    threshold_price = Column("threshold_price", Float)
    symbol = Column("symbol", String)
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())

    __table_args__ = (
        UniqueConstraint("threshold_price", "symbol", name="symbol_price"),
    )
