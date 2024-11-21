from django.db import models
from utils.models import PlasticType

class Sheet(models.Model):
    raw_type = models.ForeignKey(
        PlasticType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    mixed = models.BooleanField()
    mix_id = models.IntegerField()
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    description = models.TextField()
    pictures_URL = models.TextField()