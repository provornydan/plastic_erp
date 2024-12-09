"""API Routing handled for Sorted Plastic tags"""

from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from ninja import Router
from typing import Dict, Type

from stock.schemas import SortedRawSchema, SortedRawCreateSchema
from stock.models import SortedRaw
from utils.models import PlasticType, ColorType
from utils.schemas import Error, RawTypePatch

sorted_raw_router = Router()

@sorted_raw_router.get("/", response=list[SortedRawSchema], tags=["Sorted Plastic"])
def get_sorted_objects(request: HttpRequest) -> list[SortedRawSchema]:
    """GET endpoint to retrieve all sorted plastic entries"""

    return SortedRaw.objects.all()


@sorted_raw_router.get("/{sorted_id}/", response=SortedRawSchema, tags=["Sorted Plastic"])
def get_sorted_object(request: HttpRequest, sorted_id: str) -> SortedRawSchema:
    """GET endpoint to retrieve a particular instance of sorted plastic entry"""

    sorted = get_object_or_404(SortedRaw, id=sorted_id)
    return sorted

@sorted_raw_router.post("/", response={200: SortedRawSchema, 404: Error}, tags=["Sorted Plastic"])
def create_sorted(request: HttpRequest, sorted_entry: SortedRawCreateSchema) -> Dict[int, Type]:
    """POST endpoint to create a new entry of Sorted Raw Plastic in the Database"""

    if sorted_entry.raw_type_id:
        # We have the platic type id in the body -> need to check if such plastic exists
        type_exists = PlasticType.objects.filter(id=sorted_entry.raw_type_id).exists()
        if not type_exists:
            return 404, {"message": "Platic Type not found"}
    
    if sorted_entry.color_id:
        color_exists = ColorType.objects.filter(id=sorted_entry.color_id).exists()
        if not color_exists:
            return 404, {"message": "Color type not found"}

    sorted_raw_data = sorted_entry.model_dump()
    sorted_raw_model = SortedRaw.objects.create(**sorted_raw_data)

    return sorted_raw_model

@sorted_raw_router.post("/{sorted_id}/set-raw-type/", response=SortedRawSchema, tags=["Sorted Plastic"])
def update_sorted(request, sorted_id, raw_type: RawTypePatch):
    """POST endpoint to update the plastic type of a sorted plastic entry"""

    sorted_entry = get_object_or_404(SortedRaw, id=sorted_id)

    if raw_type.raw_type_id:
        raw_type = get_object_or_404(PlasticType, id=raw_type.raw_type_id)
        sorted_entry.raw_type = raw_type
    else:
        sorted_entry.raw_type = None

    sorted_entry.save()
    return sorted_entry