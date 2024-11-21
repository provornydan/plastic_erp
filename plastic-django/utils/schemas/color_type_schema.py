from ninja import ModelSchema
from utils.models import ColorType

class ColorTypeSchema(ModelSchema):
    class Meta:
        model = ColorType
        fields = ("id", "name")
