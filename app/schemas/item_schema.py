import logging
from pydantic import BaseModel, Field
from typing import Optional

logger = logging.getLogger()


class ItemSchema(BaseModel):
    name: str = Field()
    category_id: int = Field()
