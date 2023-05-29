from django.core.exceptions import ValidationError
from django.db import IntegrityError

from bboard import forms, models
from bboard.handler import service

def put_periodicity(form: forms.AddService):
    service_info = service.ServiceInfo(form)
    insert_list = []
    for form_data in service_info.get_list().expense_data:
        expense = models.Expenses.objects.get(pk=form_data.expense)
        insert_list.append(models.ExpensesPlan(
            expense=expense,
            purchase_date=form_data.purchase_date,
            unit=form_data.unit,
            number=form_data.number,
            price=form_data.price,
            cost=form_data.cost,
        ))
    print(insert_list)
    try:
        models.ExpensesPlan.objects.bulk_create(insert_list)
    except IntegrityError as error:
        print(error)
        raise ValidationError(error)
