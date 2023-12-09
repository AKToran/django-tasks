from django.shortcuts import render
from task_model.models import Task

def home(request):
    return render(request, 'home.html')

def show_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'show_tasks.html', {'tasks': tasks})