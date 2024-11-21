from ninja import ModelSchema
from stock.models import SortedRaw
from utils.schemas import ColorTypeSchema, PlaticTypeSchema

class SortedRawSchema(ModelSchema):
    raw_type: PlaticTypeSchema | None = None
    color_id : ColorTypeSchema | None = None

    class Meta:
        model = SortedRaw
        fields = ("id", "raw_type", "color_id", "amount")
