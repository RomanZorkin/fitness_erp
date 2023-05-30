from django.core.handlers.wsgi import WSGIRequest

from bboard import models, schemas
from bboard.handler import expenses


def get_all() -> schemas.ExpensesAll:
    query = models.ExpensesPlan.objects.all()
    expenses_list = []
    for row in query:
        expenses_list.append(schemas.Expenses(
            expense=row.expense.name,
            expense_type=row.expense.expenses_type.name,
            expense_area=row.expense.expense_area.name,
            purchase_date=row.purchase_date,
            unit=row.unit,
            number=row.number,
            price=row.price,
            cost=row.cost,
        ))
    return schemas.ExpensesAll(records=expenses_list)


def get_sample(request: WSGIRequest) -> schemas.ExpensesAll:
    query = expenses.filter_all(request)
    expenses_list = []
    for row in query:
        expenses_list.append(schemas.Expenses(
            expense=row.expense.name,
            expense_type=row.expense.expenses_type.name,
            expense_area=row.expense.expense_area.name,
            purchase_date=row.purchase_date,
            unit=row.unit,
            number=row.number,
            price=row.price,
            cost=row.cost,
        ))
    return schemas.ExpensesAll(records=expenses_list)
