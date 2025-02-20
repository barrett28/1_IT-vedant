from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI()

# Enable CORS to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (change this in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Sample data
products = [
    {"id": 1, "name": "Laptop", "price": 80000},
    {"id": 2, "name": "Smartphone", "price": 50000},
    {"id": 3, "name": "Headphones", "price": 5000},
]

# Root route
@app.get("/")
def home():
    return {"message": "Welcome to my API"}

# Get all products
@app.get("/products", response_model=List[dict])
def get_products():
    return products

# Get a single product by ID
@app.get("/product/{product_id}")
def get_product(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return product
    return {"error": "Product not found"}
