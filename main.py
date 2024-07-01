from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi_pagination import add_pagination

from src.apps.api.urls import router
from src.db.session import init_db


app = FastAPI(
    title="Terexov API",
    docs_url="/api/docs",
    redoc_url="/api/redoc",
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api")

add_pagination(app)


@app.on_event("startup")
async def on_startup():
    await init_db()


@app.get("/healthchecker")
def root():
    return {"message": "Success"}
