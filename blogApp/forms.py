# # forms.py
#
# from django import forms
# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from .models import User
# from django.contrib.auth import get_user_model
# #form for user registration
# # class CustomUserCreationForm(UserCreationForm):
# #     class Meta(UserCreationForm.Meta):
# #         model = User
# #         fields = ('email', 'first_name', 'last_name', 'password1', 'password2')
#
# User = get_user_model()
#
# class CustomUserCreationForm(forms.ModelForm):
#     password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)
#
#     class Meta:
#         model = User
#         fields = ('email', 'first_name', 'last_name')
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get('password1')
#         password2 = self.cleaned_data.get('password2')
#         if password1 and password2 and password1 != password2:
#             raise forms.ValidationError('Passwords do not match')
#         return password2
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data['password1'])
#         if commit:
#             user.save()
#         return user
#
# #form for user editing profile info
# class CustomUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm.Meta):
#         model = User
#         fields = ('email', 'first_name', 'last_name', 'bio', 'major_minor', 'position', 'company', 'class_year', 'role', 'photo', 'verified')
