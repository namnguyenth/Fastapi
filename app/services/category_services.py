from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db

from app.helper.exception_handler import CustomException
from app.helper.paging import paginate, PaginationParams
from app.models.category import Category
from app.schemas.category_schema import CategorySchema


def get_list_category(params):
    _query = db.session.query(Category)
    data = paginate(model=Category, query=_query, params=params)
    return data


def get_category(id):
    _query = db.session.query(Category).filter(
        Category.id == int(id),
        # Category.deleted_by.isnot(None),
        # Category.deleted_date.isnot(None)
    ).first()

    if not _query:
        raise CustomException(http_code=400, code='400', message="Category id is not exist")

    return {
        "title": _query.title,
        "priority": _query.priority,
        "updated_date": _query.updated_date,
        "updated_by": _query.updated_by
    }


def update_category(params: CategorySchema, _id: int):
    title = params.title
    priority = params.priority

    _query = db.session.query(Category)
    category = _query.filter(Category.id == _id).first()
    if not category:
        raise CustomException(http_code=400, code='400', message="Category id is not exist")

    category.title = title
    category.priority = priority
    category.updated_date = datetime.now()
    category.updated_by = "admin"

    db.session.commit()
    db.session.close()

    return {
        "title": title,
        "priority": priority,
        "updated_date": datetime.now(),
        "updated_by": "admin"
    }


def create_category(params: CategorySchema):
    title = params.title
    priority = int(params.priority)

    _query = db.session.query(Category)
    category = _query.filter(Category.title == title).first()
    if category:
        raise CustomException(http_code=400, code='400', message="Category id is already exist")

    new_category = Category(
        title=title,
        priority=priority,
        updated_date=datetime.now(),
        updated_by="admin",
    )
    db.session.add(new_category)
    db.session.commit()

    return {
        "title": title,
        "priority": priority,
        "updated_date": datetime.now(),
        "updated_by": "admin"
    }


def delete_category(id):
    _query = db.session.query(Category)
    category = _query.filter(Category.id == id).first()
    if not category:
        raise CustomException(http_code=400, code='400', message="Category id is already exist")

    category.updated_date = datetime.now()
    category.deleted_date = datetime.now()
    category.updated_by = "admin"
    category.deleted_by = "admin"

    db.session.commit()

    return {
        "id": id,
        "title": category.title,
        "priority": category.priority,
        "updated_date": datetime.now(),
        "updated_by": "admin",
        "deleted_date": datetime.now(),
        "deleted_by": "admin"
    }
