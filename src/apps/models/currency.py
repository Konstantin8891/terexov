from datetime import date

from sqlmodel import SQLModel, Field, Date


class Currency(SQLModel, table=True):
    id: int = Field(primary_key=True, unique=True, index=True, nullable=False)
    num_code: str = Field(nullable=False)
    char_code: str = Field(nullable=False)
    nominal: int = Field(nullable=False)
    value: float = Field(nullable=False)
    vunit_rate: float = Field(nullable=False)
    for_date: date = Field(nullable=False)
    name: str = Field(nullable=False)
