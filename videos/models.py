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
