from django.shortcuts import get_object_or_404
from ninja import Router
from stock.schemas import ProductSchema
from stock.models import Product


product_router = Router()

@product_router.get("/", response=list[ProductSchema])
def get_devices(request):
    return Product.objects.all()