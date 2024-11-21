from django.shortcuts import get_object_or_404
from ninja import Router
from stock.schemas import SortedRawSchema
from stock.models import SortedRaw

sorted_raw_router = Router()

@sorted_raw_router.get("/", response=list[SortedRawSchema])
def get_devices(request):
    return SortedRaw.objects.all()