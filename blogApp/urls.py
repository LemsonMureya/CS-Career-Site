from django.urls import include, path
from . import views
from .views import EventListView, EventDetailView

app_name = 'blogApp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('events/', EventListView.as_view(), name='event_list'),
    path('events/<slug:slug>/', EventDetailView.as_view(), name='event_detail'),
    # path('category/<str:category>/', EventCategoryView.as_view(), name='event_category'),
]
