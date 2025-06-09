from fastapi import FastAPI
from rates import get_yields

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello from FastAPI!"}

@app.get("/yields")
def read_yields():
    return get_yields()