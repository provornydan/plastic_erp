"""API Routing handled for Sorted Plastic tags"""

from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from ninja import Router

from stock.schemas import SortedRawSchema
from stock.models import SortedRaw

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
