"""API Routing handled for Unsorted Plastic tags"""

from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from ninja import Router
from typing import Dict, Type


from stock.schemas import UnsortedRawSchema, UnsortedRawCreateSchema
from stock.models import UnsortedRaw
from utils.schemas import Error
from utils.models import PlasticType



unsorted_raw_router = Router()

@unsorted_raw_router.get("/", response=list[UnsortedRawSchema], tags=["Unsorted Plastic"])
def get_unsorted_objects(request: HttpRequest) -> list[UnsortedRawSchema]:
    """GET endpoint to retrieve all unsorted plastic entries"""

    return UnsortedRaw.objects.all()

@unsorted_raw_router.get("/{unsorted_id}/", response=UnsortedRawSchema, tags=["Unsorted Plastic"])
def get_sorted_object(request: HttpRequest, unsorted_id: str) -> UnsortedRawSchema:
    """GET endpoint to retrieve a particular instance of unsorted plastic entry"""

    sorted = get_object_or_404(UnsortedRawSchema, id=unsorted_id)
    return sorted

@unsorted_raw_router.post("/", response={200: UnsortedRawSchema, 404: Error}, tags=["Unsorted Plastic"])
def create_product(request: HttpRequest, unsorted_entry: UnsortedRawCreateSchema) -> Dict[int, Type]:
    """POST endpoint to create a new entry of Unsorted Raw Plastic in the Database"""

    if unsorted_entry.raw_type_id:
        # We have the serial id in the body -> need to check if such series exists
        type_exists = PlasticType.objects.filter(id=unsorted_entry.raw_type_id).exists()
        if not type_exists:
            return 404, {"message": "Platic Type not found"}

    unsorted_raw_data = unsorted_entry.model_dump()
    unsorted_raw_model = UnsortedRaw.objects.create(**unsorted_raw_data)

    return unsorted_raw_model

