from django.shortcuts import get_object_or_404
from ninja import Router
from stock.schemas import ProductSchema, ProductTypeSchema, ProductSerialSchema
from stock.models import Product, ProductType, ProductSerial


product_router = Router()

@product_router.get("/", response=list[ProductSchema])
def get_products(request):
    return Product.objects.all()

@product_router.get("/{product_id}/", response=ProductSchema)
def get_product(request, product_id: str):
    product = get_object_or_404(Product, id=product_id)
    return product

product_type_router = Router()

@product_type_router.get("/", response=list[ProductTypeSchema])
def get_product_types(request):
    return ProductType.objects.all()

product_serial_router = Router()

@product_serial_router.get("/", response=list[ProductSerialSchema])
def get_product_serials(request):
    return ProductSerial.objects.all()