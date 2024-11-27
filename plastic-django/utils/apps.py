"""The module handles config classes to enhance application's customization"""

from django.apps import AppConfig

class UtilsConfig(AppConfig):
    """Configurations on the Utils application level"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "utils"
