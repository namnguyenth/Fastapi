import logging
from pydantic import BaseModel, Field
from typing import Optional

logger = logging.getLogger()


class CategorySchema(BaseModel):
    title: str = Field()
    priority: Optional[int]
