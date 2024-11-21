from ninja import ModelSchema
from stock.models import ProductType, ProductSerial, Product
from utils.schemas import ColorTypeSchema, PlaticTypeSchema

class ProductTypeSchema(ModelSchema):
    class Meta:
        model = ProductType
        fields = ("id", "name")

class ProductSerialSchema(ModelSchema):
    type_id: ProductTypeSchema | None = None

    class Meta:
        model = ProductSerial
        fields = ("id", "name", "description", "type_id")

# Main Class to be used for our DB
class ProductSchema(ModelSchema):
    serial_id: ProductSerialSchema | None = None

    class Meta:
        model = Product
        fields = ("id", "serial_id", "mixed", "mix_id", "pictures_URL")