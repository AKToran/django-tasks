from django import forms
from django.core import validators
import datetime

#* this is step one for forms api
#* step two views.py 

class Form(forms.Form):
    name = forms.CharField(initial='Your name here', help_text="Enter your full name")
    email = forms.EmailField(help_text="Enter your email address")
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    agree = forms.BooleanField(label="Agree to our terms and conditions")
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    CHOICES = ['1980', '1981', '1982''', '1983', '1984', '1985', '1986', '1987', '1988', '1989', '1990']
    birth_day = forms.DateField(widget=forms.SelectDateWidget(years=CHOICES))
    value = forms.DecimalField()
    message = forms.CharField(max_length = 10)
    day = forms.DateField(initial=datetime.date.today)
    COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),]
    favorite_color = forms.ChoiceField(choices=COLORS_CHOICES)
    fav_color = forms.ChoiceField(widget=forms.RadioSelect, choices=COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=COLORS_CHOICES)
    image = forms.ImageField(required=False)
    file = forms.FileField(required=False, validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'])])









