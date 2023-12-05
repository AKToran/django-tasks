from django.shortcuts import render
from .forms import Form

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)

    else:
        form = Form()

    return render(request, 'home.html', {'form':form} )

