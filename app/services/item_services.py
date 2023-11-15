from datetime import datetime

from fastapi_sqlalchemy import db

from app.helper.exception_handler import CustomException
from app.helper.paging import paginate
from app.models.item import Item
from app.schemas.item_schema import ItemSchema


def get_list_item(params):
    _query = db.session.query(Item)
    data = paginate(model=Item, query=_query, params=params)
    return data


def get_item(id):
    _query = db.session.query(Item).filter(
        Item.id == int(id),
        # Category.deleted_by.isnot(None),
        # Category.deleted_date.isnot(None)
    ).first()

    if not _query:
        raise CustomException(http_code=400, code='400', message="Item id is not exist")

    return {
        "title": _query.name,
        "category": _query.category_id,
        "updated_date": _query.updated_date,
        "updated_by": _query.updated_by
    }


def update_item(params: ItemSchema, _id: int):
    name = params.name
    category_id = params.category_id

    _query = db.session.query(Item)
    item = _query.filter(Item.id == _id).first()
    if not item:
        raise CustomException(http_code=400, code='400', message="Category id is not exist")

    item.name = name
    item.category_id = category_id
    item.updated_date = datetime.now()
    item.updated_by = "admin"

    db.session.commit()
    db.session.close()

    return {
        "title": name,
        "category_id": category_id,
        "updated_date": datetime.now(),
        "updated_by": "admin"
    }


def create_item(params: ItemSchema):
    name = params.name
    category_id = int(params.category_id)

    _query = db.session.query(Item)
    category = _query.filter(Item.name == name).first()
    if category:
        raise CustomException(http_code=400, code='400', message="Item id is already exist")

    item = Item(
        name=name,
        category_id=category_id,
        updated_date=datetime.now(),
        updated_by="admin",
    )

    db.session.add(item)
    db.session.commit()

    return {
        "nane": name,
        "category_id": category_id,
        "updated_date": datetime.now(),
        "updated_by": "admin"
    }


def delete_item(id):
    _query = db.session.query(Item)
    item = _query.filter(Item.id == id).first()
    if not item:
        raise CustomException(http_code=400, code='400', message="Item id is already exist")

    item.updated_date = datetime.now()
    item.deleted_date = datetime.now()
    item.updated_by = "admin"
    item.deleted_by = "admin"

    db.session.commit()

    return {
        "id": id,
        "title": item.name,
        "priority": item.category_id,
        "updated_date": datetime.now(),
        "updated_by": "admin",
        "deleted_date": datetime.now(),
        "deleted_by": "admin"
    }
