"""The module to define Color related models in ORM"""

from django.db import models

class ColorType(models.Model):
    """Model declaration to specify a Custom Color for Plastic"""

    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        """Convert to string"""
        return self.name
