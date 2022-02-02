from django import template
from ..models import Event

register = template.Library()

@register.inclusion_tag('stkevins/recent_events.html')
def recent_events(count=4):
    latest_events = Event.published.order_by('-publish')[:count]
    return {'latest_events': latest_events}

@register.inclusion_tag('cathedral/recent_stkevin_events.html')
def recent_stkevin_events(count=4):
    latest_stkev_events = Event.published.order_by('-publish')[:count]
    return {'latest_stkev_events': latest_stkev_events}