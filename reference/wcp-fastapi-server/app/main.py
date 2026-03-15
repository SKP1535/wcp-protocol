from fastapi import FastAPI
from .routes import router

app = FastAPI(title="WCP Reference Server")

app.include_router(router)