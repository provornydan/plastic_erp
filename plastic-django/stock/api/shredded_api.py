from django.shortcuts import get_object_or_404
from ninja import Router
from stock.schemas import ShreddedSchema
from stock.models import Shredded

shredded_router = Router()

@shredded_router.get("/", response=list[ShreddedSchema])
def get_shredded_objects(request):
    return Shredded.objects.all()

@shredded_router.get("/{shredded_id}/", response=ShreddedSchema)
def get_shredded_object(request, shredded_id: str):
    shredded = get_object_or_404(Shredded, id=shredded_id)
    return shredded