from django.contrib import admin
from swengs.homework.models import Event
from . import models


class EventAdmin(admin.ModelAdmin):
    list_display  = ('event_name', 'event_date')
    search_fields = ('event_name', 'event_date')
    sortable_by = ('event_name', 'event_date')
admin.site.register(Event,EventAdmin)