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
        fields = ['forfait', 'service']
        labels = {
            'forfait': 'Forfait',
            'service': 'Service',
        }

    def __init__(self, *args, **kwargs):
            super.__init__(*args, **kwargs)
            self.fields['service'].queryset = service.objects.none()

            if 'forfait' in self.data:
                try:
                    id_forfait = int(self.data.get('forfait'))
                    self.fields['service'].queryset = service.objects.filter(forfait=id_forfait).order_by('nom')
                except (ValueError, TypeError):
                    pass
            elif self.instance.pk:
                self.fields['service'].queryset = self.instance.forfait.service_set.order_by('nom')


class all_installation_informationForm(forms.ModelForm):
    class Meta:
        model = installation_information
        fields = ['customer', 'lat', 'lon', 'forfait', 'service', 'cle_activation']
        labels = {
            'customer': 'Customer',
            'lat': 'Latitude',
            'lon': 'Longitude',
            'forfait': 'Forfait',
            'service': 'Service',
            'cle_activation': 'Clé Activation',
        }

class ServiceForm(forms.ModelForm):
    class Meta:
        model = service
        fields = ['nom_service', 'nom_produit', 'debit', 'volume_jour', 'volume_nuit', 'validite']
        labels = {
            'nom_service': 'Nom Service',
            'nom_produit': 'Nom Produit',
            'debit': 'Débit',
            'volume_jour': 'Volume Jour',
            'volume_nuit': 'Volume Nuit',
            'validite': 'Validité',
        }
