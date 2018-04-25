# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import TipoAsignatura, Materia
from import_export.admin import ImportExportModelAdmin

'''
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('name', 'tipo_asignatura', 'teacher', 'start_date', 'end_date', 'total_hours')
    list_display_links = ('teacher', 'tipo_asignatura')

'''
@admin.register(Materia)
class MateriaAdminIE(ImportExportModelAdmin):
    pass


@admin.register(TipoAsignatura)
class MateriaAdminIE(ImportExportModelAdmin):
    pass


'''
admin.site.register(TipoAsignatura)
admin.site.register(Materia, MateriaAdmin)
'''