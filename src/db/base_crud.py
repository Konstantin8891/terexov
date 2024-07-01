from typing import Any, Generic, List, Type, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

ModelType = TypeVar("ModelType", bound=Any)


class CRUDBase(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        """
        CRUD object with default methods to Create, Read, Update, Delete (CRUD).

        **Parameters**

        * `model`: A SQLAlchemy model class

        """
        self.model = model

    async def get_list(
        self,
        db: AsyncSession,
        *,
        _select: Type[ModelType],
    ) -> List[ModelType]:
        query = select(_select)
        query = query.order_by("id")
        result = await db.exec(query)
        return result.scalars().all()
