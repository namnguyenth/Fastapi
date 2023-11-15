from app.models.model_base import BareBaseModel
from sqlalchemy import Column, String, Boolean, DateTime, Integer


class Item(BareBaseModel):
    name = Column(String(255), index=True)
    category_id = Column(String(), index=True)
