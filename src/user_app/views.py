from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class ProfileView(TemplateView):
    template_name = "user_app/profile.html"
    
