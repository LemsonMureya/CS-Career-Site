from django import template
from blogApp.models import Event

register = template.Library()

@register.inclusion_tag('event_sidebar.html')
def show_other_events(event_id):
    events = Event.objects.exclude(id=event_id).order_by('-datetime')[:3]
    return {'events': events}
