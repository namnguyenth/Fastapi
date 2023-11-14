import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db

from app.helper.exception_decorator import catch_exceptions
from app.helper.paging import paginate, PaginationParams
from app.models.category import Category
from app.schemas.category_schema import CategorySchema
from app.schemas.sche_base import DataResponse
from app.services.category_services import get_category, create_category, update_category, delete_category, \
    get_list_category

logger = logging.getLogger()
router = APIRouter()


@router.get("/{id}")
# @catch_exceptions
def get_id(id) -> Any:
    """
    API Get list Category
    """
    data = get_category(id)
    return data


@router.get("")
def get(params: PaginationParams = Depends()) -> Any:
    """
    API Get list category
    """
    data = get_list_category(params)
    return data


@router.post("")
def post(params: CategorySchema) -> Any:
    """
    API Create a category
    """
    data = create_category(params)
    return data


@router.put("/{id}")
def put(params: CategorySchema, id) -> Any:
    """
    API Update a category
    """
    data = update_category(params, id)
    return data


@router.delete("/{id}")
def put(id) -> Any:
    """
    API Delete a category
    """
    data = delete_category(id)
    return data
