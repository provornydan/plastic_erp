from django.shortcuts import get_object_or_404
from ninja import Router
from stock.schemas import (
    ProductSchema, 
    ProductTypeSchema,
    ProductTypeCreateSchema,
    ProductSerialSchema
)
from stock.models import Product, ProductType, ProductSerial
from utils.schemas import Error

# From here all endpoints mark the handling of particular created instances of Products
# -------------------------------------- #
product_router = Router()

@product_router.get("/", response=list[ProductSchema], tags=["Products"])
def get_products(request):
    return Product.objects.all()

@product_router.get("/{product_id}/", response=ProductSchema, tags=["Products"])
def get_product(request, product_id: str):
    product = get_object_or_404(Product, id=product_id)
    return product


# From here all endpoints mark the creation of Product Types: ex. Chair, Table, etc.
# -------------------------------------- #
product_type_router = Router()

@product_type_router.get("/", response=list[ProductTypeSchema], tags=["Products"])
def get_product_types(request):
    return ProductType.objects.all()

@product_type_router.post("/", response={200: ProductTypeSchema}, tags=["Products"])
def create_product_type(request, product_type: ProductTypeCreateSchema):
    product_type_data = product_type.model_dump()
    product_type_model = ProductType.objects.create(**product_type_data)

    return product_type_model


# From here all endpoints mark the creation of Product Series based on a type
# -------------------------------------- #
product_serial_router = Router()

@product_serial_router.get("/", response=list[ProductSerialSchema], tags=["Products"])
def get_product_serials(request):
    return ProductSerial.objects.all()