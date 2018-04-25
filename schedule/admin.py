from django.contrib import admin

from .models import Schedule, Room
from import_export.admin import ImportExportModelAdmin



@admin.register(Schedule)
class ScheduleAdminIE(ImportExportModelAdmin):
    pass

'''
class ScheduleAdmin(admin.ModelAdmin):

    list_display = ('program', 'annoncement', 'asignatura', 'teacher', 'room', 'day', 'hour_start', 'hour_end')
    list_display_links = ('program', 'asignatura', 'teacher')
    list_editable = ('room', 'day')

admin.site.register(Schedule, ScheduleAdmin)

'''
admin.site.register(Room)