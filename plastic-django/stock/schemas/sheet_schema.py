"""The module to define Sheets related schemas for serialization"""

from ninja import ModelSchema
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
