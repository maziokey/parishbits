from django import template
from ..models import Reflection

register = template.Library()

@register.inclusion_tag('cathedral/recent_reflections.html')
def recent_reflections(count=1):
    latest_reflections = Reflection.published.order_by('-publish')[:count]
    return {'latest_reflections': latest_reflections}