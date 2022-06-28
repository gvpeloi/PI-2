from django.views import View
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from django.urls import reverse_lazy
from .models import Profissional


class IndexView(TemplateView):
    template_name = 'index.html'

class ProfissionalList(ListView):
    model = Profissional
    queryset = Profissional.objects.all()


class ProfissioanlCreate(CreateView):
    model =Profissional
    fields = '__all__'
    success_url = reverse_lazy('profissionais')


class ProfissionalUpdate(UpdateView):
    model = Profissional
    fields = '__all__'
    success_url = reverse_lazy('profissionais')

class ProfissionalDetail(DetailView):
    queryset = Profissional.objects.all()


class ProfissionalDelete(DeleteView):
    queryset = Profissional.objects.all()
    success_url = reverse_lazy('profissionais')






