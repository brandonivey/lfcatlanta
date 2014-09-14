from django.contrib import admin

from .models import LFCSiteProfile


class LFCSiteProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'lfc_membership_id')

admin.site.register(LFCSiteProfile, LFCSiteProfileAdmin)