import matplotlib.pyplot as plt
import pandas as pd

from bboard import models


class DashBoard:

    def __init__(self) -> None:
        self.dates = []
        self.costs = []
        self.base_frame = None
        self._get_expenses()
        self._create_frame()
        self._draw_expenses_graph()

    def _get_expenses(self):
        expenses_plan = models.ExpensesPlan.objects.all()
        for row in expenses_plan:
            self.dates.append(row.purchase_date)
            self.costs.append(row.cost)

    def _create_frame(self):
        self.base_frame = pd.DataFrame({
            'date': self.dates,
            'cost': self.costs,            
        })
        self.base_frame['date'] = pd.to_datetime(self.base_frame['date'])
        self.base_frame['surplus'] = self.base_frame['cost'].cumsum()
        self.base_frame = self.base_frame.set_index('date')

    def _draw_expenses_graph(self):
        print(self.base_frame.info())
        section = self.base_frame.resample('D').sum()
        surplus = section[section['surplus'] > 0]
        plt.plot(section.index.to_list(), section['cost'].values.tolist(), c='b')
        plt.plot(surplus.index.to_list(), surplus['surplus'].values.tolist(), c='r')
        #print(section.index.to_list())
        plt.savefig('samplesite/bboard/static/bboard/exp.jpg')
