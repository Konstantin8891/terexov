from datetime import date
from typing import List

from pydantic import BaseModel


class CurrencySchema(BaseModel):
    id: int
    num_code: str
    char_code: str
    nominal: int
    value: float
    vunit_rate: float
    for_date: date
