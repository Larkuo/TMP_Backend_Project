from app.models.product import Product
from app.extensions import db

def get_all_products():
    return Product.query.all()

def get_product_by_id(product_id):
    return db.session.get(Product, product_id)

def create_new_product(data):
    new_product = Product(**data)
    db.session.add(new_product)
    db.session.commit()
    return new_product

def update_product_by_id(product_id, data):
    product = db.session.get(Product, product_id)
    for key, value in data.items():
        setattr(product, key, value)
    db.session.commit()
    return product

def delete_product_by_id(product_id):
    product = db.session.get(Product, product_id)
    db.session.delete(product)
    db.session.commit()
