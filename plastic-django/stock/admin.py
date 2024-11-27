"""The module controls which models should be manipulated through Admin GUI"""

from django.contrib import admin
from stock.models import ProductType, ProductSerial, Product, UnsortedRaw, SortedRaw, Shredded, Sheet


admin.site.register(ProductType)
admin.site.register(ProductSerial)
admin.site.register(Product)
admin.site.register(UnsortedRaw)
admin.site.register(SortedRaw)
admin.site.register(Shredded)
admin.site.register(Sheet)
