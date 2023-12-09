from django.db import models
from task_category.models import Category

class Task(models.Model):
    title = models.CharField(max_length=60)
    task_description = models.TextField()
    is_completed = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    category = models.ManyToManyField(Category, related_name='task')

    def __str__(self):
        return self.title
