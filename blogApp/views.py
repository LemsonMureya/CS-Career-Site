from django.views import View
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import Event, CustomUser
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserForm
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


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

class IndexView(TemplateView):
    template_name = "base.html"
