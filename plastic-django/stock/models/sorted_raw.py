from django.db import models
from utils.models import PlasticType, ColorType

class SortedRaw(models.Model):
    raw_type = models.ForeignKey(
        PlasticType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    color_id = models.ForeignKey(
        ColorType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    amount = models.FloatField()