import os

HOST = os.environ.get("HOST")
DATABASE_HOST = os.environ.get("DATABASE_HOST")
# Must change for PROD
DATABASE_URL = (
    f"cockroachdb://root@{DATABASE_HOST}:26257/investor_bulletin?sslmode=disable"
)
RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST")
RABBITMQ_USER = os.environ.get("RABBITMQ_USER")
RABBITMQ_PASSWORD = os.environ.get("RABBITMQ_PASSWORD")
RAPID_API_HOST = os.getenv("RAPID_API_HOST")
RAPID_API_KEY = os.getenv("RAPID_API_KEY")
