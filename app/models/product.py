from app.extensions import db

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=True)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    image_thumbnail = db.Column(db.String(255), nullable=True)
    image_mobile = db.Column(db.String(255), nullable=True)
    image_tablet = db.Column(db.String(255), nullable=True)
    image_desktop = db.Column(db.String(255), nullable=True)

    def __repr__(self):
        return f"<Product {self.name}>"
