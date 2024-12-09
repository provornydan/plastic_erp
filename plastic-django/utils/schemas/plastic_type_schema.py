"""The module to define Plastic Type related schemas for serialization"""

from ninja import ModelSchema, Schema
from utils.models import PlasticType

class PlaticTypeSchema(ModelSchema):
    """Serialize and validate the PlasticType"""

    class Meta:
        """Configuration options for a PlaticTypeSchema class"""

        model = PlasticType
        fields = ("id", "name")


class RawTypePatch(Schema):
    raw_type_id: int | None = None