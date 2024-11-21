from ninja import ModelSchema
from stock.models import UnsortedRaw

from utils.schemas import ColorTypeSchema, PlaticTypeSchema

class UnsortedRawSchema(ModelSchema):
    raw_type: PlaticTypeSchema | None = None

    class Meta:
        model = UnsortedRaw
        fields = ("id", "raw_type", "amount")