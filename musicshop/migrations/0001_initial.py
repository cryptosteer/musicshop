# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-08 17:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genero', models.CharField(max_length=50)),
                ('album', models.CharField(max_length=50)),
                ('artista', models.CharField(max_length=50)),
                ('Año', models.CharField(max_length=50)),
                ('Valor', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DetailOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('valor', models.FloatField(null=True)),
                ('article', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='musicshop.Article')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=50)),
                ('vendedor', models.CharField(max_length=50)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('total', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipeArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cassete', models.CharField(max_length=50)),
                ('lp', models.CharField(max_length=50)),
                ('cd', models.CharField(max_length=50)),
                ('vhs', models.CharField(max_length=50)),
                ('dvd', models.CharField(max_length=50)),
                ('otros', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='tipearticle',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='musicshop.TipeArticle'),
        ),
    ]
