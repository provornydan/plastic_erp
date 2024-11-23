from django.shortcuts import get_object_or_404
from ninja import Router
from stock.schemas import SheetSchema
from stock.models import Sheet

sheet_router = Router()

@sheet_router.get("/", response=list[SheetSchema])
def get_sheets(request):
    return Sheet.objects.all()


@sheet_router.get("/{sheet_id}/", response=SheetSchema)
def get_sheet(request, sheet_id: str):
    sheet = get_object_or_404(Sheet, id=sheet_id)
    return sheet