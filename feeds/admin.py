from django.contrib import admin

from mezzanine.pages.admin import PageAdmin

from .models import Feed, FeedList


class FeedAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'last_polled')
    readonly_fields = ['last_polled']

admin.site.register(Feed, FeedAdmin)
admin.site.register(FeedList, PageAdmin)
