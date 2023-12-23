""" Alert Rule Schema """
"""_summary_
This file to abstract any validation logic for the Alert Rules
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class AlertRuleBase(BaseModel):
    name: str
    threshold_price: float
    symbol: str


# Created rule obj
class AlertRule(AlertRuleBase):
    id: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


# Create request data
class AlertRuleCreate(AlertRuleBase):
    pass


# Update request data
class AlertRulePatch(AlertRuleBase):
    name: Optional[str] = None
    threshold_price: Optional[float] = None
    symbol: Optional[str] = None
    pass
