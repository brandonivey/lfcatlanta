from __future__ import absolute_import

import feedparser
from celery import shared_task

from feeds.models import Feed, Entry


@shared_task
def fetch_feeds():
    feeds = Feed.objects.all()
    for feed in feeds:
        rssfeed = feedparser.parse(feed.url)
        feed.save()
        for e in rssfeed.entries:
            new_entry, created = Entry.objects.get_or_create(
                feed = feed,
                title = e.title,
                link = e.link,
                summary = e.summary
                )


@shared_task
def test(param):
    return 'The test task executed with argument "%s" ' % param
