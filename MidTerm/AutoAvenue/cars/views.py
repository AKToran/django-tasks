from django.shortcuts import render, redirect
from . import forms
from . import models
from django.views.generic import DetailView
from cars.models import Cars
from buyers.models import BuyerHistory
from buyers.forms import BuyerHistoryForm

class CarDetailsView(DetailView):
    model = models.Cars
    pk_url_kwarg = 'id'
    template_name = 'car_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.car = car
            comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.get_object()
        comments = car.comments.all()
        comment_form = forms.CommentForm()
        
        if self.request.user.is_authenticated:
            data ={
                'name': self.request.user.username,
                'email': self.request.user.email,
            }
            comment_form = forms.CommentForm(initial=data)

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

def BuyCar(request, id):
    car = Cars.objects.get(id=id)
    car.quantity = car.quantity-1
    add_history = BuyerHistory.objects.create(buyer = request.user)
    add_history.cars.set([car])
    add_history.save()
    car.buyer.set ([request.user])
    car.save()
    return redirect('profile')

