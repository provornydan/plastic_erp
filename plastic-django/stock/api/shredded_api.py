"""API Routing handled for Shredded Plastic tags"""

from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from ninja import Router

from stock.schemas import ShreddedSchema
from stock.models import Shredded

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
