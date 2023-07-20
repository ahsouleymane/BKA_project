from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class installation_informationForm(forms.ModelForm):
    class Meta:
        model = installation_information
        fields = ['lat', 'lon']
        labels = {
            'lat': 'Latitude',
            'lon': 'Longitude',
        }
