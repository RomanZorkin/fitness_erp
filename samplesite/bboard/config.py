from datetime import datetime

from pydantic import BaseModel


class BaseDates(BaseModel):
    start: datetime = datetime(2023,7,1)
    hiring: datetime = datetime(2023,7,15)
    open: datetime = datetime(2023,8,1)


def get_period_list():
    period_list = [(0, 'единовременно'), (1, 'ежемесячно')]
    period_list.extend([(num, f'один раз в {num} месяца') for num in range(2,5)])
    period_list.extend([(num, f'один раз в {num} месяцев') for num in range(5,13)])
    return period_list
