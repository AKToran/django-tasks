from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        signup_form = forms.SignUpForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'Signup successful')
            return redirect('profile')
    
    else:
        signup_form = forms.SignUpForm()

    return render(request, 'signup.html', {'form': signup_form, 'type': 'Signup'})

@login_required
def profile(request):
    return render(request, 'profile.html')
