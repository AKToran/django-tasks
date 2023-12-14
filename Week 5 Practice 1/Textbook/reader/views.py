from django.shortcuts import render, redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm

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


def reader_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            pwd = form.cleaned_data['password']
            user = authenticate(username=name, password=pwd)
            if user is not None:
                messages.success(request,"Login successful.")
                login(request, user)
                return redirect('home')
        else:
            messages.warning(request,"Invalid username or password")
            return redirect('login')
    else:
        form = AuthenticationForm()
        return render(request, 'signup.html',{'form':form, 'type': 'Login'})


def reader_logout(request):
    logout(request)
    return redirect('login')

def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, request.user)
                messages.success(request, 'Password changed successfully')
                return redirect('profile')
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'password_change.html', {'form': form})
    else:
        return redirect('login')
    
def set_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, request.user)
                messages.success(request, 'Password changed successfully')
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        
        return render(request, 'password_change.html', {'form': form})
    