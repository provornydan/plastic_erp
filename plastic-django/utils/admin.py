"""The module controls which models should be manipulated through Admin GUI"""


from django.contrib import admin
from utils.models import ColorType, PlasticType

admin.site.register(ColorType)
admin.site.register(PlasticType)
