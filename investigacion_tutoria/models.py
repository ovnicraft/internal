# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from docente.models import Docente
from datetime import datetime

# Create your models here.


class LineaInvestigacion(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class EjeInvestigacion(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Investigacion(models.Model):
    title = models.CharField(max_length=100)
    start_date = models.DateTimeField(default=datetime.now, blank=True)
    end_date = models.DateTimeField(default=datetime.now, blank=True)
    results = models.TextField()
    linea_investigacion = models.ForeignKey(LineaInvestigacion, on_delete = models.CASCADE)


class InvestigacionDocente(models.Model):
    dedicated_hours = models.IntegerField()
    teacher = models.ForeignKey(Docente, on_delete = models.CASCADE, null=True)


class Tutoria(models.Model):
    eje = models.ForeignKey(EjeInvestigacion, on_delete = models.CASCADE, null=True)
#    program = models.ForeignKey(Programa, on_delete = models.CASCADE)
    teacher = models.ForeignKey(Docente, on_delete = models.CASCADE, null=True)

