from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

class installation_informationForm(forms.ModelForm):
    class Meta:
        model = installation_information
        fields = ['customer', 'lat', 'lon']
        labels = {
            'customer': 'Customer',
            'lat': 'Latitude',
            'lon': 'Longitude',
        }


class all_installation_informationForm(forms.ModelForm):
    class Meta:
        model = installation_information
        fields = ['customer', 'lat', 'lon', 'value', 'unit']
        labels = {
            'customer': 'Customer',
            'lat': 'Latitude',
            'lon': 'Longitude',
            'value': 'Valeur',
            'unit': 'Unité',
        }