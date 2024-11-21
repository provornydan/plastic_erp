from django.db import models
from utils.models import PlasticType

class Shredded(models.Model):
    raw_type = models.ForeignKey(
        PlasticType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    mixed = models.BooleanField()
    mix_id = models.IntegerField()
    amount = models.FloatField()