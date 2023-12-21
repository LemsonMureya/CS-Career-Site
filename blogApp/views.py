from django.views import View
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Event, CustomUser,Project, Opportunity, BlogPost, Tag
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserForm, BlogPostForm, ProjectForm, EventForm, OpportunityForm
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Project.CATEGORY_CHOICES
        context['projects'] = Project.objects.all()
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category', None)
        if category:
            queryset = queryset.filter(category=category)
        return queryset

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'
    context_object_name = 'project'

@login_required
def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user
            project.save()
            messages.success(request, 'Project created successfully')
            return redirect('blogApp:project_list')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form})

@login_required
def edit_project(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            messages.success(request, 'Project updated successfully')
            return redirect('blogApp:project_detail', pk=project.pk)
    else:
        form = ProjectForm(instance=project)
    return render(request, 'project_form.html', {'form': form, 'project': project})

@login_required
def delete_project(request, pk):
    project = get_object_or_404(Project, pk=pk, owner=request.user)
    if request.method == 'POST':
        project.delete()
        messages.success(request, 'Project deleted successfully')
        return redirect('blogApp:project_list')
    return render(request, 'confirm_project_delete.html', {'object': project})

# A view for displaying a list of events
class EventListView(ListView):
    model = Event
    template_name = 'event_list.html'
    context_object_name = 'events'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        if category:
            queryset = queryset.filter(event_type=category)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        list_events = self.get_queryset()
        paginator = Paginator(list_events, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            events = paginator.page(page)
        except PageNotAnInteger:
            events = paginator.page(1)
        except EmptyPage:
            events = paginator.page(paginator.num_pages)

        context['events'] = events
        context['category_choices'] = Event.TYPE_CHOICES

        return context

#class view for displaying event details, utilizes slugs for generating urls that are user friendly
class EventDetailView(DetailView):
    model = Event
    template_name = 'event_detail.html'
    context_object_name = 'event'
    slug_field = 'slug'

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.owner = request.user
            event.save()
            messages.success(request, 'Event created successfully')
            return redirect('blogApp:event_detail', slug=event.slug)
    else:
        form = EventForm()
    return render(request, 'event_form.html', {'form': form})

@login_required
def edit_event(request, slug):
    event = get_object_or_404(Event, slug=slug, owner=request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event updated successfully')
            return redirect('blogApp:event_detail', slug=event.slug)
    else:
        form = EventForm(instance=event)
    return render(request, 'event_form.html', {'form': form, 'event': event})

@login_required
def delete_event(request, slug):
    event = get_object_or_404(Event, slug=slug, owner=request.user)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully')
        return redirect('blogApp:event_list')  # Redirect to the event list
    return render(request, 'confirm_event_delete.html', {'object': event})

class SuccessView(TemplateView):
    template_name = 'success.html'

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save(commit=False)
        user.is_active = True
        user.save()
        messages.success(self.request, 'Your account has been created. Please check your email to activate your account.')
        return response

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('blogApp:success')

    def form_valid(self, form):
        email = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, email=email, password=password)
        if user is not None:
            login(self.request, user)
            return redirect(reverse('blogApp:success'))
        else:
            messages.error(self.request, 'Invalid email or password.')
            return super().form_invalid(form)

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

class EditProfileView(LoginRequiredMixin, View):
    form_class = CustomUserForm
    template_name = 'registration/edit_profile.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(instance=request.user)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

class OpportunityListView(ListView):
    model = Opportunity
    template_name = 'opportunity_list.html'
    context_object_name = 'opportunities'
    # add pagination or filtering here if needed

class OpportunityDetailView(DetailView):
    model = Opportunity
    template_name = 'opportunity_detail.html'
    context_object_name = 'opportunity'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recent_opportunities = Opportunity.objects.order_by('-created_date')[:5]
        context['recent_opportunities'] = recent_opportunities
        return context

@login_required
def create_opportunity(request):
    if request.method == 'POST':
        form = OpportunityForm(request.POST, request.FILES)
        if form.is_valid():
            opportunity = form.save(commit=False)
            opportunity.owner = request.user
            opportunity.save()
            messages.success(request, 'Opportunity created successfully')
            return redirect('blogApp:opportunity_list')
    else:
        form = OpportunityForm()
    return render(request, 'opportunity_form.html', {'form': form})

@login_required
def edit_opportunity(request, pk):
    opportunity = get_object_or_404(Opportunity, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = OpportunityForm(request.POST, request.FILES, instance=opportunity)
        if form.is_valid():
            form.save()
            messages.success(request, 'Opportunity updated successfully')
            return redirect('blogApp:opportunity_list')
    else:
        form = OpportunityForm(instance=opportunity)
    return render(request, 'opportunity_form.html', {'form': form, 'opportunity': opportunity})

@login_required
def delete_opportunity(request, pk):
    opportunity = get_object_or_404(Opportunity, pk=pk, owner=request.user)
    if request.method == 'POST':
        opportunity.delete()
        messages.success(request, 'Opportunity deleted successfully')
        return redirect('blogApp:opportunity_list')
    return render(request, 'confirm_opportunity_delete.html', {'opportunity': opportunity})

class JobListView(OpportunityListView):
    def get_queryset(self):
        return super().get_queryset().filter(opportunity_type='Job')

class InternshipListView(OpportunityListView):
    def get_queryset(self):
        return super().get_queryset().filter(opportunity_type='Internship')

class VolunteerListView(OpportunityListView):
    def get_queryset(self):
        return super().get_queryset().filter(opportunity_type='Volunteer')

class ResearchListView(OpportunityListView):
    def get_queryset(self):
        return super().get_queryset().filter(opportunity_type='Research')

class OtherListView(OpportunityListView):
    def get_queryset(self):
        return super().get_queryset().filter(opportunity_type='Other')

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog_list.html'
    context_object_name = 'blog_posts'
    paginate_by = 10

    def get_queryset(self):
        return BlogPost.objects.filter(is_approved=True).order_by('-created_date')

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user
            blog_post.save()
            form.save_m2m()
            return redirect('blogApp:blog_list')
        else:
            print("Form errors:", form.errors)
    else:
        form = BlogPostForm()
    return render(request, 'create_blog_post.html', {'form': form})

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog_detail.html'
    context_object_name = 'blog_post'
    slug_field = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['recent_posts'] = BlogPost.objects.order_by('-created_date')[:5]  # Last 5 posts
        context['categories'] = BlogPost.CATEGORY_CHOICES
        context['tags'] = Tag.objects.all()
        return context

@login_required
def edit_blog_post(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug, author=request.user)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, request.FILES, instance=blog_post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Post updated successfully')
            return redirect('blogApp:blog_detail', slug=blog_post.slug)
    else:
        form = BlogPostForm(instance=blog_post)
    return render(request, 'edit_blog_post.html', {'form': form})

@login_required
def delete_blog_post(request, slug):
    blog_post = get_object_or_404(BlogPost, slug=slug, author=request.user)
    if request.method == 'POST':
        blog_post.delete()
        messages.success(request, 'Post deleted successfully')
        return redirect('blogApp:blog_list')
    return render(request, 'confirm_delete.html', {'blog_post': blog_post})

class TechnicalInterviewListView(BlogListView):
    def get_queryset(self):
        return super().get_queryset().filter(category=BlogPost.TECHNICAL_INTERVIEWS)

class BehavioralInterviewListView(BlogListView):
    def get_queryset(self):
        return super().get_queryset().filter(category=BlogPost.BEHAVIORAL_INTERVIEWS)

class GradSchoolPrepListView(BlogListView):
    def get_queryset(self):
        return super().get_queryset().filter(category=BlogPost.GRAD_SCHOOL_PREP)

class CategoryListView(BlogListView):
    def get_queryset(self):
        return super().get_queryset().filter(category=self.kwargs['category'])

class TagListView(BlogListView):
    def get_queryset(self):
        return super().get_queryset().filter(tags__name=self.kwargs['tag'])

class BlogSearchListView(BlogListView):
    template_name = 'blog_search_list.html'

    def get_queryset(self):
        query = self.request.GET.get('q', '')
        self.query = query
        if query:
            return BlogPost.objects.filter(
                Q(title__icontains=query) |
                Q(description__icontains=query)
            )
        return BlogPost.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.query
        return context

class AlumniListView(ListView):
    model = CustomUser
    template_name = 'alumni_list.html'
    context_object_name = 'alumni'
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super(AlumniListView, self).get_context_data(**kwargs)
        list_alumni = CustomUser.objects.filter(role='Alumni').order_by('-class_year')
        paginator = Paginator(list_alumni, self.paginate_by)

        page = self.request.GET.get('page')

        try:
            alumni = paginator.page(page)
        except PageNotAnInteger:
            alumni = paginator.page(1)
        except EmptyPage:
            alumni = paginator.page(paginator.num_pages)

        context['alumni'] = alumni
        return context

class AlumniDetailView(DetailView):
    model = CustomUser
    template_name = 'alumni_detail.html'
    context_object_name = 'alumnus'
    pk_url_kwarg = 'id'

class IndexView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recent_opportunities = Opportunity.objects.order_by('-created_date')[:5]
        recent_events = Event.objects.order_by('-datetime')[:4]
        recent_blog_posts = BlogPost.objects.filter(is_approved=True).order_by('-created_date')[:3]
        recent_alumni = CustomUser.objects.filter(role='Alumni').order_by('-class_year')[:3]
        context['recent_opportunities'] = recent_opportunities
        context['recent_events'] = recent_events
        context['recent_blog_posts'] = recent_blog_posts
        context['recent_alumni'] = recent_alumni
        return context
