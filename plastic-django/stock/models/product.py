"""The module to define Product related models in ORM"""

import uuid
from django.db import models

class ProductType(models.Model):
    """Model declaration to initiate Product Types Table in the DB"""

    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        """Convert to string"""
        return self.name

class ProductSerial(models.Model):
    """Model declaration to initiate Product Serials Table in the DB"""

    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    product_type = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self) -> str:
        """Convert to string"""
        return self.name

class Product(models.Model):
    """Model declaration to initiate Products  Table in the DB"""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    serial = models.ForeignKey(
        ProductSerial,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    mixed = models.BooleanField()
    mix_id = models.IntegerField()
    pictures_URL = models.TextField(null=True, blank=True) # noqa: N815
