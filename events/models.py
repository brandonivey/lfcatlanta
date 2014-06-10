from django.db import models
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from mezzanine.pages.models import Page
from mezzanine.core.models import Displayable
from mezzanine.core.models import RichText
from mezzanine.utils.sites import current_site_id


class Event(Displayable, RichText):
    """ Event object """
    start = models.DateTimeField(_("start"))
    end = models.DateTimeField(_("end"))
    location = models.TextField()

    class Meta:
        verbose_name = "Event"

    def clean(self):
        super(Event, self).clean()
        if self.start > self.end:
            raise ValidationError("Start date must be sooner than end date.")

    def get_absolute_url(self):
        url_name = "event_detail"
        kwargs = {"slug": self.slug}
        return reverse(url_name, kwargs=kwargs)


class EventContainer(Page):
    """ Page object for holding a list of events """
    hide_children = models.BooleanField(default=True, verbose_name="Hide events in this container from navigation")

    class Meta:
        verbose_name = "Event Container"

    def events(self):
        """ convenience method for getting all events in a container """
        return Event.objects.published().order_by('start')


def _get_current_domain():
    return Site.objects.get(id=current_site_id()).domain
