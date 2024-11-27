"""The module to define Unsorted Plastic related models in ORM"""

from django.db import models
from utils.models import PlasticType

class UnsortedRaw(models.Model):
    """Model declaration to initiate an Unsorted Raw Plastic Table in the DB"""

    raw_type = models.ForeignKey(
        PlasticType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    amount = models.FloatField()

    def __str__(self) -> str:
        """Convert to string"""

        return f"Unsorted Of Plastic: {self.raw_type}. Id = {self.id}"
