from django.shortcuts import get_object_or_404
from ninja import Router
from stock.schemas import UnsortedRawSchema
from stock.models import UnsortedRaw


unsorted_raw_router = Router()

@unsorted_raw_router.get("/", response=list[UnsortedRawSchema])
def get_unsorted_objects(request):
    return UnsortedRaw.objects.all()

@unsorted_raw_router.get("/{unsorted_id}/", response=UnsortedRawSchema)
def get_sorted_object(request, unsorted_id: str):
    sorted = get_object_or_404(UnsortedRawSchema, id=unsorted_id)
    return sorted