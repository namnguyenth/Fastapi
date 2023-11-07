from datetime import datetime

from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import as_declarative, declared_attr


@as_declarative()
class Base:
    __abstract__ = True
    __name__: str

    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


class BareBaseModel(Base):
    __abstract__ = True

    id = Column(Integer, primary_key=True, autoincrement=True)
    updated_date = Column(DateTime, default=datetime.now)
    updated_by = Column(String(100), index=True)
    deleted_date = Column(DateTime, default=datetime.now)
    deleted_by = Column(String(100), index=True)
