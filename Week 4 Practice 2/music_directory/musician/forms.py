from django import forms
from .models import Musucian

class MusucianForm(forms.ModelForm):
    class Meta:
        model = Musucian
        fields = '__all__'
        