from embed_video.fields import EmbedVideoField

from django.db import models
from django.core.urlresolvers import reverse

from mezzanine.core.models import Displayable
from mezzanine.pages.models import Page


class Video(Displayable):
    url = EmbedVideoField(unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-pub_date",)

    def get_absolute_url(self):
        url_name = "video_detail"
        kwargs = {"slug": self.slug}
        return reverse(url_name, kwargs=kwargs)


# class VideoList(Page):
#     """ Page object for holding a list of events """
#     hide_children = models.BooleanField(default=True,
#         verbose_name="Hide feeds in this container from navigation")

#     class Meta:
#         verbose_name = "Video List"

#     @property
#     def videos(self):
#         """ convenience method for getting all events in a container """
#         return list(Video.objects.all().order_by('-pub_date'))
