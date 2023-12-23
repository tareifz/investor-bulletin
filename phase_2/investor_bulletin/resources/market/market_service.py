""" Market Service """
"""_summary_
this file to write any business logic for the Market
"""

import requests
import os
from db.models import TICKERS  # Questionable!

HOST = os.getenv("RAPID_API_HOST")
SECRET = os.getenv("RAPID_API_KEY")


# This is questionable; in real app, we may need to have a list of tickers
# for each user, so we fetch from API only the required companies.
def get_all_tickers():
    return TICKERS


headers = {"X-RapidAPI-Key": SECRET, "X-RapidAPI-Host": HOST}

querystring = {"interval": "1h", "symbol": ",".join(get_all_tickers())}


def get_market_data():
    response = requests.get(
        f"https://{HOST}/quote", headers=headers, params=querystring
    )

    return response.json()
