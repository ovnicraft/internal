from django.contrib import admin

from .models import Schedule, Room

class ScheduleAdmin(admin.ModelAdmin):

    list_display = ('program', 'annoncement', 'asignatura', 'teacher', 'room', 'day', 'hour_start', 'hour_end')
    list_display_links = ('program', 'asignatura', 'teacher')
    list_editable = ('room', 'day')

admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Room)
