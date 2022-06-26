from django.views.generic import  TemplateView, ListView, CreateView
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





