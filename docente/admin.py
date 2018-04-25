# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

from .models import (
    TipoDocente,
    ContratoDocente,
    CategoriaDocente,
    Docente
)


@admin.register(TipoDocente)
class TipoDocenteAdminIE(ImportExportModelAdmin):
    pass


@admin.register(ContratoDocente)
class ContratoDocenteAdminIE(ImportExportModelAdmin):
    pass


@admin.register(CategoriaDocente)
class CatagoriaDocenteAdminIE(ImportExportModelAdmin):
    pass


@admin.register(Docente)
class DocenteAdminIE(ImportExportModelAdmin):
    pass
'''
admin.site.register(TipoDocente)
admin.site.register(ContratoDocente)
admin.site.register(CategoriaDocente)
admin.site.register(Docente)
'''


