from __future__ import absolute_import
import datetime
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
            pubdate = datetime.datetime.strptime(e.published, "%a, %d %b %Y %H:%M:%S %Z")
            new_entry, created = Entry.objects.get_or_create(
                feed = feed,
                title = e.title,
                summary = e.summary,
                published = pubdate
                )


@shared_task
def test(param):
    return 'The test task executed with argument "%s" ' % param
