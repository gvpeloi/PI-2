from django.views.generic import FormView, TemplateView
from .forms import ProfissionalForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import Profissional


class IndexView(TemplateView):
    template_name = 'index.html'


def CadastroForm(request):
    if request.method == 'GET':
        form = ProfissionalForm()
        context = {'form' : form }
        return render(request, 'cadastro.html', context=context)
    else:
        request.method == 'POST'
        form = ProfissionalForm(request.POST)
        if form.is_valid():

           form.save()
           messages.success(request, 'CADASTRADO COM SUCESSO')
        context = {'form': form}
        return render(request, 'cadastro.html', context)

def LoginForm(request):
    form = ProfissionalForm
    context = {
        'form' : form
    }
    return render(request, 'login.html', context=context)

class BaseView(TemplateView):
    template_name = 'base.html'

def Lista(request):
    profissionais = Profissional,objects.all()
    return render(request, 'profissionais.html', {'prof': prof})




