""" Market Schema """
"""_summary_
This file to abstract any validation logic for the Market
"""

from typing import Dict
from pydantic import BaseModel, RootModel


class Ticker(BaseModel):
    price: float


TickerDict = RootModel[Dict[str, Ticker]]
