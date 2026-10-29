from fastapi import FastAPI
from mocData import products

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working"}

@app.get("/products")
def get_products():
    return products