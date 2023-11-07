import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db

from app.helper.exception_decorator import catch_exceptions
from app.helper.paging import paginate, PaginationParams
from app.models.category import Category
from app.services.category_services import get_category

logger = logging.getLogger()
router = APIRouter()


@router.get("/category")
# @catch_exceptions
def get(params: PaginationParams = Depends()) -> Any:
    """
    API Get list Category
    """
    data = get_category(params)
    return data
