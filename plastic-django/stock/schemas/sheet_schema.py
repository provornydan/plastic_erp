"""The module to define Sheets related schemas for serialization"""

from ninja import ModelSchema, Schema
from stock.models import Sheet

from utils.schemas import PlaticTypeSchema

class SheetSchema(ModelSchema):
    """Serialize and validate the Sheets Response"""

    raw_type: PlaticTypeSchema | None = None

    class Meta:
        """Configuration options for a SheetSchema class"""

        model = Sheet
        fields = ("id", "raw_type", "mixed", "mix_id", "length", \
                  "width", "height", "description", "pictures_URL")



class SheetCreateSchema(Schema):
    """Serialize and validate plastic Sheet Creation Request"""

    raw_type_id: int | None = None
    mixed: bool = False
    mix_id: int = 0
    length: float = 0
    width: float = 0
    height: float = 0
    description: str = ""
    pictures_URL: str = ""