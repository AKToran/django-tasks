from django.shortcuts import render
from cars.models import Cars
from .forms import BuyerChangeForm, BuyerRegistrationForm
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


class BuyerRegisterView(CreateView):
    form_class = BuyerRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'register.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Register'
        return context

class BuyerLoginView(LoginView):
    template_name = 'register.html'
    def get_success_url(self):
        return reverse_lazy('home')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
    
@login_required
def profile(request):
    cars = Cars.objects.filter(buyer = request.user)
    return render(request, 'profile.html', {'cars': cars})

class BuyerLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')

    


