from celery import Celery
from celery.schedules import crontab
import os
from db.models.model_base import get_db
from core.messaging import publish_json_msg
from resources.alert_rule.alert_rule_service import (
    get_all_rules,
)
from resources.market.market_schema import TickerDict
from resources.market.market_service import get_market_data
from core.settings import RABBITMQ_HOST

# Create a celery app object to start your workers


def create_celery_app():
    return Celery("app", broker=f"amqp://{RABBITMQ_HOST}")


app = create_celery_app()
app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    "every_5_mins": {
        "task": "app.check_market_prices",
        "schedule": crontab(minute="*/5"),
        "args": (),
    },
}


@app.task
def check_market_prices():
    tickers = TickerDict.model_validate(get_market_data())
    # I'm commiting the crime again plz help 🥲
    rules = get_all_rules(next(get_db()))
    print(rules)
    for rule in rules:
        if tickers.root[rule.symbol].price >= rule.threshold_price:
            publish_json_msg(
                {
                    "name": rule.name,
                    "threshold_price": rule.threshold_price,
                    "price": tickers.root[rule.symbol].price,
                    "symbol": rule.symbol,
                },
                "investor_bulletin",
                "investor_bulletin.alert.THRESHOLD_ALERT",
            )
