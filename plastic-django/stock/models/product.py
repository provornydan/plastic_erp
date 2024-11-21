import uuid
from django.db import models

class ProductType(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ProductSerial(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    type_id = models.ForeignKey(
        ProductType,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    
    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    serial_id = models.ForeignKey(
        ProductSerial,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    mixed = models.BooleanField()
    mix_id = models.IntegerField()
    pictures_URL = models.TextField()