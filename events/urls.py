from __future__ import unicode_literals

from django.conf.urls import patterns, url


urlpatterns = patterns(
    "events.views",
    url("^(?P<slug>.*)/$", "event_detail", name="event_detail"),
    )
