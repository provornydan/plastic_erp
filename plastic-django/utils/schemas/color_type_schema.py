"""The module to define Color related schemas for serialization"""

from ninja import ModelSchema
from utils.models import ColorType

class ColorTypeSchema(ModelSchema):
    """Serialize and validate the PlasticType"""

    class Meta:
        """Configuration options for a ColorTypeSchema class"""

        model = ColorType
        fields = ("id", "name")
