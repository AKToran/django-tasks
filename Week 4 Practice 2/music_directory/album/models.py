from django.db import models
from musician.models import Musucian
# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=40)
    release_date = models.DateField(auto_now_add=True)
    choices = (
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five')
    )
    rating = models.SmallIntegerField(choices=choices)
    musician = models.ManyToManyField(Musucian, related_name='album')

    def __str__(self):
        return self.name