# Generated by Django 4.0.4 on 2022-06-26 20:02

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_profissional_atividades'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profissional',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to='media', variations={'thumb': (200, 200)}, verbose_name='Imagem'),
        ),
    ]
