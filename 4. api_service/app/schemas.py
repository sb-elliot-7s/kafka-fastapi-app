from datetime import datetime

from pydantic import BaseModel, Field
from bson import ObjectId


# _id:62769234d0590ea737668a72
# from_currency_code:"USD"
# from_currency_name:"United States Dollar"
# to_currency_code:"JPY"
# to_currency_name:"Japanese Yen"
# exchange_rate:130.55
# last_refreshed:"2022-05-07T15:27:41"
# time_zone:"UTC"
# bid_price:130.55
# ask_price:130.55

class PyObjectId(ObjectId):

    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid object_id")
        return ObjectId(v)

    @classmethod
    def __modify_schema__(cls, field_schema):
        field_schema.update(type="string")


class CurrencySchema(BaseModel):
    id: PyObjectId = Field(alias='_id')
    from_currency_code: str
    from_currency_name: str
    to_currency_code: str
    to_currency_name: str
    exchange_rate: str
    last_refreshed: datetime
    time_zone: str
    bid_price: float
    ask_price: float

    class Config:
        json_encoders = {
            ObjectId: lambda x: str(x),
            datetime: lambda v: v.strftime('%Y:%m:%d %H:%M')
        }
