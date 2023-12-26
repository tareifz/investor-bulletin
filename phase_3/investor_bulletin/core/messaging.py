import json
from amqpstorm import Connection, Message
import os

HOST = os.environ.get("RABBITMQ_HOST")
USER = os.environ.get("RABBITMQ_USER")
PASSWORD = os.environ.get("RABBITMQ_PASSWORD")
# Create a connection object to publish events

# Message Properties.
properties = {"content_type": "application/json"}


def publish_msg(msg, exchange, routing_key):
    broker = Connection(HOST, USER, PASSWORD)
    channel = broker.channel()
    Message.create(
        channel=channel,
        body=msg,
        properties=properties,
    ).publish(exchange=exchange, routing_key=routing_key)


def publish_json_msg(msg, exchange, routing_key):
    publish_msg(json.dumps(msg), exchange, routing_key)
