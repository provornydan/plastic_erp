"""The module to define Shredded related schemas for serialization"""

from ninja import ModelSchema
from stock.models import Shredded
from utils.schemas import PlaticTypeSchema

class ShreddedSchema(ModelSchema):
    """Serialize and validate the Shredded Response"""

    raw_type: PlaticTypeSchema | None = None

    class Meta:
        """Configuration options for a ShreddedSchema class"""

        model = Shredded
        fields = ("id", "raw_type", "mixed", "mix_id", "amount")
