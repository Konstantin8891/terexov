from src.apps.models.currency import Currency
from src.db.base_crud import CRUDBase


class CurrencyCRUD(CRUDBase[Currency]):
    pass


DBCurrency = CurrencyCRUD(Currency)
