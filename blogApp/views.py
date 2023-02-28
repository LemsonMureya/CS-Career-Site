from django.views import View
from django.shortcuts import render
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = "demo1.html"
