from ninja import ModelSchema
from utils.models import PlasticType

class PlaticTypeSchema(ModelSchema):
    class Meta:
        model = PlasticType
        fields = ("id", "name")
