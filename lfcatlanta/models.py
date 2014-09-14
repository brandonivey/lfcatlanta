from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _


class LFCSiteProfile(models.Model):
    user = models.OneToOneField("auth.User")
    date_of_birth = models.DateField()
    lfc_membership_id = models.CharField(_("LFC Membership ID"), max_length=64)
    bio = models.TextField()

    class Meta:
        verbose_name = "LFC Site Profile"
        verbose_name_plural = "LFC Site Profiles"
