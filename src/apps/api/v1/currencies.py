import xml.etree.ElementTree as ET

from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from fastapi_pagination import paginate, Page
from inflection import underscore
from sqlmodel.ext.asyncio.session import AsyncSession

import aiohttp

from src.apps.models.currency import Currency
from src.apps.schemas.currency import CurrencySchema
from src.apps.services.currency import currency_service
from src.db.session import get_db


router = APIRouter()


@router.get("", summary="Get currencies from db", response_model=Page[CurrencySchema])
async def get_currencies(db: AsyncSession = Depends(get_db)) -> Page[CurrencySchema]:
    return paginate(await currency_service.get_currencies(db=db))
