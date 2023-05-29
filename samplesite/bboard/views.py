from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from bboard import models
from bboard.forms import AddService, BbForm
from bboard.repos import service


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = models.Rubric.objects.all()
        return context


def index(request):
    bbs = models.Bb.objects.all()
    rubrics = models.Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics': rubrics}
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
    rubrics = models.Rubric.objects.all()
    context = {'rubrics': rubrics, 'form': form}
    return render(request, 'bboard/add_service.html', context)
