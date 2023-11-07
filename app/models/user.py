from app.models.model_base import BareBaseModel
from sqlalchemy import Column, String, Boolean, DateTime, Integer


class User(BareBaseModel):
    username = Column(String(255), index=True)
    password = Column(String(255))
    email = Column(String(255), unique=True, index=True)

