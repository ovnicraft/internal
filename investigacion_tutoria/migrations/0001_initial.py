# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-18 17:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EjeInvestigacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Investigacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('start_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('end_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('results', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='InvestigacionDocente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dedicated_hours', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LineaInvestigacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tutoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eje', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investigacion_tutoria.EjeInvestigacion')),
            ],
        ),
        migrations.AddField(
            model_name='investigacion',
            name='linea_investigacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='investigacion_tutoria.LineaInvestigacion'),
        ),
    ]
