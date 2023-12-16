from django import forms 
from . models import Cars, Comments

class CarForm(forms.ModelForm):
    class Meta:
        model = Cars
        fields = '__all__'

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name', 'email', 'body']