# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-08 17:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('musicshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='cliente',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='musicshop.ClientProfile'),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='vendedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='musicshop.VendedorProfile'),
        ),
    ]
