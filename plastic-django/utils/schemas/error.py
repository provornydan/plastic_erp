"""The module to possible error schemas for serialization"""

from ninja import Schema


class Error(Schema):
    """Serialize custom error for API Responses"""

    message: str
