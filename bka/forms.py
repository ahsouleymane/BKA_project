from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

class installation_informationForm(forms.ModelForm):
    class Meta:
        model = installation_information
        fields = ['customer', 'lat', 'lon']
        labels = {
            'customer': 'Customer',
            'lat': 'Latitude',
            'lon': 'Longitude',
        }

class validation_installation_informationForm(forms.ModelForm):
    class Meta:
        model = installation_information
        fields = ['value', 'unit']
        labels = {
            'value': 'Valeur',
            'unit': 'Unité',
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