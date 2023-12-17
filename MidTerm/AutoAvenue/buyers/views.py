from django.shortcuts import render
from cars.models import Cars
from django.contrib.auth.models import User
from .forms import BuyerChangeForm, BuyerRegistrationForm
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import BuyerHistory


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
    buyer = request.user
    history = BuyerHistory.objects.filter(buyer = request.user)
    # for h in history:
    #     print(h.date)
    #     print(h.buyer.first_name)
    #     for car in h.cars.all():
    #         print(car.name)
    return render(request, 'profile.html', {'cars': cars, 'buyer': buyer, 'history': history})

class UpdateProfileView(UpdateView):
    model = User
    form_class = BuyerChangeForm
    template_name = 'update_profile.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'


class BuyerLogoutView(LogoutView):
    def get_success_url(self):
        return reverse_lazy('home')

    


