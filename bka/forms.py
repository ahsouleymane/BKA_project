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
        fields = [ 'type_forfait', 'forfait_residentiel', 'forfait_entreprise']
        labels = {
            'type_forfait': 'Type Forfait',
            'forfait_residentiel': 'Forfait Résidentiel',
            'forfait_entreprise': 'Forfait Entreprise',
        }

    def __init__(self, *args, **kwargs):
            super(validation_installation_informationForm,self).__init__(*args, **kwargs)
            self.fields['forfait_residentiel'].empty_label = "Choisir"
            self.fields['forfait_entreprise'].empty_label = "Choisir"


class all_installation_informationForm(forms.ModelForm):
    class Meta:
        model = installation_information
        fields = ['customer', 'lat', 'lon', 'type_forfait', 'forfait_residentiel', 'forfait_entreprise', 'cle_activation']
        labels = {
            'customer': 'Customer',
            'lat': 'Latitude',
            'lon': 'Longitude',
            'type_forfait': 'Type Forfait',
            'forfait_residentiel': 'Forfait Résidentiel',
            'forfait_entreprise': 'Forfait Entreprise',
            'cle_activation': 'Clé Activation',
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

class forfait_entrepriseForm(forms.ModelForm):
    class Meta:
        model = forfait_entreprise
        fields = ['nom_service', 'nom_produit', 'debit', 'volume', 'validite']
        labels = {
            'nom_service': 'Nom Service',
            'nom_produit': 'Nom Produit',
            'debit': 'Débit',
            'volume': 'Volume',
            'validite': 'Validité',
        }
