from django.shortcuts import render, redirect
from . import forms
from . import models

def add_musician(request):
    if request.method == 'POST':
        musician_form = forms.MusucianForm(request.POST)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home')
    else:
        musician_form = forms.MusucianForm()
    return render(request, 'add_musician.html', {'form': musician_form})

def edit_musician(request, id):
    musician = models.Musucian.objects.get(pk=id)
    musician_form = forms.MusucianForm(instance=musician)

    if request.method == 'POST':
        musician_form = forms.MusucianForm(request.POST, instance=musician)
        if musician_form.is_valid():
            musician_form.save()
            return redirect('home')
        
    return render(request, 'add_musician.html', {'form': musician_form})

