from flask import Blueprint, jsonify, request
from flasgger import swag_from

from app.utils.swagger_definitions import *
from app.models.product import Product
from app.schemas.product_schema import ProductSchema
from app.extensions import db
#from app.utils.decorators import admin_required

products_blueprint = Blueprint('products', __name__)
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

@products_blueprint.route('/products', methods=['GET'])
@swag_from(product_list_definition)
def get_products():
    products = Product.query.all()
    return products_schema.jsonify(products), 200

@products_blueprint.route('/products/<int:id>', methods=['GET'])
@swag_from(product_detail_definition)
def get_product(id):
    product = Product.query.get_or_404(id)
    return product_schema.jsonify(product), 200

@products_blueprint.route('/products', methods=['POST'])
@swag_from(product_create_definition)
#@admin_required
def create_product():
    data = request.json
    new_product = product_schema.load(data)
    db.session.add(new_product)
    db.session.commit()
    return product_schema.jsonify(new_product), 201

@products_blueprint.route('/products/<int:id>', methods=['PUT'])
@swag_from(product_update_definition)
#@admin_required
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.json
    updated_product = product_schema.load(data, instance=product)
    db.session.commit()
    return product_schema.jsonify(updated_product), 200

@products_blueprint.route('/products/<int:id>', methods=['DELETE'])
@swag_from(product_delete_definition)
#@admin_required
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"}), 200
