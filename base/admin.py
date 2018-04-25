from django.contrib import admin

from .models import AcademicAnnouncement, AcademicCenter, AcademicProgram, AcademicCycle
from import_export.admin import ImportExportModelAdmin



@admin.register(AcademicAnnouncement)
class AcademicAnnouncementAdminIE(ImportExportModelAdmin):
    pass


@admin.register(AcademicCenter)
class AcademicCenterAdminIE(ImportExportModelAdmin):
    pass


@admin.register(AcademicProgram)
class AcademicProgramAdminIE(ImportExportModelAdmin):
    pass


admin.site.register(AcademicCycle)

'''
admin.site.register(AcademicAnnouncement)
admin.site.register(AcademicCenter)
admin.site.register(AcademicProgram)
'''
