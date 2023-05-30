import locale
from datetime import datetime, time, timedelta
from typing import Any, List

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from django.db.models import Sum
from scipy.signal import savgol_filter

from bboard import models, config

matplotlib.use('Agg')


class DashBoard:

    def __init__(self) -> None:
        self.dates: List[Any] = []
        self.cost: List[Any] = []
        self.time_series: List[Any] = []
        self.base_frame = pd.DataFrame()
        self._get_expenses()
        self._create_time_series()
        self._create_frame()
        self._draw_expenses_graph()

    def _get_expenses(self):
        group_query = models.ExpensesPlan.objects.values(
            'purchase_date',
        ).order_by('purchase_date').annotate(total=Sum('cost'))
        for row in group_query:
            self.dates.append(datetime.combine(row['purchase_date'], time()))
            self.cost.append(row['total'])

    def _create_time_series(self):
        new_date = config.BaseDates().start
        try:
            end_date = models.ExpensesPlan.objects.latest('purchase_date').purchase_date
        except:  # noqa:E722
            end_date = new_date + timedelta(days=1)
        self.time_series = []
        while new_date <= datetime.combine(end_date, time()):
            self.time_series.append(new_date)
            new_date = new_date + timedelta(days=1)

    def _create_frame(self):
        self.base_frame = pd.DataFrame({'date': self.time_series}, index=self.time_series)
        self.base_frame[['cost', 'surplus']] = 0
        self.base_frame['income'] = 0
        self.base_frame['cost'].loc[self.dates] = self.cost
        self.base_frame['income'][self.base_frame['date'] > datetime(2023, 8, 15)] = 9900
        self.base_frame['income'][self.base_frame['date'] > datetime(2023, 9, 13)] = 14850
        self.base_frame['income'][self.base_frame['date'] > datetime(2023, 9, 24)] = 19800
        self.base_frame['balance'] = self.base_frame['income'] - self.base_frame['cost']
        self.base_frame['surplus'] = self.base_frame['balance'].cumsum()
        self.base_frame.to_csv('dash.csv')

    def _get_surplus(self, tmp_df):
        surplus_x = tmp_df['surplus'].values.tolist()
        window_length = 20
        if len(surplus_x) < 20:
            window_length = len(surplus_x)
        if window_length == 2:
            return savgol_filter(surplus_x, window_length, 1)
        return savgol_filter(surplus_x, window_length, 2)

    def _draw_expenses_graph(self):
        locale.setlocale(locale.LC_ALL, '')  # установка русского языка для даты
        tmp_df = self.base_frame[self.base_frame['date'] < datetime(2023, 10, 10)].copy()
        x_tics = tmp_df.loc[tmp_df['date'].dt.day == 15]
        plt.plot(tmp_df.index.to_list(), tmp_df['cost'].values.tolist(), c='b')
        plt.plot(tmp_df.index.to_list(), tmp_df['income'].values.tolist(), c='r')
        plt.plot(tmp_df.index.to_list(), self._get_surplus(tmp_df), c='g')
        plt.xticks(
            x_tics.index.to_list(), x_tics['date'].dt.strftime('%b %y').to_list(), rotation=45,
        )
        plt.savefig('samplesite/bboard/static/bboard/exp.jpg')
        plt.close()
