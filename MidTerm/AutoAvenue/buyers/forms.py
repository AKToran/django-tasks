from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import BuyerHistory


class BuyerRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=True)
    last_name = forms.CharField(max_length=20, required=True)
    email = forms.EmailField(required=True)
    # owned_cars = forms.IntegerField(initial=0)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
        help_texts = {
            'username': 'Max 20 characters.',
        }


    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email address already exists.')
        return email


class BuyerChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields =['username', 'first_name', 'last_name', 'email']
        help_texts = {
            'username': 'Max 20 characters.',
        }

        
class BuyerHistoryForm(forms.ModelForm):
    class Meta:
        model = BuyerHistory
        fields = '__all__'
