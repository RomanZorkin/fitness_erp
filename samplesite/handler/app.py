import matplotlib.pyplot as plt

from bboard import models

class DashBoard:

    def __init__(self) -> None:
        self.dates = []
        self.costs = []
        self._get_expenses()
        self._draw_expenses_graph()

    def _get_expenses(self):
        expenses_plan = models.ExpensesPlan.objects.all()
        for row in expenses_plan:
            self.dates.append(row.purchase_date)
            self.costs.append(row.cost)
        
    
    def _draw_expenses_graph(self):
        import os

        current_dir = os.getcwd()
        print(current_dir)

        plt.plot(self.dates, self.costs)
        plt.savefig('samplesite/bboard/static/bboard/exp.jpg')
    