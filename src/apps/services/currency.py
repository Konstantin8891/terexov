from sqlmodel.ext.asyncio.session import AsyncSession

from src.apps.db.currency import DBCurrency
from src.apps.models.currency import Currency


class CurrencyService:

    @staticmethod
    async def get_currencies(db: AsyncSession):
        return await DBCurrency.get_list(db=db, _select=Currency)


currency_service = CurrencyService
