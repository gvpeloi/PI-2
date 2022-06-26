from django.db import models
from localflavor.br.models import BRPostalCodeField
from stdimage.models import StdImageField
from cpf_field.models import CPFField

#rom django.db.models.fields import CharField
#from django.utils.translation import gettext_lazy as _

#from . import validators
#from .br_states import STATE_CHOICES

class Profissional(models.Model):
    ESTADOS_CHOICES = (
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    )
    nome = models.CharField('nome', max_length=100)
    sobrenome = models.CharField('sobrenome', max_length=100)
    telefone = models.CharField('telefone', max_length=100)
    email = models.EmailField('e-mail')
    cpf = CPFField('cpf')
    postal_code = BRPostalCodeField('cep', max_length=100)
    estado = models.CharField('estado', max_length=15, choices=ESTADOS_CHOICES)
    cidade = models.CharField('cidade', max_length=50)
    atividades = models.TextField('fale sobre os serviços que voçe oferece')
    imagem = models.ImageField(upload_to='media/images/', max_length=100, default='images/profile/avatar-default-icon.png')






    def __str__(self):
        return self.nome









