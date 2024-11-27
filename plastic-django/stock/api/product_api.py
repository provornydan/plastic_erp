"""API Routing handled for end Product tags (type, series, deliveries)"""


from django.shortcuts import get_object_or_404
from typing import Dict, Type
from django.http import HttpRequest
from ninja import Router

from stock.schemas import (
    ProductSchema,
    ProductCreateSchema,
    ProductTypeSchema,
    ProductTypeCreateSchema,
    ProductSerialSchema,
    ProductSerialCreateSchema
)
from stock.models import Product, ProductType, ProductSerial
from utils.schemas import Error


# From here all endpoints mark the creation of Product Types: ex. Chair, Table, etc.
# -------------------------------------- #
product_type_router = Router()

@product_type_router.get("/", response=list[ProductTypeSchema], tags=["Products"])
def get_product_types(request: HttpRequest) -> list[ProductTypeSchema]:
    """GET endpoint to retrieve all product type entries"""

    return ProductType.objects.all()

@product_type_router.post("/", response={200: ProductTypeSchema}, tags=["Products"])
def create_product_type(request: HttpRequest, product_type: ProductTypeCreateSchema) -> Dict[int, Type]:
    """POST endpoint to create a new entry of Product Type in the Database"""

    product_type_data = product_type.model_dump()
    product_type_model = ProductType.objects.create(**product_type_data)

    return product_type_model


# From here all endpoints mark the creation of Product Series based on a type
# -------------------------------------- #
product_serial_router = Router()

@product_serial_router.get("/", response=list[ProductSerialSchema], tags=["Products"])
def get_product_serials(request: HttpRequest) -> list[ProductSerialSchema]:
    """GET endpoint to retrieve all product serial entries"""

    return ProductSerial.objects.all()


@product_serial_router.post("/", response={200: ProductSerialSchema, 404: Error}, tags=["Products"])
def create_product_serial(request: HttpRequest, product_serial: ProductSerialCreateSchema) -> Dict[int, Type]:
    """POST endpoint to create a new entry of Product Serial in the Database"""

    if product_serial.product_type_id:
        # We have the type id in the body -> need to check if such type exists
        type_exists = ProductType.objects.filter(id=product_serial.product_type_id).exists()
        if not type_exists:
            return 404, {"message": "Product type not found"}


    product_serial_data = product_serial.model_dump()
    product_serial_model = ProductSerial.objects.create(**product_serial_data)

    return product_serial_model


# From here all endpoints mark the handling of particular created instances of Products
# -------------------------------------- #
product_router = Router()

@product_router.get("/", response=list[ProductSchema], tags=["Products"])
def get_products(request: HttpRequest) -> list[ProductSchema]:
    """GET endpoint to retrieve all product entries"""

    return Product.objects.all()

@product_router.get("/{product_id}/", response=ProductSchema, tags=["Products"])
def get_product(request: HttpRequest, product_id: str) -> ProductSchema:
    """GET endpoint to retrieve a particular instance of product entry by its id"""

    product = get_object_or_404(Product, id=product_id)
    return product

@product_router.post("/", response={200: ProductSchema, 404: Error}, tags=["Products"])
def create_product(request: HttpRequest, product: ProductCreateSchema) -> Dict[int, Type]:
    """POST endpoint to create a new entry of Product in the Database"""

    if product.serial_id:
        # We have the serial id in the body -> need to check if such series exists
        type_exists = ProductSerial.objects.filter(id=product.serial_id).exists()
        if not type_exists:
            return 404, {"message": "Product serial not found"}

    product_data = product.model_dump()
    product_model = Product.objects.create(**product_data)

    return product_model
