import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db

from app.helper.paging import paginate, PaginationParams
from app.models.user import User

logger = logging.getLogger()
router = APIRouter()


@router.get("")
def get(params: PaginationParams = Depends()) -> Any:
    """
    API Get list User
    """
    try:
        _query = db.session.query(User)
        users = paginate(model=User, query=_query, params=params)
        return users
    except Exception as e:
        return HTTPException(status_code=400, detail=logger.error(e))
