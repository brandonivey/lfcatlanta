from django.db import models

import feedparser

from mezzanine.pages.models import Page

MAX_RESULTS = 4


class Feed(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField(unique=True)
    description = models.TextField(blank=True, null=True)
    last_polled = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def fetch(self):
        entry_list = []
        feed = feedparser.parse(self.url)
        self.save()
        for entry in feed.entries:
            new_entry = {
                'title': entry.title,
                'description': entry.summary,
                'link': entry.link,
                'published': entry.published
            }
            entry_list.append(new_entry)
        return entry_list[:MAX_RESULTS]


class Entry(models.Model):
    feed = models.ForeignKey(Feed)
    title = models.CharField(max_length=2000, blank=True, null=True)
    link = models.CharField(max_length=2000)
    summary = models.TextField(blank=True, null=True)
    published = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published']
        verbose_name_plural = 'entries'

    def __unicode__(self):
        return self.title


class FeedList(Page):
    """ Page object for holding a list of events """
    hide_children = models.BooleanField(default=True,
        verbose_name="Hide feeds in this container from navigation")

    class Meta:
        verbose_name = "Feed List"

    @property
    def feeds(self):
        """ convenience method for getting all events in a container """
        return list(Feed.objects.all())
