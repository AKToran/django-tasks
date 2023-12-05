from django.shortcuts import render
from .forms import Form
from . import models

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

    else:
        form = Form()

    return render(request, 'home.html', {'form':form} )


def model(request):
    student = models.Student.objects.all()
    return render(request, 'home.html', {'data': student})