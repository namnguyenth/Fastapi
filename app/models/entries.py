from app.models.model_base import BareBaseModel
from sqlalchemy import Column, String, DateTime, Integer


class Entries(BareBaseModel):
    value = Column(Integer(), index=True)
    item_id = Column(String(), index=True)
    datetime = Column(DateTime)
    note = Column(String(500), index=True)
    tag = Column(String(25), index=True)
