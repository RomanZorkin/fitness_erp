from bboard import config, models, schemas

def get_all() -> schemas.ExpensesAll:
    expenses = models.ExpensesPlan.objects.all()
    expenses_list = []
    for row in expenses:
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