from django.db import models
from cars.models import Cars
from django.contrib.auth.models import User

class BuyerHistory(models.Model):
    cars = models.ManyToManyField(Cars, related_name='history')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
