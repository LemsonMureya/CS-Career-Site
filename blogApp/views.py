from django.views import View
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import Event, User
from django.contrib.auth import login
# from .forms import CustomUserCreationForm

#a view for displaying a list of events
class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'
    paginate_by = 10

    #methods for filtering events by category
    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(event_type=category)
        return queryset

    #method for getting data regarding categories and sending it to event_list.html template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_choices'] = Event.TYPE_CHOICES
        context['selected_category'] = self.request.GET.get('category')
        return context

#class view for displaying event details, utilizes slugs for generating urls that are user friendly
class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
    context_object_name = 'event'
    slug_field = 'slug'

#class for handling user registration
# class RegisterView(View):
#     form_class = CustomUserCreationForm
#     template_name = 'registration/register.html'
#
#     #handles get requests for form
#     def get(self, request, *args, **kwargs):
#         form = self.form_class()
#         return render(request, self.template_name, {'form': form})
#
#     #handles post requests
#     def post(self, request, *args, **kwargs):
#         form = self.form_class(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('event_list')
#         return render(request, self.template_name, {'form': form})

class IndexView(TemplateView):
    template_name = "demo1.html"
