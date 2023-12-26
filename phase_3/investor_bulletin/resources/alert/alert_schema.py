""" Alert Schema """
"""_summary_
This file to abstract any validation logic for the Alerts
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class AlertBase(BaseModel):
    name: str
    threshold_price: float
    price: float
    symbol: str


# Created Alert obj
class Alert(AlertBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


# Create request data
class AlertCreate(AlertBase):
    pass
