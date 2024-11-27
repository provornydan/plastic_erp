"""API Routing handled for Plastic Sheets tags"""

from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from ninja import Router

from stock.schemas import SheetSchema
from stock.models import Sheet

sheet_router = Router()

@sheet_router.get("/", response=list[SheetSchema], tags=["Plastic Sheets"])
def get_sheets(request: HttpRequest) -> list[SheetSchema]:
    """GET endpoint to retrieve all plastic sheet entries"""

    return Sheet.objects.all()


@sheet_router.get("/{sheet_id}/", response=SheetSchema, tags=["Plastic Sheets"])
def get_sheet(request: HttpRequest, sheet_id: str) -> list[SheetSchema]:
    """GET endpoint to retrieve a particular instance of plastic sheet entry"""

    sheet = get_object_or_404(Sheet, id=sheet_id)
    return sheet
