

from bboard import forms, models, schemas
from bboard.handler import service

def put_periodicity(form: forms.AddService):
    service_info = service.ServiceInfo(form)
    insert_list = []
    for form_data in service_info.get_list().service_data:
        service_type = models.ServiceType.objects.get(pk=form_data.service_type)
        insert_list.append(models.ServiceCost(
            service_type=service_type,
            purchase_date=form_data.purchase_date,
            unit=form_data.unit,
            number=form_data.number,
            price=form_data.price,
            cost=form_data.cost,
        ))
    models.ServiceCost.objects.bulk_create(insert_list)
