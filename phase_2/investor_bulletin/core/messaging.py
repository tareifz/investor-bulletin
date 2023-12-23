import json
from amqpstorm import Connection, Message
import os

HOST = os.environ.get("RABBITMQ_HOST")
USER = os.environ.get("RABBITMQ_USER")
PASSWORD = os.environ.get("RABBITMQ_PASSWORD")
# Create a connection object to publish events
broker = Connection(HOST, USER, PASSWORD)
channel = broker.channel()

# channel.exchange.declare(exchange="investor_bulletin")
# Message Properties.
properties = {"content_type": "application/json"}

# Create the message.
message = Message.create(
    channel=channel,
    body=json.dumps({"name": "test", "threshold_price": 101.0, "symbol": "AAPL"}),
    properties=properties,
)

if __name__ == "__main__":
    message.publish(
        exchange="investor_bulletin",
        routing_key="investor_bulletin.alert.THRESHOLD_ALERT",
    )
