"""The module to define Plastic Type related models in ORM"""

from django.db import models

class PlasticType(models.Model):
    """Model declaration to specify a Plastic Type"""

    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        """Convert to string"""
        return self.name
