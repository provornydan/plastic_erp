"""API Routing handled for Unsorted Plastic tags"""

from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from ninja import Router
from stock.schemas import UnsortedRawSchema
from stock.models import UnsortedRaw


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
