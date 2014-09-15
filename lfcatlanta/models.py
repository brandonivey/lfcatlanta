from django.db import models
from django.utils.translation import ugettext, ugettext_lazy as _


class LFCSiteProfile(models.Model):
    user = models.OneToOneField("auth.User")
    date_of_birth = models.DateField(blank=True, null=True)
    lfc_membership_id = models.CharField(_("LFC Membership ID"), max_length=64, blank=True, default='')
    phone = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = "LFC Site Profile"
        verbose_name_plural = "LFC Site Profiles"

    @property
    def full_name(self):
        return u'%s %s' % (self.user.first_name, self.user.last_name)

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def email(self):
        return self.user.email
