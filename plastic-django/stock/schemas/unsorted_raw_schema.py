"""The module to define Unsorted Plastic related schemas for serialization"""

from ninja import ModelSchema
from stock.models import UnsortedRaw

from utils.schemas import PlaticTypeSchema

class UnsortedRawSchema(ModelSchema):
    """Serialize and validate the UnsortedRaw Response"""

    raw_type: PlaticTypeSchema | None = None

    class Meta:
        """Configuration options for a UnsortedRawSchema class"""

        model = UnsortedRaw
        fields = ("id", "raw_type", "amount")
