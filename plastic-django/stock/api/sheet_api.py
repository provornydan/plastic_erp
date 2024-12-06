"""API Routing handled for Plastic Sheets tags"""

from django.shortcuts import get_object_or_404
from django.http import HttpRequest
from ninja import Router
from typing import Dict, Type

from stock.schemas import SheetSchema, SheetCreateSchema
from stock.models import Sheet
from utils.schemas import Error
from utils.models import PlasticType

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


@sheet_router.post("/", response={200: SheetSchema, 404: Error}, tags=["Plastic Sheets"])
def create_sheet(request: HttpRequest, sheet_entry: SheetCreateSchema) -> Dict[int, Type]:
    """POST endpoint to create a new entry of Plastic Sheets in the Database"""

    if sheet_entry.raw_type_id:
        # We have the platic type id in the body -> need to check if such plastic exists
        type_exists = PlasticType.objects.filter(id=sheet_entry.raw_type_id).exists()
        if not type_exists:
            return 404, {"message": "Platic Type not found"}

    sheet_data = sheet_entry.model_dump()
    sheet_model = Sheet.objects.create(**sheet_data)

    return sheet_model