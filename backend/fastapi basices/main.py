from fastapi import FastAPI
from mocdata import data

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, World!"}