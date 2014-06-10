from datetime import datetime
from django.shortcuts import render, get_object_or_404

from .models import Event


def event_detail(request, slug, template="events/event.html"):
    event = get_object_or_404(Event, slug=slug)
    return render(request, template, {'event': event})

def event_list(request, template="events/event_list.html"):
    events = list(Event.objects.filter(start__gte=datetime.now()))
    return render(request, template, {'events': events})
