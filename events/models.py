from datetime import datetime
from string import punctuation
from urllib import unquote

from django.db import models
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from mezzanine.pages.models import Page
from mezzanine.core.fields import FileField
from mezzanine.core.models import Displayable, RichText, Orderable
from mezzanine.utils.models import upload_to
from mezzanine.utils.sites import current_site_id


class Event(Displayable, RichText):
    """ Event object """
    start = models.DateTimeField(_("start"))
    end = models.DateTimeField(_("end"))
    location = models.TextField()
    external_url = models.URLField(blank=True, null=True)

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
        return list(Event.objects.published().filter(start__gte=datetime.now()).order_by('start'))


class EventImage(Orderable):
    """ images for events """
    event = models.ForeignKey(Event, related_name="images")
    image = FileField(_("Image"), max_length=200, format="Image",
                     upload_to=upload_to("events.EventImage.image", "events"))
    description = models.CharField(_("Description"), max_length=200, blank=True)

    class Meta:
        verbose_name = _("Image")
        verbose_name_plural = _("Images")

    def __unicode__(self):
        return self.description

    def save(self, *args, **kwargs):
        """
        If no description is given when created, create one from the
        file name.
        """
        if not self.id and not self.description:
            name = unquote(self.image.url).split("/")[-1].rsplit(".", 1)[0]
            name = name.replace("'", "")
            name = "".join([c if c not in punctuation else " " for c in name])
            name = "".join([s.upper() if i == 0 or name[i - 1] == " " else s
                            for i, s in enumerate(name)])
            self.description = name
        super(EventImage, self).save(*args, **kwargs)


def _get_current_domain():
    return Site.objects.get(id=current_site_id()).domain
