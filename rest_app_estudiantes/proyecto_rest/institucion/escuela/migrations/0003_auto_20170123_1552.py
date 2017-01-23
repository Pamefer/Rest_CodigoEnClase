# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0002_estudiante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='apellido',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='cedula',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='ciudad',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nombre',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='provincia',
            field=models.CharField(max_length=100, blank=True),
        ),
    ]
