from datetime import date
from typing import List

from pydantic import BaseModel


class ExpenseData(BaseModel):
    expense: str
    purchase_date: date
    unit: str
    number: int
    price: float
    cost: float


class ExpensesList(BaseModel):
    expense_data: List[ExpenseData]


class Expenses(BaseModel):
    expense: str
    expense_type: str
    expense_area: str
    purchase_date: date
    unit: str
    number: int
    price: float
    cost: float


class ExpensesAll(BaseModel):
    records: List[Expenses]
