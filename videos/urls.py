from __future__ import unicode_literals

from django.conf.urls import patterns, url


urlpatterns = patterns(
    "videos.views",
    url(r"^(?P<slug>.*)/$", "video_detail", name="video_detail"),
    url(r"^$", "video_list", name="video_list"),
    )
