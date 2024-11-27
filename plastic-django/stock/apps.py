"""The module handles config classes to enhance application's customization"""

from django.apps import AppConfig


class StockConfig(AppConfig):
    """Configurations on the Stock application level"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "stock"
