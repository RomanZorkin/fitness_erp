from django.core.handlers.wsgi import WSGIRequest
from django.db.models.query import QuerySet

from bboard import models


def is_valid_queryparam(param):
    return param != '' and param is not None


def filter_all(request: WSGIRequest) -> QuerySet:
    query = models.ExpensesPlan.objects.all()
    expense_contains = request.GET.get('expense_contains')
    cost_min = request.GET.get('cost_min')
    cost_max = request.GET.get('cost_max')
    date_min = request.GET.get('date_min')
    date_max = request.GET.get('date_max')
    expenses_type = request.GET.get('expenses_type')
    expenses_area = request.GET.get('expenses_area')

    if is_valid_queryparam(expense_contains):
        query = query.filter(expense__name__icontains=expense_contains)

    if is_valid_queryparam(cost_min):
        query = query.filter(cost__gte=cost_min)

    if is_valid_queryparam(cost_max):
        query = query.filter(cost__lte=cost_max)

    if is_valid_queryparam(date_min):
        query = query.filter(purchase_date__gte=date_min)

    if is_valid_queryparam(date_max):
        query = query.filter(purchase_date__lt=date_max)

    if is_valid_queryparam(expenses_type):
        query = query.filter(expense__expenses_type__pk__exact=expenses_type)

    if is_valid_queryparam(expenses_area):
        query = query.filter(expense__expense_area__pk__exact=expenses_area)

    return query
