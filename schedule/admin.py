from django.contrib import admin

from .models import Schedule, Room
from import_export.admin import ImportExportModelAdmin



#@admin.register(Schedule)
#class ScheduleAdminIE(ImportExportModelAdmin):
#    pass

@admin.register(Room)
class RoomAdminIE(ImportExportModelAdmin, admin.ModelAdmin):
    pass



class ScheduleAdmin(admin.ModelAdmin):

    list_display = ('program', 'asignatura', 'teacher', 'room', 'day', 'hour_start', 'hour_end', 'posted')
    list_display_links = ('program', 'asignatura', 'teacher')
    list_editable = ('room', 'day', 'posted')

admin.site.register(Schedule, ScheduleAdmin)

# admin.site.register(Room)
