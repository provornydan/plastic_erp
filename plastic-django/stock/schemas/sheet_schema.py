from ninja import ModelSchema
from stock.models import Sheet

from utils.schemas import ColorTypeSchema, PlaticTypeSchema

class SheetSchema(ModelSchema):
    raw_type: PlaticTypeSchema | None = None

    class Meta:
        model = Sheet
        fields = ("id", "raw_type", "mixed", "mix_id", "length", \
                  "width", "height", "description", "pictures_URL")