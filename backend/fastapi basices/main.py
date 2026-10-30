from fastapi import FastAPI,Request
from mocData import products
from models import Product
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
def create_products(product: Product):

    products.append(product.model_dump())
    return {
        "message": "Product created successfully",
        "data": product
    }
@app.put("/update_product/{product_id}")
def update_product(product_id: int, product: Product):
    for index, p in enumerate(products):
        if p["id"] == product_id:
            products[index] = product.model_dump()
            return {
                "message": "Product updated successfully",
                "data": product
            }
    return {"error": "Product not found"}
@app.delete("/delete_product/{product_id}")
def delete_product(product_id: int):
    for index, p in enumerate(products):
        if p["id"] == product_id:
           delete_product =products.pop(index)
           return {"message": "Product deleted successfully", "data": delete_product}
    return {"error": "Product not found"}