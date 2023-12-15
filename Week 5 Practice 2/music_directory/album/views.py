from django.shortcuts import render, redirect
from . import forms
from . import models
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class AddAlbumView(CreateView):
    model = models.Album
    form_class = forms.AlbumForm
    success_url = reverse_lazy('home')
    template_name = 'add_album.html'

@method_decorator(login_required, name='dispatch')
class EditAlbumView(UpdateView):
    model = models.Album
    form_class = forms.AlbumForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('home')
    template_name = "add_album.html"

@method_decorator(login_required, name='dispatch')
class DeleteAlbumView(DeleteView):
    model = models.Album
    template_name = "delete_album.html"
    pk_url_kwarg ='id'
    success_url = reverse_lazy('home')
