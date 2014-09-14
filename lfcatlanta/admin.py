from django.contrib import admin

from .models import LFCSiteProfile


class LFCSiteProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(LFCSiteProfile, LFCSiteProfileAdmin)