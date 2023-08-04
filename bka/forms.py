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
        fields = ['service']
        labels = {
            'service': 'Service',
        }

    def __init__(self, *args, **kwargs):
            super(validation_installation_informationForm,self).__init__(*args, **kwargs)
            self.fields['service'].empty_label = "Choisir"

class all_installation_informationForm(forms.ModelForm):
    class Meta:
        model = installation_information
        fields = ['customer', 'lat', 'lon', 'service']
        labels = {
            'customer': 'Customer',
            'lat': 'Latitude',
            'lon': 'Longitude',
            'service': 'Service',
        }

class forfait_residentielForm(forms.ModelForm):
    class Meta:
        model = forfait_residentiel
        fields = ['nom_service', 'nom_produit', 'debit', 'volume_jour', 'volume_nuit', 'validite']
        labels = {
            'nom_service': 'Nom Service',
            'nom_produit': 'Nom Produit',
            'debit': 'Débit',
            'volume_jour': 'Volume Jour',
            'volume_nuit': 'Volume Nuit',
            'validite': 'Validité',
        }