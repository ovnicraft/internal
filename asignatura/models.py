# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from datetime import datetime
from docente.models import Docente


# Create your models here.

class TipoAsignatura(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Materia(models.Model):
    name = models.CharField(max_length=100)
    tipo_asignatura = models.ForeignKey(TipoAsignatura, on_delete = models.CASCADE)
    start_date = models.DateTimeField(default=datetime.now, blank=True)
    end_date = models.DateTimeField(default=datetime.now, blank=True)
    total_hours = models.IntegerField()
    teacher = models.ForeignKey(Docente, on_delete = models.CASCADE, null=True)

    def __str__(self):
        return '{0}'.format(self.name)
