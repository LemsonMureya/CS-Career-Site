from django import template
from blogApp.models import Event, Project

register = template.Library()

@register.inclusion_tag('event_sidebar.html')
def show_other_events(event_id):
    events = Event.objects.exclude(id=event_id).order_by('-datetime')[:5]
    return {'events': events}

@register.inclusion_tag('project_sidebar.html')
def show_other_projects(project_id):
    projects = Project.objects.exclude(id=project_id).order_by('-id')[:5]
    return {'other_projects': projects}

@register.inclusion_tag('latest_projects_slideshow.html')
def latest_projects_slideshow(count=3):
    latest_projects = Project.objects.order_by('-id')[:count]
    return {'latest_projects': latest_projects}
