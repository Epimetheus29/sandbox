from fastapi import FastAPI

from app.routers.sorting import router as sorting_router
from app.db.database import engine
from app.db.models import Base

app = FastAPI(title="sandbox")

@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.get("/")
async def root():
    return {"message": "Welcome to Sandbox"}


@app.post("/string_changer/{text}")
async def string_changer(text: str):
    return {"message": text.swapcase()}


app.include_router(
    sorting_router,
    prefix="/sorting",
    tags=["sorting"]
)