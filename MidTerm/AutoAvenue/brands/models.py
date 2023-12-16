from django.db import models

class Brands(models.Model):
    name = models.CharField(max_length=25, unique=True)
    slug = models.SlugField(max_length=30, unique=True)

    def __str__(self):
        return self.name
