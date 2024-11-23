from django.shortcuts import get_object_or_404
from ninja import Router
from stock.schemas import SortedRawSchema
from stock.models import SortedRaw

sorted_raw_router = Router()

@sorted_raw_router.get("/", response=list[SortedRawSchema])
def get_sorted_objects(request):
    return SortedRaw.objects.all()


@sorted_raw_router.get("/{sorted_id}/", response=SortedRawSchema)
def get_sorted_object(request, sorted_id: str):
    sorted = get_object_or_404(SortedRaw, id=sorted_id)
    return sorted