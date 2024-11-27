"""The module to define Sorted Plastic related models in ORM"""

from django.db import models
from utils.models import PlasticType, ColorType

class SortedRaw(models.Model):
    """Model declaration to initiate a Sorted Raw Plastic Table in the DB"""

    raw_type = models.ForeignKey(
        PlasticType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    color = models.ForeignKey(
        ColorType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    amount = models.FloatField()
