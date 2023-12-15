from typing import Any
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
# from .forms import SignupForm
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.

class SignupView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Signup'
        return context

class loginView(LoginView):
    template_name = 'signup.html'
    def get_success_url(self):
        return reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
class logoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')

    

