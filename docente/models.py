# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.db import models
from django .utils import timezone

# Create your models here.

class TipoDocente(models.Model):
    teacher_type = models.CharField(max_length=100)

    def __str__(self):
        return self.teacher_type


class ContratoDocente(models.Model):
    contract = models.CharField(max_length=100, verbose_name= 'Tipo de Contrato')

    def __str__(self):
        return self.contract

    class Meta:
        verbose_name = 'Tipo de Contrato'
        verbose_name_plural = 'Tipos de Contratos'


class CategoriaDocente(models.Model):
    work_category = models.CharField(max_length=100)

    def __str__(self):
        return self.work_category


class Docente(models.Model):
    name = models.CharField(max_length=100, verbose_name= 'NOMBRES')
    last_name = models.CharField(max_length=100, verbose_name='APELLIDOS')
    email = models.EmailField()
    phone = models.CharField(max_length=10, verbose_name='Telef')
    teacher_type = models.ForeignKey('TipoDocente', verbose_name='Docente', on_delete = models.CASCADE)
    contract = models.ForeignKey('ContratoDocente', verbose_name='Tipo de Contrato', on_delete = models.CASCADE)
    work_category = models.ForeignKey('CategoriaDocente', verbose_name='Categoría', on_delete = models.CASCADE)
    centro = models.ForeignKey('base.AcademicCenter', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{0} {1}'.format(self.last_name, self.name)


    class Meta:
        verbose_name = 'Docente'
        verbose_name_plural = 'Docentes'
