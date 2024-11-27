"""The module to define Sorted Plastic related schemas for serialization"""

from ninja import ModelSchema
from stock.models import SortedRaw
from utils.schemas import ColorTypeSchema, PlaticTypeSchema

class SortedRawSchema(ModelSchema):
    """Serialize and validate the SortedRaw Response"""

    raw_type: PlaticTypeSchema | None = None
    color_id : ColorTypeSchema | None = None

    class Meta:
        """Configuration options for a SortedRawSchema class"""

        model = SortedRaw
        fields = ("id", "raw_type", "color", "amount")
