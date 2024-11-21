from django.shortcuts import get_object_or_404
from ninja import Router
from stock.schemas import SheetSchema
from stock.models import Sheet

sheet_router = Router()

@sheet_router.get("/", response=list[SheetSchema])
def get_devices(request):
    return Sheet.objects.all()