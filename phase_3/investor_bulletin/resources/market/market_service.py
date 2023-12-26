""" Market Service """
"""_summary_
this file to write any business logic for the Market
"""

import requests
import os
from db.models import TICKERS  # Questionable!
from core.settings import RAPID_API_HOST, RAPID_API_KEY


# This is questionable; in real app, we may need to have a list of tickers
# for each user, so we fetch from API only the required companies.
def get_all_tickers():
    return TICKERS


headers = {"X-RapidAPI-Key": RAPID_API_KEY, "X-RapidAPI-Host": RAPID_API_HOST}

querystring = {"symbol": ",".join(get_all_tickers())}


# I used the wrong endpoint before xD.
def get_market_data():
    response = requests.get(
        f"https://{RAPID_API_HOST}/price", headers=headers, params=querystring
    )

    return response.json()
