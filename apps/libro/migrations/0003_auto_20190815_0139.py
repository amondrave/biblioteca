# Generated by Django 2.2.4 on 2019-08-15 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0002_libro'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creacion'),
        ),
        migrations.AddField(
            model_name='libro',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de creacion'),
        ),
    ]