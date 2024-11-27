"""The module to define Shredded related models in ORM"""

from django.db import models
from utils.models import PlasticType

class Shredded(models.Model):
    """Model declaration to initiate Shredded Plastic Table in the DB"""

    raw_type = models.ForeignKey(
        PlasticType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    mixed = models.BooleanField()
    mix_id = models.IntegerField()
    amount = models.FloatField()
