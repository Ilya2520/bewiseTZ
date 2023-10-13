from fastapi import FastAPI
from app.crud import app as crud

app = FastAPI()

app.include_router(crud)


