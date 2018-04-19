# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import (
    TipoDocente,
    ContratoDocente,
    CategoriaDocente,
    Docente
)

admin.site.register(TipoDocente)
admin.site.register(ContratoDocente)
admin.site.register(CategoriaDocente)
admin.site.register(Docente)
