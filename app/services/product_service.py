from app.models.product import Product
from app.extensions import db

def get_all_products():
    return Product.query.all()

def get_product_by_id(product_id):
    return Product.query.get_or_404(product_id)

def create_product(data):
    new_product = Product(**data)
    db.session.add(new_product)
    db.session.commit()
    return new_product

def update_product(product_id, data):
    product = Product.query.get_or_404(product_id)
    for key, value in data.items():
        setattr(product, key, value)
    db.session.commit()
    return product

def delete_product(product_id):
    product = Product.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
