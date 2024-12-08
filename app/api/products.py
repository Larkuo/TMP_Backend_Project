from flask import Blueprint, jsonify, request
from flasgger import swag_from

from app.services.product_service import *
from app.utils.swagger_definitions import *
from app.models.product import Product
from app.schemas.product_schema import ProductSchema
#from app.utils.decorators import admin_required

products_blueprint = Blueprint('products', __name__)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@products_blueprint.route('/products', methods=['GET'])
@swag_from(product_list_definition)
def get_products():
    products = get_all_products()
    return products_schema.jsonify(products), 200

@products_blueprint.route('/products/<int:id>', methods=['GET'])
@swag_from(product_detail_definition)
def get_product_details(id):
    product = get_product_by_id(id)
    return product_schema.jsonify(product), 200

@products_blueprint.route('/products', methods=['POST'])
@swag_from(product_create_definition)
#@admin_required
def create_product():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid data'}), 400
    new_product = create_new_product(data)
    return product_schema.jsonify(new_product), 201

@products_blueprint.route('/products/<int:id>', methods=['PUT'])
@swag_from(product_update_definition)
#@admin_required
def update_product(id):
    product = get_product_by_id(id)
    if(isinstance(product, Product)):
        data = request.json
        updated_product = update_product_by_id(id, data)
        return product_schema.jsonify(updated_product), 200

@products_blueprint.route('/products/<int:id>', methods=['DELETE'])
@swag_from(product_delete_definition)
#@admin_required
def delete_product(id):
    product = get_product_by_id(id)
    if(isinstance(product, Product)):
        delete_product_by_id(id)
        return jsonify({"message": "Product deleted successfully"}), 200
