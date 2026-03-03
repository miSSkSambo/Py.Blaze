from fastapi import FastAPI
from app.routes import health
from app.models.base import Base
from app.core.database import engine

app = FastAPI(title="PyBlazeX")

app.include_router(health.router)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
