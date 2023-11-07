import datetime

from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db

from app.helper.exception_handler import CustomException
from app.helper.paging import paginate, PaginationParams
from app.models.category import Category


def get_category(params):
    _query = db.session.query(Category)
    data = paginate(model=Category, query=_query, params=params)
    return data


def create_category(params):
    title = params.get("title")
    priority = params.get("priority")

    _query = db.session.query(Category)
    category = _query.filter(Category.title == title).first()
    if category:
        raise CustomException(http_code=400, code='400', message="Category is already exist")

    new_category = Category(
        title=title,
        priority=priority,
        updated_date=datetime.now,
        updated_by="admin"
    )
    db.session.add(new_category)
    db.session.commit()

    return {
        "title": title,
        "priority": priority,
        "updated_date": datetime.now,
        "updated_by": "admin"
    }
