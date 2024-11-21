from django.shortcuts import get_object_or_404
from ninja import Router
from stock.schemas import ShreddedSchema
from stock.models import Shredded

shredded_router = Router()

@shredded_router.get("/", response=list[ShreddedSchema])
def get_devices(request):
    return Shredded.objects.all()