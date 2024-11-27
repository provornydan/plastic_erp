"""The module to define Product related schemas for serialization"""


from ninja import ModelSchema, Schema
from stock.models import ProductType, ProductSerial, Product

class ProductTypeSchema(ModelSchema):
    """Serialize and validate the ProductType"""

    class Meta:
        """Configuration options for a ProductTypeSchema class"""

        model = ProductType
        fields = ("id", "name")

class ProductTypeCreateSchema(Schema):
    """Serialize and validate the ProductType Request"""

    name: str

class ProductSerialSchema(ModelSchema):
    """Serialize and validate the ProductSerial Response"""

    product_type_id: ProductTypeSchema | None = None

    class Meta:
        """Configuration options for a ProductSerialSchema class"""

        model = ProductSerial
        fields = ("id", "name", "description", "product_type")

class ProductSerialCreateSchema(Schema):
    """Serialize and validate the ProductSerial Request"""

    name: str
    description: str | None = None
    product_type_id: int | None = None

# Main Class to be used for our DB in requests
class ProductSchema(ModelSchema):
    """Serialize and validate the Product (main object) Response"""

    serial_id: ProductSerialSchema | None = None

    class Meta:
        """Configuration options for a ProductSchema class"""

        model = Product
        fields = ("id", "serial", "mixed", "mix_id", "pictures_URL")

class ProductCreateSchema(Schema):
    """Serialize and validate the Product (main object) Request"""

    serial_id: int | None = None
    mixed: bool = False
    mix_id: int
    pictures_URL: str | None = None # noqa: N815
