from uvicorn import run
from fastapi import FastAPI
from api.routes import init_routes
from core.settings import HOST

app = init_routes(FastAPI())

if __name__ == "__main__":
    run(app, host=HOST)
