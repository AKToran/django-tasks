from django.shortcuts import render, redirect
from . import forms
from . import models
from django.views.generic import DetailView
from cars.models import Cars

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
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

def BuyCar(request):
    car = Cars.objects.get(id=id)
    car.quantity = car.quantity-1
    car.buyer.set ([request.user])
    car.save()
    return redirect('profile')

