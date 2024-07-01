from fastapi import APIRouter

from src.apps.api.v1.currencies import router as v1_currency_router


router = APIRouter()

router.include_router(v1_currency_router, prefix="/v1/currencies", tags=["Currency"])
