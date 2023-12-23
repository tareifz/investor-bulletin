from fastapi import APIRouter
from resources.market.market_service import get_market_data
from resources.market.market_schema import Ticker

router = APIRouter()


# Get tickers data
@router.get("/")
def get_market_data_route() -> dict[str, Ticker]:
    return get_market_data()
