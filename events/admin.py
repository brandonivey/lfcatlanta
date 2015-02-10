from django.contrib import admin
from copy import deepcopy

from mezzanine.core.admin import DisplayableAdmin, TabularDynamicInlineAdmin
from mezzanine.pages.admin import PageAdmin

from .models import Event, EventContainer, EventImage


class EventImageInline(TabularDynamicInlineAdmin):
    model = EventImage


class EventAdmin(DisplayableAdmin):
    date_hierarchy = 'start'
    inlines = (EventImageInline,)
    list_display = ("title", "start", "status")
    fieldsets = (
        (None, {
            "fields": ["title", "status"],
        }),
        ("Event details", {
            'fields': ('content', 'start', 'end', 'location', 'external_url')
        }),
        deepcopy(DisplayableAdmin.fieldsets[1]),
    )

admin.site.register(Event, EventAdmin)
admin.site.register(EventContainer, PageAdmin)
