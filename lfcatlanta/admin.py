from django.contrib import admin

from .models import LFCSiteProfile


class LFCSiteProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'last_name', 'first_name', 'lfc_membership_id', 'email')

admin.site.register(LFCSiteProfile, LFCSiteProfileAdmin)