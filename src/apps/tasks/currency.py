import asyncio
import xml.etree.ElementTree as ET
from datetime import datetime

import aiohttp
from fastapi import HTTPException
from inflection import underscore

from src.apps.models.currency import Currency
from src.core.celery_config import celery_app
from src.db.session import async_session


async def download_currencies() -> None:
    try:
        db = async_session()
        async with aiohttp.ClientSession() as session:
            async with session.get("https://cbr.ru/scripts/XML_daily.asp") as response:
                tree = ET.fromstringlist(await response.text())

                for i in range(len(tree)):
                    currency_model = Currency()
                    for_date = tree.get("Date")
                    for_date = datetime.strptime(for_date, "%d.%m.%Y")
                    for j in range(len(tree[0])):
                        value = tree[i][j].text
                        field = underscore(tree[i][j].tag)
                        if field in ("value", "vunit_rate"):
                            value = value.replace(",", ".")
                            value = float(value)
                        if field == "nominal":
                            value = int(value)
                        setattr(currency_model, field, value)
                        setattr(currency_model, "for_date", for_date)
                    db.add(currency_model)
                await db.commit()
        db.close()
    except Exception:
        raise HTTPException(status_code=408, detail="Сервис недоступен")


@celery_app.task
def download_currencies_task(*args):
    asyncio.run(download_currencies())
