"""The module to define Plastic Type related schemas for serialization"""

from ninja import ModelSchema
from utils.models import PlasticType

class PlaticTypeSchema(ModelSchema):
    """Serialize and validate the PlasticType"""

    class Meta:
        """Configuration options for a PlaticTypeSchema class"""

        model = PlasticType
        fields = ("id", "name")
