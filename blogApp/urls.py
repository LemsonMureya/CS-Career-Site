from django.urls import include, path
from . import views
from .views import (EventListView, EventDetailView, SuccessView, ProfileView, EditProfileView, IndexView, ProjectListView, ProjectDetailView,
                    create_project, edit_project,delete_project,OpportunityListView, OpportunityDetailView, JobListView, InternshipListView, ResearchListView, VolunteerListView, OtherListView,
                    BlogListView, BlogDetailView, edit_blog_post, delete_blog_post,TechnicalInterviewListView, AlumniDetailView,
                    BehavioralInterviewListView, GradSchoolPrepListView, CategoryListView,TagListView, BlogSearchListView, AlumniListView,
                    create_event, edit_event, delete_event)


app_name = 'blogApp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('events/', EventListView.as_view(), name='event_list'),
    path('events/create/', views.create_event, name='create_event'),
    path('events/edit/<slug:slug>/', views.edit_event, name='edit_event'),
    path('events/delete/<slug:slug>/', views.delete_event, name='delete_event'),
    path('events/<slug:slug>/', views.EventDetailView.as_view(), name='event_detail'),
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/create/', create_project, name='create_project'),
    path('projects/edit/<int:pk>/', edit_project, name='edit_project'),
    path('projects/delete/<int:pk>/', delete_project, name='delete_project'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('opportunities/', OpportunityListView.as_view(), name='opportunity_list'),
    path('opportunities/<int:pk>/', OpportunityDetailView.as_view(), name='opportunity_detail'),
    path('opportunities/create/', views.create_opportunity, name='create_opportunity'),
    path('opportunities/edit/<int:pk>/', views.edit_opportunity, name='edit_opportunity'),
    path('opportunities/delete/<int:pk>/', views.delete_opportunity, name='delete_opportunity'),
    path('jobs/', JobListView.as_view(), name='job_list'),
    path('internships/', InternshipListView.as_view(), name='internship_list'),
    path('other/', OtherListView.as_view(), name='other_list'),
    path('research/', ResearchListView.as_view(), name='research_list'),
    path('volunteer/', VolunteerListView.as_view(), name='volunteer_list'),
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/create/', views.create_blog_post, name='create_blog_post'),
    path('blog/edit/<slug:slug>/', edit_blog_post, name='edit_blog_post'),
    path('blog/delete/<slug:slug>/', delete_blog_post, name='delete_blog_post'),
    path('blog/<slug:slug>/', BlogDetailView.as_view(), name='blog_detail'),
    path('technical-interviews/', TechnicalInterviewListView.as_view(), name='technical_interviews_list'),
    path('behavioral-interviews/', BehavioralInterviewListView.as_view(), name='behavioral_interviews_list'),
    path('grad_school_prep/', GradSchoolPrepListView.as_view(), name='grad_school_prep_list'),
    path('blog/category/<str:category>/', CategoryListView.as_view(), name='category_list'),
    path('blog/tag/<str:tag>/', TagListView.as_view(), name='tag_list'),
    path('search/', BlogSearchListView.as_view(), name='blog_search'),
    path('alumni/', AlumniListView.as_view(), name='alumni_list'),
    path('alumni/<int:id>/', AlumniDetailView.as_view(), name='alumni_detail'),
    path('success/',SuccessView.as_view(), name='success'),
]
