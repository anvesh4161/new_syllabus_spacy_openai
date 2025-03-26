from fastapi import FastAPI
from api.api_v1.endpoints import syllabus_check

app = FastAPI()

app.include_router(syllabus_check.router, prefix="/api/v1")

@app.get("/")
def read_root():
    return {"message": "Welcome to the Japanese Syllabus Check API!"}