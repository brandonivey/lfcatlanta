from django.conf.urls import patterns, url


urlpatterns = patterns(
    "feeds.views",
    url(r"^$", "feed_list", name="feed_list"),
    )