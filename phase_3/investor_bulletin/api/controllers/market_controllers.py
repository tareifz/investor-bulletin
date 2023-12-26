from fastapi import APIRouter
from resources.market.market_service import get_market_data
from resources.market.market_schema import TickerDict

router = APIRouter()


# Get tickers data
@router.get("/")
def get_market_data_route() -> TickerDict:
    return get_market_data()
