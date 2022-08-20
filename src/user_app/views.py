from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import models
from django.urls import reverse_lazy

# Create your views here.

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "user_app/profile.html"
    model = models.User
    success_url = reverse_lazy("user_app:profile")
    login_url = reverse_lazy("user_app:login")
    
