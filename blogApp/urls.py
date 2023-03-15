from django.urls import include, path
from . import views
from .views import SuccessView, ProfileView, EditProfileView, IndexView

app_name = 'blogApp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('success/',SuccessView.as_view(), name='success'),

]
