"""
URL configuration for plastic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/

Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""

from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from stock.api.sorted_raw_api import sorted_raw_router
from stock.api.unsorted_raw_api import unsorted_raw_router
from stock.api.shredded_api import shredded_router
from stock.api.sheet_api import sheet_router
from stock.api.product_api import product_router, product_type_router, product_serial_router


api = NinjaAPI(title="Plastic ERP API")

# Register the routers from the apps
api.add_router("/sorted_raw/", sorted_raw_router)
api.add_router("/unsorted_raw/", unsorted_raw_router)
api.add_router("/shredded/", shredded_router)
api.add_router("/sheet/", sheet_router)
api.add_router("/product/", product_router)
api.add_router("/product_types/", product_type_router)
api.add_router("/product_serials/", product_serial_router)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", api.urls)
]
