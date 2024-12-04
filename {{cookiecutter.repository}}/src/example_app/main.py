"""
Setup:
    pip install fastapi uvicorn

Run:
    uvicorn main:app --reload
"""

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello_world() -> dict[str, str]:
    return {"Hello": "World"}
