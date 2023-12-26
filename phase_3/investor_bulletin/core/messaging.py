import json
from amqpstorm import Connection, Message
import os
from core.settings import RABBITMQ_HOST, RABBITMQ_USER, RABBITMQ_PASSWORD

# Create a connection object to publish events

# Message Properties.
properties = {"content_type": "application/json"}


def publish_msg(msg, exchange, routing_key):
    broker = Connection(RABBITMQ_HOST, RABBITMQ_USER, RABBITMQ_PASSWORD)
    channel = broker.channel()
    Message.create(
        channel=channel,
        body=msg,
        properties=properties,
    ).publish(exchange=exchange, routing_key=routing_key)


def publish_json_msg(msg, exchange, routing_key):
    publish_msg(json.dumps(msg), exchange, routing_key)
