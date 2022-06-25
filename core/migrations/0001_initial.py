# Generated by Django 4.0.4 on 2022-06-25 02:21

import cpf_field.models
from django.db import migrations, models
import localflavor.br.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='nome')),
                ('sobrenome', models.CharField(max_length=100, verbose_name='sobrenome')),
                ('telefone', models.CharField(max_length=100, verbose_name='telefone')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('cpf', cpf_field.models.CPFField(max_length=14, verbose_name='cpf')),
                ('postal_code', localflavor.br.models.BRPostalCodeField(max_length=9, verbose_name='cep')),
                ('estado', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=15, verbose_name='estado')),
                ('cidade', models.CharField(max_length=50, verbose_name='cidade')),
                ('atividades', models.TextField(verbose_name='fale sobre os serviços que voçe oferece')),
                ('imagem', models.ImageField(upload_to='', verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Profissional',
                'verbose_name_plural': 'Profissionais',
            },
        ),
    ]
