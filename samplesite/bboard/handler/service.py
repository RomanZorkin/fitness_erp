from datetime import date
from typing import List

from bboard import config, forms, schemas


class ServiceInfo():

    def __init__(self, form: forms.AddService) -> None:
        self.form = form
        self.data = form.cleaned_data
        self.start_date = config.BaseDates().start.date()
        self.date_list: List[date] = []
        self._get_start_date()
        self._create_date_list()

    def _get_start_date(self) -> None:
        self.start_date = date(
            year=self.data['periodicity_start'].year,
            month=self.data['periodicity_start'].month,
            day=int(self.data['purchase_day']),
        )

    def _add_month(self, current_date: date, delta: int) -> date:
        current_month = current_date.month
        next_year = current_date.year
        next_month = current_month + delta
        if next_month > 12:
            next_month = next_month - 12
            next_year = next_year + 1
        return date(year=next_year, month=next_month, day=current_date.day)


    def _create_date_list(self) -> None:
        new_date: date = self.start_date
        while new_date < self.data['periodicity_end']:
            if new_date < self.data['periodicity_start']:
                new_date = self._add_month(new_date, int(self.data['periodicity']))
                continue
            if new_date == self.start_date:
                self.date_list.append(new_date)
                new_date = self._add_month(new_date, int(self.data['periodicity']))
                if int(self.data['periodicity']) == 0:
                    break
                continue
            self.date_list.append(new_date)
            new_date = self._add_month(new_date, int(self.data['periodicity']))

    def get_list(self) -> schemas.ExpensesList:
        data_list = []
        for purchase_date in self.date_list:
            data_list.append(
                schemas.ExpenseData(
                    expense=self.data['service_type'],
                    purchase_date=purchase_date,
                    unit=self.data['unit'],
                    number=self.data['number'],
                    price=self.data['price'],
                    cost=self.data['cost'],
                )
            )
        return schemas.ExpensesList(expense_data=data_list)
