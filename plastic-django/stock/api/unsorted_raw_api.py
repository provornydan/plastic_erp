from django.shortcuts import get_object_or_404
from ninja import Router
from stock.schemas import UnsortedRawSchema
from stock.models import UnsortedRaw


unsorted_raw_router = Router()

@unsorted_raw_router.get("/", response=list[UnsortedRawSchema])
def get_devices(request):
    return UnsortedRaw.objects.all()