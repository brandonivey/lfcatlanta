from copy import deepcopy

from django.contrib import admin
from mezzanine.core.admin import DisplayableAdmin

from embed_video.admin import AdminVideoMixin

from models import Video


video_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
video_fieldsets[0][1]["fields"].insert(1, "url")


class VideoAdmin(AdminVideoMixin, DisplayableAdmin):
    list_display = ('title', 'url', 'pub_date', 'status')
    fieldsets = video_fieldsets
    readonly_fields = ['pub_date']

admin.site.register(Video, VideoAdmin)
