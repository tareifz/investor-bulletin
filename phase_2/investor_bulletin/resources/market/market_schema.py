""" Market Schema """
"""_summary_
This file to abstract any validation logic for the Market
"""

from pydantic import BaseModel

class Ticker(BaseModel):
    symbol: str
    name: str
    open: float
    close: float
    high: float
    low: float
