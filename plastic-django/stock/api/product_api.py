from django.shortcuts import get_object_or_404
from ninja import Router
from stock.schemas import ProductSchema
from stock.models import Product


product_router = Router()

@product_router.get("/", response=list[ProductSchema])
def get_products(request):
    return Product.objects.all()

@product_router.get("/{product_id}/", response=ProductSchema)
def get_product(request, product_id: str):
    product = get_object_or_404(Product, id=product_id)
    return product