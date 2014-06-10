import re
from django import template
from django.template.defaultfilters import stringfilter

from ..models import _get_current_domain, Event, EventContainer

register = template.Library()

myre = re.compile(r'([a-zA-Z0-9\-\.\_]+@[a-zA-Z0-9\-\.\_]+\.[a-zA-Z0-9\-\.\_]+)')


@register.filter(is_safe=True)
@stringfilter
def link_emails(value):
    return myre.sub("<a href='mailto:\\1'>\\1</a>", value)


@register.filter(is_safe=True)
def icalendar_url(obj, proto_param=None):
    if proto_param is None:
        proto = 'http://'
    else:
        proto = '%s://' % proto_param
    if isinstance(obj, Event):
        endfile = 'event.ics'
    elif isinstance(obj, EventContainer):
        endfile = 'calendar.ics'
    else:
        return obj
    return proto + _get_current_domain() + obj.get_absolute_url() + endfile
