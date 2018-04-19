from django.contrib import admin

from .models import AcademicAnnouncement, AcademicCenter, AcademicProgram

admin.site.register(AcademicAnnouncement)
admin.site.register(AcademicCenter)
admin.site.register(AcademicProgram)
