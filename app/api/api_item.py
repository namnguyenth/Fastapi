import logging
from typing import Any

from fastapi import APIRouter, Depends

from app.helper.paging import PaginationParams
from app.schemas.item_schema import ItemSchema

from app.services.item_services import (
    get_item,
    get_list_item,
    update_item,
    delete_item,
    create_item
)

logger = logging.getLogger()
router = APIRouter()


@router.get("/{id}")
# @catch_exceptions
def get_id(id) -> Any:
    """
    API Get a Item
    """
    data = get_item(id)
    return data


@router.get("")
def get(params: PaginationParams = Depends()) -> Any:
    """
    API Get list category
    """
    data = get_list_item(params)
    return data


@router.post("")
def post(params: ItemSchema) -> Any:
    """
    API Create a category
    """
    data = create_item(params)
    return data


@router.put("/{id}")
def put(params: ItemSchema, id) -> Any:
    """
    API Update a category
    """
    data = update_item(params, id)
    return data


@router.delete("/{id}")
def put(id) -> Any:
    """
    API Delete a category
    """
    data = delete_item(id)
    return data
