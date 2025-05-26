from fastapi import FastAPI
from app.routers import student
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(student.router)

# run command: poetry run uvicorn app.main:app --reload