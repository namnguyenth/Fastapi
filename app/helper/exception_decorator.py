from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError, HTTPException
from fastapi.responses import JSONResponse
import logging
from app.schemas.sche_base import ResponseSchemaBase
from fastapi.encoders import jsonable_encoder

logger = logging.getLogger()


def catch_exceptions(func):
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            return HTTPException(status_code=500, detail=logger.error(e))

    return wrapper
