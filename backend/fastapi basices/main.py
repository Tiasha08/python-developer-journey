from fastapi import FastAPI,Request
from mocData import products

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API is working"}

@app.get("/products")
def get_products():
    return products
#Path params
@app.get("/products/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"error": "Product not found"}
#query params
@app.get("/greet")
def greet_user(name:str,age:int):
    return {
        "greet":(f"hello {name}, you are {age} years old")
    }
#another way to write query params
@app.get("/greet2")
def greet_user2(request: Request):
    name = request.query_params.get("name")
    age = request.query_params.get("age")
    return {
        "greet":(f"hello {name}, you are {age} years old")
    }

#body data , headers - request heades,query params, cookies

#different types of http methods 
@app.post("/create_products")
def create_products():
    return("products created successfully")