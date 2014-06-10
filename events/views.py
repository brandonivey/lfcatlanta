from django.shortcuts import render, get_object_or_404

from .models import Event


def event_detail(request, slug, template="pages/event.html"):
    event = get_object_or_404(Event, slug=slug)
    return render(request, template, {'event': event})
