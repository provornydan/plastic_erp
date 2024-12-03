"""The module to define Sorted Plastic related schemas for serialization"""

from ninja import ModelSchema, Schema
from stock.models import SortedRaw
from utils.schemas import ColorTypeSchema, PlaticTypeSchema

class SortedRawSchema(ModelSchema):
    """Serialize and validate the SortedRaw Response"""

    raw_type: PlaticTypeSchema | None = None
    color : ColorTypeSchema | None = None

    class Meta:
        """Configuration options for a SortedRawSchema class"""

        model = SortedRaw
        fields = ("id", "raw_type", "color", "amount")


class SortedRawCreateSchema(Schema):
    """Serialize and validate the Sorted Raw Creation Request"""

    raw_type_id: int | None = None
    color_id : ColorTypeSchema | None = None
    amount: float = 0