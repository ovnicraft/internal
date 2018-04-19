# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from itertools import groupby

from django.shortcuts import render
from .models import Docente
from base.models import AcademicProgram
from schedule.models import Schedule


def index(request):
    maestrias = AcademicProgram.objects.all()
    datos = []
    for m in maestrias:
        maestria = {
            'maestria': m
        }
        docentes = Docente.objects.filter(centro=m.center)
        maestria.update({'docentes': docentes})
        datos.append(maestria)
    return render(request, 'docente/index.html', {'datos': datos})


def complete(dias):
    finales = []
    semana = set(['1lunes', '2martes', '3miercoles', '4jueves', '5viernes', '6sabado'])
    horario = set(d.day for d in dias)
    res = semana - horario
    res = list(res)
    for falta in res:
        dias.insert(int(falta[0]), False)
    return dias

def docente_detail(request, pk):
    grouped_hours = []
    docente = Docente.objects.get(pk=pk)
    horario = Schedule.objects.filter(teacher=docente).order_by('hour_start')
    for hour, v in groupby(horario, lambda x: x.hour_start):
        lista = list(v)
        lista.reverse()
        grouped_hours.append({'materias': complete(lista), 'hora': hour})
    return render(request, 'docente/index2.html', {'horarios': grouped_hours, 'docente': docente})
