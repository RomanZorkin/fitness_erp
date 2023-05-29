from datetime import date
from typing import List

from pydantic import BaseModel


class ServiceData(BaseModel):
    service_type: str
    purchase_date: date
    unit: str
    number: int
    price: float
    cost: float


class ServiceList(BaseModel):
    service_data: List[ServiceData]
