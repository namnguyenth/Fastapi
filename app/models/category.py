from app.models.model_base import BareBaseModel
from sqlalchemy import Column, String, Boolean, DateTime, Integer


class Category(BareBaseModel):
    title = Column(String(255), index=True)
    priority = Column(Integer)
