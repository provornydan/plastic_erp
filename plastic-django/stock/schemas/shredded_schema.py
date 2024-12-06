"""The module to define Shredded related schemas for serialization"""

from ninja import ModelSchema, Schema
from stock.models import Shredded
from utils.schemas import PlaticTypeSchema

class ShreddedSchema(ModelSchema):
    """Serialize and validate the Shredded Response"""

    raw_type: PlaticTypeSchema | None = None

    class Meta:
        """Configuration options for a ShreddedSchema class"""

        model = Shredded
        fields = ("id", "raw_type", "mixed", "mix_id", "amount")


class ShreddedCreateSchema(Schema):
    """Serialize and validate the Shredded Plastic Creation Request"""

    raw_type_id: int | None = None
    mixed: bool = False
    mix_id: int = 0
    amount: float = 0