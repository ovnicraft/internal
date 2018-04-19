# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from.models import Investigacion, InvestigacionDocente, EjeInvestigacion, LineaInvestigacion

# Register your models here.
admin.site.register(Investigacion)
admin.site.register(InvestigacionDocente)
admin.site.register(EjeInvestigacion)
admin.site.register(LineaInvestigacion)