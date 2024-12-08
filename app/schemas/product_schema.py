from app.extensions import ma
from app.models.product import Product

class ProductSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Product

    id = ma.auto_field()
    name = ma.Str(required=True)
    category = ma.Str(required=False)
    price = ma.Decimal(required=True)
    image_thumbnail = ma.Str(required=False)
    image_mobile = ma.Str(required=False)
    image_tablet = ma.Str(required=False)
    image_desktop = ma.Str(required=False)
