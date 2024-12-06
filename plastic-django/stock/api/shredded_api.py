"""API Routing handled for Shredded Plastic tags"""

from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from ninja import Router
from typing import Dict, Type

from stock.schemas import ShreddedSchema, ShreddedCreateSchema
from stock.models import Shredded
from utils.models import PlasticType
from utils.schemas import Error

shredded_router = Router()

@shredded_router.get("/", response=list[ShreddedSchema], tags=["Shredded Plastic"])
def get_shredded_objects(request: HttpRequest) -> list[ShreddedSchema]:
    """GET endpoint to retrieve all shredded plastic entries"""

    return Shredded.objects.all()

@shredded_router.get("/{shredded_id}/", response=ShreddedSchema, tags=["Shredded Plastic"])
def get_shredded_object(request: HttpRequest, shredded_id: str) -> ShreddedSchema:
    """GET endpoint to retrieve a particular instance of shredded plastic entry"""

    shredded = get_object_or_404(Shredded, id=shredded_id)
    return shredded


@shredded_router.post("/", response={200: ShreddedSchema, 404: Error}, tags=["Shredded Plastic"])
def create_shredded(request: HttpRequest, shredded_entry: ShreddedCreateSchema) -> Dict[int, Type]:
    """POST endpoint to create a new entry of Shredded Plastic in the Database"""

    if shredded_entry.raw_type_id:
        # We have the platic type id in the body -> need to check if such plastic exists
        type_exists = PlasticType.objects.filter(id=shredded_entry.raw_type_id).exists()
        if not type_exists:
            return 404, {"message": "Platic Type not found"}

    shredded_plastic_data = shredded_entry.model_dump()
    shredded_plastic_model = Shredded.objects.create(**shredded_plastic_data)

    return shredded_plastic_model