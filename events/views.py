from datetime import datetime
from django.shortcuts import render, get_object_or_404

from .models import Event, EventContainer


def event_detail(request, slug, template="events/event.html"):
    event = get_object_or_404(Event, slug=slug)
    page = EventContainer.objects.get(slug='events')
    return render(request, template, {'event': event, 'page': page})


def event_list(request, template="events/event_list.html"):
    events = list(Event.objects.filter(start__gte=datetime.now()))
    return render(request, template, {'event_list': events})
