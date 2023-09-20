# Name: Satya Shenoy
# Due Date: 9/24/23
# Program: Assignment-2 Product Service
# Course: CMSC455
#----------------------------------------------------------------------------------------------------#
# Create a Flask application named ”Product Service” that serves as the first microservice. Implement
# the following endpoints:
# /products (GET): Retrieve a list of available grocery products, including their names, prices, and
# quantities in stock.
# /products/product id (GET): Get details about a specific product by its unique ID.
# /products (POST): Allow the addition of new grocery products to the inventory with information
# such as name, price, and quantity
#----------------------------------------------------------------------------------------------------#

import os
from flask import Flask, jsonify, request
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

products = [
    {"id": 1, "name": "Chicken","price": 15, "quantity": 50},
    {"id": 2, "name": "Apples","price": 3, "quantity": 25},
    {"id": 3, "name": "Chips", "price": 2.50, "quantity": 30}
]

# Endpoint 1: Get all products
@app.route('/products', methods=['GET'])
def get_all_products():
    return jsonify({"products": products})

# Endpoint 2: Get a specific product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((product for product in products if products["id"] == product_id), None)
    if product:
        return jsonify({"product": product})
    else:
        return jsonify({"error": "Product not found"}), 404
    
# Endpoint 3: Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    new_product = {
        "id": len(products) + 1,
        "name": request.json.get('name'),
        "price": request.json.get('price'),
        "quantity": request.json.get('quantity')
    }
    products.append(new_product)
    return jsonify({"message": "Product added", "product": new_product}), 201

if __name__ == '__main__':
    app.run(debug=True)
