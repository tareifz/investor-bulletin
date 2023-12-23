""" Alert Model """
from sqlalchemy import Column, DateTime, Integer, String, Float, func
from db.models.model_base import Base


# I don't want to link this table with alert rule using foreign key
# usually we will have userid and we can have a link to alert rule if we
# wanted to delete the related alerts if the user delete the rule.
class Alert(Base):
    __tablename__ = "alert"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    name = Column("name", String)
    threshold_price = Column("threshold_price", Float)
    symbol = Column("symbol", String)
    created_at = Column(DateTime(), server_default=func.now())
    updated_at = Column(DateTime(), onupdate=func.now())
