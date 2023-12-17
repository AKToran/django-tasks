from django.db import models
from brands.models import Brands
from django.contrib.auth.models import User

# Create your models here.

class Cars(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(upload_to=('cars/uploads/'))
    brand = models.ForeignKey(Brands, on_delete=models.CASCADE, related_name='cars')
    buyer = models.ManyToManyField(User, blank=True, related_name='cars')

    def __str__(self):
        return self.name
    
class Comments(models.Model):
    car = models.ForeignKey(Cars, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=20)
    body = models.TextField()
    email = models.EmailField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name}"
    
