from datetime import datetime, time, timedelta

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
from django.db.models import Sum
from scipy.signal import savgol_filter

from bboard import models, config


class DashBoard:

    def __init__(self) -> None:
        self.dates = []
        self.cost = []
        self.time_series = []
        self.base_frame = None
        self._get_expenses()
        self._create_time_series()
        self._create_frame()
        self._draw_expenses_graph()

    def _get_expenses(self):
        group_query = models.ExpensesPlan.objects.values(
            'purchase_date',
        ).annotate(total=Sum('cost'))
        for row in group_query:
            self.dates.append(datetime.combine(row['purchase_date'], time()))
            self.cost.append(row['total'])
        print()

    def _create_time_series(self):
        new_date = config.BaseDates().start
        try:
            end_date = models.ExpensesPlan.objects.latest('purchase_date').purchase_date
        except:
            end_date = new_date + timedelta(days=1)
        self.time_series = []
        while new_date <= datetime.combine(end_date, time()):
            self.time_series.append(new_date)
            new_date = new_date + timedelta(days=1)

    def _create_frame(self):
        self.base_frame = pd.DataFrame(index=self.time_series)
        self.base_frame[['cost', 'surplus']] = 0
        self.base_frame['income'] = 30
        self.base_frame['cost'].loc[self.dates] = self.cost
        self.base_frame['balance'] = self.base_frame['income'] - self.base_frame['cost']
        self.base_frame['surplus'] = self.base_frame['balance'].cumsum()

    def _get_surplus(self):
        surplus_x = self.base_frame['surplus'].values.tolist()
        window_length = 20
        if len(surplus_x) < 20:
            window_length = len(surplus_x)
        if window_length == 2:
            return savgol_filter(surplus_x, window_length, 1)
        return savgol_filter(surplus_x, window_length, 2)

    def _draw_expenses_graph(self):
        plt.plot(self.base_frame.index.to_list(), self.base_frame['cost'].values.tolist(), c='b')
        plt.plot(self.base_frame.index.to_list(), self.base_frame['income'].values.tolist(), c='r')
        plt.plot(self.base_frame.index.to_list(), self._get_surplus(), c='g')
        plt.xticks()
        plt.savefig('samplesite/bboard/static/bboard/exp.jpg')
        plt.close()
