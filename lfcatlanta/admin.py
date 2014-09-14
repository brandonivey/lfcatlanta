from django.contrib import admin

from .models import LFCSiteProfile


class LFCSiteProfileAdmin(admin.ModelAdmin):
    list_display = ('user__first_name', 'user__last_name', 'lfc_membership_id')

admin.site.register(LFCSiteProfile, LFCSiteProfileAdmin)