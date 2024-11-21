from ninja import ModelSchema
from stock.models import Shredded
from utils.schemas import PlaticTypeSchema

class ShreddedSchema(ModelSchema):
    raw_type: PlaticTypeSchema | None = None

    class Meta:
        model = Shredded
        fields = ("id", "raw_type", "mixed", "mix_id", "amount")
