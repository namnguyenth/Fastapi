from fastapi import APIRouter

from app.api import (
    api_user,
    api_category,
    api_item
)

router = APIRouter()

router.include_router(api_user.router, tags=["user"], prefix="/users")
router.include_router(api_category.router, tags=["category"], prefix="/category")
router.include_router(api_item.router, tags=["item"], prefix="/item")
