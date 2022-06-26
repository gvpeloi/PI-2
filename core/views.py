from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DetailView, DeleteView
from .forms import ProfissionalForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render
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





