from django.shortcuts import render
from album.models import Album
from musician.models import Musucian
from django.views.generic import ListView

class HomeView(ListView):
    template_name = 'home.html'
    model = Musucian
    context_object_name = 'musicians' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        albums = Album.objects.all()
        context['albums'] = albums
        return context
    