from fastapi import APIRouter, Depends, status

from repository import CurrencyRepository
from database import get_currency_collection
from schemas import CurrencySchema

currency_router = APIRouter(prefix='/currency', tags=['currency'])


@currency_router.get('/', status_code=status.HTTP_200_OK, response_model=CurrencySchema, response_model_by_alias=False)
async def get_currency(currency_collection=Depends(get_currency_collection)):
    return await CurrencyRepository(currency_collection=currency_collection).get_currency()


@currency_router.get('/many', status_code=status.HTTP_200_OK, response_model=list[CurrencySchema], response_model_by_alias=False)
async def get_currencies(limit: int = 5, skip: int = 0, currency_collection=Depends(get_currency_collection)):
    return await CurrencyRepository(currency_collection=currency_collection).get_currencies(limit=limit, skip=skip)
