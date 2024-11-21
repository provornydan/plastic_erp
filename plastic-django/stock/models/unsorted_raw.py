from django.db import models
from utils.models import PlasticType

class UnsortedRaw(models.Model):
    raw_type = models.ForeignKey(
        PlasticType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    amount = models.FloatField()

    def __str__(self):
        return f"Unsorted Of Plastic: {self.raw_type}. Id = {self.id}" 