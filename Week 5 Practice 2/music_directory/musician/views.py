from . import forms
from . import models
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required, name='dispatch')
class CreateMusicianView(CreateView):
    model = models.Musucian
    form_class = forms.MusucianForm
    success_url = reverse_lazy('home')
    template_name = 'add_musician.html'

@method_decorator(login_required, name='dispatch')
class EditMusicianView(UpdateView):
    model = models.Musucian
    form_class = forms.MusucianForm
    pk_url_kwarg = 'id'
    template_name = 'add_musician.html'
    success_url = reverse_lazy('home')

