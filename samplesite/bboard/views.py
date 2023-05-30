from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from bboard import models
from bboard.forms import AddDevice, AddService, BbForm
from bboard.repos import service, expenses

from handler.graph import DashBoard


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AddDeviceView(CreateView):
    template_name = 'bboard/add_device.html'
    form_class = AddDevice
    success_url = reverse_lazy('deviceadd')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def index(request):
    tmpdash = DashBoard()
    del tmpdash
    bbs = models.Bb.objects.all()
    context = {'bbs': bbs}
    return render(request, 'bboard/index.html', context)


def by_rubric(request, rubric_id):
    bbs = models.Bb.objects.filter(rubric=rubric_id)
    rubrics = models.Rubric.objects.all()
    current_rubric = models.Rubric.objects.get(pk=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)


def add_service(request):
    if request.method == 'POST':
        form = AddService(request.POST)
        if form.is_valid():
            service.put_periodicity(form)
    else:
        form = AddService()
    context = {'form': form}
    return render(request, 'bboard/add_service.html', context)


def expenses_sample(request):
    exp_types = models.ExpensesType.objects.all()
    exp_types = [{'pk': row.pk, 'name': row.name} for row in exp_types]
    exp_area = models.ExpensesArea.objects.all()
    exp_area = [{'pk': row.pk, 'name': row.name} for row in exp_area]
    query_data = expenses.get_sample(request).records
    rows = [row.dict() for row in query_data]
    context = {'exp_types': exp_types, 'exp_area': exp_area, 'rows': rows}
    return render(request, 'bboard/expenses_sample.html', context)
