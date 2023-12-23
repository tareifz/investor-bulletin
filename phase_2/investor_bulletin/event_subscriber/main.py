from pika import BlockingConnection
from db.models import get_db
from resources.alert.alert_schema import AlertCreate
import resources.alert.alert_service as alert_service

# Create a connection object to start consuming events


def init_subscriber():
    return BlockingConnection()


def on_event(ch, method, properties, body):
    print(body)
    # I think I have committed a crime here 🫣
    alert_service.create_alert(AlertCreate.model_validate_json(body), next(get_db()))


if __name__ == "__main__":
    subscriber = init_subscriber()
    channel = subscriber.channel()
    channel.basic_consume(
        queue="alert-queue", on_message_callback=on_event, auto_ack=True
    )

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    subscriber.close()
