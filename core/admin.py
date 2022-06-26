from django.contrib import admin

from .models import Profissional

@admin.register(Profissional)
class ProfissionalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'telefone', 'email', 'cpf', 'postal_code', 'atividades', 'imagem')
